import time

from backend.services.background_service import BackgroundService


class LeagueWatcher(BackgroundService):

    def __init__(self, logger):
        super().__init__("LeagueWatcher")
        self.logger = logger

    def run(self):

        self.logger.info("LeagueWatcher started.")

        while not self.stopped:

            self.logger.info("Waiting for League Client...")

            time.sleep(2)

        self.logger.info("LeagueWatcher stopped.")