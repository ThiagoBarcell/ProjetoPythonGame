import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from Code.Const import GAME_VOLUME, COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_RED, \
    EVENT_CRASH
from Code.Enemy import Enemy
from Code.Entity import Entity
from Code.EntityMediator import EntityMediator
from Code.EntityFactory import EntityFactory
from Code.Incrementer import Incrementador
from Code.Player import Player


class Level:
    def __init__(self, window, name, game_mode, player_pontuacao: list[int]):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode #Modo de jogo selecionado no menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))#Inicia  o background
        self.entity_list.append(EntityFactory.get_entity('Player1'))#Adiciona o player1
        player = EntityFactory.get_entity('Player1')
        player.score = player_pontuacao[0]
        self.entity_list.append(player)

        if game_mode in [MENU_OPTION[1],MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))  # Adiciona o player2
            player.score = player_pontuacao[1]
            self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) #A cada dois segundos para gerar o inimigo
        pygame.time.set_timer(EVENT_CRASH, 100)

    def run(self, player_score: list[int]):
        # Passa a musica da fase 1
        pygame.mixer_music.set_volume(GAME_VOLUME + 0.3)
        pygame.mixer_music.load('./asset/Tema_Corrida/Level/lvl1Song.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        clock = pygame.time.Clock()

        incrementador = Incrementador()
        incrementador.iniciar()

        while True :
            clock.tick(60)
            #Faz a verificação da colisão com objetos
            EntityMediator.verifica_colisao(entity_list=self.entity_list)

            #Verifica a vida das Entidades
            EntityMediator.verifica_health(entity_list=self.entity_list)

            for ent in self.entity_list :
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                text_vida = 0
                if ent.health == 101 :
                    text_vida = 5
                elif ent.health == 81 :
                    text_vida = 4
                elif ent.health == 61:
                    text_vida = 3
                elif ent.health == 41:
                    text_vida = 2
                elif ent.health == 21:
                    text_vida = 1

                if ent.name == 'Level/car_1_01': #se for o carro vermelho
                    self.level_text(14, f'Vida Total : {text_vida}', COLOR_RED, (10, 0))
                    self.level_text(14, f'Pontos : {incrementador.valor}', COLOR_RED, (10, 15))

                # if ent.name == 'Level/car_3_01': #se for o carro amarelo
                #     self.level_text(14, f'Player2 - Helth : {ent.health}', COLOR_RED, (10, 45))

            #Eventos da classe
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    # choice = random.choice(('Enemy1', 'Enemy2'))
                    # self.entity_list.append(choice)
                    self.entity_list.append( EntityFactory.get_entity('Enemy1') )

                if event.type == EVENT_CRASH:
                    for ent in self.entity_list:
                        if ent.name == 'Level/car_1_01':
                            if ent.health <= 1:
                                if isinstance(ent, Player) and ent.name == 'Level/car_1_01':
                                    player_score[0] = incrementador.valor
                                # if isinstance(ent, Player) and ent.name == 'Level/car_3_01':
                                #     player_score[1] = incrementador.valor
                                return True

            # self.level_text(14, f'{self.name} - Timeout: {self.timeout/1000 :.1f}s', COLOR_WHITE, (10,5) )
            # self.level_text(14, f'fps : {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entidades : {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 15))

            pygame.display.flip()

    def level_text(self, text_size: int, text : str, text_color: tuple, text_pos: tuple ):
        text_font : Font = pygame.font.SysFont( name="Lucida Sans Typewriter", size=text_size )
        text_surf : Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect : Rect = text_surf.get_rect( left=text_pos[0], top=text_pos[1] )
        self.window.blit(source=text_surf, dest=text_rect)