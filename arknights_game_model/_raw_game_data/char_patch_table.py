from typing import Any

from .model import GameDataModel
from .character_table import Character


class CharPatchTable(GameDataModel):
    infos: dict[str, Any]
    patch_chars: dict[str, Character]
    unlock_conds: dict[str, Any]
    patch_detail_info_list: dict[str, Any]
