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
    global estoque, caixa, historico

    while True:
        print("\n=== CANTINA FATEC - GESTÃO ===")
        print("1. Popular Sistema (Faker)")
        print("2. Cadastrar Produto")
        print("3. Realizar Venda")
        print("4. Relatórios")
        print("5. Salvar")
        print("6. Carregar")
        print("0. Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nGerando dados...")
            novos_prods = secretaria.gerar_estoque_aleatorio(5)
            nomes_para_venda = []
            for p in novos_prods:
                estoque.inserir_no_estoque(p)
                nomes_para_venda.append(p.nome)
            
            pags, vends = secretaria.simular_vendas_aleatorias(5, nomes_para_venda)
            for i in range(len(pags)):
                if estoque.baixar_estoque(vends[i].produto_nome, vends[i].quantidade):
                    caixa.anotar_pagamento(pags[i])
                    historico.registrar_nova_venda(vends[i])
            print("✅ Feito! Use a opção 4 para ver.")

        elif opcao == "4":
            estoque.mostrar_estoque()
            historico.mostrar_relatorio_vendas()
            caixa.mostrar_pagamentos()

        elif opcao == "5":
            secretaria.salvar_sistema({"e": estoque, "c": caixa, "h": historico}, "dados.dat")

        elif opcao == "6":
            d = secretaria.carregar_sistema("dados.dat")
            if d:
                estoque, caixa, historico = d["e"], d["c"], d["h"]
                print("✅ Dados carregados!")

        elif opcao == "0": break

if __name__ == "__main__":
    menu()