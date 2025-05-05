
from typing import Any

from ..item_info_model import ItemInfoDict
from .model import GameDataModel


class BreakLadder(GameDataModel):
    kill_cnt: int
    break_fee_add: int
    rewards: list[ItemInfoDict]


class Campaign(GameDataModel):
    stage_id: str
    is_small_scale: int
    break_ladders: list[BreakLadder]
    is_customized: bool
    drop_gains: dict[str, Any]


class CampaignRotateStageOpenTime(GameDataModel):
    group_id: str
    stage_id: str
    map_id: str
    unknown_regions: list[str]
    duration: int
    start_ts: int
    end_ts: int


class CampaignTable(GameDataModel):
    campaigns: dict[str, Campaign]
    campaign_groups: dict[str, Any]
    campaign_regions: dict[str, Any]
    campaign_zones: dict[str, Any]
    campaign_missions: dict[str, Any]
    stage_index_in_zone_map: dict[str, Any]
    campaign_const_table: dict[str, Any]
    campaign_rotate_stage_open_times: list[CampaignRotateStageOpenTime]
    campaign_training_stage_open_times: list[Any]
    campaign_training_all_open_times: list[Any]
