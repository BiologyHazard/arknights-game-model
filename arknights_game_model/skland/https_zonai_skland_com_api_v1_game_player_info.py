from typing import Any

from arknights_game_model._raw_game_data.model import GameDataModel


class ShowConfig(GameDataModel):
    char_switch: bool
    skin_switch: bool
    standings_switch: bool


class Avatar(GameDataModel):
    type: str
    id: str
    url: str


class Secretary(GameDataModel):
    char_id: str
    skin_id: str


class Ap(GameDataModel):
    current: int
    max: int
    last_ap_add_time: int
    complete_recovery_time: int


class Exp(GameDataModel):
    current: int
    max: int


class Status(GameDataModel):
    uid: str
    name: str
    level: int
    avatar: Avatar
    register_ts: int
    main_stage_progress: str
    secretary: Secretary
    resume: str
    subscription_end: int
    ap: Ap
    store_ts: int
    last_online_ts: int
    char_cnt: int
    furniture_cnt: int
    skin_cnt: int
    exp: Exp


class Medal(GameDataModel):
    type: str
    template: str
    template_medal_list: list[str]
    custom_medal_layout: list[Any]
    total: int


class AssistEquip(GameDataModel):
    id: str
    level: int
    locked: bool


class AssistChar(GameDataModel):
    char_id: str
    skin_id: str
    level: int
    evolve_phase: int
    potential_rank: int
    skill_id: str
    main_skill_lvl: int
    specialize_level: int
    equip: AssistEquip | None


class Skill(GameDataModel):
    id: str
    specialize_level: int


class Equip(GameDataModel):
    id: str
    level: int
    locked: bool


class Char(GameDataModel):
    char_id: str
    skin_id: str
    level: int
    evolve_phase: int
    potential_rank: int
    main_skill_lvl: int
    skills: list[Skill]
    equip: list[Equip]
    favor_percent: int
    default_skill_id: str
    gain_time: int
    default_equip_id: str
    sort_id: int
    exp: int
    gold: int
    rarity: int


class Skin(GameDataModel):
    id: str
    ts: int


class BubbleInfo(GameDataModel):
    add: int
    ts: int


class Bubble(GameDataModel):
    normal: BubbleInfo
    assist: BubbleInfo


class BaseChar(GameDataModel):
    char_id: str
    ap: int
    last_ap_add_time: int
    index: int
    bubble: Bubble
    work_time: int


class TiredChar(BaseChar):
    room_slot_id: str


class PowerChar(BaseChar):
    pass


class ManufactureChar(BaseChar):
    pass


class TradingChar(BaseChar):
    pass


class DormitoryChar(BaseChar):
    pass


class MeetingChar(BaseChar):
    pass


class HireChar(BaseChar):
    pass


class ControlChar(BaseChar):
    pass


class BaseRoom(GameDataModel):
    slot_id: str
    level: int


class Power(BaseRoom):
    chars: list[PowerChar]


class Manufacture(BaseRoom):
    chars: list[ManufactureChar]
    complete_work_time: int
    last_update_time: int
    formula_id: str
    capacity: int
    weight: int
    complete: int
    remain: int
    speed: float


class Trading(BaseRoom):
    chars: list[TradingChar]
    complete_work_time: int
    last_update_time: int
    strategy: str
    stock: list[Any]
    stock_limit: int


class Dormitory(BaseRoom):
    # slot_id: str
    # level: int
    chars: list[DormitoryChar]
    comfort: int


class Clue(GameDataModel):
    own: int
    received: int
    daily_reward: bool
    need_receive: int
    board: list[Any]
    sharing: bool
    share_complete_time: int


class Meeting(BaseRoom):
    chars: list[MeetingChar]
    clue: Clue
    last_update_time: int
    complete_work_time: int


class Hire(BaseRoom):
    # slot_id: str
    # level: int
    chars: list[HireChar]
    state: int
    refresh_count: int
    complete_work_time: int
    slot_state: int


class Trainee(GameDataModel):
    char_id: str
    target_skill: int
    ap: int
    last_ap_add_time: int


class Trainer(GameDataModel):
    char_id: str
    ap: int
    last_ap_add_time: int


class Training(BaseRoom):
    trainee: Trainee
    trainer: Trainer
    remain_point: float
    speed: float
    last_update_time: int
    remain_secs: int
    slot_state: int


class Labor(GameDataModel):
    max_value: int
    value: int
    last_update_time: int
    remain_secs: int


class Furniture(GameDataModel):
    total: int


class Elevator(BaseRoom):
    # slot_id: str
    slot_state: int
    # level: int


class Corridor(BaseRoom):
    # slot_id: str
    slot_state: int
    # level: int


class Control(BaseRoom):
    # slot_id: str
    slot_state: int
    # level: int
    chars: list[ControlChar]


class Building(GameDataModel):
    tired_chars: list[TiredChar]
    powers: list[Power]
    manufactures: list[Manufacture]
    tradings: list[Trading]
    dormitories: list[Dormitory]
    meeting: Meeting
    hire: Hire | None  # 可能为 None
    training: Training | None  # 可能为 None
    labor: Labor
    furniture: Furniture
    elevators: list[Elevator]
    corridors: list[Corridor]
    control: Control


class RecruitItem(GameDataModel):
    """公开招募格子信息"""
    start_ts: int
    """公开招募开始的时间戳"""
    finish_ts: int
    """公开招募结束的时间戳"""
    state: int
    """2 表示正在招募，1 表示空闲，推测 0 表示未解锁（？）"""


class CampaignRecord(GameDataModel):
    """剿灭作战单个作战记录"""
    campaign_id: str
    """剿灭作战 ID"""
    max_kills: int
    """单次作战击杀数最高记录"""


class CampaignReward(GameDataModel):
    """剿灭作战每周奖励"""
    current: int
    """本周已获取的合成玉报酬"""
    total: int
    """每周报酬上限"""


class Campaign(GameDataModel):
    """剿灭作战信息"""
    records: list[CampaignRecord]
    reward: CampaignReward


class TowerRecord(GameDataModel):
    tower_id: str
    best: int


class TowerRewardItem(GameDataModel):
    current: int
    total: int


class TowerReward(GameDataModel):
    higher_item: TowerRewardItem
    lower_item: TowerRewardItem
    term_ts: int


class Tower(GameDataModel):
    """保全派驻信息"""
    records: list[TowerRecord]
    reward: TowerReward


class RogueBank(GameDataModel):
    current: int
    record: int


class RogueMedal(GameDataModel):
    total: int
    current: int


class RogueRecord(GameDataModel):
    rogue_id: str
    relic_cnt: int
    bank: RogueBank
    clear_time: int
    bp_level: int
    medal: RogueMedal


class Rogue(GameDataModel):
    """集成战略"""
    records: list[RogueRecord]


class RoutineProgress(GameDataModel):
    current: int
    total: int


class Routine(GameDataModel):
    """任务"""
    daily: RoutineProgress
    weekly: RoutineProgress


class ActivityZone(GameDataModel):
    zone_id: str
    zone_replica_id: str
    cleared_stage: int
    total_stage: int


class Activity(GameDataModel):
    """活动"""
    act_id: str
    act_replica_id: str
    zones: list[ActivityZone]


class CharInfo(GameDataModel):
    """干员信息"""
    id: str
    name: str
    nation_id: str
    group_id: str
    display_number: str
    rarity: int
    profession: str
    sub_profession_id: str
    sub_profession_name: str
    appellation: str
    sort_id: int


class SkinInfo(GameDataModel):
    """皮肤信息"""
    id: str
    name: str
    brand_id: str
    sort_id: int
    display_tag_id: str
    char_id: str


class StageInfo(GameDataModel):
    id: str
    code: str
    name: str
    zone_id: str
    diff_group: str
    stage_type: str
    danger_level: str
    ap_cost: int
    difficulty: str


class ActivityInfo(GameDataModel):
    """活动信息"""
    id: str
    name: str
    start_time: int
    end_time: int
    reward_end_time: int
    is_replicate: bool
    type: str
    drop_item_ids: list[str]
    shop_good_item_ids: list[str]
    favor_up_list: list[str]
    pic_url: str


class TowerInfo(GameDataModel):
    """保全派驻信息模型"""
    id: str
    name: str
    sub_name: str
    pic_url: str


class RogueInfo(GameDataModel):
    """集成战略信息"""
    id: str
    name: str
    sort: int
    pic_url: str


class CampaignInfo(GameDataModel):
    """剿灭作战信息"""
    id: str
    name: str
    campaign_zone_id: str
    pic_url: str


class CampaignZoneInfo(GameDataModel):
    """剿灭作战区域信息"""
    id: str
    name: str


class EquipmentInfo(GameDataModel):
    """模组信息模型"""
    id: str
    name: str
    type_icon: str
    type_name2: str | None = None
    shining_color: str


class ManufactureFormulaInfo(GameDataModel):
    """制造配方信息模型"""
    id: str
    item_id: str
    count: int
    weight: int
    costs: list[Any]
    cost_point: int


class CharAssetList(GameDataModel):
    ids: list[str]


class SkinAssetList(GameDataModel):
    ids: list[str]


class ActivityBannerList(GameDataModel):
    list: list[Any]  # 空列表


class BossRushRecord(GameDataModel):
    played: bool
    stage_id: str
    difficulty: str


class BossRush(GameDataModel):
    """引航者试炼"""
    id: str
    record: BossRushRecord
    pic_url: str


class Banner(GameDataModel):
    """森空岛 Banner"""
    id: str
    sort_id: int
    img_url: str
    link: str
    start_at_ts: str
    end_at_ts: str
    status: int


class SandboxSubQuest(GameDataModel):
    id: str
    name: str
    done: bool


class Sandbox(GameDataModel):
    """生息演算"""
    id: str
    name: str
    max_day: int
    max_day_challenge: int
    main_quest: int
    sub_quest: list[SandboxSubQuest]
    base_lv: int
    unlock_node: int
    enemy_kill: int
    create_rift: int
    fix_rift: list[int]
    pic_url: str


class Data(GameDataModel):
    current_ts: int
    show_config: ShowConfig
    status: Status
    medal: Medal
    assist_chars: list[AssistChar]
    chars: list[Char]
    skins: list[Skin]
    building: Building
    recruit: list[RecruitItem]
    campaign: Campaign
    tower: Tower
    rogue: Rogue
    routine: Routine
    activity: list[Activity]
    char_info_map: dict[str, CharInfo]
    skin_info_map: dict[str, SkinInfo]
    stage_info_map: dict[str, StageInfo]
    activity_info_map: dict[str, ActivityInfo]
    tower_info_map: dict[str, TowerInfo]
    rogue_info_map: dict[str, RogueInfo]
    campaign_info_map: dict[str, CampaignInfo]
    campaign_zone_info_map: dict[str, CampaignZoneInfo]
    equipment_info_map: dict[str, EquipmentInfo]
    manufacture_formula_info_map: dict[str, ManufactureFormulaInfo]
    char_assets: list[str]
    skin_assets: list[str]
    char_asset_list: CharAssetList | None = None  # 可能不存在
    skin_asset_list: SkinAssetList | None = None  # 可能不存在
    activity_banner_list: ActivityBannerList
    boss_rush: list[BossRush]
    banner_list: list[Banner]
    sandbox: list[Sandbox]


class HttpsZonaiSklandComApiV1GamePlayerInfo(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
