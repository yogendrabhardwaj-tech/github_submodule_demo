"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "github_submodule_demo"


def get_settings() -> Settings:
    return Settings(app_name=os.getenv("APP_NAME", "github_submodule_demo"))
