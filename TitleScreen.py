from utility import load_image
import pygame


class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
        font = pygame.font.Font(None, 50)
        self.welcome_text = font.render("Press Enter to start", True, (0, 0, 0))

    def run(self) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.logo, (90, -100))
        self.screen.blit(self.welcome_text, (350, 500))
