import pygame
from screens.abstractScreen import AbstractScreen


class AbilityScreen(AbstractScreen):
    def __init__(self, screen, runner, pokemon_team):
        super().__init__(screen=screen, runner=runner)

        self.pokemon_team = pokemon_team
        font = pygame.font.Font(None, 80)
        self.choose_text = font.render("Тут выбор абилок", True, (0, 0, 0))

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (200, 100))
