from impostos import ISS, ICMS

class CalculadorDeImposto:

    def realizar_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcular(orcamento)
        print(imposto_calculado)


if __name__ == "__main__":
    from orcamento import Orcamento

    calculador = CalculadorDeImposto()
    orcamento = Orcamento(500)

    calculador.realizar_calculo(orcamento, ISS())
    calculador.realizar_calculo(orcamento, ICMS())