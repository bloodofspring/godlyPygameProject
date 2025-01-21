import pygame

from constants import attacks_per_pokemon, window_width, window_height
from database.models import PokemonAttack
from entities import PokemonEntity
from screens.abstract import AbstractScreen
from screens.battle import StageScreen
from util import load_image, draw_button_with_background


class MoveChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner, pokemon_team):
        super().__init__(screen=screen, runner=runner)

        self.pokemon_team: list[PokemonEntity] = pokemon_team
        self.pokemon_team_position = self.player_cur_position = 0

        self.chosen_attacks: dict[PokemonEntity, list[PokemonAttack]] = {p: [] for p in self.pokemon_team}
        self.current_attack: PokemonAttack | None = None

        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.main_font = pygame.font.Font(None, 50)
        self.choose_text = self.main_font.render("Choose 4 moves for each pokemon", True, (0, 0, 0))
        self.tip_text = self.main_font.render("Choose with Space", True, (0, 0, 0))

    @property
    def current_pokemon(self):
        return self.pokemon_team[self.pokemon_team_position]

    def change_cursor_position(self, d: int):
        self.player_cur_position = (self.player_cur_position + d) % len(self.current_pokemon.db.attacks)

    def change_pokemon_team_position(self) -> bool:
        self.pokemon_team_position += 1

        if self.pokemon_team_position == len(self.pokemon_team):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.runner.change_screen(StageScreen(
                screen=self.screen,
                runner=self.runner,
                battle_counter=1,
                pokemon_team=self.pokemon_team,
                chosen_attacks=self.chosen_attacks
            ))

            return True

        return False

    def render_attacks(self):
        current_pokemon: PokemonEntity = self.current_pokemon
        attacks: tuple[PokemonAttack, ...] = tuple(map(lambda x: x.attack, current_pokemon.db.attacks))

        cut_attacks = attacks[self.player_cur_position:self.player_cur_position + 6]
        if len(cut_attacks) < 6:
            cut_attacks += attacks[:6 - len(cut_attacks)]
        attacks = cut_attacks

        for i, attack in zip(range(len(attacks)), attacks):
            if i == self.pokemon_team_position:
                rect_color = 'yellow'
                self.current_attack = attack
            elif attack in self.chosen_attacks[self.current_pokemon]:
                rect_color = 'green'
            else:
                rect_color = 'gray'

            # pygame.draw.rect(self.screen, rect_color, (620, 123 + i * 85, 350, 80), 3)
            draw_button_with_background(
                350, 80, 3, (0, 0, 0), rect_color,
                blit=True, x=620, y=123 + i * 85, screen=self.screen
            )

            self.screen.blit(self.main_font.render(attack.name, True, (0, 0, 0)), (630, 145 + i * 85))
            self.screen.blit(load_image(f'pokemonTypes/{attack.type.name}.PNG', -1), (875, 146 + i * 85))

    def render_pokemons(self):
        for i, pokemon in zip(range(len(self.pokemon_team)), self.pokemon_team):
            if i == self.pokemon_team_position:
                rect_color = 'yellow'
            else:
                rect_color = 'gray'

            # pygame.draw.rect(self.screen, rect_color, (45, 123 + i * 85, 550, 80), 3)
            draw_button_with_background(
                550, 80, 3, (0, 0, 0), rect_color,
                blit=True, x=45, y=123 + i * 85, screen=self.screen
            )

            self.screen.blit(self.main_font.render(pokemon.name, True, (0, 0, 0)), (205, 145 + i * 85))
            self.screen.blit(pokemon.icon, (55, 113 + i * 85)) 

            rect_start_x = 500
            for t in pokemon.types:
                self.screen.blit(load_image(f'pokemonTypes/{t.type.name}.PNG', -1), (rect_start_x, 146 + i * 85))
                rect_start_x -= 100

    def select_attack(self):
        if self.current_attack in self.chosen_attacks[self.current_pokemon]:
            self.chosen_attacks[self.current_pokemon].remove(self.current_attack)
            return

        self.chosen_attacks[self.current_pokemon].append(self.current_attack)

    def handle_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            if event.key == pygame.K_SPACE:
                self.select_attack()

            if event.key in (pygame.K_w, pygame.K_UP):
                self.change_cursor_position(-1)

            if event.key in (pygame.K_s, pygame.K_DOWN):
                self.change_cursor_position(1)

    def update(self, events, **kwargs) -> None:
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.choose_text, (210, 0))
        self.screen.blit(self.tip_text, (350, 50))

        if len(self.chosen_attacks[self.current_pokemon]) == attacks_per_pokemon:
            if self.change_pokemon_team_position():
                return

        self.render_pokemons()
        self.render_attacks()

        self.handle_events(events=events)
