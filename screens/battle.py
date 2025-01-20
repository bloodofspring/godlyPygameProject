import pygame
from screens.abstract import AbstractScreen
from util import load_image
import constants
from database.models import PokemonAttack
from entities import PokemonEntity
import random


class BattleScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter, pokemon_team, chosen_attacks):
        super().__init__(screen=screen, runner=runner)
        self.pokemon_team = pokemon_team
        self.chosen_attacks = chosen_attacks
        self.battle_counter = battle_counter
        self.fighting_pokemon = pokemon_team[0]
        self.cursor_position: list[int] = [0, 0]
        self.current_ally_frame = 1
        self.current_enemy_frame = 1

        self.battlefield = pygame.transform.scale(load_image('battlefield.png'), (constants.window_width, constants.window_height))

        self.attack_font = pygame.font.Font(None, 50)
        self.name_font = pygame.font.Font(None, 55)

        if self.battle_counter != 3:
            pygame.mixer.music.load('static/music/battle_music.mp3')
        else:
            pygame.mixer.music.load('static/music/last_battle_music.mp3')
        pygame.mixer.music.play(loops=-1)  # -1 означает, что музыка бесконечно зациклена

        self.generate_enemy()

    def generate_enemy(self):
        self.enemy_pokemon = random.choices([PokemonEntity(i) for i in constants.pokemon_names], k=6)
        self.enemy_attacks: dict[PokemonEntity, list[PokemonAttack]] = {}
        for i in self.enemy_pokemon:
            self.enemy_attacks[i] = random.choices(list(map(lambda x: x.attack, i.db.attacks)), k=4)
        self.enemy_fighting_pokemon = self.enemy_pokemon[0]

    def change_cursor_position(self, x, y):
        if y == 0:
            if self.cursor_position[1] == 2:
                self.cursor_position[0] = (self.cursor_position[0] + x) % 5
            else:
                self.cursor_position[0] = (self.cursor_position[0] + x) % 2
        else:
            if self.cursor_position[1] == 2:
                self.cursor_position[0] = min(1, self.cursor_position[0])
            self.cursor_position[1] = (self.cursor_position[1] + y) % 3

    def render_buttons(self):
        for x in range(2):
            for y in range(2):
                if x == self.cursor_position[0] and y == self.cursor_position[1]:
                    pygame.draw.rect(self.screen, pygame.Color('yellow'), (480 + x * 255, 440 + y * 75, 250, 70), 3)
                else:
                    pygame.draw.rect(self.screen, pygame.Color('gray'), (480 + x * 255, 440 + y * 75, 250, 70), 3)
        for x in range(5):
            if x == self.cursor_position[0] and self.cursor_position[1] == 2:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (15 + x * 195, 600, 190, 80), 3)
            else:
                pygame.draw.rect(self.screen, pygame.Color('gray'), (15 + x * 195, 600, 190, 80), 3)

    def render_reserved_pokemon(self):
        for i in range(5):
            self.screen.blit(self.pokemon_team[i + 1].icon, (15 + i * 195, 590))

    def render_fighting_pokemon_hp(self):
        pygame.draw.rect(self.screen, pygame.Color('white'), (10, 280, 300, 80))
        ally_name = self.name_font.render(self.fighting_pokemon.name, True, (0, 0, 0))
        self.screen.blit(ally_name, (10 + (300 - ally_name.get_width()) // 2, 280))
        pygame.draw.line(self.screen, pygame.Color('green'), (20, 330), (300, 330), 5)
        ally_ratio = (self.fighting_pokemon.hp - self.fighting_pokemon.current_hp) / self.fighting_pokemon.hp
        if ally_ratio != 0:
            pygame.draw.line(self.screen, pygame.Color('red'), (300, 330), (300 - int(180 * ally_ratio), 330), 5)

        pygame.draw.rect(self.screen, pygame.Color('white'), (690, 80, 300, 80))
        enemy_name = self.name_font.render(self.enemy_fighting_pokemon.name, True, (0, 0, 0))
        self.screen.blit(enemy_name, (690 + (300 - enemy_name.get_width()) // 2, 80))
        pygame.draw.line(self.screen, pygame.Color('green'), (700, 130), (980, 130), 5)
        enemy_ratio = (self.enemy_fighting_pokemon.hp - self.enemy_fighting_pokemon.current_hp) / self.enemy_fighting_pokemon.hp
        if enemy_ratio != 0:
            pygame.draw.line(self.screen, pygame.Color('red'), (980, 130), (980 - int(180 * enemy_ratio), 130), 5)

    def render_pokemon_attacks(self):
        for y in range(2):
            for x in range(2):
                move_text = self.attack_font.render(self.chosen_attacks[self.fighting_pokemon][x * 2 + y].name, True, (0, 0, 0))
                self.screen.blit(move_text, (490 + x * 255, 460 + y * 75))

    def render_ally_fighting_pokemon(self):
        frame = self.fighting_pokemon.back_frames[(self.current_ally_frame - 1) // 3]
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        self.screen.blit(frame, (250, 400))
        self.current_ally_frame += 1
        if self.current_ally_frame // 3 == len(self.fighting_pokemon.back_frames):
            self.current_ally_frame = 1

    def render_enemy_fighting_pokemon(self):
        frame = self.enemy_fighting_pokemon.front_frames[(self.current_enemy_frame - 1) // 3]
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        self.screen.blit(frame, (620, 240))
        self.current_enemy_frame += 1
        if self.current_enemy_frame // 3 == len(self.enemy_fighting_pokemon.front_frames):
            self.current_enemy_frame = 1


    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        ...  # ToDo: тут применение приёма / замена покемона
                    if event.key in (pygame.K_w, pygame.K_UP):
                        self.change_cursor_position(0, -1)

                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        self.change_cursor_position(0, 1)

                    if event.key in (pygame.K_a, pygame.K_LEFT):
                        self.change_cursor_position(-1, 0)

                    if event.key in (pygame.K_d, pygame.K_RIGHT):
                        self.change_cursor_position(1, 0)


    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.battlefield, (0, 0))

        self.render_buttons()
        self.render_reserved_pokemon()
        self.render_pokemon_attacks()
        self.render_ally_fighting_pokemon()
        self.render_enemy_fighting_pokemon()
        self.render_fighting_pokemon_hp()


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
                        self.runner.change_screen(
                            BattleScreen(screen=self.screen, runner=self.runner, battle_counter=self.battle_counter,
                                         pokemon_team=self.pokemon_team, chosen_attacks=self.chosen_attacks))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.stage_text, (260, 250))