import pygame

from abc import ABC, abstractmethod


class AbsScreen(ABC):
    def __init__(self, screen):
        self.screen = screen

    @abstractmethod
    def update(self):
        raise NotImplemented