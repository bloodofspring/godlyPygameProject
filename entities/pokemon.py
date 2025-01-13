from util import load_image
from pokemon_stats import pokemon_stats


class Pokemon:
    def __init__(self, name: str):
        # ToDo: Добавить загрузку статов из конфига или бд
        self.name = name
        self.hp = pokemon_stats[name]['hp']
        self.attack = pokemon_stats[name]['atk']
        self.defence = pokemon_stats[name]['def']
        self.special_attack = pokemon_stats[name]['sp.atk']
        self.special_defence = pokemon_stats[name]['sp.def']
        self.speed = pokemon_stats[name]['speed']
        self.types = pokemon_stats[name]['types']
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
