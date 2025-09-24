import re
from itertools import accumulate
from collections.abc import Iterable


def escape_description(s: str) -> str:
    """删除所有的自定义标签"""
    return re.sub(r"<[^>]*?>", "", s)


def find_dollar_tags(s: str) -> list[str]:
    """查找所有的 <$...> 标签"""
    return re.findall(r"<\$(.+?)>", s)


def find_at_tags(s: str) -> list[str]:
    """查找所有的 <@...> 标签"""
    return re.findall(r"<@(.+?)>", s)


def 计算累计消耗(干员升级消耗: Iterable[Iterable[int]]) -> list[list[int]]:
    return [list(accumulate(filter(lambda x: x > 0, 升级消耗列表), initial=0)) for 升级消耗列表 in 干员升级消耗]
