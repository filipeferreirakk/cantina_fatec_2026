class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def editar_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.quantidade = nova_quantidade
        else:
            print("Erro: A quantidade não pode ser negativa.")

class NoProduto:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None