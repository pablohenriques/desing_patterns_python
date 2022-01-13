from abc import ABCMeta, abstractmethod

class EstadoOrcamento:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.desconto_aplicado = False

    @abstractmethod
    def aplicar_desconto_extra(self, orcamento):
        pass

    @abstractmethod    
    def aprovar(self, orcamento):
        pass

    @abstractmethod
    def reprovar(self, orcamento):
        pass

    @abstractmethod
    def reprovar(self, orcamento):
        pass
    
    @abstractmethod
    def finalizar(self, orcamento):
        pass


class EmAprovacao(EstadoOrcamento):
    
    def aplicar_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.adicionar_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        raise Exception('Desconto já aplicado')
    
    def aprovar(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprovar(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finalizar(self, orcamento):
        raise Exception('Orçamento em aprovação não pode ser finalizado')

class Aprovado(EstadoOrcamento):
    
    def aplicar_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.adicionar_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        raise Exception('Desconto já aplicado')
    
    def aprovar(self, orcamento):
        raise Exception('Orçamento já aprovado')

    def reprovar(self, orcamento):
        raise Exception('Orçamento aprovado não pode ser reprovado')

    def finalizar(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(EstadoOrcamento):
    
    def aplicar_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprovar(self, orcamento):
        raise Exception('Orçamento já reprovado')

    def reprovar(self, orcamento):
        raise Exception('Orçamento já reprovado')

    def finalizar(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(EstadoOrcamento):
    
    def aplicar_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprovar(self, orcamento):
        raise Exception('Orçamento já finalizado')

    def reprovar(self, orcamento):
        raise Exception('Orçamento já finalizado')

    def finalizar(self, orcamento):
        raise Exception('Orçamento já finalizado')

class Orcamento:

    def __init__(self):
        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aprovar(self):
        self.estado_atual.aprovar(orcamento)

    def reprovar(self):
        self.estado_atual.reprovar(orcamento)

    def finalizar(self):
        self.estado_atual.finalizar(orcamento)
    
    def aplicar_desconto_extra(self):
        self.estado_atual.aplicar_desconto_extra(self)

    def adicionar_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra
    
    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)
    
    def adicionar_item(self, item):
        self.__itens.append(item)


class Item:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":
    orcamento = Orcamento()
    
    orcamento.adicionar_item(Item('item - 1', 50))
    orcamento.adicionar_item(Item('item - 2', 200))
    orcamento.adicionar_item(Item('item - 3', 250))

    print(orcamento.valor)
    orcamento.aprovar()
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)