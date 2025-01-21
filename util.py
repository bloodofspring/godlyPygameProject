import pygame
import os
import random
from constants import pokemon_names


all_sprites = pygame.sprite.Group()


def draw_button_with_background(
        width: int, height: int,
        border_width: int | None, border_color: tuple[int, int, int] | str | None,
        background_color: tuple[int, int, int] | str, alpha: int = 128,
        blit: bool = False, x: int | None = None, y: int | None = None, screen: pygame.Surface | None = None
) -> pygame.Surface:
    surface = pygame.Surface((width, height))
    surface.set_alpha(alpha)
    surface.fill(background_color)

    if border_width is not None and border_width > 0:
        pygame.draw.rect(surface, border_color, (0, 0, width - 1, height - 1), border_width)

    if blit:
        screen.blit(surface, (x, y)

    return surface


def load_image(name, colorkey=None, path="static/images"):
    fullname = os.path.join(path, name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit("Resource file not found")

    image = pygame.image.load(fullname)

    if colorkey is None:
        return image.convert_alpha()

    image = image.convert()

    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image


class HorizontalBorder(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2):
        super().__init__(all_sprites)
        self.image = pygame.Surface([x2 - x1, 1])
        self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class PokeSprite(pygame.sprite.Sprite):
    def __init__(self, pos, bouncy_surface):
        super().__init__(all_sprites)
        self.bouncy_surface = bouncy_surface
        pokemon = random.choice(pokemon_names)
        self.image = load_image(f'{pokemon}/icon.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1] - self.image.get_height()
        self.velocity_y = -9
        self.velocity_x = 2
        self.time = 0

    def update(self):
        self.time += 1
        if not pygame.sprite.collide_mask(self, self.bouncy_surface):
            self.rect = self.rect.move(-self.velocity_x, self.velocity_y)
        else:
            self.velocity_y = -9
            self.rect = self.rect.move(-self.velocity_x, self.velocity_y)
        if self.time % 2:
            self.velocity_y += 1