from pathlib import Path

import yaml

from backend.config.settings import Settings


class ConfigLoader:

    @staticmethod
    def load(path: str | Path = "config/settings.yaml") -> Settings:

        config_path = Path(path)

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with config_path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = yaml.safe_load(file)

        return Settings.model_validate(data)