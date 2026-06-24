# atributos são variáveis internas do objeto que definem seus comportamentos

# características de um objeto

# os atributos são definidos dentro do método construtor __init__

class Funcionario:

    ano_atual = 2026 # esse valor vai ser o mesmo para todos os objetos dessa classe

    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo

# aqui a classe Funcionario possui 4 atributos: nome, salário, idade e cargo

# atributos de instância:
    # self.nome
    # self.salario
    # self.idade
    # self.cargo

# atributos de classe:
    # ano_atual

if __name__ == "__main__":

# a criação de um objeto é chamado de instanciar uma classe

    func1 = Funcionario("Paulo", 1500, 21, "Auxiliar Administrativo")
    func2 = Funcionario("Liz", 1800, 24, "Marketing") # instância = objeto

    print(func1.nome)
    print(func1.idade)

    print(func2.nome)
    print(func2.idade)