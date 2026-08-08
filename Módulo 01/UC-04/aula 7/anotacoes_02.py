class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # GETTER (Permite ler o nome: pessoa1.nome)
    @property
    def nome(self):
        return self.__nome
    
    # SETTER (Permite alterar o nome de forma segura: pessoa1.nome = "Gabriel")
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    # GETTER para a idade
    @property
    def idade(self):
        return self.__idade
    
pessoa1 = Pessoa("Pedro", "20")
print(pessoa1.nome)   # Saída: Pedro
print(pessoa1.idade)  # Saída: 20

# Altera usando o setter
pessoa1.nome = "Gabriel"

# Lê usando os getters (sem usar os underlines!)
print(pessoa1.nome)   # Saída: Gabriel
print(pessoa1.idade)  # Saída: 20
