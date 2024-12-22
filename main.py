import pygame
import sys
from utility import load_image

def main():
    pygame.init()
    pygame.display.set_caption("Pokemon PvE game")
    image = load_image('icon.png', colorkey=-1)
    pygame.display.set_icon(image)
    size = width, height = 1000, 700

    screen = pygame.display.set_mode(size)

    running = True
    FPS = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        ...   # тут переход с заставки на выбор покемонов
        ...

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()