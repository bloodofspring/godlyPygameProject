import pygame

from abc import ABC, abstractmethod


class AbsScreen(ABC):
    def __init__(self, screen):
        self.screen = screen

    @abstractmethod
    def update(self):
        raise NotImplemented



class ContinueScreen(AbsScreen):
    def __init__(self, screen):
        super().__init__(screen)

        self.text_font = pygame.font.Font(None, 150)
        self.continue_text = self.text_font.render("Continue?", True, (0, 0, 0))

    # def update(self) -> None:
    #     self.screen.fill((255, 255, 255))
    #     self.screen.blit(self.continue_text, (250, 100))


