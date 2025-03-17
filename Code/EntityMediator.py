from Code.Enemy import Enemy
from Code.Entity import Entity


class EntityMediator: #classe Mediator de acordo com design pattern não tem init

    @staticmethod #esse "__" no início do metodo significa que ele é privado apenas a essa classe, ou seja, so pode ser chamado aqui
    def __verifica_janela_colisao(enti : Entity): #aqui verifica se chegou ao limite da tela
        if isinstance(enti, Enemy):
            if enti.rect.right < 0:
                enti.health = 0
        pass


    @staticmethod
    def verifica_colisao(entity_list: list[Entity] ):
        for i in range(len(entity_list)): #aqui pega a lista de entidades
            entity_geral = entity_list[i] #passa a entidade atual para a variavel
            EntityMediator.__verifica_janela_colisao(entity_geral)

    @staticmethod
    def verifica_health(entity_list: list[Entity]):
        for enti in entity_list:
            if enti.health <= 0:
                entity_list.remove(enti)
