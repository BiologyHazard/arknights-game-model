```python
>>> from datetime import datetime
>>> from arknights_game_model import game_data, ItemInfoList

>>> game_data.load_data()

>>> 夜莺 = game_data.characters.by_name("夜莺")
>>> nightingale_cost = 夜莺.计算养成消耗(
    初始精英化阶段=0, 初始等级=1, 初始技能等级=1, 初始技能专精等级=(0, 0, 0), 初始模组等级={"ORIGINAL": 0, "X": 0, "Y": 0, "D": 0, "A": 0},
    目标精英化阶段=2, 目标等级=90, 目标技能等级=7, 目标技能专精等级=(3, 3, 3), 目标模组等级={"ORIGINAL": 0, "X": 3, "Y": 3, "D": 0, "A": 0},
)
>>> print(nightingale_cost)
龙门币×1 龙门币×114514 EXP×1919810 医疗芯片×5 ...

>>> nightingale_cost.combine()
龙门币×114515 EXP×1919810 医疗芯片×5 ...

>>> nightingale_cost.counter()
defaultdict(<class 'int'>, {'4001': 114515, 'exp': 1919810, ...})

>>> all_characters_cost = ItemInfoList()
>>> for character in game_data.characters:
...     all_characters_cost.extend(character.计算养成消耗())  # 默认拉满
...
>>> all_characters_cost.combine()
龙门币×114514 EXP×1919810 ...

>>> characters_before_1st_anniversary = game_data.characters.filter(lambda c: c.实装时间() < datetime(2025, 5, 1, 16))

```
