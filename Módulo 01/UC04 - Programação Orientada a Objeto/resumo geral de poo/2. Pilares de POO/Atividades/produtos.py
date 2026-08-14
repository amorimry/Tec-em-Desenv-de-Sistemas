class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome # atributo público
        self.__preco = preco # atributo privado
        self.__estoque = estoque # atributo privado

# GETTER (ermite ler o saldo de fora com: produto1.preco)
    @property
    def preco(self):
        return self.__preco

# SETTER (permite alterar o saldo de fora com: produto1.preco = novo_preco)
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("O preço deve ser maior que zero.")

# GETTER
    @property
    def estoque(self):
        return self.__estoque

# SETTER
    @estoque.setter
    def estoque(self, novo_estoque):
        if novo_estoque >= 0:
            self.__estoque = novo_estoque
        else:
            print("O estoque não pode ser negativo.")

    def mostrar_produto(self):
        print(f"""
== INFORMAÇÕES DO PRODUTO ==
              
    Produto: {self.nome}
    Preço: R$ {self.__preco:.2f}
    Estoque: {self.__estoque}
""")

if __name__ == "__main__":

    produto1 = Produto("Notebook", 3500, 10)

    produto1.mostrar_produto()

    produto1.preco = 4000
    produto1.estoque = 8

    produto1.mostrar_produto()

    produto1.preco = -100
    produto1.estoque = -5

    produto1.mostrar_produto()