from pydantic import ConfigDict

from arknights_game_model._raw_game_data.model import GameDataModel


class Skill(GameDataModel):
    id: str
    level: int


class Equip(GameDataModel):
    id: str
    level: int


class Character(GameDataModel):
    id: str
    level: int
    evolve_phase: int
    main_skill_level: int
    skills: list[Skill]
    equips: list[Equip]
    potential_rank: int


class Item(GameDataModel):
    model_config = ConfigDict(strict=False)

    id: str
    count: int


class Data(GameDataModel):
    characters: list[Character]
    items: list[Item]


class HttpsZonaiSklandComApiV1GameCultivatePlayer(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
