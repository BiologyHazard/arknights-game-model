from arknights_game_model.model import GameDataModel

from .building_data import BuildingData
from .campaign_table import CampaignTable
from .char_patch_table import CharPatchTable
from .character_table import CharacterTable
from .gamedata_const import GamedataConst
from .item_table import ItemTable
from .stage_table import StageTable
from .uniequip_table import UniEquipTable


class Excel(GameDataModel):
    building_data: BuildingData
    campaign_table: CampaignTable
    char_patch_table: CharPatchTable
    character_table: CharacterTable
    gamedata_const: GamedataConst
    item_table: ItemTable
    stage_table: StageTable
    uniequip_table: UniEquipTable
