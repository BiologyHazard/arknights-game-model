import json
from pathlib import Path
from typing import Any

from arknights_game_model.model import GameDataModel

from .excel.building_data import BuildingData
from .excel.campaign_table import CampaignTable
from .excel.char_patch_table import CharPatchTable
from .excel.character_table import CharacterTable
from .excel.gamedata_const import GamedataConst
from .excel.item_table import ItemTable
from .excel.stage_table import StageTable
from .excel.uniequip_table import UniEquipTable


class Excel(GameDataModel):
    building_data: BuildingData
    campaign_table: CampaignTable
    char_patch_table: CharPatchTable
    character_table: CharacterTable
    gamedata_const: GamedataConst
    item_table: ItemTable
    stage_table: StageTable
    uniequip_table: UniEquipTable


class ArknightsGameData(GameDataModel):
    excel: Excel


data_structure = {
    "excel": {
        "building_data": "json",
        "campaign_table": "json",
        "char_patch_table": "json",
        "character_table": "json",
        "gamedata_const": "json",
        "item_table": "json",
        "stage_table": "json",
        "uniequip_table": "json",
    },
}


def _load_recursive(path: Path, structure: dict[str, Any]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for key, value in structure.items():
        if isinstance(value, dict):
            data[key] = _load_recursive(path / key, value)  # type: ignore
        elif value == "json":
            file_path = path / f"{key}.{value}"
            with file_path.open("r", encoding="utf-8") as f:
                data[key] = json.load(f)
    return data


def load_data(path: Path):
    return _load_recursive(path, data_structure)
