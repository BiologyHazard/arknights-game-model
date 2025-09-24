from pydantic import Field

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
    id: str
    count: int = Field(strict=False)


class Data(GameDataModel):
    characters: list[Character]
    items: list[Item]


class HttpsZonaiSklandComApiV1GameCultivatePlayer(GameDataModel):
    code: int
    message: str
    timestamp: str
    data: Data
