from estoque import Produto, FilaEstoque
from pagamento import Pagamento, ListaDePagamentos
from venda import Venda, HistoricoVendas
from dados import GerenciadorDeDados
from datetime import datetime

# Inicialização
estoque = FilaEstoque()
caixa = ListaDePagamentos()
historico = HistoricoVendas()
secretaria = GerenciadorDeDados()

def menu():
    global estoque, caixa, historico

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
            print("\nPopulando sistema com dados aleatórios...")
            # Gera e insere produtos
            produtos_fake = secretaria.gerar_estoque_aleatorio(5)
            for p in produtos_fake:
                estoque.inserir_no_estoque(p)
            
            # Gera e insere vendas/pagamentos
            pagamentos_f, vendas_f = secretaria.simular_vendas_aleatorias(5, estoque)
            for p in pagamentos_f:
                caixa.anotar_pagamento(p)
            for v in vendas_f:
                historico.registrar_nova_venda(v)
            print("Sistema populado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do produto: ")
            p_compra = float(input("Preço de compra: "))
            p_venda = float(input("Preço de venda: "))
            data_venc = input("Data de vencimento (DD/MM/AAAA): ")
            qtd = int(input("Quantidade: "))
            novo = Produto(nome, p_compra, p_venda, datetime.now().strftime("%d/%m/%Y"), data_venc, qtd)
            estoque.inserir_no_estoque(novo)

        elif opcao == "3":
            print("\n--- NOVA VENDA ---")
            prod_nome = input("O que o aluno quer comprar? ")
            qtd_venda = int(input("Quantidade: "))
            
            if estoque.baixar_estoque(prod_nome, qtd_venda):
                cliente = input("Nome do Aluno/Professor: ")
                cat = input("Categoria (aluno/professor/servidor): ")
                curso = input("Curso (IA ou ESG): ")
                valor_total = float(input("Valor total da venda: R$ "))
                
                agora = datetime.now()
                data_s = agora.strftime("%d/%m/%Y")
                hora_s = agora.strftime("%H:%M")

                p = Pagamento(cliente, cat, curso, valor_total, data_s, hora_s)
                v = Venda(cliente, prod_nome, qtd_venda, valor_total, f"{data_s} {hora_s}")
                
                caixa.anotar_pagamento(p)
                historico.registrar_nova_venda(v)
                print("Venda concluída com sucesso!")

        elif opcao == "4":
            historico.mostrar_relatorio_vendas()
            caixa.mostrar_pagamentos()

        elif opcao == "5":
            dados = {"estoque": estoque, "caixa": caixa, "historico": historico}
            secretaria.salvar_sistema(dados, "dados_cantina.dat")

        elif opcao == "6":
            dados_carregados = secretaria.carregar_sistema("dados_cantina.dat")
            if dados_carregados:
                estoque = dados_carregados["estoque"]
                caixa = dados_carregados["caixa"]
                historico = dados_carregados["historico"]
                print("Dados carregados com sucesso!")

        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()