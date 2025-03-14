from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from character_model import 干员类


@dataclass
class 道具类:
    类型ID: ClassVar[str]
    ID: str
    类型: 道具类


@dataclass
class 物品类(道具类):
    名称: str
    描述: str
    稀有度: int
    类型: str


@dataclass
class 作战记录类(物品类):
    类型ID: ClassVar[str] = "CARD_EXP"
    EXP: int


@dataclass
class 理智药类(物品类):
    恢复理智: int


@dataclass
class 信物类(物品类):
    干员: 干员类


@dataclass
class 干员皮肤类(道具类):
    干员: 干员类


@dataclass
class 家具类(道具类):
    名称: str


@dataclass
class 名片头像类(道具类):
    名称: str


@dataclass
class 首页场景类(道具类):
    名称: str


@dataclass
class 界面主题类(道具类):
    名称: str


@dataclass
class 名片主题类(道具类):
    名称: str


@dataclass
class 自走车装备类(道具类):
    名称: str
