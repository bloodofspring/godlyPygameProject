from abc import ABC, abstractmethod


class AbstractScreen(ABC):
    def __init__(self, screen, runner):
        self.screen = screen
        self.runner = runner

    @abstractmethod
    def update(self):
        raise NotImplemented
