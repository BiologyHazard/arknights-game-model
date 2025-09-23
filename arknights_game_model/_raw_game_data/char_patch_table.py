from typing import Any

from .character_table import CharacterData
from .model import GameDataModel


class CharPatchTable(GameDataModel):
    infos: dict[str, Any]
    patch_chars: dict[str, CharacterData]
    unlock_conds: dict[str, Any]
    patch_detail_info_list: dict[str, Any]
