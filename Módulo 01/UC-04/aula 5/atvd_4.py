class Produto():
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.total_calculado = False

    def mostrar_dados(self):
        print(f"""
-- Dados do Produto --
              
    NOME: {self.nome}
    PREÇO: R$ {self.preco:,.2f}
    QUANTIDADE: {self.qtd} und
""")

    def valor_total(self):
        self.preco = self.preco * self.qtd
        self.total_calculado = True
        print(f"""
    --- Valor total calculado!
""")
        
    def aplicar_desconto(self, percentual):
        if self.qtd > 1 and self.total_calculado:
            desconto = (percentual / 100) * self.preco
            self.preco -= desconto
            print(f"""
        --- Desconto de {percentual}% aplicato na compra!
    """)
        else:
            print("""
    OBS: Compra acima de 1 unidade.
        --- Calcule o valor total antes de aplicar o desconto!
""")


if __name__ == "__main__":

    produto1 = Produto("Geladeira", 3200, 1)
    produto2 = Produto("Celular", 2200, 2)

    produto1.mostrar_dados()
    produto1.aplicar_desconto(25)
    produto1.mostrar_dados()
    produto1.valor_total()
    produto1.mostrar_dados()

    print("-----------------------------------------------")

    produto2.mostrar_dados()
    produto2.aplicar_desconto(30)
    produto2.valor_total()
    produto2.mostrar_dados()
    produto2.aplicar_desconto(30)
    produto2.mostrar_dados()
    produto2.aplicar_desconto(10)
    produto2.mostrar_dados()