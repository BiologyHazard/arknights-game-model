from __future__ import annotations

from typing import TYPE_CHECKING

from ._raw_game_data import ArknightsGameData, load_data
from ._raw_game_data.excel.item_table import Item as ItemInGame
from .building_model import WorkshopFormula
from .character_model import Character, UniEquip, UniEquipDict
from .config import get_config
from .item_info_model import ItemInfoList
from .item_model import Item
from .log import logger
from .utils import 计算累计消耗

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path
    from typing import Self

    from ._raw_game_data.excel.character_table import CharacterData


class CharacterDict(dict[str, Character]):
    def by_id(self, character_id: str) -> Character:
        return self[character_id]

    def by_name(self, character_name: str) -> Character:
        for character in self.values():
            if character.name == character_name:
                return character
        raise KeyError(f"Character {character_name!r} not found")

    def filter(self, function: Callable[[Character], bool]) -> Self:
        return self.__class__((k, v) for k, v in self.items() if function(v))

    def 全干员拉满消耗(self) -> ItemInfoList:
        item_info_list = ItemInfoList()
        for character in self.values():
            item_info_list.extend(character.拉满消耗())
        return item_info_list

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__name__}({super().__repr__()})"


class ItemDict(dict[str, Item]):
    def by_id(self, item_id: str) -> Item:
        return self[item_id]

    def by_name(self, item_name: str) -> Item:
        for item in self.values():
            if item.name == item_name:
                return item
        raise ValueError(f"Item {item_name!r} not found")

    def filter(self, function: Callable[[Item], bool]) -> Self:
        return self.__class__((k, v) for k, v in self.items() if function(v))

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__name__}({super().__repr__()})"


class GameData:
    raw_data: ArknightsGameData
    characters: CharacterDict
    items: ItemDict
    uniequips: dict[str, UniEquip]
    workshop_formulas: dict[str, WorkshopFormula]

    def load_data(self) -> None:
        logger.info("Loading game data...")
        config = get_config()
        logger.configure(extra={"arknights_game_model_log_level": config.log_level})
        logger.info(f"Loaded config: {config!r}")

        self.raw_data = load_data(config.gamedata_folder)
        self.load_characters(config.online_time_path)
        self.load_items(config.yituliu_item_value_path)
        self.load_uniequips()
        self.load_workshop_formulas()
        self.calc_game_consts()

    def _is_char_in_game(self, char_id: str, character_data: CharacterData) -> bool:
        """
        判断是否为实装干员，有这么几种方法：
        1. 在 `building_data` 的 `chars` 字典的 key 中（判断是否有基建技能）
        2. `item_obtain_approach` 不为 `None`
        """
        criterion_1 = char_id in self.raw_data.excel.building_data.chars
        criterion_2 = character_data.item_obtain_approach is not None
        if not (criterion_1 == criterion_2):
            logger.warning(
                f"干员 {char_id} 的实装状态不一致：根据基建技能判断为 {criterion_1}，根据获取途径判断为 {criterion_2}"
            )
        return criterion_1 or criterion_2

    def load_characters(self, online_time_path: Path):
        # 非升变干员
        self.characters = CharacterDict(
            (id, Character(id=id, raw_data=character_data, is_patch_char=False))
            for id, character_data in self.raw_data.excel.character_table.items()
            if self._is_char_in_game(id, character_data)
        )
        # 升变干员
        self.characters.update(
            (id, Character(id=id, raw_data=character, is_patch_char=True))
            for id, character in self.raw_data.excel.char_patch_table.patch_chars.items()
        )
        # 干员上线时间
        from .prts_wiki.char_cn_online_time_patch import patch_to

        patch_to(self, online_time_path)

    def load_items(self, yituliu_item_value_path: Path):
        self.items = ItemDict((id, Item(raw_data=item)) for id, item in self.raw_data.excel.item_table.items.items())

        # 添加 EXP 物品
        exp_item_in_game = ItemInGame(
            item_id="exp",
            name="EXP",
            description=None,
            rarity=0,
            icon_id="",
            override_bkg=None,
            stack_icon_id=None,
            sort_id=0,
            usage=None,
            obtain_approach=None,
            hide_in_item_get=False,
            classify_type="MATERIAL",
            item_type="EXP",
            stage_drop_list=[],
            building_product_list=[],
            voucher_relate_list=[],
            shop_relate_info_list=[],
        )
        EXP_item = Item(exp_item_in_game)
        self.items[exp_item_in_game.item_id] = EXP_item

        # 一图流物品价值
        from .yituliu.item_value import patch_to

        patch_to(self, yituliu_item_value_path)

    def load_uniequips(self):
        # 获取模组上线时间
        equip_online_timestamp: dict[str, int] = {}
        for equip_track in self.raw_data.excel.uniequip_table.equip_track_dict:
            for track_item in equip_track.track_list:
                equip_online_timestamp[track_item.equip_id] = equip_track.time_stamp

        self.uniequips = UniEquipDict(
            (uniequip_id, UniEquip(uniequip, online_timestamp=equip_online_timestamp[uniequip_id]))
            for uniequip_id, uniequip in self.raw_data.excel.uniequip_table.equip_dict.items()
        )

    def load_workshop_formulas(self):
        self.workshop_formulas = dict(
            (id, WorkshopFormula(formula)) for id, formula in self.raw_data.excel.building_data.workshop_formulas.items()
        )

    def calc_game_consts(self):
        self.累计消耗EXP = 计算累计消耗(self.raw_data.excel.gamedata_const.character_exp_map)
        self.累计消耗龙门币 = 计算累计消耗(self.raw_data.excel.gamedata_const.character_upgrade_cost_map)


game_data = GameData()
