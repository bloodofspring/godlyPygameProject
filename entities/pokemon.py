from database.models import Pokemon
from util import load_image


class PokemonEntity:
    def __init__(self, name: str, db_id: int | None = None):
        if db_id:
            self.db: Pokemon = Pokemon.get_by_id(db_id)
        else:
            self.db: Pokemon = Pokemon.get(name=name)

        self.name = self.db.name
        self.hp = self.db.stats.hp
        self.attack = self.db.stats.attack
        self.defence = self.db.stats.defence
        self.special_attack = self.db.stats.special_attack
        self.special_defence = self.db.stats.special_defence
        self.speed = self.db.stats.speed
        self.types = self.db.types

        self.icon = load_image('icon.png', path=f'static/images/{self.name}')
        self.current_hp = self.hp

    def take_damage(self, damage: int) -> None:
        if damage > self.current_hp:
            self.current_hp = 0
            self.faint()
            return

        self.current_hp -= damage

    def faint(self) -> None:
        raise NotImplementedError
