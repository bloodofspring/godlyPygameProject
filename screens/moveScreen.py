import pygame

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

        title_font = pygame.font.Font(None, 50)
        self.pokemon_font = pygame.font.Font(None, 50)
        self.choose_text = title_font.render("Choose 4 moves for each pokemon", True, (0, 0, 0))
        self.tip_text = title_font.render("Choose with Space and press Enter when ready", True, (0, 0, 0))

    def change_player_position(self, d: int):
        self.player_cur_position = (self.player_cur_position + d) % len(self.pokemon_team)

    def change_pokemon_team_position(self, d: int = 1):
        self.pokemon_team_position += d

        if self.pokemon_team_position == len(self.pokemon_team):
            print("Changing screen...")
            # self.runner.change_screen() ToDo: add next screen and uncomment

    def render_attacks(self):
        current_pokemon: PokemonEntity = self.pokemon_team[self.pokemon_team_position]
        attacks: tuple[PokemonAttack, ...] = tuple(map(lambda x: x.attack, current_pokemon.db.attacks))

        # print(list(map(lambda x: x.name, attacks))) ToDo: Remove

        for i, attack in zip(range(len(attacks)), attacks):
            if i == self.player_cur_position:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (690, 123 + i * 85, 250, 80), 3)
            else:
                rect_color = pygame.Color('gray')
                # if chosen: rect_color = pygame.Color('green')
                pygame.draw.rect(self.screen, rect_color, (690, 123 + i * 85, 250, 80), 3)

            attack_text = self.pokemon_font.render(attack.name, True, (0, 0, 0))
            self.screen.blit(attack_text, (700, 145 + i * 85))
            self.screen.blit(load_image(f'pokemonTypes/{attack.type.name}.PNG'), (575, 146 + i * 85))

    def render_pokemons(self):
        for i, pokemon in zip(range(len(self.pokemon_team)), self.pokemon_team):
            if i == self.pokemon_team_position:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (65, 123 + i * 85, 600, 80), 3)
            else:
                rect_color = pygame.Color('gray')
                pygame.draw.rect(self.screen, rect_color, (65, 123 + i * 85, 600, 80), 3)

            pokemon_text = self.pokemon_font.render(pokemon.name, True, (0, 0, 0))
            self.screen.blit(pokemon_text, (225, 145 + i * 85))
            self.screen.blit(pokemon.icon, (75, 113 + i * 85))

            if len(pokemon.types) == 1:
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (575, 146 + i * 85))
            else:
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (475, 146 + i * 85))
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[1].type.name}.PNG'), (575, 146 + i * 85))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        pass  # To the next screen

                    if event.key == pygame.K_SPACE:
                        pass  # enable attack

                    if event.key in (pygame.K_w, pygame.K_UP):
                        self.change_player_position(-1)

                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        self.change_player_position(1)

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (210, 0))
        self.screen.blit(self.tip_text, (100, 50))

        self.render_pokemons()
        self.render_attacks()

        self.handle_events(events=events)


# class TeamChoosingScreen(AbstractScreen):
#     def __init__(self, screen, runner):
#         super().__init__(screen=screen, runner=runner)
#         title_font = pygame.font.Font(None, 50)
#         self.pokemon_font = pygame.font.Font(None, 50)
#         self.choose_text = title_font.render("Choose 6 pokemon for battle", True, (0, 0, 0))
#         self.tip_text = title_font.render("Choose with Space and press Enter when ready", True, (0, 0, 0))
#         self.all_pokemon = [[PokemonEntity(i), False] for i in pokemon_names]
#         self.cursor_pos = 0
#
#     def handle_events(self, events) -> None:
#         for event in events:
#             match event.type:
#                 case pygame.KEYUP:
#                     if event.key == pygame.K_RETURN:
#                         if len(list(filter(lambda x: x[1], self.all_pokemon))) == 6:
#                             pokemon_team = [i[0] for i in list(filter(lambda x: x[1], self.all_pokemon))]
#                             self.runner.change_screen(
#                                 MoveChoosingScreen(screen=self.screen, runner=self.runner, pokemon_team=pokemon_team))
#                     if event.key == pygame.K_SPACE:
#                         if not sum(map(lambda x: x[1], self.all_pokemon)) == 6 or self.all_pokemon[self.cursor_pos][1]:
#                             self.all_pokemon[self.cursor_pos][1] = not self.all_pokemon[self.cursor_pos][1]
#                     if event.key in (pygame.K_w, pygame.K_UP):
#                         self.cursor_pos = (self.cursor_pos - 1) % len(self.all_pokemon)
#                     if event.key in (pygame.K_s, pygame.K_DOWN):
#                         self.cursor_pos = (self.cursor_pos + 1) % len(self.all_pokemon)
#
#     def display_pokemon(self):
#         for i in range(7):
#             if i == 3:
#                 pygame.draw.rect(self.screen, pygame.Color('yellow'), (200, 100 + i * 85, 600, 80), 3)
#             else:
#                 rect_color = (pygame.Color('grey'), pygame.Color('green'))[
#                     self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)][1]]
#                 pygame.draw.rect(self.screen, rect_color, (200, 100 + i * 85, 600, 80), 3)
#
#             pokemon_text = self.pokemon_font.render(
#                 self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)][0].name, True, (0, 0, 0))
#             pokemon = self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)][0]
#             self.screen.blit(pokemon_text, (350, 125 + i * 85))
#             self.screen.blit(pokemon.icon, (200, 90 + i * 85))
#             if len(pokemon.types) == 1:
#                 self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (700, 123 + i * 85))
#             else:
#                 self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (600, 123 + i * 85))
#                 self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[1].type.name}.PNG'), (700, 123 + i * 85))
#
#     def update(self, events, **kwargs) -> None:
#         self.handle_events(events)
#         self.screen.fill((255, 255, 255))
#         self.screen.blit(self.choose_text, (260, 0))
#         self.screen.blit(self.tip_text, (100, 50))
#         self.display_pokemon()
