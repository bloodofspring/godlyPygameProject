import pygame

from screens.abstractScreen import AbstractScreen


class TeamChoosingScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)
        title_font = pygame.font.Font(None, 50)
        self.pokemon_font = pygame.font.Font(None, 50)
        self.choose_text = title_font.render("Choose 6 pokemon for battle", True, (0, 0, 0))
        self.tip_text = title_font.render("Choose with Space and press Enter when ready", True, (0, 0, 0))
        self.test_list_of_pokemon = [[str(i), False] for i in range(20)]
        self.cursor_pos = 0
        self.amount_of_chosen_pokemon = 0

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        if self.amount_of_chosen_pokemon == 6:
                            ...  # переход на следующий экран
                    if event.key == pygame.K_SPACE:
                        self.test_list_of_pokemon[self.cursor_pos][1] = not self.test_list_of_pokemon[self.cursor_pos][1]
                    if event.key in (pygame.K_w, pygame.K_UP):
                        self.cursor_pos = (self.cursor_pos - 1) % len(self.test_list_of_pokemon)
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        self.cursor_pos = (self.cursor_pos + 1) % len(self.test_list_of_pokemon)

    def display_pokemon(self):
        for i in range(7):
            if i == 3:
                pygame.draw.rect(self.screen, pygame.Color('yellow'), (200, 120 + i * 80, 600, 70), 3)
            else:
                rect_color = (pygame.Color('red'), pygame.Color('green'))[self.test_list_of_pokemon[(self.cursor_pos + i - 3) % len(self.test_list_of_pokemon)][1]]
                pygame.draw.rect(self.screen, rect_color, (200, 120 + i * 80, 600, 70), 3)
            pokemon_text = self.pokemon_font.render(self.test_list_of_pokemon[(self.cursor_pos + i - 3) % len(self.test_list_of_pokemon)][0], True, (0, 0, 0))
            self.screen.blit(pokemon_text, (350, 140 + i * 80))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.choose_text, (260, 0))
        self.screen.blit(self.tip_text, (100, 60))
        self.display_pokemon()
