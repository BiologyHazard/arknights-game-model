from ._raw_game_data.excel.building_data import WorkshopFormula as WorkshopFormulaInGame
from .item_info_model import ItemInfo, ItemInfoList


class WorkshopFormula:
    _raw_data: WorkshopFormulaInGame

    def __init__(self, raw_data: WorkshopFormulaInGame):
        self._raw_data = raw_data

    @property
    def sort_id(self) -> int:
        return self._raw_data.sort_id

    @property
    def formula_id(self) -> str:
        return self._raw_data.formula_id

    @property
    def rarity(self) -> int:
        return self._raw_data.rarity

    @property
    def item_id(self) -> str:
        return self._raw_data.item_id

    @property
    def count(self) -> int:
        return self._raw_data.count

    @property
    def main_product_item_info(self) -> ItemInfo:
        return ItemInfo(self.item_id, self.count)

    @property
    def gold_cost(self) -> int:
        return self._raw_data.gold_cost

    @property
    def costs(self) -> ItemInfoList:
        item_info_list = ItemInfoList.new(self._raw_data.costs)
        if self.gold_cost:
            item_info_list.append(ItemInfo("4001", self.gold_cost))
        return item_info_list

    @property
    def extra_outcomes(self) -> ItemInfoList:
        extra_outcome_rate = self._raw_data.extra_outcome_rate
        total_weight = sum(outcome.weight for outcome in self._raw_data.extra_outcome_group)
        item_info_list = ItemInfoList.new(
            (outcome.item_id, outcome.item_count * outcome.weight / total_weight * extra_outcome_rate)
            for outcome in self._raw_data.extra_outcome_group
        )
        return item_info_list

    def __repr__(self):
        return f"<{self.__class__.__module__}.{self.__class__.__name__}(formula_id={self.formula_id!r}, main_product={str(self.main_product_item_info)!r}, costs={str(self.costs)!r}) at {id(self):#x}>"
