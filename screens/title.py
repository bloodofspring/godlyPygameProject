import pygame
import random

from screens.abstractScreen import AbstractScreen
from screens.teamChoosing import TeamChoosingScreen
from util import load_image, PokeSprite, HorizontalBorder, all_sprites


class TitleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
        self.welcome_text_font = pygame.font.Font(None, 50)

        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (logo.get_width() // 3 * 2, logo.get_height() // 3 * 2))

        # ToDo: Поправить порнуху (разграничить flicker_frequency и welcome_text_color_change_delta, а то делают одно и то же)
        self.welcome_text_color: tuple[int, int, int] = (0, 0, 0)
        self.flicker_frequency = 1
        self.welcome_text_color_change_delta: int = 5

        self.jumping: bool = False
        self.jump_counter = 0
        self.horizontal_border = HorizontalBorder(-200, 700, 1500)

        pygame.mixer.music.load('static/music/title_music.mp3')
        pygame.mixer.music.play()

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.runner.change_screen(TeamChoosingScreen(screen=self.screen, runner=self.runner))
                        pygame.mixer.music.pause()
                        pygame.mixer.music.unload()

    def update_welcome_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            rendered_text = self.welcome_text_font.render("Press Enter to start", True, self.welcome_text_color)
            self.screen.blit(rendered_text, (350, 450))

            return

        if any(map(lambda x: x == 255, self.welcome_text_color)):
            self.welcome_text_color_change_delta = abs(self.welcome_text_color_change_delta) * -1

        if any(map(lambda x: x == 0, self.welcome_text_color)):
            self.welcome_text_color_change_delta = abs(self.welcome_text_color_change_delta)

        self.welcome_text_color = tuple(map(lambda x: (x + self.welcome_text_color_change_delta) % 256, self.welcome_text_color))

        rendered_text = self.welcome_text_font.render("Press Enter to start", True, self.welcome_text_color)
        self.screen.blit(rendered_text, (350, 450))

    def random_pokemon_jumping(self):
        if (not self.jumping) and random.random() > 0.99:
            self.jumping = True
            self.pokemon = PokeSprite((1100, 700), self.horizontal_border)
        elif self.jumping:
            if self.pokemon.rect.x < -100:
                self.jumping = False
                all_sprites.remove(self.pokemon)

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.logo, (90, -100))
        self.random_pokemon_jumping()
        all_sprites.draw(self.screen)
        all_sprites.update()

        self.update_welcome_text()
