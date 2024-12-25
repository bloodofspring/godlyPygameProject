from util import load_image


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
            return

        self.hp -= damage

    def faint(self) -> None:
        raise NotImplementedError
