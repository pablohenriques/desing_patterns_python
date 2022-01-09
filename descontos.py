
class DescontoCincoItens:

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto
    
    def calcular(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcular(orcamento)

class DescontoMaisQuinhentosReais:

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcular(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcular(orcamento)

class SemDesconto:

    def calcular(self, orcamento):
        return 0