from database.models import Pokemon
from util import load_image
import os


<<<<<<< HEAD
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
        self.front_frames = [load_image(f'front{i}.png', path=f'static/images/{self.name}') for i in range(len(os.listdir(f'static/images/{self.name}')) // 2)]
        self.back_frames = [load_image(f'back{i}.png', path=f'static/images/{self.name}') for i in range(len(os.listdir(f'static/images/{self.name}')) // 2)]

        self.current_hp = self.hp

    def take_damage(self, damage: int) -> None:
        if damage > self.current_hp:
            self.current_hp = 0
=======
class Pokemon:
    def __init__(self, id):
        self.id = id
        # тестовый вариант, тут грузить из базы данных с помощью id, все стаы тут для теста
        self.name = "Charizard"
        self.attack = 1
        self.current_hp = 1
        self.defense = 1
        self.speed = 1
        self.icon = load_image('icon.png', path='static/images/Charizard')

    def take_damage(self, damage: int) -> None:
        if damage > self.current_hp:
            self.hp = 0
            self.faint()
>>>>>>> main
            return

        self.hp -= damage

    def __repr__(self):
        return f"PokemonEntity(db_id={self.db.ID})"
