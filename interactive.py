from datetime import UTC, date, datetime, time, timedelta, timezone
from pathlib import Path

import pandas as pd

from arknights_game_model._raw_game_data import ArknightsGameData, load_data
from arknights_game_model.building_model import WorkshopFormula
from arknights_game_model.character_model import Professions, UniEquip, 职业ID_to_职业
from arknights_game_model.game_data import CharacterDict, GameData, ItemDict, game_data
from arknights_game_model.item_info_model import ItemBundle, ItemInfo, ItemInfoList

CST = timezone(timedelta(hours=8))
fts = datetime.fromtimestamp

game_data.load_data()

gd: GameData = game_data
P = Professions
p: dict[str, Professions] = 职业ID_to_职业
ii = ItemInfo
iil = ItemInfoList
iib = ItemBundle

c: CharacterDict = game_data.characters
i: ItemDict = game_data.items
u: dict[str, UniEquip] = game_data.uniequips
wf: dict[str, WorkshopFormula] = game_data.workshop_formulas

for character in c.values():
    globals()[character.name] = character
for item in i.values():
    globals()[item.name] = item
for uniequip in u.values():
    globals()[uniequip.uniequip_name] = uniequip


del character, item, uniequip  # type: ignore
