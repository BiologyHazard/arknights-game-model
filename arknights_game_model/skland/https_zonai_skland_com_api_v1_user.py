from typing import Any

from arknights_game_model.model import GameDataModel


class CreatorIdentifier(GameDataModel):
    id: int
    name: str
    description: str
    status: int
    applicable: int
    created_at_ts: int
    updated_at_ts: int


class ScoreInfo(GameDataModel):
    game_id: int
    level: int
    icon_url: str
    checked_days: int
    score: int
    game_name: str
    level_url: str


class Pendant(GameDataModel):
    id: int
    icon_url: str
    title: str
    description: str


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
    birthday: str
    hg_id: str
    creator_identifiers: list[CreatorIdentifier]
    score_info_list: list[ScoreInfo]
    pendant: Pendant
    show_id: str


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


class Teenager(GameDataModel):
    user_id: str
    status: int
    allow: bool
    popup: bool


class TeenagerMeta(GameDataModel):
    duration: int
    start: str
    end: str


class Entry(GameDataModel):
    title: str
    subtitle: str
    icon_url: str
    scheme: str


class Im(GameDataModel):
    im_uid: str
    no_reminder: bool


class Background(GameDataModel):
    id: int
    url: str
    resource_kind: int


class Share(GameDataModel):
    link: str


class Data(GameDataModel):
    user: User
    user_rts: UserRts
    relation: Relation
    user_sanction_list: list[Any]  # 空列表
    game_status: GameStatus
    moderator: Moderator
    user_info_apply: UserInfoApply
    teenager: Teenager
    teenager_meta: TeenagerMeta
    entries: list[Entry]
    pendant: Pendant
    im: Im
    background: Background
    share: Share


class HttpsZonaiSklandComApiV1User(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
