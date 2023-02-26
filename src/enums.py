from enum import Enum


class StrEnum(str, Enum):
    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class EnvEnum(StrEnum):
    DEV: str = "dev"
    STAGGING: str = "stagging"
    PROD: str = "prod"


class LLMTypeEnum(StrEnum):
    HUGGINGFACE: str = "huggingface"
    OPENAI: str = "openai"


class AinetworkProviderURLEnum(StrEnum):
    TEST_NET: str = "https://testnet-api.ainetwork.ai"
    MAIN_NET: str = "https://mainnet-api.ainetwork.ai"
