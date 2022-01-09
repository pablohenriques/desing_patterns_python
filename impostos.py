from abc import ABCMeta, abstractmethod
class TemplateImpostoCondicional:

    __metaclass__ = ABCMeta

    def calcular(self, orcamento):
        if self.usar_taxa_maxima(orcamento):
            return self.maxima_taxacao(orcamento)
        return self.minima_taxacao(orcamento)

    @abstractmethod
    def usar_taxa_maxima(orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(orcamento):
        pass

    @abstractmethod
    def minima_taxacao(orcamento):
        pass

class ISS:
    def calcular(self, orcamento):
        return orcamento.valor * 0.1

class ICMS:
    def calcular(self, orcamento):
        return orcamento.valor * 0.06

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