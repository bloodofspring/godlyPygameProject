import sys

import pygame

from constants import window_width, window_height, game_fps
from screens.suggestContinue import ContinueScreen
from screens.title import TitleScreen
from util import load_image


def setup_window():
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))

    pygame.display.set_caption("Pokemon PvE game")
    pygame.display.set_icon(load_image('icon.png'))

    return window


class GameRunner:
    def __init__(self, game_window):
        self.game_window = game_window
        self.current_screen = TitleScreen(screen=self.game_window, runner=self)

        self.is_running: bool = True
        self.frame: int = 0
        self.clock = pygame.time.Clock()

    def handle_events(self, events):
        for event in events:
            match event.type:
                case pygame.QUIT:
                    self.is_running = False

    def start(self):
        while self.is_running:
            self.frame = (self.frame + 1) % game_fps

            events = pygame.event.get()
            self.handle_events(events=events)

            self.current_screen.update(events, frame=self.frame)

            self.clock.tick(game_fps)
            pygame.display.flip()

        self.quit()

    @staticmethod
    def quit():
        pygame.quit()


if __name__ == "__main__":
    runner = GameRunner(game_window=setup_window())
    sys.exit(runner.start())
