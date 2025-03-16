from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory: #classe Factory de acordo com design pattern não tem init

    @staticmethod
    def get_entity(entity_name : str, position=(0,0)):
        match entity_name :
            case 'Level1Bg':
                list_road = []
                #Posições das imagens que serão usadas de background
                positions = [30, -50, 530]
                for i in range(3):
                    #Configura a imagem de acordo com o Background
                    list_road.append(Background( name=f'Level1/Road_0{i}', position=(positions[i],0)))
                    list_road.append(Background(name=f'Level1/Road_0{i}', position=(positions[i], WIN_HEIGHT)))

                return list_road