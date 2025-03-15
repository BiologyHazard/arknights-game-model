from log import logger


@logger.catch()
def main1():
    from load_data import load_data, 干员代号_to_干员, 干员字典, 道具名称_to_道具, 道具字典, 模组表
    from utils import 计算干员升级消耗
    import gamedata_const_model as gcm
    load_data()
    # print(gcm.累计消耗龙门币)
    # print(gcm.精英化消耗龙门币)
    # print(gcm.干员等级上限)
    # print(干员代号_to_干员["夜莺"].计算精英化消耗(2))
    print(模组表)


@logger.catch()
def main2():
    from arknights_game_model.game_data import game_data
    from arknights_game_model._raw_game_data.game_data import ArknightsGameData, load_data

    game_data.load_data()
    print(game_data.characters.by_name("休谟斯").拉满消耗())


if __name__ == "__main__":
    main2()
