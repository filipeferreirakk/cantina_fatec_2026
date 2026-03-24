import pickle
from faker import Faker
import random
from datetime import datetime

from estoque import Produto
from pagamento import Pagamento
from venda import Venda

class GerenciadorDeDados:
    def __init__(self):
        self.faker = Faker('pt_BR')

    def gerar_estoque_aleatorio(self, quantidade):
        produtos_fakes = []
        opcoes_lanches = ["Coxinha", "Kibe", "Suco de Laranja", "Pão de Queijo", "Café", "Misto Quente"]
        
        for _ in range(quantidade):
            nome = self.faker.random_element(elements=opcoes_lanches)
            p_compra = round(random.uniform(2.0, 5.0), 2)
            p_venda = round(p_compra * 2, 2)
            data_c = self.faker.date_this_year().strftime("%d/%m/%Y")
            data_v = "31/12/2026"
            qtd = random.randint(5, 20)
            
            novo_p = Produto(nome, p_compra, p_venda, data_c, data_v, qtd)
            produtos_fakes.append(novo_p)
        return produtos_fakes

    def simular_vendas_aleatorias(self, quantidade, estoque_atual):
        vendas_fakes = []
        pagamentos_fakes = []
        
        for _ in range(quantidade):
            nome_aluno = self.faker.name()
            curso = self.faker.random_element(elements=("IA", "ESG"))
            cat = self.faker.random_element(elements=("aluno", "professor", "servidor"))
            
            item_nome = self.faker.random_element(elements=("Coxinha", "Suco de Laranja"))
            valor = 8.0
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

            p = Pagamento(nome_aluno, cat, curso, valor, data_hora.split()[0], data_hora.split()[1])
            v = Venda(nome_aluno, item_nome, 1, valor, data_hora)
            
            pagamentos_fakes.append(p)
            vendas_fakes.append(v)
            
        return pagamentos_fakes, vendas_fakes

    def salvar_sistema(self, objeto_para_salvar, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(objeto_para_salvar, arquivo)
        print(f"Sucesso: Dados guardados em {nome_arquivo}!")

    def carregar_sistema(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                return pickle.load(arquivo)
        except FileNotFoundError:
            print("Aviso: Nenhum ficheiro encontrado. Começando do zero.")
            return None