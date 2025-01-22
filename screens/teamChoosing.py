import pygame

from constants import pokemon_names, window_width, window_height
from entities import PokemonEntity
from screens.abstract import AbstractScreen
from screens.moveChoosing import MoveChoosingScreen
from util import load_image, draw_button_with_background


class TeamChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        self.main_font = pygame.font.Font("static/fonts/pixelFont.TTF", 50)
        self.choose_text = self.main_font.render("Choose  6  pokemon  for  battle", True, (0, 0, 0))
        secondary_font = pygame.font.Font("static/fonts/pixelFont.TTF", 40)
        self.tip_text = secondary_font.render("Choose  with  Space  and  press  Enter  when  ready", True, (0, 0, 0))

        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.all_pokemon: list[PokemonEntity] = [PokemonEntity(i) for i in pokemon_names]
        self.chosen_pokemons = {x: False for x in self.all_pokemon}
        self.cursor_pos = 0

        pygame.mixer.music.load('static/music/preparations_music.mp3')
        pygame.mixer.music.play(loops=-1)  # -1 означает, что музыка бесконечно зациклена

    @property
    def six_pokemon_chosen(self):
        return tuple(self.chosen_pokemons.values()).count(True) == 6

    @property
    def pokemon_cursor_on(self):
        return self.all_pokemon[self.cursor_pos]

    def handle_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            if event.key == pygame.K_RETURN and self.six_pokemon_chosen:
                self.runner.change_screen(MoveChoosingScreen(
                    screen=self.screen,
                    runner=self.runner,
                    pokemon_team=list(filter(lambda k: self.chosen_pokemons[k], self.chosen_pokemons))
                ))

            if event.key == pygame.K_SPACE and (not self.six_pokemon_chosen or self.chosen_pokemons[self.pokemon_cursor_on]):
                self.chosen_pokemons[self.pokemon_cursor_on] = not self.chosen_pokemons[self.pokemon_cursor_on]

            if event.key in (pygame.K_w, pygame.K_UP):
                self.cursor_pos = (self.cursor_pos - 1) % len(self.all_pokemon)

            if event.key in (pygame.K_s, pygame.K_DOWN):
                self.cursor_pos = (self.cursor_pos + 1) % len(self.all_pokemon)

    def display_pokemon(self):
        for i in range(7):
            pokemon = self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)]

            if i == 3:
                rect_color = 'yellow'
            elif self.chosen_pokemons[pokemon]:
                rect_color = 'green'
            else:
                rect_color = 'grey'

            draw_button_with_background(
                600, 80, 3, (0, 0, 0), rect_color,
                blit=True, x=200, y=100 + i * 85, screen=self.screen
            )

            self.screen.blit(self.main_font.render(pokemon.name, True, (0, 0, 0)), (330, 115 + i * 85))
            self.screen.blit(pokemon.icon, (200, 90 + i * 85))

            rect_start_x = 700
            for t in pokemon.types:
                self.screen.blit(load_image(f'pokemonTypes/{t.type.name}.PNG', -1), (rect_start_x, 123 + i * 85))
                rect_start_x -= 100

    def update(self, events, **kwargs) -> None:
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.choose_text, (165, 0))
        self.screen.blit(self.tip_text, (80, 50))

        self.display_pokemon()
        self.handle_events(events)
