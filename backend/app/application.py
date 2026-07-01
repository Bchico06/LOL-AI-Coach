import time

from backend.app.state_machine import StateMachine
from backend.config import ConfigLoader
from backend.league.watcher import LeagueWatcher
from backend.logging.logger import LoggerFactory


class Application:
    """
    Orquestador principal de la aplicación.
    Se encarga de inicializar los servicios y mantener
    vivo el ciclo principal del programa.
    """

    def __init__(self) -> None:
        # Cargar configuración
        self.settings = ConfigLoader.load()

        # Crear logger
        self.logger = LoggerFactory.create(
            name=self.settings.app.name,
            level=self.settings.logging.level,
            log_file=self.settings.logging.file,
        )

        # Máquina de estados
        self.state_machine = StateMachine()

        # Servicios
        self.league_watcher = LeagueWatcher(self.logger)

    def run(self) -> None:
        """
        Inicia la aplicación y todos los servicios necesarios.
        """

        self.logger.info("=" * 60)
        self.logger.info(
            "%s v%s",
            self.settings.app.name,
            self.settings.app.version,
        )
        self.logger.info("=" * 60)

        self.logger.info("Starting application...")

        # Iniciar servicios
        self.league_watcher.start()

        try:
            while True:
                # Más adelante la StateMachine tomará decisiones aquí
                self.state_machine.update()
                time.sleep(1)

        except KeyboardInterrupt:
            self.logger.info("Stopping application...")

        finally:
            self.league_watcher.stop()
            self.logger.info("Application closed.")