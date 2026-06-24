# encapsulamento serve para poder ocultar detalhes internos do funcionamento de uma classe
# é feito usando métodos e variáveis privadas, que não pode ser acessada diretamente fora da classe
# proteção de dados

class Funcionario:

    ano_atual = 2026

    def __init__(self, nome, idade, cpf, salario, cargo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    def apresentar_func(self):
        print(f"""
-- DADOS DO FUNCIONÁRIO --
              
        Nome: {self.nome}
        Idade: {self.idade} anos
        CPF: {self.cpf}
        Salário: R$ {self.salario:,.2f}
        Cargo: {self.cargo}
""")
        
    def inserir_atividade(self, atividade):
        print(f"""
-- ATIVIDADE DO DIA PARA O FUNCIONÁRIO --
              
        Nome: {self.nome}
        Atividade de hoje: {atividade.upper()}
""")
        
    def aumentar_salario(self, porcentagem_de_aumento):
        novo_salario = self.salario * (1 + porcentagem_de_aumento / 100)
        self.salario = novo_salario


if __name__ == "__main__":

    func1 = Funcionario("Paulo", 1500, 21, "Auxiliar Administrativo")
    func2 = Funcionario("Liz", 1800, 24, "Marketing")