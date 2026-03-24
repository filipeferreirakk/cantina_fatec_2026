import os
import platform
from datetime import datetime

from estoque import Produto, FilaEstoque
from pagamento import Pagamento, ListaDePagamentos
from venda import Venda, HistoricoVendas
from dados import GerenciadorDeDados

class Cores:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    RESET = '\033[0m'
    NEGRITO = '\033[1m'

estoque = FilaEstoque()
caixa = ListaDePagamentos()
historico = HistoricoVendas()
secretaria = GerenciadorDeDados()

def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def menu():
    global estoque, caixa, historico

    while True:
        limpar_tela()
        print(f"{Cores.AZUL}{Cores.NEGRITO}=============================================")
        print("       SISTEMA DE GESTÃO - CANTINA FATEC")
        print("=============================================" + f"{Cores.RESET}")
        print(f" [1] Popular Sistema (Faker)")
        print(f" [2] Cadastrar Produto Manualmente")
        print(f" [3] Realizar Venda")
        print(f" [4] Ver Relatórios Completos")
        print(f" [5] Salvar Dados (Pickle)")
        print(f" [6] Carregar Dados (Pickle)")
        print(f" [0] Sair do Sistema")
        print(f"{Cores.AZUL}---------------------------------------------{Cores.RESET}")
        
        opcao = input(f"{Cores.NEGRITO}Escolha uma opção: {Cores.RESET}")

        if opcao == "1":
            limpar_tela()
            print(f"{Cores.AMARELO}--- GERANDO DADOS ALEATÓRIOS (FAKER) ---{Cores.RESET}")
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
            print(f"\n{Cores.VERDE}✅ Sistema populado com sucesso!{Cores.RESET}")
            input(f"\n{Cores.AMARELO}Pressione ENTER para voltar...{Cores.RESET}")

        elif opcao == "2":
            limpar_tela()
            print(f"{Cores.AMARELO}--- CADASTRO DE PRODUTO ---{Cores.RESET}")
            try:
                nome = input("Nome: ")
                p_compra = float(input("Preço de Compra: "))
                p_venda = float(input("Preço de Venda: "))
                venc = input("Vencimento (DD/MM/AAAA): ")
                qtd = int(input("Quantidade: "))
                novo = Produto(nome, p_compra, p_venda, datetime.now().strftime("%d/%m/%Y"), venc, qtd)
                estoque.inserir_no_estoque(novo)
                print(f"\n{Cores.VERDE}✅ Produto cadastrado!{Cores.RESET}")
            except ValueError:
                print(f"\n{Cores.VERMELHO}❌ Erro: Entrada inválida. Preços e quantidades devem ser números.{Cores.RESET}")
            input(f"\n{Cores.AMARELO}Pressione ENTER para voltar...{Cores.RESET}")

        elif opcao == "3":
            limpar_tela()
            print(f"{Cores.AMARELO}--- REALIZAR VENDA ---{Cores.RESET}")
            try:
                prod_nome = input("Produto: ")
                qtd_venda = int(input("Quantidade: "))
                
                if estoque.baixar_estoque(prod_nome, qtd_venda):
                    cliente = input("Nome do Cliente: ")
                    curso = input("Curso (IA/ESG): ")
                    v_total = float(input("Valor Total R$: "))
                    agora = datetime.now()
                    p = Pagamento(cliente, "aluno", curso, v_total, agora.strftime("%d/%m/%Y"), agora.strftime("%H:%M"))
                    v = Venda(cliente, prod_nome, qtd_venda, v_total, agora.strftime("%d/%m/%Y %H:%M"))
                    caixa.anotar_pagamento(p)
                    historico.registrar_nova_venda(v)
                    print(f"\n{Cores.VERDE}✅ Venda concluída!{Cores.RESET}")
                else:
                    print(f"\n{Cores.VERMELHO}❌ Erro: Estoque insuficiente ou produto não encontrado.{Cores.RESET}")
            except ValueError:
                print(f"\n{Cores.VERMELHO}❌ Erro: Você deve digitar números válidos para quantidade e valor!{Cores.RESET}")
            input(f"\n{Cores.AMARELO}Pressione ENTER para voltar...{Cores.RESET}")

        elif opcao == "4":
            limpar_tela()
            print(f"{Cores.AZUL}=== RELATÓRIOS DO SISTEMA ==={Cores.RESET}")
            estoque.mostrar_estoque()
            historico.mostrar_relatorio_vendas()
            caixa.mostrar_pagamentos()
            input(f"\n{Cores.AMARELO}Pressione ENTER para voltar ao menu...{Cores.RESET}")

        elif opcao == "5":
            secretaria.salvar_sistema({"e": estoque, "c": caixa, "h": historico}, "dados.dat")
            input(f"\n{Cores.AMARELO}Pressione ENTER para voltar...{Cores.RESET}")

        elif opcao == "6":
            d = secretaria.carregar_sistema("dados.dat")
            if d:
                estoque, caixa, historico = d["e"], d["c"], d["h"]
                print(f"\n{Cores.VERDE}✅ Dados restaurados!{Cores.RESET}")
            input(f"\n{Cores.AMARELO}Pressione ENTER para voltar...{Cores.RESET}")

        elif opcao == "0":
            break

if __name__ == "__main__":
    menu()