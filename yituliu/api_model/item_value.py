from enum import Enum

from pydantic import ConfigDict

from .model import GameDataModel


class ItemType(Enum):
    GREY = "grey"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    ORANGE = "orange"


class ItemValue(GameDataModel):
    model_config: ConfigDict = ConfigDict(strict=False)

    id: int
    item_id: str
    item_name: str
    item_value: float
    item_value_ap: float
    type: ItemType
    rarity: int
    card_num: int
    version: str
    weight: float


class ItemValueApi(GameDataModel):
    code: int
    msg: str
    data: list[ItemValue]
