import pygame
import os


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
