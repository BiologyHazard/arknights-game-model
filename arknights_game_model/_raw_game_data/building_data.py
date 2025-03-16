from typing import Any

from pydantic import ConfigDict

from .model import GameDataModel
from ..item_info_model import ItemInfoDict


class ExtraOutcome(GameDataModel):
    weight: int
    item_id: str
    item_count: int


class RequireRoom(GameDataModel):
    room_id: str
    room_level: int
    room_count: int


class UnlockStage(GameDataModel):
    stage_id: str
    rank: int


class WorkshopFormula(GameDataModel):
    sort_id: int
    formula_id: str
    rarity: int
    item_id: str
    count: int
    gold_cost: int
    ap_cost: int
    formula_type: str
    buff_type: str
    extra_outcome_rate: float
    extra_outcome_group: list[ExtraOutcome]
    costs: list[ItemInfoDict]
    require_rooms: list[RequireRoom]
    require_stages: list[Any]


class BuildingData(GameDataModel):
    model_config = ConfigDict(extra="allow")

    chars: dict[str, Any]
    workshop_formulas: dict[str, WorkshopFormula]
