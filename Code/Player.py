import pygame.key

from Code.Const import WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name : str, position : tuple):
        super().__init__(name, position )

    def move(self):
        pressed_key = pygame.key.get_pressed() #passa pra variavel a tecla digitada
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= 2

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += 2

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 2

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 2
        pass
