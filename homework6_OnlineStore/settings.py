from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    NAME_MIN_LENGTH: int = 2
    NAME_MAX_LENGTH: int = 64
    EMAIL_MIN_LENGTH: int = 5
    EMAIL_MAX_LENGTH: int = 64
    PASSWORD_MIN_LENGTH: int = 5
    PASSWORD_MAX_LENGTH: int = 64
    STRING_MAX_LENGTH: int = 128
    MIN_PRICE: float = 0.0

    class Config:
        env_file = '.env'


settings = Settings()
