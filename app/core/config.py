#configs globais da aplicação 
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Pet API"
    APP_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file = ".env", env_file_encoding = "utf-8"
    )

    #descrição base da API

settings = Settings()
