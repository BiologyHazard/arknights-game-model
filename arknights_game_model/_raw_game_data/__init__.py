import json
from pathlib import Path
from typing import Any

from pydantic.config import ExtraValues

from arknights_game_model.model import GameDataModel

from .excel import Excel


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
            data[key] = _load_recursive(path / key, value)
        elif value == "json":
            file_path = path / f"{key}.{value}"
            with file_path.open("r", encoding="utf-8") as f:
                data[key] = json.load(f)
    return data


def load_data(path: Path, *, strict: bool | None = None, extra: ExtraValues | None = None) -> ArknightsGameData:
    if strict:
        strict = None
    if extra == "forbid":
        extra = None
    return ArknightsGameData.model_validate(_load_recursive(path, data_structure), strict=strict, extra=extra)
