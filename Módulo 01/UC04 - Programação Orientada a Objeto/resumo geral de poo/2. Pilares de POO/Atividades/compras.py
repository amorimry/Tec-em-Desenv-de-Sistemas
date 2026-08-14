class Pix():
    def pagar(self, valor):
        print(f"Pix gerado no valor de R$ {valor:.2f}.")

    def __str__(self):
        return "Pix"

class Cartao():
    def pagar(self, valor):
        print(f"Fatura do cartão gerada no valor de R$ {valor:.2f}.")

    def __str__(self):
        return "Cartão"

class Boleto():
    def pagar(self, valor):
         print(f"Boleto gerado no valor de R$ {valor:.2f}.")

    def __str__(self): # opção para dizer para cada classe como ela deve se comportar quando virar um texto/string, tranformando o nome da classe em um texto normal, sem ser a localização da memória dela
        return "Boleto"

def processar_pagamento(pagamento, valor):
    pagamento.pagar(valor)
    print(f"Pagamento efetuado com sucesso por {pagamento}.")

    # pagamento.pagar(valor)
    # nome_metodo = pagamento.__class__.__name__ # opção também para transformar o nome da classe
    # print(f"Pagamento efetuado com sucesso por {nome_metodo}.")

pix = Pix()
cartao = Cartao()

processar_pagamento(pix, 100)
processar_pagamento(cartao, 200)