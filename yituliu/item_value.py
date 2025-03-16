from pathlib import Path

from arknights_game_model.item_info_model import ItemInfoList
from arknights_game_model.log import logger

from .api_model.item_value import ItemValueApi


class YituliuItemValue:
    def __init__(self, path: Path):
        self.item_value_api = ItemValueApi.model_validate_json(path.read_text("utf-8"))
        self.item_id_to_value = {
            x.item_id: x.item_value_ap
            for x in self.item_value_api.data
        }

    def calculate_total_value(self, item_info_list: ItemInfoList):
        value = 0
        for item_info in item_info_list:
            if item_info.item_id == "exp":
                value += self.item_id_to_value["2003"] * item_info.count / 1000
            else:
                if item_info.item_id not in self.item_id_to_value:
                    logger.warning(f"未找到 {item_info.item_id} 的价值")
                    continue
                value += self.item_id_to_value[item_info.item_id] * item_info.count
        return value
