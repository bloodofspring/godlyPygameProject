import pygame

from constants import pokemon_names
from entities import PokemonEntity
from screens.abstract import AbstractScreen
from screens.moveChoosing import MoveChoosingScreen
from util import load_image


class TeamChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)
        title_font = pygame.font.Font(None, 50)
        self.pokemon_font = pygame.font.Font(None, 50)
        self.choose_text = title_font.render("Choose 6 pokemon for battle", True, (0, 0, 0))
        self.tip_text = title_font.render("Choose with Space and press Enter when ready", True, (0, 0, 0))
        self.all_pokemon = [[PokemonEntity(i), False] for i in pokemon_names]
        self.cursor_pos = 0

        pygame.mixer.music.load('static/music/preparations_music.mp3')
        pygame.mixer.music.play(loops=-1)  # -1 означает, что музыка бесконечно зациклена

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        if len(list(filter(lambda x: x[1], self.all_pokemon))) == 6:
                            pokemon_team = [i[0] for i in list(filter(lambda x: x[1], self.all_pokemon))]
                            self.runner.change_screen(
                                MoveChoosingScreen(screen=self.screen, runner=self.runner, pokemon_team=pokemon_team))
                    if event.key == pygame.K_SPACE:
                        if not sum(map(lambda x: x[1], self.all_pokemon)) == 6 or self.all_pokemon[self.cursor_pos][1]:
                            self.all_pokemon[self.cursor_pos][1] = not self.all_pokemon[self.cursor_pos][1]
                    if event.key in (pygame.K_w, pygame.K_UP):
                        self.cursor_pos = (self.cursor_pos - 1) % len(self.all_pokemon)
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        self.cursor_pos = (self.cursor_pos + 1) % len(self.all_pokemon)

    def display_pokemon(self):
        for i in range(7):
            if i == 3:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (200, 100 + i * 85, 600, 80), 3)
            else:
                rect_color = (pygame.Color('grey'), pygame.Color('green'))[
                    self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)][1]]
                pygame.draw.rect(self.screen, rect_color, (200, 100 + i * 85, 600, 80), 3)

            pokemon_text = self.pokemon_font.render(
                self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)][0].name, True, (0, 0, 0))
            pokemon = self.all_pokemon[(self.cursor_pos + i - 3) % len(self.all_pokemon)][0]
            self.screen.blit(pokemon_text, (350, 125 + i * 85))
            self.screen.blit(pokemon.icon, (200, 90 + i * 85))
            if len(pokemon.types) == 1:
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (700, 123 + i * 85))
            else:
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[0].type.name}.PNG'), (600, 123 + i * 85))
                self.screen.blit(load_image(f'pokemonTypes/{pokemon.types[1].type.name}.PNG'), (700, 123 + i * 85))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (260, 0))
        self.screen.blit(self.tip_text, (100, 50))
        self.display_pokemon()
