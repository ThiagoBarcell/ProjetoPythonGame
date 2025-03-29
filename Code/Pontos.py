

import pygame
from pygame import Surface, Rect
from pygame.examples.aliens import Score
from pygame.font import Font

from Code.Const import COLOR_YELLOW, PONTOS_POSI, MENU_OPTION


class Pontuacao:
    def __init__(self,window): #Constructor da classe
        self.window = window
        self.surf = pygame.image.load('./asset/Tema_Corrida/Score/bg_Pontuacao.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def salvar_pontuacao(self,game_mode: str, player_pontos: list[int]):
        pygame.mixer_music.load('./asset/Tema_Corrida/Score/Pontuacao_MusicBG.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        # Desenhando a imagem na tela
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.texto_pontuacao( 48, 'Game Over', COLOR_YELLOW, PONTOS_POSI['Title'] )
            if game_mode ==MENU_OPTION[0]:
                text = 'Jogador 1 digite seu nick ( 4 caracteres ) : '
            # Atualizar o display para aparecer na tela
            pygame.display.flip()
            pass

    def mostra_pontuacao(self):
        pygame.mixer_music.load('./asset/Tema_Corrida/Score/Pontuacao_MusicBG.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        # Desenhando a imagem na tela
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            #Atualizar o display para aparecer na tela
            pygame.display.flip()
            pass

    def texto_pontuacao(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font: Font = pygame.font.SysFont( "Lucida Sans Typewriter", text_size)
        surf: Surface = font.render(text, True, text_color).convert_alpha()
        rect: Rect = surf.get_rect(center=text_center_pos)
        self.window.blit( surf, rect)