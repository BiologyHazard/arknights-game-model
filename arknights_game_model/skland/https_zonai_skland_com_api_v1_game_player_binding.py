from pydantic import Field

from arknights_game_model.model import GameDataModel


class Binding(GameDataModel):
    uid: str
    is_official: bool
    is_default: bool
    channel_master_id: str
    channel_name: str
    nick_name: str
    is_delete: bool
    game_name: str
    game_id: int
    roles: list = Field(max_length=0)
    default_role: None


class AppInfo(GameDataModel):
    app_code: str
    app_name: str
    binding_list: list[Binding]
    default_uid: str | None = None


class Data(GameDataModel):
    list: list[AppInfo]


class HttpsZonaiSklandComApiV1GamePlayerBinding(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
