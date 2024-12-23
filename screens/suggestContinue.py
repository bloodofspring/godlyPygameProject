import pygame

from screens.abstractScreen import AbstractScreen


class ContinueScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        self.text_font = pygame.font.Font(None, 150)
        self.continue_text = self.text_font.render("Continue?", True, (0, 0, 0))

        self.frequency = 60
        self.counter_value = 10
        self.counter_text = self.text_font.render(str(self.counter_value), True, (0, 0, 0))

    def update_counter(self):
        if self.counter_value == 0:
            return

        if self.runner.frame % self.frequency == 0:
            self.counter_value -= 1

        self.counter_text = self.text_font.render(str(self.counter_value), True, (0, 0, 0))
        self.screen.blit(self.counter_text, (450, 250))

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.continue_text, (250, 100))
        self.update_counter()
