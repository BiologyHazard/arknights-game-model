from __future__ import annotations

from enum import Enum

from pydantic import ConfigDict, Field

from arknights_game_model.item_info_model import ItemBundle

from .model import GameDataModel


class SpecialOperatorTargetType(Enum):
    NONE = 0
    ROGUE = 1


class PowerData(GameDataModel):
    nation_id: str | None
    group_id: str | None
    team_id: str | None


class UnlockCondition(GameDataModel):
    phase: int
    level: int


class BlackboardDataPair(GameDataModel):
    key: str
    value: float
    value_str: str | None


class TraitData(GameDataModel):
    unlock_condition: UnlockCondition
    required_potential_rank: int
    blackboard: list[BlackboardDataPair]
    override_descripton: str | None
    prefab_key: str | None
    range_id: str | None


class TraitDataBundle(GameDataModel):
    candidates: list[TraitData]


class AttributesData(GameDataModel):
    max_hp: int
    atk: int
    def_: int = Field(alias="def")
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
    attract_immune: bool


class AttributeKeyFrame(GameDataModel):
    level: int
    data: AttributesData


class PhaseData(GameDataModel):
    character_prefab_key: str
    range_id: str | None
    max_level: int
    attributes_key_frames: list[AttributeKeyFrame]
    evolve_cost: list[ItemBundle]


class SpecializeLevelData(GameDataModel):
    unlock_cond: UnlockCondition
    lvl_up_time: int
    level_up_cost: list[ItemBundle]


class MainSkill(GameDataModel):
    skill_id: str | None
    override_prefab_key: str | None
    override_token_key: str | None
    level_up_cost_cond: list[SpecializeLevelData]
    unlock_cond: UnlockCondition


class TalentData(GameDataModel):
    unlock_condition: UnlockCondition
    required_potential_rank: int
    prefab_key: str
    name: str | None
    description: str | None
    range_id: str | None
    blackboard: list[BlackboardDataPair]
    token_key: str | None
    is_hide_talent: bool


class TalentDataBundle(GameDataModel):
    candidates: list[TalentData]


class AttributeModifier(GameDataModel):
    attribute_type: int
    formula_item: int
    value: float
    load_from_blackboard: bool
    fetch_base_value_from_source_entity: bool


class AttributeModifierData(GameDataModel):
    abnormal_flags: list[int] = Field(max_length=0)
    abnormal_immunes: list[int] = Field(max_length=0)
    abnormal_antis: list[int] = Field(max_length=0)
    abnormal_combos: list[int] = Field(max_length=0)
    abnormal_combo_immunes: list[int] = Field(max_length=0)
    attribute_modifiers: list[AttributeModifier]


class ExternalBuff(GameDataModel):
    attributes: AttributeModifierData


class PotentialRank(GameDataModel):
    type: int
    description: str
    buff: ExternalBuff | None
    equivalent_cost: list[ItemBundle] = Field(max_length=0)


class AllSkillLvlup(GameDataModel):
    unlock_cond: UnlockCondition
    lvl_up_cost: list[ItemBundle]


class CharacterData(GameDataModel):
    model_config = ConfigDict(strict=False)

    name: str
    description: str | None
    sort_index: int
    sp_target_type: SpecialOperatorTargetType
    sp_target_id: str | None
    can_use_general_potential_item: bool
    can_use_activity_potential_item: bool
    potential_item_id: str | None
    activity_potential_item_id: str | None
    classic_potential_item_id: str | None
    nation_id: str | None
    group_id: str | None
    team_id: str | None
    main_power: PowerData
    sub_power: list[PowerData]
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
    trait: TraitDataBundle | None
    phases: list[PhaseData]
    display_token_dict: dict[str, bool]
    skills: list[MainSkill]
    talents: list[TalentDataBundle]
    potential_ranks: list[PotentialRank]
    favor_key_frames: list[AttributeKeyFrame]
    all_skill_lvlup: list[AllSkillLvlup]


type CharacterTable = dict[str, CharacterData]
