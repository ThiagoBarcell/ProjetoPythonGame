import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True :
            menu = Menu(self.window)
            menu_return = menu.run() #recebe a opção selecionada no menu

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level( self.window, name='Level 1', game_mode=menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit() #Fecha a janela
                quit() #fecha a aplicação
            else:
                pass