import pygame
import sys
from utility import load_image
from TitleScreen import TitleScreen
from TeamChoosingScreen import TeamChoosingScreen


def main():
    pygame.init()
    pygame.display.set_caption("Pokemon PvE game")
    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)
    icon = load_image('icon.png')
    pygame.display.set_icon(icon)

    current_screen = TitleScreen(screen)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        current_screen.run()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        current_screen = TeamChoosingScreen(screen)
        ...

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
