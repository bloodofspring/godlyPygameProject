class AbstractPokemon:
    def __init__(self):
        self.name = "Meow-meow"
        self.attack = 1
        self.hp = 1
        self.defense = 1
        self.speed = 1

    def take_damage(self, damage: int) -> None:
        if damage > self.hp:
            self.hp = 0
            self.faint()
            return

        self.hp -= damage

    def faint(self) -> None:
        raise NotImplementedError
