import pygame
from screens.abstract import AbstractScreen
from entities import PokemonEntity
from util import load_image, get_screen
from constants import window_width, window_height


class GameOverScreen(AbstractScreen):
    def __init__(self, screen, runner, pokemon_team):
        super().__init__(screen=screen, runner=runner)

        font = pygame.font.Font(None, 80)
        small_font = pygame.font.Font(None, 50)
        self.gratitude_text = font.render("Game over!", True, (0, 0, 0))
        self.little_praise_text = small_font.render("However, your team did a good job", True, (0, 0, 0))
        self.pokemon_team: list[PokemonEntity] = pokemon_team

        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.animation_frames: list[int] = [1 for _ in range(len(self.pokemon_team))]

        self.very_small_font = pygame.font.Font(None, 30)
        self.flicker_frequency = 1
        self.alpha_delta = 5
        self.current_alpha: int = 255

        pygame.mixer.music.load('static/music/credits_music.mp3')
        pygame.mixer.music.play()

    def beautiful_animation(self):
        for i in range(len(self.pokemon_team)):
            animation = self.pokemon_team[i].front_frames[(self.animation_frames[i] - 1) // 3]
            self.screen.blit(animation, (170 + 120 * i, 600 - int(50 * abs(2.5 - i))))
            self.animation_frames[i] += 1
            if self.animation_frames[i] // 3 == len(self.pokemon_team[i].front_frames):
                self.animation_frames[i] = 1

    def handle_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            self.runner.change_screen(get_screen(name="TitleScreen")(screen=self.screen, runner=self.runner))

    def update_flickering_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            return

        rendered_text = self.very_small_font.render("Press any key", True, (0, 0, 0))

        if self.current_alpha == 255:
            self.alpha_delta = abs(self.alpha_delta) * -1

        if self.current_alpha == 0:
            self.alpha_delta = abs(self.alpha_delta)

        self.current_alpha = (self.current_alpha + self.alpha_delta) % 256
        rendered_text.set_alpha(self.current_alpha)
        self.screen.blit(rendered_text, (440, 210))

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.gratitude_text, (350, 100))
        self.screen.blit(self.little_praise_text, (250, 160))
        self.update_flickering_text()
        self.beautiful_animation()

        self.handle_events(events=events)
