from util import load_image


class Pokemon:
    def __init__(self, entity_id: int):
        self.id = entity_id
        # ToDo: Добавить загрузку статов из конфига или бд
        self.name = "Charizard"
        self.attack = 1
        self.current_hp = 1
        self.defense = 1
        self.speed = 1
        self.icon = load_image('icon.png', path='static/images/Charizard')

    def take_damage(self, damage: int) -> None:
        if damage > self.current_hp:
            self.current_hp = 0
            self.faint()
            return

        self.current_hp -= damage

    def faint(self) -> None:
        raise NotImplementedError
