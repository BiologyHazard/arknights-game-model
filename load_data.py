
import gamedata_const_model as gcm
from character_model import ID_to_职业, 干员类, 技能类, 精英化阶段类
from uniequip_table import UniequipTable
from excels import *
from item_model import 物品类, 道具类
from utils import 计算累计消耗, 计算干员升级消耗

道具字典: dict[str, 道具类] = {}
干员字典: dict[str, 干员类] = {}

道具名称_to_道具: dict[str, 道具类] = {}
干员代号_to_干员: dict[str, 干员类] = {}
模组表: UniequipTable = UniequipTable.model_validate(uniequip_table)


def load_data():
    global 模组表
    # 读取游戏常数
    gcm.精英化消耗龙门币 = gamedata_const["evolveGoldCost"]
    gcm.干员升级消耗EXP = gamedata_const["characterExpMap"]
    gcm.干员升级消耗龙门币 = gamedata_const["characterUpgradeCostMap"]
    gcm.干员等级上限 = gamedata_const["maxLevel"]
    gcm.干员精英化阶段上限 = [len(x) - 1 for x in gcm.干员等级上限]

    gcm.累计消耗EXP = 计算累计消耗(gcm.干员升级消耗EXP)
    gcm.累计消耗龙门币 = 计算累计消耗(gcm.干员升级消耗龙门币)

    # 创建道具 EXP
    道具字典["exp"] = 物品类(ID="exp", 名称="EXP", 描述="用于干员升级的经验", 稀有度=0)

    # 读取道具
    for item_id, item_info in item_table["items"].items():
        item = 物品类(
            ID=item_info["itemId"],
            名称=item_info["name"],
            描述=item_info["description"],
            稀有度=item_info["rarity"],
            # 类型=item_info.get("itemType"),
        )
        if item_id in 道具字典:
            raise
        道具字典[item_id] = item

    # 读取干员
    for character_id, character_info in character_table.items():
        if character_info["profession"] in ("TOKEN", "TRAP"):
            continue

        精英化阶段列表 = []
        for phase in character_info["phases"]:
            精英化阶段 = 精英化阶段类(
                等级上限=phase["maxLevel"],
                _升级消耗=phase["evolveCost"]
            )
            精英化阶段列表.append(精英化阶段)

        技能列表 = []
        for skill_info in character_info["skills"]:
            技能 = 技能类(
                ID=skill_info["skillId"],
                _专精消耗=[x["levelUpCost"] for x in skill_info["levelUpCostCond"]]
            )
            技能列表.append(技能)

        character = 干员类(
            ID=character_id,
            代号=character_info["name"],
            描述=character_info["description"],
            稀有度=character_info["rarity"],
            最大潜能等级=character_info["maxPotentialLevel"],
            _信物ID=character_info["potentialItemId"],
            位置=character_info["position"],
            标签列表=character_info["tagList"],
            是异格干员=character_info["isSpChar"],
            职业=ID_to_职业[character_info["profession"]],
            职业分支=character_info["subProfessionId"],
            精英化阶段列表=精英化阶段列表,
            技能列表=技能列表,
            _通用技能升级消耗=[x["lvlUpCost"] for x in character_info["allSkillLvlup"]],
        )
        干员字典[character_id] = character

        # 模组表 = UniequipTable.model_validate(uniequip_table)

        道具名称_to_道具.update({item.名称: item for item in 道具字典.values()})
        干员代号_to_干员.update({character.代号: character for character in 干员字典.values()})
