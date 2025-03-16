from Code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from Code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centery -= 1 #ENTITY_SPEED
        if self.rect.bottom <= 0:
           self.rect.top = WIN_HEIGHT