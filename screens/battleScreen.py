import pygame
from screens.abstractScreen import AbstractScreen
# from screens.StageDisplayScreen import StageScreen
# ToDo: спасите от цикличного импорта

class BattleScreen(AbstractScreen):
    def __init__(self, screen, runner, battle_counter, pokemon_team, chosen_attacks):
        super().__init__(screen=screen, runner=runner)
        self.pokemon_team = pokemon_team
        self.chosen_attacks = chosen_attacks
        self.battle_counter = battle_counter
        self.fighting_pokemon = pokemon_team[0]
        self.cursor_position: list[int, int] = [0, 0]
        self.current_ally_frame = 1

        self.font = pygame.font.Font(None, 50)

        if self.battle_counter != 3:
            pygame.mixer.music.load('static/music/battle_music.mp3')
        else:
            pygame.mixer.music.load('static/music/last_battle_music.mp3')
        pygame.mixer.music.play(loops=-1)  # -1 означает, что музыка бесконечно зациклена

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
                    pygame.draw.rect(self.screen, pygame.Color('yellow'), (15 + x * 255, 440 + y * 75, 250, 70), 3)
                else:
                    pygame.draw.rect(self.screen, pygame.Color('gray'), (15 + x * 255, 440 + y * 75, 250, 70), 3)
        for x in range(5):
            if x == self.cursor_position[0] and self.cursor_position[1] == 2:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (15 + x * 195, 600, 190, 80), 3)
            else:
                pygame.draw.rect(self.screen, pygame.Color('gray'), (15 + x * 195, 600, 190, 80), 3)

    def render_reserved_pokemon(self):
        for i in range(5):
            self.screen.blit(self.pokemon_team[i + 1].icon, (15 + i * 195, 590))

    def render_pokemon_attacks(self):
        for y in range(2):
            for x in range(2):
                move_text = self.font.render(self.chosen_attacks[self.fighting_pokemon][x * 2 + y].name, True, (0, 0, 0))
                self.screen.blit(move_text, (25 + x * 255, 460 + y * 75))

    def render_ally_fighting_pokemon(self):
        frame = self.fighting_pokemon.back_frames[(self.current_ally_frame - 1) // 3]
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        self.screen.blit(frame, (50, 250))
        self.current_ally_frame += 1
        if self.current_ally_frame // 3 == len(self.fighting_pokemon.back_frames):
            self.current_ally_frame = 1


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

        self.render_buttons()
        self.render_reserved_pokemon()
        self.render_pokemon_attacks()
        self.render_ally_fighting_pokemon()