from __future__ import annotations

import sys
from collections import defaultdict
from collections.abc import Iterable, Mapping
from typing import TYPE_CHECKING, NamedTuple, Self, SupportsIndex, TypedDict, overload

type ItemInfoLike = ItemInfo | tuple[str, int | float] | str | ItemBundle
type ItemInfoListLike = ItemInfoList | Iterable[ItemInfoLike] | str

if TYPE_CHECKING:
    import pandas as pd

    from .item_model import Item


class ItemBundle(TypedDict):
    id: str
    count: int
    type: str


REPLACE_DICT = {
    "\\": r"\\",
    "\t": r"\t",
    "\n": r"\n",
    "\r": r"\r",
    "\f": r"\f",
    "\v": r"\v",
    " ": r"\s",
    "×": r"\c",
}


def escape_str(s: str) -> str:
    for k, v in REPLACE_DICT.items():
        s = s.replace(k, v)
    return s


def unescape_str(s: str) -> str:
    for k, v in REPLACE_DICT.items():
        s = s.replace(v, k)
    return s


class ItemInfo(NamedTuple):
    item_id: str
    count: int | float = 1  # type: ignore

    @classmethod
    def new(cls, arg: ItemInfoLike) -> Self:
        if isinstance(arg, cls):
            return arg
        elif isinstance(arg, str):
            return cls.from_str(arg)
        elif isinstance(arg, dict):
            return cls.from_item_info_dict(arg)
        else:
            return cls(*arg)

    @classmethod
    def from_item_info_dict(cls, item_info_dict: ItemBundle) -> Self:
        return cls(item_id=item_info_dict["id"], count=item_info_dict["count"])

    @classmethod
    def from_name_and_count(cls, name: str, count: int | float = 1) -> Self:
        from .game_data import game_data

        item_id = game_data.items.by_name(name).item_id
        return cls(item_id, count)

    @classmethod
    def from_str(cls, s: str) -> Self:
        if "×" not in s:
            return cls(s)
        display_name, count = s.split("×")
        name = unescape_str(display_name)
        try:
            count = int(count)
        except ValueError:
            count = float(count)
        return cls.from_name_and_count(name, count)

    @property
    def item(self) -> Item:
        from .game_data import game_data

        return game_data.items.by_id(self.item_id)

    def yituliu_item_value(self, *, strict: bool) -> float:
        if strict and not hasattr(self.item, "yituliu_item_value"):
            raise ValueError(f"物品 {self.item_id} 没有一图流价值")
        else:
            return getattr(self.item, "yituliu_item_value", 0)

    def __str__(self) -> str:
        try:
            name = self.item.name
        except KeyError:
            name = self.item_id
        display_name = escape_str(name)
        return f"{display_name}×{self.count}"


class ItemInfoList(list[ItemInfo]):
    @classmethod
    def new(cls, arg: ItemInfoListLike) -> Self:
        if isinstance(arg, cls):
            return arg
        elif isinstance(arg, str):
            return cls.from_str(arg)
        else:
            return cls(ItemInfo.new(item) for item in arg)

    @classmethod
    def from_name_and_count(cls, items: Iterable[tuple[str, int | float]]) -> Self:
        return cls(ItemInfo.from_name_and_count(name, count) for name, count in items)

    @classmethod
    def from_str(cls, s: str) -> Self:
        return cls(ItemInfo.from_str(item_str) for item_str in s.split())

    @classmethod
    def from_counter(cls, counter: Mapping[str, int | float]) -> Self:
        return cls(ItemInfo(item_id, count) for item_id, count in counter.items())

    def counter(self) -> defaultdict[str, int | float]:
        counter: defaultdict[str, int | float] = defaultdict(int)
        for item_id, count in self:
            counter[item_id] += count
        return counter

    def combine(self) -> Self:
        counter = self.counter()
        return self.__class__(ItemInfo(item_id, count) for item_id, count in counter.items())

    def combine_in_place(self) -> None:
        counter = self.counter()
        self.clear()
        self.extend(ItemInfo(item_id, count) for item_id, count in counter.items())

    def _拆分特定稀有度精英材料(self, rarity: int) -> Self:
        item_info_list = self.__class__()
        for item_info in self:
            item = item_info.item
            count = item_info.count
            if item.is_elite_material and item.rarity == rarity:
                workshop_formulas_craft_self = item.workshop_formulas_craft_self()
                assert len(workshop_formulas_craft_self) == 1
                formula = next(iter(workshop_formulas_craft_self.values()))
                item_info_list.extend(
                    ItemInfo(item_info.item_id, item_info.count * count)
                    for item_info in formula.costs
                    if item_info.item_id != "4001"
                )
            else:
                item_info_list.append(item_info)
        return item_info_list

    def 拆分到紫材料(self) -> Self:
        return self._拆分特定稀有度精英材料(4)

    def 拆分到蓝材料(self) -> Self:
        拆分到紫材料 = self.拆分到紫材料()
        return 拆分到紫材料._拆分特定稀有度精英材料(3)

    def sort_by_sort_id(self, reverse: bool = False) -> Self:
        return self.__class__(sorted(self, key=lambda item_info: item_info.item.sort_id, reverse=reverse))

    def sort_in_place_by_sort_id(self, reverse: bool = False) -> None:
        self.sort(key=lambda item_info: item_info.item.sort_id, reverse=reverse)

    def yituliu_item_value(self, *, strict: bool) -> float:
        return sum(item_info.yituliu_item_value(strict=strict) * item_info.count for item_info in self)

    def to_csv(self) -> str:
        import csv
        from io import StringIO

        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["物品 ID", "物品名称", "数量"])
        for item_info in self:
            writer.writerow([item_info.item_id, item_info.item.name, item_info.count])
        return output.getvalue()

    def to_dataframe(self) -> pd.DataFrame:
        import pandas as pd

        data = {
            "物品 ID": [item_info.item_id for item_info in self],
            "物品名称": [item_info.item.name for item_info in self],
            "数量": [item_info.count for item_info in self],
        }

        return pd.DataFrame(data)

    def to_clipboard(self) -> None:
        import pyperclip

        pyperclip.copy(self.to_csv())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"

    def __str__(self) -> str:
        return " ".join(map(str, self))

    def copy(self) -> Self:
        return self.__class__(self)

    def append(self, item: ItemInfoLike, /) -> None:
        super().append(ItemInfo.new(item))

    def extend(self, items: ItemInfoListLike, /) -> None:
        super().extend(self.__class__.new(items))

    def index(self, item: ItemInfoLike, start: SupportsIndex = 0, stop: SupportsIndex = sys.maxsize, /) -> int:
        return super().index(ItemInfo.new(item), start, stop)

    def count(self, item: ItemInfoLike, /) -> int:
        return super().count(ItemInfo.new(item))

    def insert(self, index: SupportsIndex, item: ItemInfoLike, /) -> None:
        super().insert(index, ItemInfo.new(item))

    def remove(self, item: ItemInfoLike, /) -> None:
        super().remove(ItemInfo.new(item))

    @overload
    def __getitem__(self, i: SupportsIndex, /) -> ItemInfo: ...

    @overload
    def __getitem__(self, s: slice, /) -> Self: ...

    def __getitem__(self, index: SupportsIndex | slice, /) -> ItemInfo | Self:
        if isinstance(index, slice):
            return self.__class__(super().__getitem__(index))
        else:
            return super().__getitem__(index)

    @overload
    def __setitem__(self, key: SupportsIndex, value: ItemInfoLike, /) -> None: ...

    @overload
    def __setitem__(self, key: slice, value: ItemInfoListLike, /) -> None: ...

    def __setitem__(self, key: SupportsIndex | slice, value: ItemInfoLike | ItemInfoListLike, /) -> None:
        if isinstance(key, slice):
            super().__setitem__(key, self.__class__.new(value))  # type: ignore
        else:
            super().__setitem__(key, ItemInfo.new(value))  # type: ignore

    def __add__(self, other: ItemInfoListLike, /) -> Self:  # type: ignore
        return self.__class__(super().__add__(ItemInfoList.new(other)))

    def __radd__(self, other: ItemInfoListLike, /) -> Self:
        return self.__class__(ItemInfoList.new(other).__add__(self))

    def __iadd__(self, other: ItemInfoListLike, /) -> Self:
        self.extend(other)
        return self

    def __mul__(self, value: SupportsIndex, /) -> Self:
        return self.__class__(super().__mul__(value))

    def __rmul__(self, value: SupportsIndex, /) -> Self:
        return self.__class__(super().__rmul__(value))

    def __imul__(self, value: SupportsIndex, /) -> Self:
        return self.__class__(super().__imul__(value))

    def __contains__(self, item: object, /) -> bool:
        if super().__contains__(item):
            return True
        try:
            return super().__contains__(ItemInfo.new(item))  # type: ignore
        except Exception:
            return False

    def __gt__(self, other: ItemInfoListLike, /) -> bool:
        return super().__gt__(ItemInfoList.new(other))

    def __ge__(self, other: ItemInfoListLike, /) -> bool:
        return super().__ge__(ItemInfoList.new(other))

    def __lt__(self, other: ItemInfoListLike, /) -> bool:
        return super().__lt__(ItemInfoList.new(other))

    def __le__(self, other: ItemInfoListLike, /) -> bool:
        return super().__le__(ItemInfoList.new(other))

    def __eq__(self, other: object, /) -> bool:
        if super().__eq__(other):
            return True
        try:
            return super().__eq__(ItemInfoList.new(other))  # type: ignore
        except Exception:
            return False
