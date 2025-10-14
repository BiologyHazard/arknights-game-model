from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    import pandas as pd
    from pandas._typing import FilePath, WriteBuffer

    from arknights_game_model.game_data import GameData


special_character_ids = {
    "阿米娅": "char_002_amiya",
    "阿米娅(近卫)": "char_1001_amiya2",
    "阿米娅(医疗)": "char_1037_amiya3",
}

char_online_time_url = "https://prts.wiki/api.php?action=parse&page=%E5%B9%B2%E5%91%98%E4%B8%8A%E7%BA%BF%E6%97%B6%E9%97%B4%E4%B8%80%E8%A7%88&format=json"
"""https://prts.wiki/api.php?action=parse&page=干员上线时间一览&format=json"""
mod_online_time_url = "https://prts.wiki/api.php?action=parse&page=%E5%B9%B2%E5%91%98%E6%A8%A1%E7%BB%84%E4%B8%80%E8%A7%88/%E4%B8%8A%E7%BA%BF%E6%97%B6%E9%97%B4&format=json"
"""https://prts.wiki/api.php?action=parse&page=干员模组一览/上线时间&format=json"""


def fetch_data_from_prts_wiki(save_to: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None) -> pd.DataFrame:
    import io
    import json
    import urllib.request

    import pandas as pd

    with urllib.request.urlopen(char_online_time_url) as response:
        obj = json.load(response)
    html = obj["parse"]["text"]["*"]
    string_io = io.StringIO(html)

    df = pd.read_html(string_io)[0]

    if save_to is not None:
        df.to_csv(save_to, index=False, encoding="utf-8")

    return df


def patch_to(game_data: GameData, path: Path) -> None:
    import pandas as pd

    from arknights_game_model.log import logger

    if not path.is_file():
        raise FileNotFoundError(f"{path} 不存在，请先调用 fetch_data_from_prts_wiki() 下载数据")

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

    not_in_wiki_names = [
        character.name for character in game_data.characters.values() if character.name not in df["干员"].values
    ]
    not_in_gamedata_names = [name for name in df["干员"] if name not in character_name_to_id]
    if not_in_wiki_names:
        logger.warning(f"以下干员在 character_table 中，但不在 PRTS Wiki 干员上线时间一览中：\n{', '.join(not_in_wiki_names)}")
    if not_in_gamedata_names:
        logger.warning(f"以下干员在 PRTS Wiki 上线时间表中，但不在 character_table 中：\n{', '.join(not_in_gamedata_names)}")


if __name__ == "__main__":
    import sys

    df = fetch_data_from_prts_wiki(sys.stdout)
