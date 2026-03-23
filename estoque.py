class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def alterar_estoque(self, nova_quantidade):
        self.quantidade = nova_quantidade

class No:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class FilaEstoque:
    def __init__(self):
        self.primeiro = None 
        self.ultimo = None

    def inserir_no_estoque(self, novo_produto):
        nova_caixinha = No(novo_produto)

        if self.primeiro is None:
            self.primeiro = nova_caixinha
            self.ultimo = nova_caixinha
        else:
            self.ultimo.proximo = nova_caixinha
            self.ultimo = nova_caixinha
        print(f"Sucesso: {novo_produto.nome} entrou no estoque!")

    def mostrar_estoque(self):
        atual = self.primeiro
        
        if atual is None:
            print("O estoque está totalmente vazio!")
            return

        print("\n--- LISTA DE PRODUTOS NO ESTOQUE ---")
        while atual is not None:
            p = atual.produto
            print(f"Nome: {p.nome} | Qtd: {p.quantidade} | Vencimento: {p.data_vencimento}")
            atual = atual.proximo

minha_cantina = FilaEstoque()

item1 = Produto("Coxinha", 4.00, 8.00, "23/03/2026", "25/03/2026", 10)
item2 = Produto("Suco de Laranja", 3.00, 6.00, "23/03/2026", "24/03/2026", 5)

minha_cantina.inserir_no_estoque(item1)
minha_cantina.inserir_no_estoque(item2)

minha_cantina.mostrar_estoque()

item1.alterar_estoque(8)
print("Ajustando estoque da Coxinha...")
minha_cantina.mostrar_estoque()