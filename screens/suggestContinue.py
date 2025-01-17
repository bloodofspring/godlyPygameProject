import pygame

from screens.abstract import AbstractScreen
from screens.credits import CreditsScreen
from screens.teamChoosing import TeamChoosingScreen


class ContinueScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        self.text_font = pygame.font.Font(None, 150)
        self.continue_text = self.text_font.render("Continue?", True, (0, 0, 0))

        self.frequency = 60
        self.counter_value = 9

    def update_counter(self):
        if self.counter_value == 0:
            self.runner.change_screen(CreditsScreen(screen=self.screen, runner=self.runner))

        if self.runner.frame % self.frequency == 0:
            self.counter_value -= 1

        counter_text = self.text_font.render(str(self.counter_value), True, (0, 0, 0))
        self.screen.blit(counter_text, (480, 400))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.runner.change_screen(TeamChoosingScreen(screen=self.screen, runner=self.runner))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.continue_text, (250, 100))
        self.update_counter()
