from enum import Enum, auto


class AppState(Enum):
    BOOTING = auto()
    WAITING_CLIENT = auto()
    CLIENT_READY = auto()
    IN_QUEUE = auto()
    CHAMP_SELECT = auto()
    LOADING = auto()
    IN_GAME = auto()
    POST_GAME = auto()
    SHUTDOWN = auto()