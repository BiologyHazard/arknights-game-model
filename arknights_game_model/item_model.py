from ._raw_game_data.item_table import Item as ItemInGame
from .building_model import WorkshopFormula


class Item:
    _raw_data: ItemInGame

    def __init__(self, raw_data: ItemInGame):
        self._raw_data = raw_data

    @property
    def item_id(self) -> str:
        return self._raw_data.item_id

    @property
    def name(self) -> str:
        return self._raw_data.name

    @property
    def rarity(self) -> int:
        return self._raw_data.rarity

    @property
    def sort_id(self) -> int:
        return self._raw_data.sort_id

    @property
    def is_elite_material(self) -> bool:
        return 100000 <= self.sort_id < 200000

    def workshop_formulas_craft_self(self) -> dict[str, WorkshopFormula]:
        """合成自身的配方"""
        # 还可以通过 self._raw_data.building_product_list 获取，不清楚是否等价。
        from .game_data import game_data
        return {
            formula_id: formula
            for formula_id, formula in game_data.workshop_formulas.items()
            if formula.item_id == self.item_id
        }

    def workshop_formulas_craft_other(self) -> dict[str, WorkshopFormula]:
        """合成其他物品的配方"""
        from .game_data import game_data
        return {
            formula_id: formula
            for formula_id, formula in game_data.workshop_formulas.items()
            if self.item_id in formula.costs
        }

    def __repr__(self):
        return f"<{self.__class__.__module__}.{self.__class__.__name__} {self.name!r} at {id(self):#x}>"
