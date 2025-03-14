import re
from itertools import accumulate
import gamedata_const_model as gcm


def escape_description(s):
    """删除所有的HTML标签"""
    return re.sub(r'<[^>]*?>', '', s)


def 计算累计消耗(干员升级消耗: list[list[int]]) -> list[list[int]]:
    return [list(accumulate(filter(lambda x: x > 0, 升级消耗列表), initial=0)) for 升级消耗列表 in 干员升级消耗]


def 检查干员等级合法性(稀有度: int, 精英化阶段: int, 等级: int) -> bool:
    if 稀有度 < 0 or 稀有度 >= len(gcm.干员等级上限):
        return False

    if 精英化阶段 < 0 or 精英化阶段 >= len(gcm.干员等级上限[稀有度]):
        return False

    if 等级 < 1 or 等级 > gcm.干员等级上限[稀有度][精英化阶段]:
        return False

    return True


def 计算干员升级消耗(稀有度: int, 初始精英化阶段: int, 初始等级: int, 目标精英化阶段: int, 目标等级: int) -> tuple[int, int]:
    import gamedata_const_model as gcm

    if not 检查干员等级合法性(稀有度, 初始精英化阶段, 初始等级):
        raise ValueError("初始等级不合法")

    if not 检查干员等级合法性(稀有度, 目标精英化阶段, 目标等级):
        raise ValueError("目标等级不合法")

    if (初始精英化阶段, 初始等级) >= (目标精英化阶段, 目标等级):
        return (0, 0)

    EXP = 0
    龙门币 = 0
    for 当前精英化阶段 in range(初始精英化阶段, 目标精英化阶段 + 1):
        当前精英化阶段初始等级 = 初始等级 if 当前精英化阶段 == 初始精英化阶段 else 1
        当前精英化阶段目标等级 = 目标等级 if 当前精英化阶段 == 目标精英化阶段 else gcm.干员等级上限[稀有度][当前精英化阶段]
        EXP += gcm.累计消耗EXP[当前精英化阶段][当前精英化阶段目标等级-1] - gcm.累计消耗EXP[当前精英化阶段][当前精英化阶段初始等级-1]
        龙门币 += gcm.累计消耗龙门币[当前精英化阶段][当前精英化阶段目标等级-1] - gcm.累计消耗龙门币[当前精英化阶段][当前精英化阶段初始等级-1]

    return (EXP, 龙门币)
