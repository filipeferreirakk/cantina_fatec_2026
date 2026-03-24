class Pagamento:
    def __init__(self, nome_pagador, categoria, curso, valor_pago, data, hora):
        self.__nome_pagador = nome_pagador
        self.__categoria = categoria
        self.__curso = curso
        self.__valor_pago = valor_pago
        self.__data = data
        self.__hora = hora

    @property
    def nome_pagador(self):
        return self.__nome_pagador

    @property
    def categoria(self):
        return self.__categoria

    @property
    def curso(self):
        return self.__curso

    @property
    def valor_pago(self):
        return self.__valor_pago

    @property
    def data(self):
        return self.__data

    @property
    def hora(self):
        return self.__hora


class NoPagamento:
    def __init__(self, pagamento):
        self.__pagamento = pagamento
        self.__proximo = None

    @property
    def pagamento(self):
        return self.__pagamento

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, proximo_no):
        self.__proximo = proximo_no


class ListaDePagamentos:
    def __init__(self):
        self.__primeiro = None 
        self.__ultimo = None

    def anotar_pagamento(self, novo_pagamento):
        nova_caixinha = NoPagamento(novo_pagamento)

        if self.__primeiro is None:
            self.__primeiro = nova_caixinha
            self.__ultimo = nova_caixinha
        else:
            self.__ultimo.proximo = nova_caixinha
            self.__ultimo = nova_caixinha
        
        print(f"[CAIXA] PIX de R$ {novo_pagamento.valor_pago} recebido.")

    def mostrar_pagamentos(self):
        atual = self.__primeiro
        
        if atual is None:
            print("\n[CAIXA] Nenhum pagamento registrado.")
            return

        print("\n--- HISTÓRICO DE PIX RECEBIDOS ---")
        while atual is not None:
            p = atual.pagamento
            print(f"Pagador: {p.nome_pagador:20} | Valor: R$ {p.valor_pago:6.2f} | Data: {p.data} {p.hora}")
            atual = atual.proximo

    @property
    def primeiro(self):
        return self.__primeiro