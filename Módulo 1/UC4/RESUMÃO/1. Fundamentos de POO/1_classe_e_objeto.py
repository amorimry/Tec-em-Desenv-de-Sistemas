# classe é um modelo, tipo um molde para poder criar objetos

# definindo a estrutura de um funcionário que ele precisa ter

# self é "eu mesmo", não precisa mexer nele
    # é a representação do objeto dentro da classe, permintindo guardar os dados

class Funcionario:
    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo

# linha de código para proteger as partes que vc escreve quando tá testando em um local que tem class, método, função...
if __name__ == "__main__":

    func1 = Funcionario("Paulo", 1500, 21, "Auxiliar Administrativo") # essa linha completa é o objeto construído a partir de uma classe = instância
    func2 = Funcionario("Liz", 1800, 24, "Marketing")

    print(func1.nome)
    print(func1.idade)

    print(func2.nome)
    print(func2.idade)