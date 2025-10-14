from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from arknights_game_model.game_data import GameData


def patch_to(game_data: GameData, path: Path) -> None:
    from arknights_game_model.log import logger

    if not path.is_file():
        raise FileNotFoundError(f"Item value file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)

    if "data" in obj:  # 来自后端
        item_id_to_value: dict[str, float] = {x["itemId"]: x["itemValueAp"] for x in obj["data"]}
        item_id_to_name: dict[str, str] = {x["itemId"]: x["itemName"] for x in obj["data"]}

    else:  # 来自前端
        item_id_to_value = {x["id"]: x["apValue"] for x in obj}
        item_id_to_name = {x["id"]: x["name"] for x in obj}

    if "2003" in item_id_to_value:
        item_id_to_value["exp"] = item_id_to_value["2003"] / 1000

    # for item_id, item in game_data.items.items():
    #     if item_id in item_id_to_value:
    #         item._yituliu_item_value = item_id_to_value[item_id]

    for item_id, item_value in item_id_to_value.items():
        if item_id in game_data.items:
            game_data.items[item_id]._yituliu_item_value = item_value

    not_in_yituliu_names = [item.name for item_id, item in game_data.items.items() if item_id not in item_id_to_value.keys()]
    not_in_item_table_names = [item_name for item_id, item_name in item_id_to_name.items() if item_id not in game_data.items]
    if not_in_yituliu_names:
        logger.warning(f"以下物品在 item_table 中，但不在一图流物品价值表中：\n{', '.join(not_in_yituliu_names)}")
    if not_in_item_table_names:
        logger.warning(f"以下物品在一图流物品价值表中，但不在 item_table 中：\n{', '.join(not_in_item_table_names)}")
