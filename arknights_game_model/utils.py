import re
from itertools import accumulate


def escape_description(s):
    """删除所有的HTML标签"""
    return re.sub(r"<[^>]*?>", "", s)


def 计算累计消耗(干员升级消耗: list[list[int]]) -> list[list[int]]:
    return [list(accumulate(filter(lambda x: x > 0, 升级消耗列表), initial=0)) for 升级消耗列表 in 干员升级消耗]
