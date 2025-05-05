from typing import Any

from pydantic import Field, ConfigDict

from ..item_info_model import ItemInfoDict
from .model import GameDataModel


class Power(GameDataModel):
    nation_id: str | None
    group_id: str | None
    team_id: str | None


class UnlockCondition(GameDataModel):
    phase: int
    level: int


class Blackboard(GameDataModel):
    key: str
    value: float
    value_str: str | None


class TraitCandidate(GameDataModel):
    unlock_condition: UnlockCondition
    required_potential_rank: int
    blackboard: list[Blackboard]
    override_descripton: str | None
    prefab_key: str | None
    range_id: str | None


class Trait(GameDataModel):
    candidates: list[TraitCandidate]


class AttributeKeyFrameData(GameDataModel):
    max_hp: int
    atk: int
    def_: int = Field(alias='def')
    magic_resistance: float
    cost: int
    block_cnt: int
    move_speed: float
    attack_speed: float
    base_attack_time: float
    respawn_time: int
    hp_recovery_per_sec: float
    sp_recovery_per_sec: float
    max_deploy_count: int
    max_deck_stack_cnt: int
    taunt_level: int
    mass_level: int
    base_force_level: int
    stun_immune: bool
    silence_immune: bool
    sleep_immune: bool
    frozen_immune: bool
    levitate_immune: bool
    disarmed_combat_immune: bool
    feared_immune: bool
    palsy_immune: bool


class AttributeKeyFrame(GameDataModel):
    level: int
    data: AttributeKeyFrameData


class Phase(GameDataModel):
    character_prefab_key: str
    range_id: str | None
    max_level: int
    attributes_key_frames: list[AttributeKeyFrame]
    evolve_cost: list[ItemInfoDict]


class LevelUpCostCond(GameDataModel):
    unlock_cond: UnlockCondition
    lvl_up_time: int
    level_up_cost: list[ItemInfoDict]


class Skill(GameDataModel):
    skill_id: str | None
    override_prefab_key: str | None
    override_token_key: str | None
    unlock_cond: UnlockCondition
    level_up_cost_cond: list[LevelUpCostCond]


class TalentCandidate(GameDataModel):
    unlock_condition: UnlockCondition
    required_potential_rank: int
    prefab_key: str
    name: str | None
    description: str | None
    range_id: str | None
    blackboard: list[Blackboard]
    token_key: str | None
    is_hide_talent: bool


class Talent(GameDataModel):
    candidates: list[TalentCandidate]


class PotentialRank(GameDataModel):
    type: int
    description: str
    buff: dict[str, Any] | None
    equivalent_cost: list = Field(max_length=0)


class AllSkillLvlup(GameDataModel):
    unlock_cond: UnlockCondition
    lvl_up_cost: list[ItemInfoDict]


class Character(GameDataModel):
    name: str
    description: str | None
    sort_index: int
    can_use_general_potential_item: bool
    can_use_activity_potential_item: bool
    potential_item_id: str | None
    activity_potential_item_id: str | None
    classic_potential_item_id: str | None
    nation_id: str | None
    group_id: str | None
    team_id: str | None
    main_power: Power
    sub_power: list[Power]
    display_number: str | None
    appellation: str
    position: str
    tag_list: list[str]
    item_usage: str | None
    item_desc: str | None
    item_obtain_approach: str | None
    is_not_obtainable: bool
    is_sp_char: bool
    max_potential_level: int
    rarity: int
    profession: str
    sub_profession_id: str
    trait: Trait | None
    phases: list[Phase]
    display_token_dict: dict[str, bool]
    skills: list[Skill]
    talents: list[Talent]
    potential_ranks: list[PotentialRank]
    favor_key_frames: list[AttributeKeyFrame]
    all_skill_lvlup: list[AllSkillLvlup]


type CharacterTable = dict[str, Character]
