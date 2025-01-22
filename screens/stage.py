import pygame

from screens import AbstractScreen
from util import get_screen


class StageScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter, pokemon_team, chosen_attacks):
        super().__init__(screen=screen, runner=runner)

        self.pokemon_team = pokemon_team
        self.chosen_attacks = chosen_attacks
        self.battle_counter = battle_counter
        font = pygame.font.Font(None, 200)
        self.stage_text = font.render(f"Stage {battle_counter}", True, (0, 0, 0))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.runner.change_screen(get_screen(name="BattleScreen")(
                            screen=self.screen,
                            runner=self.runner,
                            battle_counter=self.battle_counter,
                            pokemon_team=self.pokemon_team,
                            chosen_attacks=self.chosen_attacks
                        ))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.stage_text, (260, 250))
