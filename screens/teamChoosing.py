import pygame

from screens.abstractScreen import AbstractScreen


class TeamChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        font = pygame.font.Font(None, 50)
        self.choose_text = font.render("Choose 6 pokemon for battle", True, (0, 0, 0))

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (280, 0))
