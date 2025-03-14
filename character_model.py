from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from models import ItemInfoList, ItemInfoDict
from utils import 计算干员升级消耗
if TYPE_CHECKING:
    from item_model import 信物类


@dataclass
class 职业类:
    ID: str
    名称: str


近卫 = 职业类(ID="WARRIOR", 名称="近卫")
狙击 = 职业类(ID="SNIPER", 名称="狙击")
重装 = 职业类(ID="TANK", 名称="重装")
医疗 = 职业类(ID="MEDIC", 名称="医疗")
辅助 = 职业类(ID="SUPPORT", 名称="辅助")
术师 = 职业类(ID="CASTER", 名称="术师")
特种 = 职业类(ID="SPECIAL", 名称="特种")
先锋 = 职业类(ID="PIONEER", 名称="先锋")
职业列表 = [近卫, 狙击, 重装, 医疗, 辅助, 术师, 特种, 先锋]


ID_to_职业 = {
    "WARRIOR": 近卫,
    "SNIPER": 狙击,
    "TANK": 重装,
    "MEDIC": 医疗,
    "SUPPORT": 辅助,
    "CASTER": 术师,
    "SPECIAL": 特种,
    "PIONEER": 先锋,
}


职业名称_to_职业 = {
    "近卫": 近卫,
    "狙击": 狙击,
    "重装": 重装,
    "医疗": 医疗,
    "辅助": 辅助,
    "术师": 术师,
    "特种": 特种,
    "先锋": 先锋,
}


@dataclass
class 精英化阶段类:
    等级上限: int
    _升级消耗: ItemInfoDict

    @property
    def 升级消耗(self) -> ItemInfoList:
        return ItemInfoList.new(self._升级消耗)


@dataclass
class 技能类:
    ID: str
    _专精消耗: list[ItemInfoDict]

    @property
    def 专精消耗(self) -> list[ItemInfoList]:
        return [ItemInfoList.new(x) for x in self._专精消耗]


@dataclass
class 干员类:
    ID: str
    代号: str
    描述: str
    稀有度: int
    最大潜能等级: int
    _信物: str | None
    位置: str
    标签列表: list[str]
    是异格干员: bool
    职业: 职业类
    职业分支: str
    精英化阶段列表: list[精英化阶段类]
    技能列表: list[技能类]
    _通用技能升级消耗: list[ItemInfoDict]

    @property
    def 信物(self) -> 信物类 | None:
        from load_data import 道具字典
        if self._信物 is None:
            return None
        return 道具字典[self._信物]

    @property
    def 通用技能升级消耗(self) -> list[ItemInfoList]:
        return [ItemInfoList.new(x) for x in self._通用技能升级消耗]

    def 计算等级升级消耗(self, 初始精英化阶段: int, 初始等级: int, 目标精英化阶段: int, 目标等级: int) -> ItemInfoList:
        return 计算干员升级消耗(self.稀有度, 初始精英化阶段, 初始等级, 目标精英化阶段, 目标等级)
