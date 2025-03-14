from log import logger


@logger.catch()
def main():
    from load_data import load_data
    from utils import 计算干员升级消耗
    load_data()
    print(计算干员升级消耗(6-1, 0, 1, 2, 90))


if __name__ == "__main__":
    main()
