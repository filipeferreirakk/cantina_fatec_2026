class Venda:
    def __init__(self, nome_cliente, produto_nome, quantidade, valor_total, data_hora):
        self.nome_cliente = nome_cliente
        self.produto_nome = produto_nome
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.data_hora = data_hora

class NoVenda:
    def __init__(self, venda):
        self.venda = venda
        self.proximo = None

class HistoricoVendas:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def registrar_nova_venda(self, venda):
        novo_no = NoVenda(venda)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def mostrar_relatorio_vendas(self):
        print("\n--- RELATÓRIO DE VENDAS (QUEM CONSUMIU O QUÊ) ---")
        atual = self.primeiro
        if atual is None:
            print("Nenhuma venda registrada.")
            return
        
        while atual is not None:
            v = atual.venda
            print(f"Cliente: {v.nome_cliente} | Comprou: {v.quantidade}x {v.produto_nome} | Total: R${v.valor_total} | Data: {v.data_hora}")
            atual = atual.proximo