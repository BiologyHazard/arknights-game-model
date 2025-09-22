from pathlib import Path

from arknights_game_model.building_model import WorkshopFormula
from arknights_game_model.character_model import Professions, UniEquip, 职业ID_to_职业
from arknights_game_model.game_data import CharacterDict, GameData, ItemDict, game_data
from arknights_game_model.item_info_model import ItemInfo, ItemInfoDict, ItemInfoList

game_data.load_data(gamedata_folder=Path("ArknightsGameResource/gamedata"), online_time_path=Path("prts_wiki/干员上线时间.csv"), yituliu_item_value_path=Path("yituliu/json/item.json"))

gd: GameData = game_data
P = Professions
p: dict[str, Professions] = 职业ID_to_职业
ii = ItemInfo
iil = ItemInfoList
iid = ItemInfoDict

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
