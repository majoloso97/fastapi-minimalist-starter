from pydantic import BaseSettings


class Settings(BaseSettings):
    HELLO_MSG: str
    WELCOME_TEMPLATE: str


settings = Settings()
