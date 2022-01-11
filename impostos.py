from abc import ABCMeta, abstractmethod

class Imposto:

    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calcular_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        return self.__outro_imposto.calcular(orcamento)
    
    @abstractmethod
    def calcula(self, orcamento):
        pass

class TemplateImpostoCondicional(Imposto):

    __metaclass__ = ABCMeta

    def calcular(self, orcamento):
        if self.usar_taxa_maxima(orcamento):
            return self.maxima_taxacao(orcamento) + self.calcular_outro_imposto(orcamento)
        return self.minima_taxacao(orcamento) + self.calcular_outro_imposto(orcamento)

    @abstractmethod
    def usar_taxa_maxima(orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(orcamento):
        pass

    @abstractmethod
    def minima_taxacao(orcamento):
        pass

def IPVX(metodo_ou_funcao):
    '** chama o cálculo do imposto do ISS, pega o resultado e soma com R$ 50,00 **'
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper
class ISS(Imposto):

    @IPVX
    def calcular(self, orcamento):
        return orcamento.valor * 0.1 + self.calcular_outro_imposto(orcamento)

class ICMS(Imposto):

    def calcular(self, orcamento):
        return orcamento.valor * 0.06 + self.calcular_outro_imposto(orcamento)

class ICPP(TemplateImpostoCondicional):
   
    def usar_taxa_maxima(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(TemplateImpostoCondicional):

    def __encontrar_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
    
    def usar_taxa_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__encontrar_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06