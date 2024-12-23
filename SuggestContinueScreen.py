import pygame


class ContinueScreen:
    def __init__(self, screen):
        self.screen = screen
        self.text_font = pygame.font.Font(None, 150)
        self.continue_text = self.text_font.render("Continue?", True, (0, 0, 0))
        self.counter = 999
        self.counter_text = self.text_font.render(str(self.counter // 100), True, (0, 0, 0))

    def update(self) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.continue_text, (250, 100))
        self.counter -= 1
        self.counter_text = self.text_font.render(str(self.counter // 100), True, (0, 0, 0))
        self.screen.blit(self.counter_text, (450, 250))