class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__data_compra = data_compra
        self.__data_vencimento = data_vencimento
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @property
    def preco_compra(self):
        return self.__preco_compra

    @property
    def preco_venda(self):
        return self.__preco_venda

    @property
    def data_compra(self):
        return self.__data_compra

    @property
    def data_vencimento(self):
        return self.__data_vencimento

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd
        else:
            print("Erro: A quantidade não pode ser negativa.")

class No:
    def __init__(self, produto):
        self.__produto = produto
        self.__proximo = None

    @property
    def produto(self):
        return self.__produto

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, valor):
        self.__proximo = valor

class FilaEstoque:
    def __init__(self):
        self.__primeiro = None 
        self.__ultimo = None

    def inserir_no_estoque(self, novo_produto):
        nova_caixinha = No(novo_produto)
        if self.__primeiro is None:
            self.__primeiro = nova_caixinha
            self.__ultimo = nova_caixinha
        else:
            self.__ultimo.proximo = nova_caixinha
            self.__ultimo = nova_caixinha

    def baixar_estoque(self, nome_busca, qtd_vendida):
        atual = self.__primeiro
        
        while atual is not None:
            if atual.produto.nome == nome_busca:
                if atual.produto.quantidade >= qtd_vendida:
                    atual.produto.quantidade -= qtd_vendida
                    return True
                else:
                    return False
            atual = atual.proximo
        return False

    def mostrar_estoque(self):
        atual = self.__primeiro
        if atual is None:
            print("\n[ESTOQUE] Vazio.")
            return

        print("\n--- STATUS ATUAL DO ESTOQUE ---")
        while atual is not None:
            p = atual.produto
            print(f"Produto: {p.nome:15} | Qtd: {p.quantidade:3} | Vence: {p.data_vencimento}")
            atual = atual.proximo

    @property
    def primeiro(self):
        return self.__primeiro