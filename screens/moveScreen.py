import pygame
from screens.abstractScreen import AbstractScreen


class MoveChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner, pokemon_team):
        super().__init__(screen=screen, runner=runner)

        self.pokemon_team = pokemon_team

        title_font = pygame.font.Font(None, 50)
        self.pokemon_font = pygame.font.Font(None, 50)
        self.choose_text = title_font.render("Choose 4 moves for each pokemon", True, (0, 0, 0))
        self.tip_text = title_font.render("Choose with Space and press Enter when ready", True, (0, 0, 0))

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (210, 0))
        self.screen.blit(self.tip_text, (100, 50))
