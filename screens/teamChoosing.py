from util import load_image
import pygame


class TeamChoosingScreen:
    def __init__(self, screen):
        self.screen = screen
        font = pygame.font.Font(None, 50)
        self.choose_text = font.render("Choose 6 pokemon for battle", True, (0, 0, 0))

    def update(self) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (280, 0))