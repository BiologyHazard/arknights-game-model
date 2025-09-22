from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from functools import lru_cache
from typing import TYPE_CHECKING, NamedTuple

from ._raw_game_data.building_data import Char as CharInGame
from ._raw_game_data.character_table import Character as CharacterInGame
from ._raw_game_data.character_table import SpTargetType
from ._raw_game_data.uniequip_table import Uniequip as UniequipInGame
from .item_info_model import ItemInfoList

if TYPE_CHECKING:
    from pandas import Timestamp


class Profession(NamedTuple):
    ID: str
    名称: str


class Professions(Enum):
    近卫 = Profession(ID="WARRIOR", 名称="近卫")
    狙击 = Profession(ID="SNIPER", 名称="狙击")
    重装 = Profession(ID="TANK", 名称="重装")
    医疗 = Profession(ID="MEDIC", 名称="医疗")
    辅助 = Profession(ID="SUPPORT", 名称="辅助")
    术师 = Profession(ID="CASTER", 名称="术师")
    特种 = Profession(ID="SPECIAL", 名称="特种")
    先锋 = Profession(ID="PIONEER", 名称="先锋")


职业ID_to_职业 = {x.value.ID: x for x in Professions}
职业名称_to_职业 = {x.value.名称: x for x in Professions}


class UniEquip:
    _raw_data: UniequipInGame
    _online_timestamp: int

    def __init__(self, raw_data: UniequipInGame, online_timestamp: int | None = None):
        self._raw_data = raw_data
        if online_timestamp is not None:
            self._online_timestamp = online_timestamp

    @property
    def uniequip_id(self) -> str:
        return self._raw_data.uni_equip_id

    @property
    def uniequip_name(self) -> str:
        return self._raw_data.uni_equip_name

    @property
    def type_name1(self) -> str:
        return self._raw_data.type_name1

    @property
    def type_name2(self) -> str | None:
        return self._raw_data.type_name2

    @property
    def is_original(self) -> bool:
        b1 = self.type_name1 == "ORIGINAL"
        b2 = self.type_name2 is None
        assert b1 == b2
        return b1

    @property
    def character_id(self) -> str:
        """获取模组对应的干员 ID"""
        return self._raw_data.char_id

    @property
    def online_timestamp(self) -> int:
        """获取模组上线时间戳"""
        return self._online_timestamp

    def character(self) -> Character:
        """获取模组对应的干员"""
        from .game_data import game_data
        return game_data.characters.by_id(self._raw_data.char_id)

    def 升级一次消耗(self, 目标等级: int) -> ItemInfoList:
        """等级范围 `[1, 3]`"""
        if not 1 <= 目标等级 <= 3:
            raise ValueError("目标等级不合法")
        if str(目标等级) not in self._raw_data.item_cost:
            raise ValueError(f"模组 {self!r} 无法升级到等级 {目标等级}")

        return ItemInfoList.new(self._raw_data.item_cost[str(目标等级)])

    def 升级消耗(self, 初始等级: int | None = None, 目标等级: int | None = None) -> ItemInfoList:
        """等级范围 `[0, 3]`"""
        if 初始等级 is None:
            初始等级 = 0
        if 目标等级 is None:
            目标等级 = 0 if self.is_original else 3

        item_info_list = ItemInfoList()
        for 当前等级 in range(初始等级, 目标等级):
            item_info_list.extend(self.升级一次消耗(当前等级 + 1))
        return item_info_list

    def __repr__(self) -> str:
        return f"<{self.__class__.__module__}.{self.__class__.__name__} uniequip_id={self.uniequip_id!r} uniequip_name={self.uniequip_name!r} type_name1={self.type_name1!r} type_name2={self.type_name2!r}>"


class Character:
    _id: str
    _raw_data: CharacterInGame
    _is_patch_char: bool
    _cn_online_time: Timestamp

    def __init__(self, id: str, raw_data: CharacterInGame, is_patch_char: bool, cn_online_time: Timestamp | None = None):
        self._id = id
        self._raw_data = raw_data
        self._is_patch_char = is_patch_char
        if cn_online_time is not None:
            self._cn_online_time = cn_online_time

    @property
    def id(self) -> str:
        return self._id

    @property
    def is_patch_char(self) -> bool:
        return self._is_patch_char

    @property
    def name(self) -> str:
        return self._raw_data.name

    @property
    def sp_target_type(self) -> SpTargetType:
        return self._raw_data.sp_target_type

    @property
    def rarity(self) -> int:
        return self._raw_data.rarity

    @property
    def max_potential_level(self) -> int:
        return self._raw_data.max_potential_level

    @property
    def profession(self) -> Professions:
        return 职业ID_to_职业[self._raw_data.profession]

    @property
    def tag_list(self) -> list[str]:
        return self._raw_data.tag_list

    @property
    def skill_count(self) -> int:
        return len(self._raw_data.skills)

    @property
    def max_skill_level(self) -> int:
        return len(self._raw_data.all_skill_lvlup) + 1

    @property
    def max_elite_level(self) -> int:
        return len(self._raw_data.phases) - 1

    @property
    def cn_online_time(self) -> Timestamp:
        """干员上线时间，数据来自 PRTS Wiki，若不存在则抛出 `AttributeError`"""
        return self._cn_online_time

    def max_level(self, elite_level: int) -> int:
        return self._raw_data.phases[elite_level].max_level

    @lru_cache
    def uniequip_ids(self) -> list[str]:
        from .game_data import game_data
        return game_data.raw_data.excel.uniequip_table.char_equip.get(self._id, [])

    def uniquips(self) -> UniEquipDict:
        from .game_data import game_data
        return UniEquipDict((uniequip_id, game_data.uniequips[uniequip_id]) for uniequip_id in self.uniequip_ids())

    def get_uniequip_by_type(self, type_name: str) -> UniEquip:
        if type_name == "α":
            type_name = "A"
        if type_name == "Δ":
            type_name = "D"
        for uniequip in self.uniquips().values():
            if type_name.upper() in (uniequip.type_name1, uniequip.type_name2):
                return uniequip
        raise ValueError(f"干员 {self.name} 未找到类型为 {type_name!r} 的模组")

    def get_uniequip(self, id_or_type: str) -> UniEquip:
        if id_or_type in self.uniquips():
            return self.uniquips()[id_or_type]
        else:
            return self.get_uniequip_by_type(id_or_type)

    def 精英化一次消耗(self, 目标精英化阶段: int) -> ItemInfoList:
        """精英化阶段范围 `[1, 2]`"""
        if not 1 <= 目标精英化阶段 <= self.max_elite_level:
            raise ValueError("精英化阶段不合法")

        if self.sp_target_type == SpTargetType.ROGUE:
            return ItemInfoList()

        from .game_data import game_data
        龙门币 = game_data.raw_data.excel.gamedata_const.evolve_gold_cost[self._raw_data.rarity][目标精英化阶段 - 1]
        item_info_list = ItemInfoList.from_name_and_count([("龙门币", 龙门币)])
        item_info_list.extend(self._raw_data.phases[目标精英化阶段].evolve_cost)
        return item_info_list

    def 精英化消耗(self, 初始精英化阶段: int | None = None, 目标精英化阶段: int | None = None) -> ItemInfoList:
        """精英化阶段范围 `[0, 2]`"""
        if 初始精英化阶段 is None:
            初始精英化阶段 = 0
        if 目标精英化阶段 is None:
            目标精英化阶段 = self.max_elite_level

        item_info_list = ItemInfoList()
        for 当前精英化阶段 in range(初始精英化阶段, 目标精英化阶段):
            item_info_list.extend(self.精英化一次消耗(当前精英化阶段 + 1))
        return item_info_list

    def 等级升级一次消耗(self, 精英化阶段: int, 初始等级: int | None = None, 目标等级: int | None = None) -> ItemInfoList:
        """
        计算从初始等级升级到目标等级的消耗，含升级所需的EXP和龙门币
        精英化阶段范围 `[0, 2]`
        """
        if 初始等级 is None:
            初始等级 = 1
        if 目标等级 is None:
            目标等级 = self.max_level(精英化阶段)
        if not 0 <= 精英化阶段 <= self.max_elite_level:
            raise ValueError("精英化阶段不合法")
        if not 1 <= 初始等级 <= self.max_level(精英化阶段):
            raise ValueError("初始等级不合法")
        if not 1 <= 目标等级 <= self.max_level(精英化阶段):
            raise ValueError("目标等级不合法")
        if 初始等级 >= 目标等级:
            return ItemInfoList()
        if self.sp_target_type == SpTargetType.ROGUE:
            return ItemInfoList()

        from .game_data import game_data
        EXP = game_data.累计消耗EXP[精英化阶段][目标等级 - 1] - game_data.累计消耗EXP[精英化阶段][初始等级 - 1]
        龙门币 = game_data.累计消耗龙门币[精英化阶段][目标等级 - 1] - game_data.累计消耗龙门币[精英化阶段][初始等级 - 1]
        return ItemInfoList.from_name_and_count([("EXP", EXP), ("龙门币", 龙门币)])

    def 等级升级消耗(self, 初始精英化阶段: int | None = None, 初始等级: int | None = None, 目标精英化阶段: int | None = None, 目标等级: int | None = None) -> ItemInfoList:
        """计算从初始等级升级到目标等级的消耗，仅含升级所需的EXP和龙门币"""
        if 初始精英化阶段 is None:
            初始精英化阶段 = 0
        if 目标精英化阶段 is None:
            目标精英化阶段 = self.max_elite_level

        item_info_list = ItemInfoList()
        for 当前精英化阶段 in range(初始精英化阶段, 目标精英化阶段 + 1):
            当前精英化阶段初始等级 = 初始等级 if 当前精英化阶段 == 初始精英化阶段 else 1
            当前精英化阶段目标等级 = 目标等级 if 当前精英化阶段 == 目标精英化阶段 else self.max_level(当前精英化阶段)
            item_info_list.extend(self.等级升级一次消耗(当前精英化阶段, 当前精英化阶段初始等级, 当前精英化阶段目标等级))
        return item_info_list

    def 精英化等级升级消耗(self, 初始精英化阶段: int | None = None, 初始等级: int | None = None, 目标精英化阶段: int | None = None, 目标等级: int | None = None) -> ItemInfoList:
        """计算从初始等级升级到目标等级的消耗，含升级所需的EXP和龙门币，以及精英化所需的龙门币、精英材料"""
        item_info_list = ItemInfoList()
        item_info_list.extend(self.精英化消耗(初始精英化阶段, 目标精英化阶段))
        item_info_list.extend(self.等级升级消耗(初始精英化阶段, 初始等级, 目标精英化阶段, 目标等级))
        return item_info_list

    def 通用技能升级一次消耗(self, 目标技能等级: int) -> ItemInfoList:
        """等级范围 `[2, 7]`"""
        if self.skill_count == 0:
            raise ValueError("该干员没有技能")
        if not 2 <= 目标技能等级 <= 7:
            raise ValueError("目标技能等级不合法")
        return ItemInfoList.new(self._raw_data.all_skill_lvlup[目标技能等级 - 2].lvl_up_cost)

    def 通用技能升级消耗(self, 初始技能等级: int | None = None, 目标技能等级: int | None = None) -> ItemInfoList:
        """等级范围 `[1, 7]`"""
        if 初始技能等级 is None:
            初始技能等级 = 1
        if 目标技能等级 is None:
            目标技能等级 = self.max_skill_level

        item_info_list = ItemInfoList()
        for 当前技能等级 in range(初始技能等级, 目标技能等级):
            item_info_list.extend(self.通用技能升级一次消耗(当前技能等级 + 1))
        return item_info_list

    def 技能专精一次消耗(self, 技能序号: int, 目标技能专精等级: int) -> ItemInfoList:
        """
        技能序号范围 `[1, 3]`
        专精等级范围 `[1, 3]`
        """
        if not 1 <= 技能序号 <= self.skill_count:
            raise ValueError("技能序号不合法")
        if not 1 <= 目标技能专精等级 <= 3:
            raise ValueError("目标技能专精等级不合法")

        return ItemInfoList.new(self._raw_data.skills[技能序号 - 1].level_up_cost_cond[目标技能专精等级 - 1].level_up_cost)

    def 技能专精消耗(self, 技能序号: int, 初始技能专精等级: int | None = None, 目标技能专精等级: int | None = None) -> ItemInfoList:
        """
        技能序号范围 `[1, 3]`
        专精等级范围 `[0, 3]`
        """
        if 初始技能专精等级 is None:
            初始技能专精等级 = 0
        if 目标技能专精等级 is None:
            目标技能专精等级 = len(self._raw_data.skills[技能序号 - 1].level_up_cost_cond)

        item_info_list = ItemInfoList()
        for 当前技能专精等级 in range(初始技能专精等级, 目标技能专精等级):
            item_info_list.extend(self.技能专精一次消耗(技能序号, 当前技能专精等级 + 1))
        return item_info_list

    def 模组升级一次消耗(self, 模组ID或类型: str, 目标模组等级: int) -> ItemInfoList:
        uniequip = self.get_uniequip(模组ID或类型)
        return uniequip.升级一次消耗(目标模组等级)

    def 模组升级消耗(self, 模组ID或类型: str, 初始模组等级: int | None = None, 目标模组等级: int | None = None) -> ItemInfoList:
        uniequip = self.get_uniequip(模组ID或类型)
        return uniequip.升级消耗(初始模组等级, 目标模组等级)

    def 养成消耗(
        self,
        初始精英化阶段: int | None = None,
        初始等级: int | None = None,
        初始技能等级: int | None = None,
        初始技能专精等级列表: Iterable[int | None] | None = None,
        初始模组等级字典: dict[str, int | None] | None = None,
        目标精英化阶段: int | None = None,
        目标等级: int | None = None,
        目标技能等级: int | None = None,
        目标技能专精等级列表: Iterable[int | None] | None = None,
        目标模组等级字典: dict[str, int | None] | None = None,
    ) -> ItemInfoList:
        if 初始技能专精等级列表 is None:
            初始技能专精等级列表 = [None] * self.skill_count
        if 目标技能专精等级列表 is None:
            目标技能专精等级列表 = [None] * self.skill_count
        专属模组ID列表 = [uniequip_id for uniequip_id, uniequip in self.uniquips().items() if not uniequip.is_original]
        if 初始模组等级字典 is None:
            初始模组等级字典 = dict.fromkeys(专属模组ID列表, None)
        if 目标模组等级字典 is None:
            目标模组等级字典 = dict.fromkeys(专属模组ID列表, None)
        item_info_list = ItemInfoList()
        item_info_list.extend(self.精英化等级升级消耗(初始精英化阶段, 初始等级, 目标精英化阶段, 目标等级))
        item_info_list.extend(self.通用技能升级消耗(初始技能等级, 目标技能等级))
        for 技能序号, (初始技能专精等级, 目标技能专精等级) in enumerate(zip(初始技能专精等级列表, 目标技能专精等级列表), start=1):
            item_info_list.extend(self.技能专精消耗(技能序号, 初始技能专精等级, 目标技能专精等级))
        for uniequip_id, uniequip in self.uniquips().items():
            if uniequip.is_original:
                continue
            在初始模组等级字典中 = uniequip_id in 初始模组等级字典 or uniequip.type_name2 in 初始模组等级字典
            在目标模组等级字典中 = uniequip_id in 目标模组等级字典 or uniequip.type_name2 in 目标模组等级字典
            if 在初始模组等级字典中 and 在目标模组等级字典中:
                初始模组等级 = (初始模组等级字典[uniequip_id] if uniequip_id in 初始模组等级字典
                          else 初始模组等级字典[uniequip.type_name2])  # type: ignore
                目标模组等级 = (目标模组等级字典[uniequip_id] if uniequip_id in 目标模组等级字典
                          else 目标模组等级字典[uniequip.type_name2])  # type: ignore
                item_info_list.extend(self.模组升级消耗(uniequip_id, 初始模组等级, 目标模组等级))
            elif 在初始模组等级字典中 or 在目标模组等级字典中:
                raise ValueError(f"模组 {uniequip!r} 的初始等级和目标等级需同时指定")
        return item_info_list

    def 拉满消耗(self) -> ItemInfoList:
        """
        未对升变干员特殊处理
        """
        item_info_list = ItemInfoList()
        item_info_list.extend(self.精英化等级升级消耗())
        item_info_list.extend(self.通用技能升级消耗())
        for 技能序号 in range(1, self.skill_count + 1):
            item_info_list.extend(self.技能专精消耗(技能序号))
        for uniequip in self.uniquips().values():
            item_info_list.extend(uniequip.升级消耗())
        return item_info_list

    def __repr__(self) -> str:
        return f"<{self.__class__.__module__}.{self.__class__.__name__} id={self.id!r} name={self.name!r}>"


class UniEquipDict(dict[str, UniEquip]):
    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__name__}({super().__repr__()})"
