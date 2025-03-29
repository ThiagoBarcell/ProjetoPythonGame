import pygame
from pygame.examples.aliens import Score

from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu
from Code.Pontos import Pontuacao


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True :
            pontos = Pontuacao(self.window)

            menu = Menu(self.window)
            menu_return = menu.run() #recebe a opção selecionada no menu

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_pontos = [0, 0] # pontos do jogador 1 e do 2
                level = Level( self.window, name='Level 1', game_mode=menu_return, player_pontuacao=player_pontos)
                level_return = level.run(player_pontos)
                if level_return:
                    pontos.salvar_pontuacao(menu_return, player_pontos)

            elif menu_return == MENU_OPTION[3]:
                pontos.mostra_pontuacao()
                pass

            elif menu_return == MENU_OPTION[4]:
                pygame.quit() #Fecha a janela
                quit() #fecha a aplicação
            else:
                pass