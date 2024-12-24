import pygame

from screens.abstractScreen import AbstractScreen
from screens.teamChoosing import TeamChoosingScreen
from util import load_image


class TitleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        logo = load_image('logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
        self.welcome_text_font = pygame.font.Font(None, 50)

        self.welcome_text_color: tuple[int, int, int] = (0, 0, 0)
        self.flicker_frequency = 1
        self.delta: int = 5

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.runner.current_screen = TeamChoosingScreen(screen=self.screen, runner=self.runner)

    def update_welcome_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            rendered_text = self.welcome_text_font.render("Press Enter to start", True, self.welcome_text_color)
            self.screen.blit(rendered_text, (350, 500))

            return

        if any(map(lambda x: x == 255, self.welcome_text_color)):
            self.delta = abs(self.delta) * -1

        if any(map(lambda x: x == 0, self.welcome_text_color)):
            self.delta = abs(self.delta)

        self.welcome_text_color = tuple(map(lambda x: (x + self.delta) % 256, self.welcome_text_color))

        rendered_text = self.welcome_text_font.render("Press Enter to start", True, self.welcome_text_color)
        self.screen.blit(rendered_text, (350, 500))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.logo, (90, -100))

        self.update_welcome_text()
