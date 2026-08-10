# ENCAPSULAMENTO
# usado para proteger os dados de uma classe e controlar como esses dados podem ser acessados ou alterados.
# prática de proteger os atributos de uma classe, permitindo que eles sejam acessados ou modificados apenas de forma controlada.
# em vez de alterar um atributo diretamente, criamos métodos para controlar essa alteração.

# class Pessoa():
#     def __init__(self, nome, idade):
#         self.nome = nome # isso seria um atributo público, onde pode ser acessado fora da class
#         self.idade = idade

# class Pessoa():
#     def __init__(self, nome, idade):
#         self._nome = nome # isso seria um atributo protegido por convenção, pois com um _ indica que aquele atributo não pode ser alterado diretamente
#         self._idade = idade

class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome # isso seria um atributo privado, pois tê, dois _
        self.__idade = idade

    # def exibir(self):
    #     print(f"Nome: {self.__nome}\nIdade: {self.__idade}")


pessoa1 = Pessoa("Pedro", "20")

# print(pessoa1.nome)
# print(pessoa1.idade)

pessoa1.__nome = "Gabriel"

# print(pessoa1.nome)
# print(pessoa1.idade)

print(pessoa1.__nome)
print(pessoa1.__idade)


