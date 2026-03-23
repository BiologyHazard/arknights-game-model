from pydantic import ConfigDict

from arknights_game_model.model import GameDataModel


class MatrixEntry(GameDataModel):
    model_config = ConfigDict(extra="allow")

    stage_id: str
    item_id: str
    quantity: int
    times: int
    start: int
    end: int


class Matrix(GameDataModel):
    matrix: list[MatrixEntry]
