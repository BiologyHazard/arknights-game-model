from typing import Any

from arknights_game_model._raw_game_data.model import GameDataModel


class CreatorIdentifier(GameDataModel):
    id: int
    name: str
    description: str
    status: int
    applicable: int
    created_at_ts: int
    updated_at_ts: int
    i18n_name: dict[str, Any]  # 空字典
    i18n_description: dict[str, Any]  # 空字典


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
    score_info_list: list[Any]  # 空列表


class Relation(GameDataModel):
    follow: bool
    fans: bool
    black: bool
    blacked: bool
    blocked: bool
    fans_at_ts: int


class UserRts(GameDataModel):
    follow: str
    fans: str


class Im(GameDataModel):
    im_uid: str
    no_reminder: bool


class ListElement(GameDataModel):
    user: User
    relation: Relation
    user_rts: UserRts
    im: Im


class Data(GameDataModel):
    list: list[ListElement]
    page_token: str
    page_size: int
    has_more: bool


class HttpsZonaiSklandComApiV1SearchUser(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
