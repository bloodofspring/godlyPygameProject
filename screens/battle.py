import pygame
from screens.abstract import AbstractScreen


class BattleScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter):
        super().__init__(screen=screen, runner=runner)

        font = pygame.font.Font(None, 80)
        self.choose_text = font.render("This is Battle Screen!", True, (0, 0, 0))

        if battle_counter != 3:
            pygame.mixer.music.load('static/music/battle_music.mp3')
        else:
            pygame.mixer.music.load('static/music/last_battle_music.mp3')
        pygame.mixer.music.play(loops=-1)  # -1 означает, что музыка бесконечно зациклена

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (200, 100))
