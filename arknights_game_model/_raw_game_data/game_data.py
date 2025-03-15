import json
from pathlib import Path

from pydantic import BaseModel

from .character_table import CharacterTable
from .gamedata_const import GamedataConst
from .item_table import ItemTable
from .uniequip_table import UniequipTable


class Excel(BaseModel):
    character_table: CharacterTable
    gamedata_const: GamedataConst
    item_table: ItemTable
    uniequip_table: UniequipTable


class ArknightsGameData(BaseModel):
    excel: Excel


data_structure = {
    "excel": {
        "character_table": "json",
        "gamedata_const": "json",
        "item_table": "json",
        "uniequip_table": "json",
    }
}


def _load_recursive(path: Path, structure: dict) -> dict:
    data = {}
    for key, value in structure.items():
        if isinstance(value, dict):
            data[key] = _load_recursive(path / key, value)
        elif value == "json":
            file_path = path / f"{key}.{value}"
            with open(file_path, 'r', encoding='utf-8') as f:
                data[key] = json.load(f)
    return data


def load_data(path: Path):
    return _load_recursive(path, data_structure)
