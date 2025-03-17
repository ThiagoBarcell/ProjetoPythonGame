import sys
import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import GAME_VOLUME, ENTITY_SPEED_FIXO, COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode #Modo de jogo selecionado no menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))#Inicia  o background
        self.entity_list.append(EntityFactory.get_entity('Player1'))#Adiciona o player1

        if game_mode in [MENU_OPTION[1],MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))  # Adiciona o player2

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) #A cada dois segundos para gerar o inimigo

    def run(self):
        # Passa a musica da fase 1
        pygame.mixer_music.set_volume(GAME_VOLUME + 0.3)
        pygame.mixer_music.load('./asset/Tema_Corrida/Level/lvl1Song.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        clock = pygame.time.Clock()

        while True :
            clock.tick(60)

            for ent in self.entity_list :
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            #Eventos da classe
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    #choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append( EntityFactory.get_entity('Enemy1') )

            self.level_text(14, f'{self.name} - Timeout: {self.timeout/1000 :.1f}s', COLOR_WHITE, (10,5) )
            self.level_text(14, f'fps : {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades : {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 15))

            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text : str, text_color: tuple, text_pos: tuple ):
        text_font : Font = pygame.font.SysFont( name="Lucida Sans Typewriter", size=text_size )
        text_surf : Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect : Rect = text_surf.get_rect( left=text_pos[0], top=text_pos[1] )
        self.window.blit(source=text_surf, dest=text_rect)