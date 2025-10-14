from typing import Any

from arknights_game_model.model import GameDataModel

from .character_table import CharacterData


class CharPatchTable(GameDataModel):
    infos: dict[str, Any]
    patch_chars: dict[str, CharacterData]
    unlock_conds: dict[str, Any]
    patch_detail_info_list: dict[str, Any]
