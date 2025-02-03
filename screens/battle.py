import math
import random

import pygame

import constants
from database.models import PokemonAttack, PokemonTypeInteraction
from entities import PokemonEntity
from screens import AbstractScreen
from screens.credits import CreditsScreen
from util import load_image, draw_button_with_background, get_screen


class HealthBar:
    BAR_LENGTH: int = 192

    def __init__(self, xpos: int, ypos: int, screen: pygame.Surface, entity_to_track: PokemonEntity):
        self.xpos = xpos
        self.ypos = ypos
        self.screen = screen

        self.bar = pygame.transform.scale(load_image("health-bar.png"), (250, 35))
        self.hp_font = pygame.font.Font("static/fonts/pixelFont.TTF", 40)

        self.entity_to_track: PokemonEntity = entity_to_track
        self.full_hp = entity_to_track.hp
        self.hp = entity_to_track.current_hp
        self.entity_name = entity_to_track.name

    @property
    def red_bar_length(self) -> int:
        return math.ceil((self.BAR_LENGTH / self.full_hp) * self.hp)

    def render_bar_borders(self):
        white_dots = (49, 98, 147, 196)
        for i in white_dots:
            pygame.draw.rect(self.screen, (235, 235, 235), (self.xpos + i, self.ypos + 54, 4, 4))

        borders = (94, 143, 192)
        for i in borders:
            if i <= self.red_bar_length + 48:
                center_pixel_color = (180, 0, 0)
            else:
                center_pixel_color = (180, 180, 180)

            pygame.draw.rect(self.screen, (0, 0, 0), (self.xpos + i, self.ypos + 54, 4, 5))
            pygame.draw.rect(self.screen, center_pixel_color, (self.xpos + i, self.ypos + 59, 4, 5))
            pygame.draw.rect(self.screen, (0, 0, 0), (self.xpos + i, self.ypos + 64, 4, 5))

    def render_line(self, front_color: tuple[int, int, int], secondary_color: tuple[int, int, int], consider_hp: bool):
        left = self.xpos + 49
        right = self.red_bar_length if consider_hp else self.BAR_LENGTH

        pygame.draw.rect(self.screen, front_color, (left, self.ypos + 54, right, 14))
        pygame.draw.rect(self.screen, secondary_color, (left, self.ypos + 63, right, 5))

    def render_hp_bar_sections(self):
        self.render_line(front_color=(235, 235, 235), secondary_color=(180, 180, 180), consider_hp=False)
        self.render_line(front_color=(255, 0, 0), secondary_color=(180, 0, 0), consider_hp=True)
        self.render_bar_borders()

    def update(self, entity_to_track):
        self.entity_to_track = entity_to_track
        self.full_hp = self.entity_to_track.hp
        self.hp = self.entity_to_track.current_hp
        self.entity_name = self.entity_to_track.name
        self.render()

    def render(self):
        back_width = draw_button_with_background(
            320, 80, 3, (0, 0, 0), "gray",
            blit=True, x=self.xpos, y=self.ypos, screen=self.screen
        ).get_width()

        self.screen.blit(self.bar, (self.xpos, self.ypos + 40))

        rendered_text = self.hp_font.render(self.entity_name, True, (0, 0, 0))
        self.screen.blit(rendered_text, (self.xpos + (back_width - rendered_text.get_width()) / 2, self.ypos + 6))

        rendered_text = self.hp_font.render(str(self.hp), True, (0, 0, 0))
        self.screen.blit(rendered_text, (self.xpos + 250, self.ypos + 40))
        self.render_hp_bar_sections()

class ButtonsBar:
    def __init__(self, screen: pygame.Surface, pokemon_team, chosen_attacks, fighting_pokemon):
        self.screen = screen

        self.cursor_pos_x = 0
        self.cursor_pos_y = 0

        self.pokemon_team = pokemon_team
        self.chosen_attacks = chosen_attacks
        self.fighting_pokemon = fighting_pokemon
        self.attack_font = pygame.font.Font("static/fonts/pixelFont.TTF", 30)

    def change_cursor_position(self, x: int, y: int):
        if y == 0:
            if self.cursor_pos_y == 2:
                self.cursor_pos_x = (self.cursor_pos_x + x) % 5
            else:
                self.cursor_pos_x = (self.cursor_pos_x + x) % 2
        else:
            if self.cursor_pos_y == 2:
                self.cursor_pos_x = min(1, self.cursor_pos_x)
            self.cursor_pos_y = (self.cursor_pos_y + y) % 3

    def render_pokemon_attacks(self):
        for y in range(2):
            for x in range(2):
                move_text = self.attack_font.render(
                    self.chosen_attacks[self.fighting_pokemon][x * 2 + y].name, True, (0, 0, 0)
                )
                self.screen.blit(move_text, (490 + x * 255, 460 + y * 75))

    def render_reserved_pokemon(self):
        for i in range(5):
            self.screen.blit(self.pokemon_team[i + 1].icon, (15 + i * 195, 590))
    
    def render(self):
        # ToDo: redo this
        #          [x][x] 0
        #          [x][x] 1
        # [x][x][x][x][x] 2
        #  0  1  2  3  4  /
        # To This
        #          [x][x] 2
        #          [x][x] 1
        # [x][x][x][x][x] 0
        #  4  3  2  1  0  /
        for x in range(2):
            for y in range(2):
                draw_button_with_background(
                    250, 70, 3, (0, 0, 0),
                    (255, 255, 0) if x == self.cursor_pos_x and y == self.cursor_pos_y else (255, 255, 255),
                    blit=True, x=480 + x * 255, y=440 + y * 75, screen=self.screen
                )

        for x in range(5):
            if self.pokemon_team[x + 1].current_hp > 0:
                if x == self.cursor_pos_x and self.cursor_pos_y == 2:
                    background = (255, 255, 0)
                else:
                    background = (255, 255, 255)
            else:
                if x == self.cursor_pos_x and self.cursor_pos_y == 2:
                    background = (128, 128, 0)
                else:
                    background = (128, 128, 128)

            draw_button_with_background(
                190, 80, 3, (0, 0, 0), background,
                blit=True, x=15 + x * 195, y=600, screen=self.screen
            )
            self.render_reserved_pokemon()
            self.render_pokemon_attacks()

    def update(self, fighting_pokemon):
        self.fighting_pokemon = fighting_pokemon
        self.render()


class BattleScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter, pokemon_team, chosen_attacks):
        super().__init__(screen=screen, runner=runner)

        self.chosen_attacks = chosen_attacks
        self.pokemon_team: list[PokemonEntity, ...] = pokemon_team
        self.fighting_pokemon: PokemonEntity = pokemon_team[0]

        for i in self.pokemon_team:
            i.current_hp = i.hp

        self.battle_counter = battle_counter

        self.current_ally_frame = 1
        self.current_enemy_frame = 1

        self.enemy_pokemon = random.choices([PokemonEntity(i) for i in constants.pokemon_names], k=6)
        if battle_counter == 3:
            for p in self.enemy_pokemon:
                p.increase_dmg(k=1.5)
        self.enemy_fighting_pokemon: PokemonEntity = self.enemy_pokemon[0]
        self.enemy_attacks = {}

        for i in self.enemy_pokemon:
            self.enemy_attacks[i] = random.choices(list(map(lambda x: x.attack, i.db.attacks)), k=4)

        self.battlefield = pygame.transform.scale(
            load_image('battlefield.png'),
            (constants.window_width, constants.window_height)
        )
        self.setup_music()

        self.button_bar = ButtonsBar(self.screen, self.pokemon_team, self.chosen_attacks, self.fighting_pokemon)

        self.ally_hp_bar = HealthBar(10, 280, self.screen, self.fighting_pokemon)
        self.enemy_hp_bar = HealthBar(670, 80, self.screen, self.enemy_fighting_pokemon)

    def setup_music(self):
        if self.battle_counter != 3:
            pygame.mixer.music.load('static/music/battle_music.mp3')
        else:
            pygame.mixer.music.load('static/music/last_battle_music.mp3')
        pygame.mixer.music.play(loops=-1)

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

    def ally_turn(self):
        if self.fighting_pokemon.current_hp != 0 and self.button_bar.cursor_pos_y != 2:
            attack: PokemonAttack = self.chosen_attacks[self.fighting_pokemon][
                self.button_bar.cursor_pos_x * 2 + self.button_bar.cursor_pos_y
            ]

            if attack.accuracy / 100 > random.random():
                ally_damage = attack.power

                if attack.category == 'physical':
                    ally_damage = ally_damage * self.fighting_pokemon.attack / self.enemy_fighting_pokemon.defense
                else:
                    ally_damage = ally_damage * self.fighting_pokemon.special_attack / self.enemy_fighting_pokemon.special_defense

                if attack.type in [t.type.name for t in self.fighting_pokemon.types]:
                    ally_damage *= 1.5

                for ep_type in map(lambda x: x.type, self.enemy_fighting_pokemon.types):
                    k = PokemonTypeInteraction.select().where(
                        (PokemonTypeInteraction.first == attack.type) & (PokemonTypeInteraction.second == ep_type)
                    )[0].k
                    ally_damage *= k

                ally_damage = int(ally_damage)

                if self.enemy_fighting_pokemon.speed > self.fighting_pokemon.speed:
                    self.enemy_turn()
                    if self.fighting_pokemon.current_hp > 0:
                        self.enemy_fighting_pokemon.take_damage(ally_damage)
                        if self.enemy_fighting_pokemon.current_hp == 0:
                            self.enemy_turn()
                else:
                    self.enemy_fighting_pokemon.take_damage(ally_damage)
                    self.enemy_turn()
            else:
                self.enemy_turn()

            if all(map(lambda x: x.current_hp == 0, self.pokemon_team)):
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                self.runner.change_screen(get_screen(name="ContinueScreen")(
                    screen=self.screen,
                    runner=self.runner,
                    battle_counter=self.battle_counter + 1,
                    pokemon_team=self.pokemon_team,
                    chosen_attacks=self.chosen_attacks
                ))
            return

        if self.fighting_pokemon.current_hp == 0:
            if all(map(lambda x: x.current_hp == 0, self.pokemon_team)):
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                self.runner.change_screen(get_screen(name="ContinueScreen")(
                    screen=self.screen,
                    runner=self.runner,
                    battle_counter=self.battle_counter + 1,
                    pokemon_team=self.pokemon_team,
                    chosen_attacks=self.chosen_attacks
                ))
            elif self.pokemon_team[self.button_bar.cursor_pos_x + 1].current_hp != 0:
                self.current_ally_frame = 1
                self.pokemon_team[0], self.pokemon_team[self.button_bar.cursor_pos_x + 1] = self.pokemon_team[
                    self.button_bar.cursor_pos_x + 1], self.pokemon_team[0]
                self.fighting_pokemon = self.pokemon_team[0]
            return

        if self.pokemon_team[self.button_bar.cursor_pos_x + 1].current_hp != 0:
            self.current_ally_frame = 1
            self.pokemon_team[0], self.pokemon_team[self.button_bar.cursor_pos_x + 1] = self.pokemon_team[
                self.button_bar.cursor_pos_x + 1], self.pokemon_team[0]
            self.fighting_pokemon = self.pokemon_team[0]
            if self.fighting_pokemon.current_hp != 0:
                self.enemy_turn()

    def enemy_turn(self):
        if self.enemy_fighting_pokemon.current_hp != 0:
            attack: PokemonAttack = random.choice(self.enemy_attacks[self.enemy_fighting_pokemon])
            if attack.accuracy / 100 > random.random():
                enemy_damage = attack.power
                if attack.category == 'physical':
                    enemy_damage = enemy_damage * self.enemy_fighting_pokemon.attack / self.fighting_pokemon.defense
                else:
                    enemy_damage = enemy_damage * self.enemy_fighting_pokemon.special_attack / self.fighting_pokemon.special_defense
                if attack.type in [t.type.name for t in self.enemy_fighting_pokemon.types]:
                    enemy_damage *= 1.5

                for al_type in map(lambda x: x.type, self.fighting_pokemon.types):
                    k = PokemonTypeInteraction.select().where(
                        (PokemonTypeInteraction.first == attack.type) & (PokemonTypeInteraction.second == al_type)
                    )[0].k
                    enemy_damage *= k

                enemy_damage = int(enemy_damage)
                self.fighting_pokemon.take_damage(enemy_damage)
            return

        if len(self.enemy_pokemon) > 1:
            self.enemy_pokemon = list(filter(lambda x: x.current_hp > 0, self.enemy_pokemon))
            self.enemy_fighting_pokemon = self.enemy_pokemon[0]
            self.current_enemy_frame = 1
        else:
            if self.battle_counter == 3:
                self.runner.change_screen(CreditsScreen(
                    screen=self.screen,
                    runner=self.runner,
                    pokemon_team=self.pokemon_team
                ))
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                self.runner.change_screen(get_screen(name="StageScreen")(
                    screen=self.screen,
                    runner=self.runner,
                    battle_counter=self.battle_counter + 1,
                    pokemon_team=self.pokemon_team,
                    chosen_attacks=self.chosen_attacks
                ))

    def handle_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            if event.key == pygame.K_RETURN:
                self.ally_turn()
    
            if event.key in (pygame.K_w, pygame.K_UP):
                self.button_bar.change_cursor_position(0, -1)
    
            if event.key in (pygame.K_s, pygame.K_DOWN):
                self.button_bar.change_cursor_position(0, 1)
    
            if event.key in (pygame.K_a, pygame.K_LEFT):
                self.button_bar.change_cursor_position(-1, 0)
    
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                self.button_bar.change_cursor_position(1, 0)

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.blit(self.battlefield, (0, 0))

        self.button_bar.update(fighting_pokemon=self.fighting_pokemon)

        self.render_ally_fighting_pokemon()
        self.render_enemy_fighting_pokemon()

        self.ally_hp_bar.update(entity_to_track=self.fighting_pokemon)
        self.enemy_hp_bar.update(entity_to_track=self.enemy_fighting_pokemon)
