from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Callable, Self

from arknights_game_model.character_model import UniEquipDict

from ._raw_game_data.game_data import ArknightsGameData, load_data
from ._raw_game_data.item_table import Item as ItemInGame
from .character_model import Character, UniEquip
from .item_model import Item
from .utils import 计算累计消耗


class CharacterDict(dict[str, Character]):
    def by_id(self, character_id: str) -> Character:
        return self[character_id]

    def by_name(self, character_name: str) -> Character:
        for character in self.values():
            if character.name == character_name:
                return character
        raise ValueError(f"Character {character_name!r} not found")

    def filter(self, function: Callable[[Character], bool]) -> Self:
        return self.__class__((k, v) for k, v in self.items() if function(v))


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


class GameData:
    _raw_data: ArknightsGameData
    characters: CharacterDict
    items: ItemDict
    uniequips: dict[str, UniEquip]

    def load_data(self, path: Path = Path("ArknightsGameResource/gamedata")):
        self._raw_data = ArknightsGameData.model_validate(load_data(path))
        self.load_characters()
        self.load_items()
        self.load_uniequips()
        self.calc_game_consts()

    def load_characters(self):
        self.characters = CharacterDict(
            (id, Character(id=id, raw_data=character))
            for id, character in self._raw_data.excel.character_table.items()
        )

    def load_items(self):
        self.items = ItemDict(
            (id, Item(raw_data=item))
            for id, item in self._raw_data.excel.item_table.items.items()
        )

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
        )

        EXP_item = Item(exp_item_in_game)
        self.items[exp_item_in_game.item_id] = EXP_item

    def load_uniequips(self):
        self.uniequips = UniEquipDict(
            (id, UniEquip(uniequip))
            for id, uniequip in self._raw_data.excel.uniequip_table.equip_dict.items()
        )

    def calc_game_consts(self):
        self.累计消耗EXP = 计算累计消耗(self._raw_data.excel.gamedata_const.character_exp_map)
        self.累计消耗龙门币 = 计算累计消耗(self._raw_data.excel.gamedata_const.character_upgrade_cost_map)


game_data = GameData()
