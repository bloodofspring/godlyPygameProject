from utility import load_image
import pygame


class TeamChoosingScreen:
    def __init__(self, screen):
        self.screen = screen

    def run(self) -> None:
        self.screen.fill((255, 255, 255))