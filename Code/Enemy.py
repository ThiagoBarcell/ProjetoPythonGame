from Code.Const import WIN_WIDTH
from Code.Entity import Entity
from Code.Incrementer import Incrementador


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx -= 10 #velocidadee dos carros inimigos