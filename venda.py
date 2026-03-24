class Venda:
    def __init__(self, nome_cliente, produto_nome, quantidade, valor_total, data_hora):
        self.__nome_cliente = nome_cliente
        self.__produto_nome = produto_nome
        self.__quantidade = quantidade
        self.__valor_total = valor_total
        self.__data_hora = data_hora

    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @property
    def produto_nome(self):
        return self.__produto_nome

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def data_hora(self):
        return self.__data_hora


class NoVenda:
    def __init__(self, venda):
        self.__venda = venda
        self.__proximo = None

    @property
    def venda(self):
        return self.__venda

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, proximo_no):
        self.__proximo = proximo_no


class HistoricoVendas:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None

    def registrar_nova_venda(self, venda):
        novo_no = NoVenda(venda)
        if self.__primeiro is None:
            self.__primeiro = novo_no
            self.__ultimo = novo_no
        else:
            self.__ultimo.proximo = novo_no
            self.__ultimo = novo_no

    def mostrar_relatorio_vendas(self):
        print("\n--- RELATÓRIO DE CONSUMO ---")
        atual = self.__primeiro
        if atual is None:
            print("[HISTÓRICO] Nenhuma venda registrada.")
            return
        
        while atual is not None:
            v = atual.venda
            print(f"Cliente: {v.nome_cliente:20} | Produto: {v.quantidade}x {v.produto_nome:15} | Total: R$ {v.valor_total:6.2f}")
            atual = atual.proximo

    @property
    def primeiro(self):
        return self.__primeiro