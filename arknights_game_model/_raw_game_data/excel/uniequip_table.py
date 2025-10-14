from pydantic_extra_types.color import Color

from arknights_game_model.item_info_model import ItemBundle
from arknights_game_model.model import GameDataModel


class UniEquipData(GameDataModel, strict=False):
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
    item_cost: dict[int, list[ItemBundle]]
    type: str
    uni_equip_get_time: int
    uni_equip_show_end: int
    char_equip_order: int
    has_unlock_mission: bool
    is_special_equip: bool
    special_equip_desc: str | None
    special_equip_color: Color | None
    char_color: Color | None


class UniEquipMissionData(GameDataModel):
    template: str
    desc: str
    param_list: list[str]
    uni_equip_mission_id: str
    uni_equip_mission_sort: int
    uni_equip_id: str
    jump_stage_id: str | None


class SubProfessionData(GameDataModel):
    sub_profession_id: str
    sub_profession_name: str
    sub_profession_catagory: int


class UniEquipTypeInfo(GameDataModel):
    uni_equip_type_name: str
    sort_id: int
    is_special: bool
    is_initial: bool


class UniEquipTrack(GameDataModel):
    char_id: str
    equip_id: str
    type: int
    archive_show_time_end: int


class UniEquipTimeInfo(GameDataModel):
    time_stamp: int
    track_list: list[UniEquipTrack]


class UniEquipTable(GameDataModel):
    equip_dict: dict[str, UniEquipData]
    mission_list: dict[str, UniEquipMissionData]
    sub_prof_dict: dict[str, SubProfessionData]
    sub_prof_to_prof_dict: dict[str, int]
    char_equip: dict[str, list[str]]
    equip_type_infos: list[UniEquipTypeInfo]
    equip_track_dict: list[UniEquipTimeInfo]
