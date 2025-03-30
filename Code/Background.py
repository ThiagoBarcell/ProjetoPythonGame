
from Code.Const import WIN_HEIGHT, WIN_WIDTH
from Code.Entity import Entity


class Background(Entity): #Fundo da tela
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= 10 #velocidade
        if self.rect.right <= 0:
           self.rect.left = WIN_WIDTH