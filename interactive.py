from arknights_game_model.character_model import Professions as P
from arknights_game_model.character_model import 职业ID_to_职业 as p
from arknights_game_model.game_data import game_data

game_data.load_data()

c = game_data.characters
i = game_data.items
u = game_data.uniequips
wf = game_data.workshop_formulas

for character in c.values():
    globals()[character.name] = character
for item in i.values():
    globals()[item.name] = item
for uniequip in u.values():
    globals()[uniequip.uniequip_name] = uniequip
