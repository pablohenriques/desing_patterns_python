from impostos import ISS, ICMS, ICPP, IKCV

class CalculadorDeImposto:

    def realizar_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcular(orcamento)
        print("{:.2f}".format(imposto_calculado))


if __name__ == "__main__":
    from orcamento import Orcamento, Item

    calculador = CalculadorDeImposto()
    orcamento = Orcamento()
    
    orcamento.adicionar_item(Item('item - 1', 50))
    orcamento.adicionar_item(Item('item - 2', 200))
    orcamento.adicionar_item(Item('item - 3', 250))

    print("ISS e ICMS")
    calculador.realizar_calculo(orcamento, ISS())
    calculador.realizar_calculo(orcamento, ICMS())
    
    print("ISS com ICMS")
    calculador.realizar_calculo(orcamento, ISS(ICMS()))

    print("ICPP e IKCV")
    calculador.realizar_calculo(orcamento, ICPP())
    calculador.realizar_calculo(orcamento, IKCV())
    
    print("ICPP com IKCV")
    calculador.realizar_calculo(orcamento, ICPP(IKCV()))