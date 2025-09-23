from typing import Any, Literal

from pydantic import ConfigDict

from arknights_game_model.item_info_model import ItemBundle

from .model import GameDataModel


class Cond(GameDataModel):
    phase: int
    level: int


class BuffDataItem(GameDataModel):
    buff_id: str
    cond: Cond


class BuffCharItem(GameDataModel):
    buff_data: list[BuffDataItem]


class Char(GameDataModel):
    char_id: str
    max_manpower: Literal[8640000]
    buff_char: list[BuffCharItem]


class Buff(GameDataModel):
    buff_id: str
    buff_name: str
    buff_icon: str
    skill_icon: str
    sort_id: int
    buff_color: str
    text_color: str
    buff_category: str
    room_type: str
    description: str
    efficiency: int
    target_group_sort_id: int
    targets: list[str]


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
    costs: list[ItemBundle]
    require_rooms: list[RequireRoom]
    require_stages: list[Any]


class BuildingData(GameDataModel):
    model_config = ConfigDict(extra="allow")

    chars: dict[str, Char]
    buffs: dict[str, Buff]
    workshop_formulas: dict[str, WorkshopFormula]
