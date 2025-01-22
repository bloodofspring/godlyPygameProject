import pygame

from constants import window_width, window_height
from screens import AbstractScreen
from screens.gameOver import GameOverScreen
from util import get_screen, load_image


class ContinueScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter, pokemon_team, chosen_attacks):
        super().__init__(screen=screen, runner=runner)
        self.battle_counter = battle_counter
        self.pokemon_team = pokemon_team
        self.chosen_attacks = chosen_attacks

        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.text_font = pygame.font.Font("static/fonts/pixelFont.TTF", 80)
        self.continue_text = self.text_font.render("Press  enter  to  continue", True, (0, 0, 0))

        self.frequency = 60
        self.counter_value = 9

    def update_counter(self):
        if self.counter_value == 0:
            self.runner.change_screen(GameOverScreen(screen=self.screen, runner=self.runner, pokemon_team=self.pokemon_team))

        if self.runner.frame % self.frequency == 0:
            self.counter_value -= 1

        counter_text = self.text_font.render(str(self.counter_value), True, (0, 0, 0))
        self.screen.blit(counter_text, (480, 350))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.runner.change_screen(get_screen(name="StageScreen")(
                            screen=self.screen,
                            runner=self.runner,
                            battle_counter=1,
                            pokemon_team=self.pokemon_team,
                            chosen_attacks=self.chosen_attacks
                        ))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.continue_text, (35, 100))
        self.update_counter()
