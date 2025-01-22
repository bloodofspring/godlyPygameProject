import pygame

from constants import window_width, window_height
from screens import AbstractScreen
from util import get_screen, load_image


class StageScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter, pokemon_team, chosen_attacks):
        super().__init__(screen=screen, runner=runner)

        self.background = pygame.transform.scale(load_image('battlefield.png'), (window_width, window_height))
        self.background.set_alpha(0)
        self.background_alpha_change_delta = 2
        self.background_alpha_change_frequency = 1

        self.pokemon_team = pokemon_team
        self.chosen_attacks = chosen_attacks
        self.battle_counter = battle_counter
        font = pygame.font.Font("static/fonts/pixelFont.TTF", 200)
        self.stage_text = font.render(f"Stage {battle_counter}", True, (0, 0, 0))

    def handle_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            if event.key == pygame.K_RETURN:
                self.background_alpha_change_delta = 15

    def blit_background(self):
        if self.runner.frame % self.background_alpha_change_frequency:
            return

        if self.background.get_alpha() + self.background_alpha_change_delta > 255:
            self.runner.change_screen(get_screen(name="BattleScreen")(
                screen=self.screen,
                runner=self.runner,
                battle_counter=self.battle_counter,
                pokemon_team=self.pokemon_team,
                chosen_attacks=self.chosen_attacks
            ))

        self.background.set_alpha(self.background.get_alpha() + self.background_alpha_change_delta)
        self.screen.blit(self.background, (0, 0))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((128, 128, 128))
        self.blit_background()
        self.screen.blit(self.stage_text, (260, 250))
