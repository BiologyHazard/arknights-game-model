from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Iterable, NamedTuple, Self, SupportsIndex, TypedDict, overload

type ItemInfoLike = ItemInfo | tuple[str, int | float] | str | ItemInfoDict
type ItemInfoListLike = ItemInfoList | Iterable[ItemInfoLike] | str

if TYPE_CHECKING:
    from .item_model import Item


class ItemInfoDict(TypedDict):
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
    def from_item_info_dict(cls, item_info_dict: ItemInfoDict) -> Self:
        return cls(item_id=item_info_dict["id"],
                   count=item_info_dict["count"])

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

    def __str__(self) -> str:
        display_name = escape_str(self.item.name)
        return f"{display_name}×{self.count}"


class ItemInfoList(list[ItemInfo]):
    # def __init__(self, items: Iterable[ItemInfoLike] = ()) -> None:
    #     super().__init__(ItemInfo.new(item) for item in items)

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
        if s == f"{cls.__name__}()":
            return cls()
        return cls(ItemInfo.from_str(item_str) for item_str in s.split())

    def extend(self, items: Iterable[ItemInfoLike]) -> None:
        super().extend(ItemInfo.new(item) for item in items)

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

    @overload
    def __getitem__(self, __i: SupportsIndex) -> ItemInfo:
        ...

    @overload
    def __getitem__(self, __s: slice) -> Self:
        ...

    def __getitem__(self, index: SupportsIndex | slice) -> ItemInfo | Self:
        if isinstance(index, slice):
            return self.__class__(super().__getitem__(index))
        return super().__getitem__(index)

    def __str__(self) -> str:
        if not self:
            return f"{self.__class__.__name__}()"
        return " ".join(map(str, self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"
