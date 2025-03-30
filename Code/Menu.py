import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE, GAME_VOLUME


class Menu:
    # ao criar o objeto ja carrega o background
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Tema_Corrida/Level/BG_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        #Define a opção do menu atual
        menu_option = 0
        #Configura a musica do menu
        pygame.mixer_music.set_volume(GAME_VOLUME)
        pygame.mixer_music.load('./asset/Tema_Corrida/on-the-road-to-the-eighties_59sec-177566.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            #cria o título do menu
            self.menu_text(text_size=50, text='Car', text_color=COLOR_YELLOW,
                           text_center_pos=((WIN_WIDTH / 2), 40))
            self.menu_text(text_size=50, text='Scape', text_color=COLOR_YELLOW,
                           text_center_pos=((WIN_WIDTH / 2), 80))

            #Cria e passa os parametros para o menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option :
                    self.menu_text_opcoes(text_size=20, text=MENU_OPTION[i], text_color=COLOR_YELLOW,
                           text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else :
                    self.menu_text_opcoes(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE,
                                          text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            # check por todos os eventos
            # fecha a janela
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() #close window
                   quit() #sai da tela

               #Verifica a tecla que foi digitada
               if event.type == pygame.KEYDOWN:
                   # se foi setinha para baixo incrementa o menu
                   if event.key == pygame.K_DOWN:
                       if menu_option < len(MENU_OPTION) - 1 :
                           menu_option += 1 #faz o incremente da variavel
                       else:
                           menu_option = 0

                   # se foi setinha para cima incrementa o menu
                   if event.key == pygame.K_UP:
                       if menu_option > 0 :
                           menu_option -= 1 #faz o decremente da variavel
                       else:
                           menu_option = len(MENU_OPTION) - 1

                   # se o enter foi digitado
                   if event.key == pygame.K_RETURN:
                       return MENU_OPTION[menu_option]

            # Atualiza a tela para mandar as informações
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text_opcoes(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)