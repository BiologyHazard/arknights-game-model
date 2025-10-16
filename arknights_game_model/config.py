from pydantic import DirectoryPath, FilePath, field_validator
from pydantic.config import ExtraValues
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_prefix="arknights_game_model_",
        cli_parse_args=True,
        cli_kebab_case=True,
        extra="allow",
    )

    log_level: int | str = "INFO"
    """日志等级"""

    gamedata_folder: DirectoryPath
    """游戏数据文件夹路径"""
    online_time_path: FilePath
    """干员上线时间文件路径"""
    yituliu_item_value_path: FilePath
    """一图流物品价值文件路径"""

    pydantic_model_validate_strict: bool = False
    """是否启用 Pydantic 严格模式"""
    pydantic_model_validate_extra: ExtraValues = "allow"
    """Pydantic 模型额外字段处理方式"""

    @field_validator("log_level", mode="after")
    @classmethod
    def validate_log_level(cls, v: int | str) -> int | str:
        if isinstance(v, str) and v.isdigit():
            return int(v)
        elif isinstance(v, str):
            return v.upper()
        else:
            return v
