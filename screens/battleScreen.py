import pygame
from screens.abstractScreen import AbstractScreen


class BattleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        font = pygame.font.Font(None, 80)
        self.choose_text = font.render("This is Battle Screen!", True, (0, 0, 0))

        # pygame.mixer.music.load('static/music/credits_music.mp3')
        # pygame.mixer.music.play()

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (200, 100))
