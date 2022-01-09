from descontos import DescontoCincoItens, DescontoMaisQuinhentosReais, SemDesconto

class CalculadorDeDescontos:

    def calcula(self, orcamento):
        desconto = DescontoCincoItens(
            DescontoMaisQuinhentosReais(
                SemDesconto()
            )
        ).calcular(orcamento)
        return desconto


if __name__ == "__main__":
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adicionar_item(Item('item - 1', 100))
    orcamento.adicionar_item(Item('item - 2', 50))
    orcamento.adicionar_item(Item('item - 3', 500))
    # orcamento.adicionar_item(Item('item - 4', 500))

    # print(orcamento.valor)

    calculador = CalculadorDeDescontos()
    desconto_calculado = calculador.calcula(orcamento)
    print("{:.2f}".format(desconto_calculado))