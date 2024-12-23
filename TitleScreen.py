from utility import load_image
import pygame


class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
        self.welcome_text_font = pygame.font.Font(None, 50)
        self.welcome_text_color = 2
        self.welcome_text_color_change = 2
        self.welcome_text = self.welcome_text_font.render("Press Enter to start", True, [self.welcome_text_color for _ in range(3)])

    def run(self) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.logo, (90, -100))
        if self.welcome_text_color in (0, 200):
            self.welcome_text_color_change = -self.welcome_text_color_change
        self.welcome_text_color += self.welcome_text_color_change
        self.welcome_text = self.welcome_text_font.render("Press Enter to start", True, [self.welcome_text_color for _ in range(3)])
        self.screen.blit(self.welcome_text, (350, 500))

    def handle_event(self, event):  # может быть, позже удалю
        ...

