from pydoc import text

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE


class Menu:
    # ao criar o objeto ja carrega o background
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Tema_Corrida/Kit_Background/city 1/6.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        #Configura a musica do menu
        pygame.mixer_music.set_volume(0.4)
        pygame.mixer_music.load('./asset/Tema_Corrida/on-the-road-to-the-eighties_59sec-177566.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            #cria o título do menu
            self.menu_text(text_size=50, text='Car Crash', text_color=COLOR_YELLOW,
                           text_center_pos=((WIN_WIDTH / 2), 70))

            #Cria e passa os parametros para o menu
            for i in range(len(MENU_OPTION)):
                self.menu_text_opcoes(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE,
                           text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            #Atualiza a tela para mandar as informações
            pygame.display.flip()

            # check por todos os eventos
            # fecha a janela
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() #close window
                   quit() #sai da tela

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Magneto", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text_opcoes(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)