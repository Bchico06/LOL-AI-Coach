from pathlib import Path
import logging


class LoggerFactory:

    @staticmethod
    def create(
        name: str,
        level: str,
        log_file: str,
    ) -> logging.Logger:

        Path(log_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(level)

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s | %(message)s",
            "%H:%M:%S",
        )

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)

        return logger