from estoque import Produto, FilaEstoque
from pagamento import Pagamento, ListaDePagamentos
from venda import Venda, HistoricoVendas
from dados import GerenciadorDeDados
from datetime import datetime

estoque = FilaEstoque()
caixa = ListaDePagamentos()
historico = HistoricoVendas()
secretaria = GerenciadorDeDados()

def menu():
    while True:
        print("\n=== CANTINA FATEC - SISTEMA DE GESTÃO ===")
        print("1. Popular Sistema (Faker)")
        print("2. Cadastrar Produto Manualmente")
        print("3. Realizar Venda (Simulação)")
        print("4. Ver Relatórios (Vendas e Consumo)")
        print("5. Salvar Dados (Pickle)")
        print("6. Carregar Dados (Pickle)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Populando sistema com dados aleatórios...")
            
        elif opcao == "2":
            nome = input("Nome do produto: ")
            preco_v = float(input("Preço de venda: "))
            qtd = int(input("Quantidade: "))
            novo = Produto(nome, 0.0, preco_v, "24/03", "30/12", qtd)
            estoque.inserir_no_estoque(novo)

        elif opcao == "3":
            print("\n--- NOVA VENDA ---")
            prod_nome = input("O que o aluno quer comprar? ")
            qtd_venda = int(input("Quantidade: "))
            
            if estoque.baixar_estoque(prod_nome, qtd_venda):
                cliente = input("Nome do Aluno: ")
                curso = input("Curso (IA ou ESG): ")
                valor_total = 10.0
                
                p = Pagamento(cliente, "aluno", curso, valor_total, "24/03", "10:00")
                v = Venda(cliente, prod_nome, qtd_venda, valor_total, "24/03 10:00")
                
                caixa.anotar_pagamento(p)
                historico.registrar_nova_venda(v)
                print("Venda concluída com sucesso!")

        elif opcao == "4":
            historico.mostrar_relatorio_vendas() [cite: 24]
            caixa.mostrar_pagamentos()

        elif opcao == "5":
            secretaria.salvar_sistema({"estoque": estoque, "caixa": caixa, "historico": historico}, "dados_cantina.dat") [cite: 22]

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()