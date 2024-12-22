class AbstractPokemon:
    def __init__(self):
        self.name = ''
        self.attack = 0
        self.hp = 0
        self.defense = 0
        self.speed = 0

    def take_damage(self, damage) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.faint()

    def faint(self) -> None:
        ...