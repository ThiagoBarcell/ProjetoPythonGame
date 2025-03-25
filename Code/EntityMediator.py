from Code.Enemy import Enemy
from Code.Entity import Entity
from Code.Player import Player


class EntityMediator: #classe Mediator de acordo com design pattern não tem init

    @staticmethod #esse "__" no início do metodo significa que ele é privado apenas a essa classe, ou seja, so pode ser chamado aqui
    def __verifica_janela_colisao(enti : Entity): #aqui verifica se chegou ao limite da tela
        if isinstance(enti, Enemy):
            if enti.rect.right < 0:
                enti.health = 0
        pass

    @staticmethod
    def __verifica_colisao_entidade(enti1, enti2: Entity):
        valida_interacao = False
        if isinstance(enti1, Enemy) and isinstance(enti2, Player) :
            valida_interacao = True

        elif isinstance(enti1, Player) and isinstance(enti2, Enemy) :
            valida_interacao = True

        if valida_interacao: #Se não tiver nada ja validar se é True ou seja, se não tem nada faz o mesmo que ==True
            if (enti1.rect.right >= enti2.rect.left and enti1.rect.left <= enti2.rect.right and
                enti1.rect.bottom >= enti2.rect.top and enti1.rect.top <= enti2.rect.bottom):
                enti1.health -= enti2.damage
                enti2.health -= enti1.damage
                enti1.last_damage = enti2.name
                enti2.last_damage = enti1.name


    @staticmethod
    def verifica_colisao(entity_list: list[Entity] ):
        for i in range(len(entity_list)): #aqui pega a lista de entidades
            entity_geral1 = entity_list[i] #passa a entidade atual para a variavel
            EntityMediator.__verifica_janela_colisao(entity_geral1)
            for j in range(i+1, len(entity_list)):
                entity_geral2 = entity_list[j]
                EntityMediator.__verifica_colisao_entidade(entity_geral1, entity_geral2)


    @staticmethod
    def verifica_health(entity_list: list[Entity]):
        for enti in entity_list:
            if enti.health <= 0:
                entity_list.remove(enti)