from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    IS_DEBUG: bool
    ORIGINS: list[str]

    model_config = SettingsConfigDict(
        # Load .env first
        env_file=('.env')
    )