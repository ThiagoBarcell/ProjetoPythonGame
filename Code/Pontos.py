

import pygame
from pygame import Surface, Rect
from pygame.font import Font


class Pontuacao:
    def __init__(self,window): #Constructor da classe
        self.window = window
        self.surf = pygame.image.load('./asset/Tema_Corrida/Score/bg_Pontuacao.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def salvar_pontuacao(self,menu_return: str, player_pontos: list[int]):
        pygame.mixer_music.load('./asset/Tema_Corrida/Score/Pontuacao_MusicBG.mp3')
        pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia
        # Desenhando a imagem na tela
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            # Atualizar o display para aparecer na tela
            pygame.display.flip()
            pass
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

        pass

    def texto_pontuacao(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)