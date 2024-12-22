import pygame
import sys
from utility import load_image

def main():
    pygame.init()
    pygame.display.set_caption("Pokemon PvE game")
    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)

    icon = load_image('icon.png')
    pygame.display.set_icon(icon)
    logo = load_image('logo.png')
    logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))

    font = pygame.font.Font(None, 50)
    welcome_text = font.render("Press Enter to start", True, (0, 0, 0))

    running = True
    FPS = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill((255, 255, 255))
        screen.blit(logo, (90, -100))
        screen.blit(welcome_text, (350, 500))
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