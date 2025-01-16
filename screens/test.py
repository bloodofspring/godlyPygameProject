from screens.abstractScreen import AbstractScreen


class EmptyScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

    def update(self, events, **kwargs):
        pass
