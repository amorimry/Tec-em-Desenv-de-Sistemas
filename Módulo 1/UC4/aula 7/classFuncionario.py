class Funcionario:
    # método contrutor - cria o objeto
    # definindo a estrutura de um funcionário que ele precisa ter
    def __init__(self, nome, salario, idade, cargo): # função que serve para configurar a variavel e me devolver um elemento do tipo Funcionario / self é "eu mesmo", não precisa mexer nele
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo


class Funcionario:
    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo