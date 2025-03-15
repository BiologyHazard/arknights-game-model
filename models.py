from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Iterable, NamedTuple, Self, SupportsIndex, TypedDict, overload

if TYPE_CHECKING:
    from item_model import 道具类


type ItemInfoLike = ItemInfo | tuple[str, int | float] | str | ItemInfoDict
type ItemInfoListLike = ItemInfoList | Iterable[ItemInfoLike] | str


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


class ItemInfo(NamedTuple):
    item_id: str
    count: int | float = 1

    @classmethod
    def new(cls, arg: ItemInfoLike) -> Self:
        if isinstance(arg, cls):
            return arg
        elif isinstance(arg, str):
            raise NotImplementedError
        elif isinstance(arg, dict):
            return cls.from_item_info_dict(arg)
        else:
            return cls(*arg)

    @classmethod
    def from_item_info_dict(cls, item_info_dict: ItemInfoDict) -> Self:
        return cls(item_id=item_info_dict["id"],
                   count=item_info_dict["count"])

    @property
    def item(self) -> 道具类:
        from load_data import 道具字典
        return 道具字典[self.item_id]

    def __str__(self) -> str:
        from load_data import 道具字典
        display_name = 道具字典[self.item_id].名称
        for k, v in REPLACE_DICT.items():
            display_name = display_name.replace(k, v)
        return f"{display_name}×{self.count}"


class ItemInfoList(list[ItemInfo]):
    @classmethod
    def new(cls, arg: ItemInfoListLike) -> Self:
        if isinstance(arg, cls):
            return arg
        elif isinstance(arg, str):
            raise NotImplementedError
        else:
            return cls(ItemInfo.new(item) for item in arg)

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

    def __str__(self) -> str:
        if not self:
            return f"{self.__class__.__name__}()"
        return " ".join(map(str, self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"
