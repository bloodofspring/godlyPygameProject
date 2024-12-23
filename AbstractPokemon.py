class AbstractPokemon:
    def __init__(self):
        self.name = 'name'
        self.attack = 1
        self.hp = 1
        self.defense = 1
        self.speed = 1

    def take_damage(self, damage) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.faint()

    def faint(self) -> None:
        ...