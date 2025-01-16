import pygame

from constants import attacks_per_pokemon
from database.models import PokemonAttack
from entities import PokemonEntity
from screens.abstractScreen import AbstractScreen
from util import load_image


class MoveChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner, pokemon_team):
        super().__init__(screen=screen, runner=runner)

        self.pokemon_team: list[PokemonEntity] = pokemon_team
        self.pokemon_team_position = 0
        self.player_cur_position: int = 0

        self.chosen_attacks: dict[PokemonEntity, list[PokemonAttack]] = {}

        for pokemon in self.pokemon_team:
            self.chosen_attacks[pokemon] = []

        self.current_attack: PokemonAttack | None = None

        title_font = pygame.font.Font(None, 50)
        self.pokemon_font = pygame.font.Font(None, 50)
        self.choose_text = title_font.render("Choose 4 moves for each pokemon", True, (0, 0, 0))
        self.tip_text = title_font.render("Choose with Space and press Enter when ready", True, (0, 0, 0))

    def change_player_position(self, d: int):
        self.player_cur_position = (self.player_cur_position + d) % len(self.pokemon_team[self.pokemon_team_position].db.attacks)

    def change_pokemon_team_position(self, d: int = 1):
        self.pokemon_team_position += d

        if self.pokemon_team_position == len(self.pokemon_team):
            print("Changing screen...")
            # self.runner.change_screen() ToDo: add next screen and uncomment

    def render_attacks(self):
        current_pokemon: PokemonEntity = self.pokemon_team[self.pokemon_team_position]
        attacks: tuple[PokemonAttack, ...] = tuple(map(lambda x: x.attack, current_pokemon.db.attacks))

        cut_attacks = attacks[self.player_cur_position:self.player_cur_position + 6]
        if len(cut_attacks) < 6:
            cut_attacks += attacks[:6-len(cut_attacks)]
        attacks = cut_attacks

        for i, attack in zip(range(len(attacks)), attacks):
            if i == self.pokemon_team_position:
                self.current_attack = attack
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (620, 123 + i * 85, 350, 80), 3)
            else:
                rect_color = pygame.Color('gray')

                if attack in self.chosen_attacks[self.pokemon_team[self.pokemon_team_position]]:
                    rect_color = pygame.Color('green')

                pygame.draw.rect(self.screen, rect_color, (620, 123 + i * 85, 350, 80), 3)

            attack_text = self.pokemon_font.render(attack.name, True, (0, 0, 0))
            self.screen.blit(attack_text, (630, 145 + i * 85))
            self.screen.blit(load_image(f'pokemonTypes/{attack.type.name}.PNG'), (875, 146 + i * 85))

    def render_pokemons(self):
        for i, pokemon in zip(range(len(self.pokemon_team)), self.pokemon_team):
            if i == self.pokemon_team_position:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (45, 123 + i * 85, 550, 80), 3)
            else:
                rect_color = pygame.Color('gray')
                pygame.draw.rect(self.screen, rect_color, (45, 123 + i * 85, 550, 80), 3)

            pokemon_text = self.pokemon_font.render(pokemon.name, True, (0, 0, 0))
            self.screen.blit(pokemon_text, (205, 145 + i * 85))
            self.screen.blit(pokemon.icon, (55, 113 + i * 85))

            if len(pokemon.types) == 1:
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (500, 146 + i * 85))
            else:
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (400, 146 + i * 85))
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[1].type.name}.PNG'), (500, 146 + i * 85))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if self.current_attack in self.chosen_attacks[self.pokemon_team[self.pokemon_team_position]]:
                            self.chosen_attacks[self.pokemon_team[self.pokemon_team_position]].remove(self.current_attack)
                        else:
                            self.chosen_attacks[self.pokemon_team[self.pokemon_team_position]].append(self.current_attack)

                    if event.key in (pygame.K_w, pygame.K_UP):
                        self.change_player_position(-1)

                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        self.change_player_position(1)

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (210, 0))
        self.screen.blit(self.tip_text, (100, 50))

        if len(self.chosen_attacks[self.pokemon_team[self.pokemon_team_position]]) == attacks_per_pokemon:
            self.change_pokemon_team_position()

        self.render_pokemons()
        self.render_attacks()

        self.handle_events(events=events)
