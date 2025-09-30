from enum import StrEnum
from typing import Any, Literal

from pydantic import ConfigDict, Field

from arknights_game_model.item_info_model import ItemBundle

from .model import GameDataModel


class RoomType(StrEnum):
    NONE = 'NONE'
    CONTROL = 'CONTROL'
    POWER = 'POWER'
    MANUFACTURE = 'MANUFACTURE'
    SHOP = 'SHOP'
    DORMITORY = 'DORMITORY'
    MEETING = 'MEETING'
    HIRE = 'HIRE'
    ELEVATOR = 'ELEVATOR'
    CORRIDOR = 'CORRIDOR'
    TRADING = 'TRADING'
    WORKSHOP = 'WORKSHOP'
    TRAINING = 'TRAINING'
    PRIVATE = 'PRIVATE'
    FUNCTIONAL = 'FUNCTIONAL'
    ALL = 'ALL'


class FormulaItemType(StrEnum):
    NONE = 'NONE'
    F_EVOLVE = 'F_EVOLVE'
    F_BUILDING = 'F_BUILDING'
    F_GOLD = 'F_GOLD'
    F_DIAMOND = 'F_DIAMOND'
    F_FURNITURE = 'F_FURNITURE'
    F_EXP = 'F_EXP'
    F_ASC = 'F_ASC'
    F_SKILL = 'F_SKILL'


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


class UnlockRoom(GameDataModel):
    room_id: RoomType = Field(strict=False)
    room_level: int
    room_count: int


class UnlockStage(GameDataModel):
    stage_id: str
    rank: int


class ManufactFormula(GameDataModel):
    formula_id: str
    item_id: str
    count: int
    weight: int
    cost_point: int
    formula_type: FormulaItemType = Field(strict=False)
    buff_type: str
    costs: list[ItemBundle]
    require_rooms: list[UnlockRoom]
    require_stages: list[UnlockStage]


class ExtraOutcome(GameDataModel):
    weight: int
    item_id: str
    item_count: int


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
    require_rooms: list[UnlockRoom]
    require_stages: list[UnlockStage]


class BuildingData(GameDataModel):
    model_config = ConfigDict(extra="allow")

    chars: dict[str, Char]
    buffs: dict[str, Buff]
    manufact_formulas: dict[str, ManufactFormula]
    # shop_formulas: dict[str, Any]  # 空字典
    workshop_formulas: dict[str, WorkshopFormula]
    trading_order_des_dict: dict[str, str]
