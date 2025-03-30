
import random
from Code.Background import Background
from Code.Const import WIN_HEIGHT, WIN_WIDTH
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory: #classe Factory de acordo com design pattern não tem init

    @staticmethod
    def get_entity(entity_name : str, position=(0,0)):
        match entity_name :
            case 'Level1Bg':
                list_road = []

                #Posições das imagens que serão usadas de background
                positions = [-80, -70, 290]
                for i in range(3):
                    #Configura a imagem de acordo com o Background
                    list_road.append(Background( name=f'Level/Road_0{i}', position=(0 ,positions[i])))
                    list_road.append(Background(name=f'Level/Road_0{i}', position=(WIN_WIDTH,positions[i])))
                return list_road

            case 'Player1' :
                return Player( name=f'Level/car_1_01', position=( 10, ( WIN_HEIGHT / 2 ) - 50 ) ) #procura o arquivo do carro e
                                                                                             #posiciona ele na tela
            case 'Player2':
                return Player(name=f'Level/car_3_01',
                              position=(10, (WIN_HEIGHT / 2) + 50))

            case 'Enemy1':
                return Enemy(name=f'Level/car_2_01', position=(WIN_WIDTH + 10 , random.randint(40, WIN_HEIGHT - 40))) #define a posição

            case 'Enemy2':
                return Enemy(name=f'Level/car_3_01', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))