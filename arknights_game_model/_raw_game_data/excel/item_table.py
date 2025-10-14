from arknights_game_model.item_info_model import ItemBundle
from arknights_game_model.model import GameDataModel

# class OccurPer(Enum):
#     ALWAYS = "ALWAYS"


# class RoomType(Enum):
#     MANUFACTURE = "MANUFACTURE"

type OccPer = str
type RoomType = str


class StageDrop(GameDataModel):
    stage_id: str
    occ_per: OccPer
    sort_id: int


class BuildingProduct(GameDataModel):
    room_type: RoomType
    formula_id: str


class VoucherRelate(GameDataModel):
    voucher_id: str
    voucher_item_type: str


class ShopRelateInfo(GameDataModel):
    shop_type: int
    shop_group: int
    start_ts: int


class Item(GameDataModel):
    item_id: str
    name: str
    description: str | None
    rarity: int
    icon_id: str
    override_bkg: None
    stack_icon_id: str | None
    sort_id: int
    usage: str | None
    obtain_approach: str | None
    hide_in_item_get: bool
    classify_type: str
    item_type: str
    stage_drop_list: list[StageDrop]
    building_product_list: list[BuildingProduct]
    voucher_relate_list: list[VoucherRelate]
    shop_relate_info_list: list[ShopRelateInfo]


class ExpItem(GameDataModel):
    id: str
    gain_exp: int


class ApSupply(GameDataModel):
    id: str
    ap: int
    has_ts: bool


class CharVoucherItem(GameDataModel):
    id: str
    display_type: int


class UniCollectionItem(GameDataModel):
    uni_collection_item_id: str
    unique_item: list[ItemBundle]


class ItemPackInfo(GameDataModel):
    pack_id: str
    content: list[ItemBundle]


class FullPotentialCharacter(GameDataModel):
    item_id: str
    ts: int


class ActivityPotentialCharacter(GameDataModel):
    char_id: str


class FavorCharacter(GameDataModel):
    item_id: str
    char_id: str
    favor_add_amt: int


class ItemTable(GameDataModel):
    items: dict[str, Item]
    exp_items: dict[str, ExpItem]
    potential_items: dict[str, dict[str, str]]
    ap_supplies: dict[str, ApSupply]
    char_voucher_items: dict[str, CharVoucherItem]
    unique_info: dict[str, int]
    item_time_limit: dict[str, int]
    uni_collection_info: dict[str, UniCollectionItem]
    item_pack_infos: dict[str, ItemPackInfo]
    full_potential_characters: dict[str, FullPotentialCharacter]
    activity_potential_characters: dict[str, ActivityPotentialCharacter]
    favor_characters: dict[str, FavorCharacter]
    item_shop_name_dict: dict[str, str]
