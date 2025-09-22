from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from arknights_game_model.game_data import GameData


special_character_ids = {
    "阿米娅": "char_002_amiya",
    "阿米娅(近卫)": "char_1001_amiya2",
    "阿米娅(医疗)": "char_1037_amiya3",
}

char_online_time_url = "https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%8A%E7%BA%BF%E6%97%B6%E9%97%B4%E4%B8%80%E8%A7%88"
""" <https://prts.wiki/w/干员上线时间一览> """
mod_online_time_url = "https://prts.wiki/w/%E5%B9%B2%E5%91%98%E6%A8%A1%E7%BB%84%E4%B8%80%E8%A7%88/%E4%B8%8A%E7%BA%BF%E6%97%B6%E9%97%B4"
""" <https://prts.wiki/w/干员模组一览/上线时间> """


def fetch_data_from_prts_wiki(save_path: Path | None) -> pd.DataFrame:
    df = pd.read_html(char_online_time_url)[0]

    if save_path is not None:
        df.to_csv(save_path, index=False)

    return df


def patch_to(game_data: GameData, path: Path) -> None:
    from arknights_game_model.log import logger

    if not path.is_file():
        raise FileNotFoundError(f"{path} 不存在，请先调用 fetch_data_from_prts_wiki() 下载数据")

    import pandas as pd

    df = pd.read_csv(path)
    df["国服上线时间"] = pd.to_datetime(df["国服上线时间"], format="%Y年%m月%d日 %H:%M").dt.tz_localize("Asia/Shanghai")

    character_name_to_id = {character.name: character.id for character in game_data.characters.values()} | special_character_ids

    for index, row in df.iterrows():
        name = row["干员"]
        if name not in character_name_to_id:
            continue
        character_id = character_name_to_id[name]
        character = game_data.characters.by_id(character_id)
        online_time = row["国服上线时间"]
        character._cn_online_time = online_time

    not_in_wiki_names = [character.name for character_id, character in game_data.characters.items() if character_id not in character_name_to_id.values()]
    not_in_table_names = [name for name in df["干员"] if name not in character_name_to_id]
    if not_in_wiki_names:
        logger.warning(f"以下干员在 character_table 中，但不在 PRTS Wiki 上线时间表中：\n{', '.join(not_in_wiki_names)}")
    if not_in_table_names:
        logger.warning(f"以下干员在 PRTS Wiki 上线时间表中，但不在 character_table 中：\n{', '.join(not_in_table_names)}")
