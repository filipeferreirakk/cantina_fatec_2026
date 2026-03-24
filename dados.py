import pickle
from faker import Faker

class GerenciadorDeDados:
    def __init__(self):
        self.faker = Faker('pt_BR')

    def gerar_alunos_aleatorios(self, quantidade):
        lista_fake = []
        for _ in range(quantidade):
            aluno = {
                "nome": self.faker.name(),
                "categoria": "aluno",
                "curso": self.faker.random_element(elements=("IA", "ESG"))
            }
            lista_fake.append(aluno)
        return lista_fake

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