from typing import Any

from pydantic import ConfigDict

from arknights_game_model.model import GameDataModel


class Privacy(GameDataModel):
    is_show_friend_code: bool
    is_show_data_card: bool
    is_show_data_detail: bool


class Gameplat(GameDataModel):
    key: str
    name: str
    level: int
    account_status: int
    game_num: int
    game_playtime: int
    account_worth: int
    is_binding: bool
    is_data_public: bool
    skip_url: str
    bg_color: str
    icon: str
    privacy: Privacy
    about_url: str
    last_online_at: int
    large_icon: str
    plat_user_id: str


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


# 游戏卡片相关模型
class GameCardPrivacy(GameDataModel):
    card_on: bool
    detail_on: bool
    game_relation_on: bool


class ArknightsGameData(GameDataModel):
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


class Decoration(GameDataModel):
    id: int
    url: str
    kind: int
    resource_kind: int
    top_color: str
    text_color: str
    background_url: str
    character_kv_name: str


class GameCard(GameDataModel):
    id: int
    name: str
    icon: str
    bg_url: str
    privacy: GameCardPrivacy
    link: str
    arknights: ArknightsGameData
    icon_border_color: str
    game_char: str
    decoration: Decoration
    channel_id: int


# 用户信息相关模型
class CreatorIdentifier(GameDataModel):
    id: int
    name: str
    description: str
    status: int
    applicable: int
    created_at_ts: int
    updated_at_ts: int
    i18n_name: dict
    i18n_description: dict


class ScoreInfo(GameDataModel):
    game_id: int
    level: int
    icon_url: str
    checked_days: int
    score: int
    game_name: str
    level_url: str


class User(GameDataModel):
    id: str
    nickname: str
    profile: str
    avatar_code: int
    avatar: str
    background_code: int
    is_creator: bool
    status: int
    operation_status: int
    identity: int
    kind: int
    latest_ip_location: str
    moderator_status: int
    moderator_change_time: int
    gender: int
    hg_id: str
    creator_identifiers: list[CreatorIdentifier]
    score_info_list: list[ScoreInfo]


class UserRts(GameDataModel):
    liked: str
    collect: str
    comment: str
    follow: str
    fans: str
    black: str
    pub: str


class Relation(GameDataModel):
    follow: bool
    fans: bool
    black: bool
    blacked: bool
    blocked: bool
    fans_at_ts: int


class GameStatus(GameDataModel):
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


class Moderator(GameDataModel):
    is_moderator: bool


class UserInfoApply(GameDataModel):
    nickname: str
    profile: str


class UserGamePrivacy(GameDataModel):
    card_on: bool
    detail_on: bool
    game_relation_on: bool | None = None  # 部分游戏无此字段，设为可选


class OneClickProtection(GameDataModel):
    on_off: bool


class UserPrivacy(GameDataModel):
    fans_on_off: bool
    follow_on_off: bool
    collection_on_off: bool
    game_on_off: bool
    watermark_on_off: bool
    personalized_recommendation_on_off: bool
    game_detail_on_off: bool
    games: dict[str, UserGamePrivacy]  # key为gameId字符串（如"1"）
    receive_not_fans_on_off: bool
    one_click_protection: OneClickProtection


class Background(GameDataModel):
    id: int
    url: str
    resource_kind: int


class Share(GameDataModel):
    link: str


class Im(GameDataModel):
    im_uid: str
    no_reminder: bool


class UserInfo(GameDataModel):
    user: User
    user_rts: UserRts
    relation: Relation
    game_status: GameStatus
    moderator: Moderator
    user_info_apply: UserInfoApply
    privacy: UserPrivacy
    entries: list[Any]  # 空列表
    im: Im
    background: Background
    share: Share


class Data(GameDataModel):
    gameplat_list: list[Gameplat]  # 空列表
    game_card_list: list[GameCard]
    user_info: UserInfo


class HttpsZonaiSklandComApiV1UserCenter(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
