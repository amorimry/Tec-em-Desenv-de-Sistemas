# métodos de instância são funções definidas dentro de uma classe que operam sobre os dados específicos de um objeto individual
    # lembrando que instância é o objeto criado a partir de uma classe

class Funcionario:

    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo

# método de instância
    def apresentar_func(self):
        print(f"""
-- DADOS DO FUNCIONÁRIO --
              
        Nome: {self.nome}
        Salário: R$ {self.salario:,.2f}
        Idade: {self.idade} anos
        Cargo: {self.cargo}
""")