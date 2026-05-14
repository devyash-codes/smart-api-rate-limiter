from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")

    RATE_LIMIT_PER_MINUTE = int(
        os.getenv("RATE_LIMIT_PER_MINUTE", 5)
    )

    APP_NAME = os.getenv(
        "APP_NAME",
        "Smart API Rate Limiter"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"


settings = Settings()

