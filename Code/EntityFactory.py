import pygame
from Code.Background import Background
from Code.Const import WIN_HEIGHT, GAME_VOLUME


class EntityFactory: #classe Factory de acordo com design pattern não tem init

    @staticmethod
    def get_entity(entity_name : str, position=(0,0)):
        match entity_name :
            case 'Level1Bg':
                list_road = []

                #Passa a musica da fase 1
                pygame.mixer_music.set_volume(GAME_VOLUME + 0.3)
                pygame.mixer_music.load('./asset/Tema_Corrida/Level1/lvl1Song.mp3')
                pygame.mixer_music.play(-1)  # esse -1 significa que quando terminar a musica reinicia

                #Posições das imagens que serão usadas de background
                positions = [30, -50, 530]
                for i in range(3):
                    #Configura a imagem de acordo com o Background
                    list_road.append(Background( name=f'Level1/Road_0{i}', position=(positions[i],0)))
                    list_road.append(Background(name=f'Level1/Road_0{i}', position=(positions[i], WIN_HEIGHT)))

                return list_road