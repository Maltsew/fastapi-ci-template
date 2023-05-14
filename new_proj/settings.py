"""
module docstring
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    class docstring
    """
    main_url: str = ''


settings = Settings()
