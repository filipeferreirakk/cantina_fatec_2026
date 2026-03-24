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

    def editar_quantidade_por_nome(self, nome_busca, nova_qtd):
        atual = self.primeiro
        encontrou = False

        while atual is not None:
            if atual.produto.nome == nome_busca:
                atual.produto.alterar_estoque(nova_qtd)
                print(f"Pronto! Agora temos {nova_qtd} de {nome_busca}.")
                encontrou = True
                break
            atual = atual.proximo
        
        if not encontrou:
            print(f"Não achei '{nome_busca}' no estoque.")

    def baixar_estoque(self, nome_busca, qtd_vendida):
        atual = self.primeiro
        
        while atual is not None:
            if atual.produto.nome == nome_busca:
                if atual.produto.quantidade >= qtd_vendida:
                    atual.produto.quantidade -= qtd_vendida
                    print(f"Venda feita! Saíram {qtd_vendida} de {nome_busca}.")
                    return True
                else:
                    print(f"Erro: Só temos {atual.produto.quantidade} de {nome_busca}!")
                    return False
            atual = atual.proximo
        
        print("Produto não encontrado para venda.")
        return False

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
minha_cantina.inserir_no_estoque(Produto("Coxinha", 4.0, 8.0, "23/03", "25/03", 10))
minha_cantina.inserir_no_estoque(Produto("Suco", 3.0, 6.0, "23/03", "24/03", 5))
minha_cantina.editar_quantidade_por_nome("Coxinha", 15)
minha_cantina.baixar_estoque("Suco", 2)
minha_cantina.mostrar_estoque()