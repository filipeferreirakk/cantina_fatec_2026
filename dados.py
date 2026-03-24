import pickle
import random
from datetime import datetime
from faker import Faker

from estoque import Produto
from pagamento import Pagamento
from venda import Venda

class GerenciadorDeDados:
    def __init__(self):
        self.__faker = Faker('pt_BR')
        self.__opcoes_lanches = ["Coxinha", "Kibe", "Suco de Laranja", "Pão de Queijo", "Café", "Misto Quente"]

    def gerar_estoque_aleatorio(self, quantidade):
        produtos_temporarios = []
        for _ in range(quantidade):
            nome = self.__faker.random_element(elements=self.__opcoes_lanches)
            p_compra = round(random.uniform(2.0, 5.0), 2)
            p_venda = round(p_compra * 2, 2)
            data_c = self.__faker.date_this_year().strftime("%d/%m/%Y")
            data_v = "31/12/2026"
            qtd = random.randint(10, 30)
            
            novo_p = Produto(nome, p_compra, p_venda, data_c, data_v, qtd)
            produtos_temporarios.append(novo_p)
        return produtos_temporarios

    def simular_vendas_aleatorias(self, quantidade, lista_nomes):
        vendas_temp = []
        pagamentos_temp = []
        
        if not lista_nomes:
            return [], []

        for _ in range(quantidade):
            nome_aluno = self.__faker.name()
            curso = self.__faker.random_element(elements=("IA", "ESG"))
            cat = self.__faker.random_element(elements=("aluno", "professor", "servidor"))
            item_nome = self.__faker.random_element(elements=lista_nomes)
            valor = round(random.uniform(6.0, 12.0), 2)
            agora = datetime.now()

            p = Pagamento(nome_aluno, cat, curso, valor, agora.strftime("%d/%m/%Y"), agora.strftime("%H:%M"))
            v = Venda(nome_aluno, item_nome, 1, valor, agora.strftime("%d/%m/%Y %H:%M"))
            
            pagamentos_temp.append(p)
            vendas_temp.append(v)
            
        return pagamentos_temp, vendas_temp

    def salvar_sistema(self, objeto_para_salvar, nome_arquivo):
        try:
            with open(nome_arquivo, 'wb') as arquivo:
                pickle.dump(objeto_para_salvar, arquivo)
            print(f"\n✅ Banco de dados '{nome_arquivo}' atualizado com sucesso!")
        except Exception as e:
            print(f"\n❌ Erro ao salvar dados: {e}")

    def carregar_sistema(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                return pickle.load(arquivo)
        except FileNotFoundError:
            print(f"\n⚠️ Arquivo '{nome_arquivo}' não encontrado. Iniciando sistema vazio.")
            return None
        except Exception as e:
            print(f"\n❌ Erro ao carregar banco de dados: {e}")
            return None