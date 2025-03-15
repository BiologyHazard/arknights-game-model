from typing import Any, Optional

from pydantic import Field
from pydantic_extra_types.color import Color

from .model import GameDataModel
from ..item_info_model import ItemInfoDict


class Uniequip(GameDataModel):
    uni_equip_id: str
    uni_equip_name: str
    uni_equip_icon: str
    uni_equip_desc: str
    type_icon: str
    type_name1: str
    type_name2: str | None
    equip_shining_color: str
    show_evolve_phase: int
    unlock_evolve_phase: int
    char_id: str
    tmpl_id: str | None
    show_level: int
    unlock_level: int
    mission_list: list[str]
    unlock_favors: dict[str, int]
    item_cost: dict[str, list[ItemInfoDict]]
    type: str
    uni_equip_get_time: int
    uni_equip_show_end: int
    char_equip_order: int
    has_unlock_mission: bool
    is_special_equip: bool
    special_equip_desc: str | None
    special_equip_color: Color | None
    char_color: Color | None


class Mission(GameDataModel):
    template: str
    desc: str
    param_list: list[str]
    uni_equip_mission_id: str
    uni_equip_mission_sort: int
    uni_equip_id: str
    jump_stage_id: str | None


class SubProf(GameDataModel):
    sub_profession_id: str
    sub_profession_name: str
    sub_profession_catagory: int


class EquipTypeInfo(GameDataModel):
    uni_equip_type_name: str
    sort_id: int
    is_special: bool
    is_initial: bool


class EquipTrackInfo(GameDataModel):
    char_id: str
    equip_id: str
    type: int
    archive_show_time_end: int


class EquipTrack(GameDataModel):
    time_stamp: int
    track_list: list[EquipTrackInfo]


class UniequipTable(GameDataModel):
    equip_dict: dict[str, Uniequip]
    mission_list: dict[str, Mission]
    sub_prof_dict: dict[str, SubProf]
    sub_prof_to_prof_dict: dict[str, int]
    char_equip: dict[str, list[str]]
    equip_type_infos: list[EquipTypeInfo]
    equip_track_dict: list[EquipTrack]
