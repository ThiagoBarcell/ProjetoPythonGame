from abc import ABC, abstractmethod

import pygame.image

from Code.Const import HEALTH_GLOBAL, DAMAGE_GLOBAL, ENTITY_PONTOS


class Entity(ABC):
    def __init__(self, name : str, position : tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/Tema_Corrida/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = HEALTH_GLOBAL[self.name]
        self.damage = DAMAGE_GLOBAL[self.name]
        self.pontos = ENTITY_PONTOS[self.name]
        self.last_damage = 'None'

    @abstractmethod
    def move(self):
        pass