from database.models import Pokemon
from util import load_image
import os


class PokemonEntity:
    def __init__(self, name: str | None = None, db_id: int | None = None):
        if db_id:
            self.db: Pokemon = Pokemon.get_by_id(db_id)
        else:
            self.db: Pokemon = Pokemon.get(name=name)

        self.name = self.db.name
        self.hp = int(self.db.stats.hp * 2.5)
        self.attack = self.db.stats.attack
        self.defense = self.db.stats.defense
        self.special_attack = self.db.stats.special_attack
        self.special_defense = self.db.stats.special_defense
        self.speed = self.db.stats.speed
        self.types = self.db.types

        self.icon = load_image('icon.png', path=f'static/images/{self.name}')
        self.front_frames = [load_image(f'front{i}.png', path=f'static/images/{self.name}') for i in range(len(os.listdir(f'static/images/{self.name}')) // 2 - 1)]
        self.back_frames = [load_image(f'back{i}.png', path=f'static/images/{self.name}') for i in range(len(os.listdir(f'static/images/{self.name}')) // 2 - 1)]

        self.current_hp = self.hp

    def take_damage(self, damage: int) -> None:
        if damage > self.current_hp:
            self.current_hp = 0
            return

        self.current_hp -= damage

    def __repr__(self):
        return f"PokemonEntity(db_id={self.db.ID})"
