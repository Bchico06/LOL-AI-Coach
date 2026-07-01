from backend.app.states import AppState


class StateMachine:
    def __init__(self):
        self.state = AppState.BOOTING

    def set_state(self, state: AppState) -> None:
        self.state = state

    def get_state(self) -> AppState:
        return self.state

    def update(self) -> None:
        # Más adelante acá irán las transiciones automáticas.
        pass