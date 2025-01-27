import pygame
import random
import math

from screens.abstract import AbstractScreen
from screens.teamChoosing import TeamChoosingScreen
<<<<<<< HEAD
from util import load_image, PokeSprite, HorizontalBorder, all_sprites
from constants import window_width, window_height
=======
from util import load_image
>>>>>>> main


class TitleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
        self.welcome_text_font = pygame.font.Font("static/fonts/pixelFont.TTF", 50)

<<<<<<< HEAD
        background = load_image('forest_background.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.welcome_text_alpha: int = 255
        self.flicker_frequency = 1
        self.alpha_change_delta: int = 5
=======
        self.welcome_text_color: tuple[int, int, int] = (0, 0, 0)
        self.flicker_frequency = 1
        self.delta: int = 5
>>>>>>> main

        self.jumping: bool = False
        self.jump_counter = 0
        self.jump_x, self.jump_y = 1100, 600
        self.list_of_bouncing_pokemon = ('Blaziken', 'Charizard', 'Gengar', 'Groudon', 'Lapras', 'Lucario', 'Mew', 'Pikachu', 'Sceptile')

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
<<<<<<< HEAD
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        self.runner.change_screen(TeamChoosingScreen(screen=self.screen, runner=self.runner))
=======
                        self.runner.current_screen = TeamChoosingScreen(screen=self.screen, runner=self.runner)
>>>>>>> main

    def update_welcome_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            rendered_text = self.welcome_text_font.render("Press  Enter  to  start", True, self.welcome_text_alpha)
            self.screen.blit(rendered_text, (260, 370))

            return

<<<<<<< HEAD
        if self.welcome_text_alpha == 255:
            self.alpha_change_delta = abs(self.alpha_change_delta) * -1

        if self.welcome_text_alpha == 0:
            self.alpha_change_delta = abs(self.alpha_change_delta)

        rendered_text = self.welcome_text_font.render("Press  Enter  to  start", True, (0, 0, 0))
        self.welcome_text_alpha = (self.welcome_text_alpha + self.alpha_change_delta) % 256
        rendered_text.set_alpha(self.welcome_text_alpha)
        self.screen.blit(rendered_text, (260, 370))
=======
        if any(map(lambda x: x == 255, self.welcome_text_color)):
            self.delta = abs(self.delta) * -1

        if any(map(lambda x: x == 0, self.welcome_text_color)):
            self.delta = abs(self.delta)

        self.welcome_text_color = tuple(map(lambda x: (x + self.delta) % 256, self.welcome_text_color))

        rendered_text = self.welcome_text_font.render("Press Enter to start", True, self.welcome_text_color)
        self.screen.blit(rendered_text, (350, 450))
>>>>>>> main

    def random_pokemon_jumping(self):
        if (not self.jumping) and random.random() > 0.995:
            self.jumping = True
            pokemon = random.choice(self.list_of_bouncing_pokemon)
            self.pokemon_icon = load_image(f'{pokemon}/icon.png')
            self.screen.blit(self.pokemon_icon, (self.jump_x, self.jump_y))
        elif self.jumping:
            if self.runner.frame == 0:
                self.jump_counter += 1
            angle = self.runner.frame / 30 * math.pi
            self.jump_x -= 2
            self.jump_y = 600 - int(50 * abs(math.sin(angle)))
            self.screen.blit(self.pokemon_icon, (self.jump_x, self.jump_y))
            if self.jump_x < -100:
                self.jumping = False
                self.jump_counter = 0
                self.jump_x, self.jump_y = 1100, 600


    def update(self, events, **kwargs) -> None:
        self.handle_events(events)

        self.screen.fill((255, 255, 255))
<<<<<<< HEAD
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.logo, (90, -140))
=======
        self.screen.blit(self.logo, (90, -100))
>>>>>>> main
        self.random_pokemon_jumping()

        self.update_welcome_text()
