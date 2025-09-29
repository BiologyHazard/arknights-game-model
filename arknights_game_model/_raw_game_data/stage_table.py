from enum import Enum, IntEnum, StrEnum

from pydantic import Field

from ..item_info_model import ItemBundle
from .model import GameDataModel


class StageType(StrEnum):
    MAIN = 'MAIN'
    DAILY = 'DAILY'
    TRAINING = 'TRAINING'
    ACTIVITY = 'ACTIVITY'
    GUIDE = 'GUIDE'
    SUB = 'SUB'
    CAMPAIGN = 'CAMPAIGN'
    SPECIAL_STORY = 'SPECIAL_STORY'
    HANDBOOK_BATTLE = 'HANDBOOK_BATTLE'
    CLIMB_TOWER = 'CLIMB_TOWER'
    ENUM = 'ENUM'


class LevelData_Difficulty(StrEnum):
    NONE = 'NONE'
    NORMAL = 'NORMAL'
    FOUR_STAR = 'FOUR_STAR'
    EASY = 'EASY'
    SIX_STAR = 'SIX_STAR'
    ALL = 'ALL'


class StageData_PerformanceStageFlag(StrEnum):
    NORMAL_STAGE = 'NORMAL_STAGE'
    PERFORMANCE_STAGE = 'PERFORMANCE_STAGE'


class StageDiffGroup(StrEnum):
    NONE = 'NONE'
    EASY = 'EASY'
    NORMAL = 'NORMAL'
    TOUGH = 'TOUGH'
    ALL = 'ALL'


class PlayerBattleRank(StrEnum):
    FAIL = 'FAIL'
    PASS = 'PASS'
    COMPLETE = 'COMPLETE'
    ERR_ZERO = 'ERR_ZERO'


class StageData_ConditionDesc(GameDataModel):
    stage_id: str
    complete_state: PlayerBattleRank | int  # kengxxiao 的仓库是 str，yuanyan3060 的仓库是 int


class AppearanceStyle(StrEnum):
    MAIN_NORMAL = 'MAIN_NORMAL'
    MAIN_PREDEFINED = 'MAIN_PREDEFINED'
    SUB = 'SUB'
    TRAINING = 'TRAINING'
    HIGH_DIFFICULTY = 'HIGH_DIFFICULTY'
    MIST_OPS = 'MIST_OPS'
    SPECIAL_STORY = 'SPECIAL_STORY'


class ItemType(StrEnum):
    NONE = 'NONE'
    CHAR = 'CHAR'
    CARD_EXP = 'CARD_EXP'
    MATERIAL = 'MATERIAL'
    GOLD = 'GOLD'
    EXP_PLAYER = 'EXP_PLAYER'
    TKT_TRY = 'TKT_TRY'
    TKT_RECRUIT = 'TKT_RECRUIT'
    TKT_INST_FIN = 'TKT_INST_FIN'
    TKT_GACHA = 'TKT_GACHA'
    ACTIVITY_COIN = 'ACTIVITY_COIN'
    DIAMOND = 'DIAMOND'
    DIAMOND_SHD = 'DIAMOND_SHD'
    HGG_SHD = 'HGG_SHD'
    LGG_SHD = 'LGG_SHD'
    FURN = 'FURN'
    AP_GAMEPLAY = 'AP_GAMEPLAY'
    AP_BASE = 'AP_BASE'
    SOCIAL_PT = 'SOCIAL_PT'
    CHAR_SKIN = 'CHAR_SKIN'
    TKT_GACHA_10 = 'TKT_GACHA_10'
    TKT_GACHA_PRSV = 'TKT_GACHA_PRSV'
    AP_ITEM = 'AP_ITEM'
    AP_SUPPLY = 'AP_SUPPLY'
    RENAMING_CARD = 'RENAMING_CARD'
    RENAMING_CARD_2 = 'RENAMING_CARD_2'
    ET_STAGE = 'ET_STAGE'
    ACTIVITY_ITEM = 'ACTIVITY_ITEM'
    VOUCHER_PICK = 'VOUCHER_PICK'
    VOUCHER_CGACHA = 'VOUCHER_CGACHA'
    VOUCHER_MGACHA = 'VOUCHER_MGACHA'
    CRS_SHOP_COIN = 'CRS_SHOP_COIN'
    CRS_RUNE_COIN = 'CRS_RUNE_COIN'
    LMTGS_COIN = 'LMTGS_COIN'
    EPGS_COIN = 'EPGS_COIN'
    LIMITED_TKT_GACHA_10 = 'LIMITED_TKT_GACHA_10'
    LIMITED_FREE_GACHA = 'LIMITED_FREE_GACHA'
    REP_COIN = 'REP_COIN'
    ROGUELIKE = 'ROGUELIKE'
    LINKAGE_TKT_GACHA_10 = 'LINKAGE_TKT_GACHA_10'
    VOUCHER_ELITE_II_4 = 'VOUCHER_ELITE_II_4'
    VOUCHER_ELITE_II_5 = 'VOUCHER_ELITE_II_5'
    VOUCHER_ELITE_II_6 = 'VOUCHER_ELITE_II_6'
    VOUCHER_SKIN = 'VOUCHER_SKIN'
    RETRO_COIN = 'RETRO_COIN'
    PLAYER_AVATAR = 'PLAYER_AVATAR'
    UNI_COLLECTION = 'UNI_COLLECTION'
    VOUCHER_FULL_POTENTIAL = 'VOUCHER_FULL_POTENTIAL'
    RL_COIN = 'RL_COIN'
    RETURN_CREDIT = 'RETURN_CREDIT'
    MEDAL = 'MEDAL'
    CHARM = 'CHARM'
    HOME_BACKGROUND = 'HOME_BACKGROUND'
    EXTERMINATION_AGENT = 'EXTERMINATION_AGENT'
    OPTIONAL_VOUCHER_PICK = 'OPTIONAL_VOUCHER_PICK'
    ACT_CART_COMPONENT = 'ACT_CART_COMPONENT'
    VOUCHER_LEVELMAX_6 = 'VOUCHER_LEVELMAX_6'
    VOUCHER_LEVELMAX_5 = 'VOUCHER_LEVELMAX_5'
    VOUCHER_LEVELMAX_4 = 'VOUCHER_LEVELMAX_4'
    VOUCHER_SKILL_SPECIALLEVELMAX_6 = 'VOUCHER_SKILL_SPECIALLEVELMAX_6'
    VOUCHER_SKILL_SPECIALLEVELMAX_5 = 'VOUCHER_SKILL_SPECIALLEVELMAX_5'
    VOUCHER_SKILL_SPECIALLEVELMAX_4 = 'VOUCHER_SKILL_SPECIALLEVELMAX_4'
    ACTIVITY_POTENTIAL = 'ACTIVITY_POTENTIAL'
    ITEM_PACK = 'ITEM_PACK'
    SANDBOX = 'SANDBOX'
    FAVOR_ADD_ITEM = 'FAVOR_ADD_ITEM'
    CLASSIC_SHD = 'CLASSIC_SHD'
    CLASSIC_TKT_GACHA = 'CLASSIC_TKT_GACHA'
    CLASSIC_TKT_GACHA_10 = 'CLASSIC_TKT_GACHA_10'
    LIMITED_BUFF = 'LIMITED_BUFF'
    CLASSIC_FES_PICK_TIER_5 = 'CLASSIC_FES_PICK_TIER_5'
    CLASSIC_FES_PICK_TIER_6 = 'CLASSIC_FES_PICK_TIER_6'
    RETURN_PROGRESS = 'RETURN_PROGRESS'
    NEW_PROGRESS = 'NEW_PROGRESS'
    MCARD_VOUCHER = 'MCARD_VOUCHER'
    MATERIAL_ISSUE_VOUCHER = 'MATERIAL_ISSUE_VOUCHER'
    CRS_SHOP_COIN_V2 = 'CRS_SHOP_COIN_V2'
    HOME_THEME = 'HOME_THEME'
    SANDBOX_PERM = 'SANDBOX_PERM'
    SANDBOX_TOKEN = 'SANDBOX_TOKEN'
    TEMPLATE_TRAP = 'TEMPLATE_TRAP'
    NAME_CARD_SKIN = 'NAME_CARD_SKIN'
    EMOTICON_SET = 'EMOTICON_SET'
    EXCLUSIVE_TKT_GACHA = 'EXCLUSIVE_TKT_GACHA'
    EXCLUSIVE_TKT_GACHA_10 = 'EXCLUSIVE_TKT_GACHA_10'
    SO_CHAR_EXP = 'SO_CHAR_EXP'
    GIFTPACKAGE_TKT = 'GIFTPACKAGE_TKT'
    ACT1VHALFIDLE_ITEM = 'ACT1VHALFIDLE_ITEM'


# class ItemBundle(GameDataModel):
#     id: str
#     count: int
#     type: ItemType


class StageDropType(StrEnum):
    NONE = 'NONE'
    ONCE = 'ONCE'
    NORMAL = 'NORMAL'
    SPECIAL = 'SPECIAL'
    ADDITIONAL = 'ADDITIONAL'
    APRETURN = 'APRETURN'
    DIAMOND_MATERIAL = 'DIAMOND_MATERIAL'
    FUNITURE_DROP = 'FUNITURE_DROP'
    COMPLETE = 'COMPLETE'
    CHARM_DROP = 'CHARM_DROP'
    OVERRIDE_DROP = 'OVERRIDE_DROP'
    ITEM_RETURN = 'ITEM_RETURN'


class WeightItemBundle(GameDataModel):
    id: str
    type: ItemType = Field(strict=False)
    drop_type: StageDropType
    count: int
    weight: int


class StageData_DisplayRewards(GameDataModel):
    type: ItemType = Field(strict=False)
    id: str
    drop_type: StageDropType | int  # kengxxiao 的仓库是 str，yuanyan3060 的仓库是 int


class OccPer(StrEnum):
    ALWAYS = 'ALWAYS'
    ALMOST = 'ALMOST'
    USUAL = 'USUAL'
    OFTEN = 'OFTEN'
    SOMETIMES = 'SOMETIMES'
    NEVER = 'NEVER'
    DEFINITELY_BUFF = 'DEFINITELY_BUFF'


class StageData_DisplayDetailRewards(GameDataModel):
    occ_percent: OccPer | int  # kengxxiao 的仓库是 str，yuanyan3060 的仓库是 int
    type: ItemType = Field(strict=False)
    id: str
    drop_type: StageDropType | int  # kengxxiao 的仓库是 str，yuanyan3060 的仓库是 int


class StageData_StageDropInfo(GameDataModel):
    first_pass_rewards: list[ItemBundle]
    first_complete_rewards: list[ItemBundle]
    pass_rewards: list[list[WeightItemBundle]]
    complete_rewards: list[list[WeightItemBundle]]
    display_rewards: list[StageData_DisplayRewards]
    display_detail_rewards: list[StageData_DisplayDetailRewards]


class StageData_ExtraConditionDesc(GameDataModel):
    index: int
    template: str
    unlock_param: list[str]


class StageData_SpecialStageUnlockProgressType(StrEnum):
    ONCE = 'ONCE'
    PROGRESS = 'PROGRESS'


class StageData_SpecialProgressInfo(GameDataModel, strict=False):
    progress_type: StageData_SpecialStageUnlockProgressType = Field(strict=False)
    desc_list: dict[int, str]


class StageData_SpecialStoryInfo(GameDataModel):
    stage_id: str
    rewards: list[ItemBundle]
    progress_info: StageData_SpecialProgressInfo
    image_id: str


class StageData(GameDataModel):
    stage_type: StageType = Field(strict=False)
    difficulty: LevelData_Difficulty = Field(strict=False)
    performance_stage_flag: StageData_PerformanceStageFlag = Field(strict=False)
    diff_group: StageDiffGroup = Field(strict=False)
    unlock_condition: list[StageData_ConditionDesc]
    stage_id: str
    level_id: str | None
    zone_id: str
    code: str
    name: str | None
    description: str | None
    hard_staged_id: str | None
    six_star_stage_id: str | None
    danger_level: str | None
    danger_point: float
    loading_pic_id: str
    can_practice: bool
    can_battle_replay: bool
    ap_cost: int
    ap_fail_return: int
    max_slot: int
    et_item_id: str | None
    et_cost: int
    et_fail_return: int
    et_button_style: str | None
    ap_protect_times: int
    diamond_once_drop: int
    practice_ticket_cost: int
    daily_stage_difficulty: int
    exp_gain: int
    gold_gain: int
    lose_exp_gain: int
    lose_gold_gain: int
    pass_favor: int
    complete_favor: int
    sl_progress: int
    display_main_item: str | None
    hilight_mark: bool
    boss_mark: bool
    is_predefined: bool
    is_hard_predefined: bool
    is_skill_selectable_predefined: bool
    is_story_only: bool
    appearance_style: AppearanceStyle | int  # kengxxiao 的仓库是 str，yuanyan3060 的仓库是 int
    stage_drop_info: StageData_StageDropInfo
    can_use_charm: bool
    can_use_tech: bool
    can_use_trap_tool: bool
    can_use_battle_performance: bool
    can_use_firework: bool
    can_multiple_battle: bool
    start_button_override_id: str | None
    is_stage_patch: bool
    main_stage_id: str | None
    extra_condition: list[StageData_ExtraConditionDesc]
    extra_info: list[StageData_SpecialStoryInfo]
    six_star_base_desc: str | None
    six_star_display_reward_list: list[ItemBundle]
    advanced_rune_id_list1: list[str]
    advanced_rune_id_list2: list[str]


class RuneStageGroupData_RuneStageInst(GameDataModel):
    stage_id: str
    active_packed_rune_ids: list[str]


class RuneStageGroupData(GameDataModel):
    group_id: str
    active_rune_stages: list[RuneStageGroupData_RuneStageInst]
    start_ts: int
    end_ts: int


class MapThemeData(GameDataModel):
    theme_id: str
    unit_color: str
    buildable_color: str
    theme_type: str
    trap_tint_color: str
    emission_color: str


class TileAppendInfo(GameDataModel):
    tile_key: str
    name: str
    description: str
    is_functional: bool


class WeeklyForceOpenTable(GameDataModel):
    id: str
    start_time: int
    end_time: int
    force_open_list: list[str]


class TimelyDropTimeInfo(GameDataModel):
    start_ts: int
    end_ts: int
    stage_pic: str
    drop_pic_id: str
    stage_unlock: str
    entrance_down_pic_id: str
    entrance_up_pic_id: str
    timely_group_id: str
    weekly_pic_id: str
    is_replace: bool
    ap_supply_out_of_date_dict: dict[str, int]


class OverrideDropInfo(GameDataModel):
    item_id: str
    start_ts: int
    end_ts: int
    zone_range: str
    times: int
    name: str
    eg_name: str
    desc1: str
    desc2: str
    desc3: str
    drop_tag: str
    drop_type_desc: str
    drop_info: dict[str, StageData_StageDropInfo]


class OverrideUnlockInfo(GameDataModel):
    group_id: str
    start_time: int
    end_time: int
    unlock_dict: dict[str, list[StageData_ConditionDesc]]


class TimelyDropInfo(GameDataModel):
    drop_info: dict[str, StageData_StageDropInfo]


class StageValidInfo(GameDataModel):
    start_ts: int
    end_ts: int


class FogType(StrEnum):
    ZONE = 'ZONE'
    STAGE = 'STAGE'


class StageButtonInFogRenderType(StrEnum):
    HIDE = 'HIDE'
    SHOW_WITH_FOG_SIX_STAR = 'SHOW_WITH_FOG_SIX_STAR'


class StageFogInfo(GameDataModel):
    lock_id: str
    fog_type: FogType
    stage_button_in_fog_render_type: StageButtonInFogRenderType
    stage_id: str
    lock_name: str
    lock_desc: str
    unlock_item_id: str
    unlock_item_type: ItemType
    unlock_item_num: int
    preposed_stage_id: str
    preposed_lock_id: str


class EvolvePhase(StrEnum):
    PHASE_0 = 'PHASE_0'
    PHASE_1 = 'PHASE_1'
    PHASE_2 = 'PHASE_2'
    PHASE_3 = 'PHASE_3'
    E_NUM = 'E_NUM'


class StageStartCond_RequireChar(GameDataModel):
    char_id: str
    evolve_phase: EvolvePhase


class StageStartCond(GameDataModel):
    require_chars: list[StageStartCond_RequireChar]
    exclude_assists: list[str]
    is_not_pass: bool


class StageDiffGroupTable(GameDataModel):
    normal_id: str
    tough_id: str
    easy_id: str


class StoryStageShowGroup(GameDataModel):
    display_record_id: str
    stage_id: str
    according_stage_id: str
    diff_group: StageDiffGroup


class SpecialBattleFinishStageData(GameDataModel):
    stage_id: str
    skip_accomplish_perform: bool


class RecordRewardServerData(GameDataModel):
    stage_id: str
    rewards: list[ItemBundle]


class ApProtectZoneInfo_TimeRange(GameDataModel):
    start_ts: int
    end_ts: int


class ApProtectZoneInfo(GameDataModel):
    zone_id: str
    time_ranges: list[ApProtectZoneInfo_TimeRange]


class OverrideGameMode(StrEnum):
    NONE = 'NONE'
    ACT27SIDE = 'ACT27SIDE'


class ActCustomStageData(GameDataModel):
    override_game_mode: OverrideGameMode


class StorylineType(StrEnum):
    CONTINUE = 'CONTINUE'
    DISCRETE = 'DISCRETE'


class StorylineLocationType(StrEnum):
    STORY_SET = 'STORY_SET'
    BEFORE = 'BEFORE'
    AFTER = 'AFTER'
    MAINLINE_SPLIT = 'MAINLINE_SPLIT'


class StorylineMainlineSplitData(GameDataModel):
    icon_id: str


class StorylineLocationData(GameDataModel):
    location_id: str
    location_type: StorylineLocationType
    sort_id: int
    start_time: int
    present_stage_id: str
    unlock_stage_id: str
    relevant_story_set_id: str
    mainline_split_data: StorylineMainlineSplitData


class StorylineData(GameDataModel):
    storyline_id: str
    storyline_type: StorylineType
    sort_id: int
    storyline_name: str
    storyline_icon_id: str
    background_id: str
    start_ts: int
    locations: dict[str, StorylineLocationData]


class StorylineStorySetType(StrEnum):
    MAINLINE = 'MAINLINE'
    SS = 'SS'
    COLLECT = 'COLLECT'


class StorylineMainlineData(GameDataModel):
    zone_id: str
    retro_id: str
    deco_image_id: str


class StorylineSSData(GameDataModel):
    name: str
    desc: str
    background_id: str
    tags: list[str]
    reopen_activity_id: str
    retro_activity_id: str
    is_recommended: bool
    recommend_hide_stage_id: str
    override_stage_list: list[str]


class StorylineCollectData(GameDataModel):
    name: str
    desc: str
    background_id: str


class StorylineStorySetData(GameDataModel):
    story_set_id: str
    story_set_type: StorylineStorySetType
    sort_by_year: int
    sort_within_year: int
    kv_image_id: str
    title_image_id: str
    background_id: str
    game_music_id: str
    core_reward_type: ItemType
    core_reward_id: str
    relevant_activity_id: str
    mainline_data: StorylineMainlineData
    ss_data: StorylineSSData
    collect_data: StorylineCollectData


class StorylineTagData(GameDataModel):
    tag_id: str
    sort_id: int
    tag_desc: str
    text_color: str
    bkg_color: str


class StorylineConstData(GameDataModel):
    recommend_hide_guide_group_id: str
    tutorial_select_storyline_id: str


class SixStarRuneData(GameDataModel):
    rune_id: str
    rune_desc: str
    rune_key: str


class SixStarMilestoneRewardType(StrEnum):
    UNLOCK_STAGE = 'UNLOCK_STAGE'
    REWARD = 'REWARD'


class SixStarMilestoneItemData(GameDataModel):
    id: str
    sort_id: int
    node_point: int
    reward_type: SixStarMilestoneRewardType
    unlock_stage_fog: str
    unlock_stage_id: str
    unlock_stage_name: str
    reward_list: list[ItemBundle]


class SixStarMilestoneGroupData(GameDataModel):
    group_id: str
    stage_id_list: list[str]
    milestone_data_list: list[SixStarMilestoneItemData]


class SixStarStageCompatibleDropType(StrEnum):
    COMPLETE_ONLY = 'COMPLETE_ONLY'


class SixStarLinkedStageCompatibleInfo(GameDataModel):
    stage_id: str
    ap_cost: int
    ap_fail_return: int
    drop_type: SixStarStageCompatibleDropType


class StageTable(GameDataModel, extra="allow"):
    stages: dict[str, StageData]
    # rune_stage_groups: dict[str, RuneStageGroupData]
    # map_themes: dict[str, MapThemeData]
    # tile_info: dict[str, TileAppendInfo]
    # force_open_table: dict[str, WeeklyForceOpenTable]
    # timely_stage_drop_info: dict[str, TimelyDropTimeInfo]
    # override_drop_info: dict[str, OverrideDropInfo]
    # override_unlock_info: dict[str, OverrideUnlockInfo]
    # timely_table: dict[str, TimelyDropInfo]
    # stage_valid_info: dict[str, StageValidInfo]
    # stage_fog_info: dict[str, StageFogInfo]
    # stage_start_conds: dict[str, StageStartCond]
    # diff_group_table: dict[str, StageDiffGroupTable]
    # story_stage_show_group: dict[str, dict[StageDiffGroup, StoryStageShowGroup]]
    # special_battle_finish_stage_data: dict[str, SpecialBattleFinishStageData]
    # record_reward_data: dict[str, RecordRewardServerData]
    # ap_protect_zone_info: dict[str, ApProtectZoneInfo]
    # anti_spoiler_dict: dict[str, list[str]]
    # act_custom_stage_datas: dict[str, ActCustomStageData]
    # sp_normal_stage_id_for4_star_list: list[str]
    # storylines: dict[str, StorylineData]
    # storyline_story_sets: dict[str, StorylineStorySetData]
    # storyline_tags: dict[str, StorylineTagData]
    # storyline_const: StorylineConstData
    # six_star_rune_data: dict[str, SixStarRuneData]
    # six_star_milestone_info: dict[str, SixStarMilestoneGroupData]
    # six_star_compatible_info: dict[str, SixStarLinkedStageCompatibleInfo]


# Root Type: StageTable
