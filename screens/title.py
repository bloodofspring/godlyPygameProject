import pygame
import random

from screens.abstract import AbstractScreen
from screens.teamChoosing import TeamChoosingScreen
from util import load_image, PokeSprite, HorizontalBorder, all_sprites
from constants import window_width, window_height


class TitleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
        self.welcome_text_font = pygame.font.Font("static/fonts/pixelFont.TTF", 50)

        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.welcome_text_alpha: int = 255
        self.flicker_frequency = 1
        self.alpha_change_delta: int = 5

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
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        self.runner.change_screen(TeamChoosingScreen(screen=self.screen, runner=self.runner))

    def update_welcome_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            rendered_text = self.welcome_text_font.render("Press  Enter  to  start", True, self.welcome_text_alpha)
            self.screen.blit(rendered_text, (260, 370))

            return

        if self.welcome_text_alpha == 255:
            self.alpha_change_delta = abs(self.alpha_change_delta) * -1

        if self.welcome_text_alpha == 0:
            self.alpha_change_delta = abs(self.alpha_change_delta)

        rendered_text = self.welcome_text_font.render("Press  Enter  to  start", True, (0, 0, 0))
        self.welcome_text_alpha = (self.welcome_text_alpha + self.alpha_change_delta) % 256
        rendered_text.set_alpha(self.welcome_text_alpha)
        self.screen.blit(rendered_text, (260, 370))

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
        self.screen.blit(self.logo, (90, -140))
        self.random_pokemon_jumping()
        all_sprites.draw(self.screen)
        all_sprites.update()

        self.update_welcome_text()
