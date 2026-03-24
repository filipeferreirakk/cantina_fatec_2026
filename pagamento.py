class Pagamento:
    def __init__(self, nome_pagador, categoria, curso, valor_pago, data, hora):
        self.nome_pagador = nome_pagador
        self.categoria = categoria
        self.curso = curso
        self.valor_pago = valor_pago
        self.data = data
        self.hora = hora

class NoPagamento:
    def __init__(self, pagamento):
        self.pagamento = pagamento
        self.proximo = None

class ListaDePagamentos:
    def __init__(self):
        self.primeiro = None 
        self.ultimo = None

    def anotar_pagamento(self, novo_pagamento):
        nova_caixinha = NoPagamento(novo_pagamento)

        if self.primeiro is None:
            self.primeiro = nova_caixinha
            self.ultimo = nova_caixinha
        else:
            self.ultimo.proximo = nova_caixinha
            self.ultimo = nova_caixinha
        print(f"PIX de R$ {novo_pagamento.valor_pago} do(a) {novo_pagamento.nome_pagador} recebido!")

    def mostrar_pagamentos(self):
        atual = self.primeiro
        
        if atual is None:
            print("Nenhum pagamento foi feito ainda na cantina.")
            return

        print("\n--- HISTÓRICO DE PIX RECEBIDOS ---")
        while atual is not None:
            p = atual.pagamento
            print(f"Quem pagou: {p.nome_pagador} ({p.categoria} de {p.curso}) | Valor: R$ {p.valor_pago} | Quando: {p.data} às {p.hora}")
            atual = atual.proximo

meus_pagamentos = ListaDePagamentos()
pix1 = Pagamento("Joãozinho", "aluno", "IA", 8.00, "24/03/2026", "08:30")
pix2 = Pagamento("Prof. Maria", "professor", "ESG", 6.00, "24/03/2026", "08:40")
meus_pagamentos.anotar_pagamento(pix1)
meus_pagamentos.anotar_pagamento(pix2)
meus_pagamentos.mostrar_pagamentos()