import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from Code.Const import COLOR_YELLOW, PONTOS_POSI, MENU_OPTION, COLOR_WHITE, COLOR_BLACK
from Code.DBProxy import DBProxy


class Pontuacao:
    def __init__(self,window): #Constructor da classe
        self.window = window
        self.surf = pygame.image.load('./asset/Tema_Corrida/Score/bg_Pontuacao.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def salvar_pontuacao(self,game_mode: str, player_pontos: list[int]):
        pygame.mixer_music.load('./asset/Tema_Corrida/Score/Pontuacao_MusicBG.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        db_proxi = DBProxy('DB_PONTUACAO')
        name = ''
        score = 0
        while True:
            # Desenhando a imagem na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.texto_pontuacao( 48, 'Game Over', COLOR_BLACK, PONTOS_POSI['Title'] )
            if game_mode ==MENU_OPTION[0]:
                score = player_pontos[0]
                text = 'Digite seu nick ( 6 caracteres ) : '

            #se for modo de jogo cooperativo
            if game_mode == MENU_OPTION[1]:
                score =  ( (player_pontos[0] + player_pontos[1]) / 2 )
                text = 'Digite o nome do Time ( 4 caracteres ) : '

            # se for modo de jogo Competitivo
            if game_mode == MENU_OPTION[2]:
                if player_pontos[0] >= player_pontos[1]:
                    score = player_pontos[0]
                    text = 'Jogador 1 digite seu nick (4 characters):'
                else:
                    score = player_pontos[1]
                    text = 'Jogador 2 digite seu nick (4 characters):'

            self.texto_pontuacao( 15, text, COLOR_BLACK, PONTOS_POSI['EnterName'] )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 6:
                        db_proxi.insere_dados({'date': get_formatted_date(), 'name':name, 'score':score })
                        self.mostra_pontuacao()
                        return
                    elif event.key == K_BACKSPACE :
                        name = name[:-1] #apaga o ultimo caractere
                    else:
                        if len(name)< 6:
                            name += event.unicode

            self.texto_pontuacao(20, name, COLOR_BLACK, PONTOS_POSI['Name'])

            # Atualizar o display para aparecer na tela
            pygame.display.flip()
            pass

    def mostra_pontuacao(self):
        pygame.mixer_music.load('./asset/Tema_Corrida/Score/Pontuacao_MusicBG.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        # Desenhando a imagem na tela
        self.window.blit(source=self.surf, dest=self.rect)
        self.texto_pontuacao(48, 'TOP 10', COLOR_BLACK, PONTOS_POSI['Title'])
        self.texto_pontuacao(20, '  Nome       Pontos       Data      ', COLOR_BLACK, PONTOS_POSI['Label'])
        db_proxy = DBProxy('DB_PONTUACAO')
        lista_pontos = db_proxy.retorna_top10()
        db_proxy.close()

        for pontos in lista_pontos:
            id_,player_name,player_pts,player_data = pontos
            self.texto_pontuacao(20, f' {player_name}     {player_pts:05d}     {player_data}', COLOR_BLACK,
                            PONTOS_POSI[lista_pontos.index(pontos)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            #Atualizar o display para aparecer na tela
            pygame.display.flip()
            pass

    def texto_pontuacao(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font: Font = pygame.font.SysFont( "Lucida Sans Typewriter", text_size)
        surf: Surface = font.render(text, True, text_color).convert_alpha()
        rect: Rect = surf.get_rect(center=text_center_pos)
        self.window.blit( surf, rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"