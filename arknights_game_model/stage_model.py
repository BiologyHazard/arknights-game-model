from ._raw_game_data.excel.stage_table import StageData as StageDataInGame
from ._raw_game_data.excel.stage_table import StageData_StageDropInfo as StageDropInfoInGame


class Item:
    def __init__(self, stage_id: str) -> None:
        self._stage_id = stage_id

    @property
    def raw_data(self) -> StageDataInGame:
        from .game_data import game_data

        return game_data.raw_data.excel.stage_table.stages[self._stage_id]

    @property
    def code(self) -> str:
        return self.raw_data.code

    @property
    def name(self) -> str | None:
        return self.raw_data.name

    @property
    def ap_cost(self) -> int:
        return self.raw_data.ap_cost

    @property
    def stage_drop_info(self) -> StageDropInfoInGame:
        return self.raw_data.stage_drop_info

    def __repr__(self):
        return f"<{self.__class__.__module__}.{self.__class__.__name__} stage_id={self._stage_id!r} code={self.code!r} name={self.name!r}>"
