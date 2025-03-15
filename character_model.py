from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Sequence

from models import ItemInfoList, ItemInfoDict, ItemInfo
from utils import 计算干员升级消耗
import gamedata_const_model as gcm

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
    _升级消耗: list[ItemInfoDict]

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
    _信物ID: str | None
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
        if self._信物ID is None:
            return None
        return 道具字典[self._信物ID]

    @property
    def 通用技能升级消耗(self) -> list[ItemInfoList]:
        return [ItemInfoList.new(x) for x in self._通用技能升级消耗]

    def 计算精英化消耗(self, 目标精英化阶段: int) -> ItemInfoList:
        if not 1 <= 目标精英化阶段 <= gcm.干员精英化阶段上限[self.稀有度]:
            raise ValueError("精英化阶段不合法")

        龙门币 = gcm.精英化消耗龙门币[self.稀有度][目标精英化阶段-1]
        item_info_list = ItemInfoList.new([("4001", 龙门币)])
        item_info_list.extend(self.精英化阶段列表[目标精英化阶段].升级消耗)

        return item_info_list

    def 计算等级升级消耗(self, 初始精英化阶段: int, 初始等级: int, 目标精英化阶段: int, 目标等级: int) -> ItemInfoList:
        """计算从初始等级升级到目标等级的消耗，含升级所需的EXP和龙门币，以及精英化所需的龙门币、精英材料"""
        EXP, 龙门币 = 计算干员升级消耗(self.稀有度, 初始精英化阶段, 初始等级, 目标精英化阶段, 目标等级)
        item_info_list = ItemInfoList.new([("exp", EXP), ("4001", 龙门币)])
        for 当前精英化阶段 in range(初始精英化阶段, 目标精英化阶段 + 1):
            item_info_list.extend(self.计算精英化消耗(当前精英化阶段))
        return item_info_list

    def 计算通用技能升级消耗(self, 初始技能等级: int, 目标技能等级: int) -> ItemInfoList:
        """计算从初始技能等级升级到目标技能等级的消耗，含技能升级所需的技能专精材料"""
        if not 1 <= 初始技能等级 <= 7:
            raise ValueError("初始技能等级不合法")
        if not 1 <= 目标技能等级 <= 7:
            raise ValueError("目标技能等级不合法")
        if 初始技能等级 >= 目标技能等级:
            return ItemInfoList()

        item_info_list = ItemInfoList()
        for 当前等级 in range(初始技能等级, 目标技能等级):
            item_info_list.extend(self.通用技能升级消耗[当前等级-1])

        return item_info_list

    def 计算技能专精消耗(self, 技能序号: int, 初始技能专精等级: int, 目标技能专精等级: int) -> ItemInfoList:
        if not 1 <= 初始技能专精等级 <= 3:
            raise ValueError("初始技能专精等级不合法")
        if not 1 <= 目标技能专精等级 <= 3:
            raise ValueError("目标技能专精等级不合法")
        if 初始技能专精等级 >= 目标技能专精等级:
            return ItemInfoList()

        item_info_list = ItemInfoList()
        for 当前等级 in range(初始技能专精等级, 目标技能专精等级):
            item_info_list.extend(self.技能列表[技能序号].专精消耗[当前等级-1])

        return item_info_list

    def 计算养成消耗(
        self,
        初始精英化阶段: int, 初始等级: int, 初始技能等级: int, 初始技能专精等级: Sequence[int],
        目标精英化阶段: int, 目标等级: int, 目标技能等级: int, 目标技能专精等级: Sequence[int],
    ) -> ItemInfoList:
        item_info_list = ItemInfoList()
        item_info_list.extend(self.计算等级升级消耗(初始精英化阶段, 初始等级, 目标精英化阶段, 目标等级))
        item_info_list.extend(self.计算通用技能升级消耗(初始技能等级, 目标技能等级))
        for 技能序号, (初始, 目标) in enumerate(zip(初始技能专精等级, 目标技能专精等级)):
            item_info_list.extend(self.计算技能专精消耗(技能序号, 初始, 目标))
        return item_info_list
