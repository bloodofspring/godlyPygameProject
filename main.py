import pygame
import sys

from constants import window_width, window_height, game_fps

from util import load_image
from screens.titleScreen import TitleScreen
from screens.suggestContinueScreen import ContinueScreen


def setup_window():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))

    pygame.display.set_caption("Pokemon PvE game")
    pygame.display.set_icon(load_image('icon.png'))

    return screen


def main():
    screen = setup_window()

    current_screen = TitleScreen(screen)

    is_running = True
    clock = pygame.time.Clock()

    while is_running:

        current_screen.update()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    is_running = False
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        current_screen = ContinueScreen(screen)
                        #  current_screen = TeamChoosingScreen(screen)

        clock.tick(game_fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
