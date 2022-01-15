from datetime import date


class Item:

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class NotaFiscal:
 
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores = []):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao

        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não podem ter mais de 20 caracteres')
        self.__detalhes = detalhes

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':
    from criador_nota_fiscal import CriadorNotaFiscal
    from observadores import imprimir, enviar_por_email, salvar_em_banco

    itens = [
        Item('Item A', 100),
        Item('Item B', 200)
    ]

    nf = NotaFiscal(
        cnpj='FHSA Limitada',
        razao_social='0123456789',
        itens=itens,
        observadores=[imprimir, enviar_por_email, salvar_em_banco]
    )

    # nfb = (
    #    CriadorNotaFiscal()
    #        .com_razao_social('FHSA Limitada')
    #        .com_cnpj('0123456789')
    #        .com_itens(itens)
    #        .construir()
    # )