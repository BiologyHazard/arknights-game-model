from __future__ import annotations

from ._raw_game_data.character_table import Character as CharacterInGame
from ._raw_game_data.item_table import Item as ItemInGame
from ._raw_game_data.uniequip_table import Uniequip as UniequipInGame


class Item:
    _raw_data: ItemInGame

    def __init__(self, raw_data: ItemInGame):
        self._raw_data = raw_data

    @property
    def item_id(self) -> str:
        return self._raw_data.item_id

    @property
    def name(self) -> str:
        return self._raw_data.name
