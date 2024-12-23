import pygame

from screens.abstractScreen import AbstractScreen
from util import load_image


class TitleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(load_image('logo.png'), (logo.get_width() // 2, logo.get_height() // 2))
        self.welcome_text_font = pygame.font.Font(None, 50)
        self.welcome_text_color = 2
        self.welcome_text_color_change = 2
        self.welcome_text = self.welcome_text_font.render("Press Enter to start", True,
                                                          [self.welcome_text_color for _ in range(3)])

    def update(self) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.logo, (90, -100))

        if self.welcome_text_color in (0, 200):
            self.welcome_text_color_change = -self.welcome_text_color_change

        self.welcome_text_color += self.welcome_text_color_change
        self.welcome_text = self.welcome_text_font.render("Press Enter to start", True,
                                                          [self.welcome_text_color for _ in range(3)])
        self.screen.blit(self.welcome_text, (350, 500))
