from enum import Enum


class StrEnum(str, Enum):
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class EnvEnum(StrEnum):
    DEV: str = "dev"
    STAGGING: str = "stagging"
    PROD: str = "prod"


class LLMTypeEnum(StrEnum):
    HUGGINGFACE: str = "huggingface"
    OPENAI: str = "openai"
