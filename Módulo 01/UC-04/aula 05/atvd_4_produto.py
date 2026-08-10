class Produto():
    def __init__(self, nome, preco_und, qtd):
        self.nome = nome
        self.preco_und = preco_und
        self.preco_total = preco_und * qtd
        self.qtd = qtd

    def mostrar_dados(self):
        print(f"""
-- Dados do Produto --
              
    NOME: {self.nome}
    PREÇO UND: R$ {self.preco_und:,.2f}
    QUANTIDADE: {self.qtd} und
""")

    def valor_total(self):
        print(f"""
-- Valor Total --
              
    R$ {self.preco_total:,.2f}
""")
        
    def aplicar_desconto(self, percentual):
        desconto = (100 - percentual) / 100
        # self.preco_total = (self.preco_total * desconto)
        print(f"""
-- Descontos --
              
    Valor da compra: R$ {self.preco_total:,.2f}
    Valor do desconto: {percentual}%
    
    Valor final com desconto: R$ {(self.preco_total * desconto):,.2f}
""")


if __name__ == "__main__":

    produto1 = Produto("Geladeira", 3200, 1)
    produto2 = Produto("Celular", 2200, 2)

    produto1.mostrar_dados()

    produto1.aplicar_desconto(25)

    print("-----------------------------------------------")

    produto2.mostrar_dados()
    produto2.valor_total()

    produto2.aplicar_desconto(10)