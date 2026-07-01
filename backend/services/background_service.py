from __future__ import annotations

from abc import ABC, abstractmethod
from threading import Event, Thread


class BackgroundService(ABC):
    """
    Clase base para todos los servicios que se ejecutan
    en segundo plano.
    """

    def __init__(self, name: str):
        self.name = name
        self._thread: Thread | None = None
        self._stop_event = Event()

    def start(self) -> None:

        if self.is_running():
            return

        self._stop_event.clear()

        self._thread = Thread(
            target=self.run,
            name=self.name,
            daemon=True,
        )

        self._thread.start()

    def stop(self) -> None:

        self._stop_event.set()

        if self._thread:
            self._thread.join(timeout=2)

    def is_running(self) -> bool:

        return (
            self._thread is not None
            and self._thread.is_alive()
        )

    @property
    def stopped(self) -> bool:

        return self._stop_event.is_set()

    @abstractmethod
    def run(self) -> None:
        """
        Método principal del servicio.
        """
        pass