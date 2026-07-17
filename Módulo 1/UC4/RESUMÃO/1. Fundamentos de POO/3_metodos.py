# é uma função, mas dentro de uma classe essa função passa a se chamar método
# ação que o objeto pode executar

# def __init__ é um método construtor (cria o objeto), que serve para configurar a variavel e me devolver um elemento do tipo Funcionario

    # __init__ serve para iniciar o objeto com os dados dele

    # def __init__(self, nome, salario, idade, cargo): linha do método construtor __init__

class Funcionario:

    ano_atual = 2026

    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo

    def apresentar_func(self):
        print(f"""
-- DADOS DO FUNCIONÁRIO --
              
        Nome: {self.nome}
        Salário: R$ {self.salario:,.2f}
        Idade: {self.idade} anos
        Cargo: {self.cargo}
""")
        
    def inserir_atividade(self, atividade):
        print(f"""
-- ATIVIDADE DO DIA PARA O FUNCIONÁRIO --
              
        Nome: {self.nome}
        Atividade de hoje: {atividade.upper()}
""")
        
    def aumentar_salario(self, porcentagem_de_aumento):
        novo_salario = self.salario * (1 + porcentagem_de_aumento / 100) # cálculo para aumentar em 20% o valor do salário atual
        self.salario = novo_salario
        
# criado três métodos para a classe Funcionario

# o self é entendido como algo que aponta para a instância atual que está executando o método

# == LOCALIDADE DO MÉTODO ==

# 

    # MÉTODOS ESPECIAIS
    def __str__ (self):
        return f"O funcionário {self.nome}, com {self.idade} anos de idade, recebe R$ {self.salario} trabalhando no cargo de {self.cargo}."

if __name__ == "__main__":

    func1 = Funcionario("Paulo", 1500, 21, "Auxiliar Administrativo")
    func2 = Funcionario("Liz", 1800, 24, "Marketing")

    func1.inserir_atividade("organizar planilhas.")
    func2.apresentar_func() # chamando o método para rodar
    func2.aumentar_salario(20) # vai aumentar o salário mais 20% do valor atual
    func2.apresentar_func() # mudou a informação do salário no objeto em que rodou o método

    print(func2)
