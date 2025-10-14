from pydantic import BaseModel, ConfigDict, model_validator


def remove_underline(s: str) -> str:
    return s.replace("_", "")


class GameDataModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=remove_underline,
        loc_by_alias=False,
        extra="forbid",
        strict=True,
    )

    @model_validator(mode="before")
    @classmethod
    def to_lower(cls, data):
        if isinstance(data, dict):
            return {(k.lower().replace("_", "") if isinstance(k, str) else k): v for k, v in data.items()}
        else:
            return data
