# um método de classe é aquele que pertence à classe em si, e não a uma instância específica

# ele é criado utilizando o decorador @classmethod e seu primeiro parâmetro é sempre cls (uma referência à própria classe, em vez de self)

# usar um método de classe é ideal para poder criar construtores alternativos ou acessar/modificar alguma variável da classe

class Funcionario:

    empresa = "Tech Solutions"

    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo

    # método de instância comum
    def apresentar_func(self):
        print(f"""
-- DADOS DO FUNCIONÁRIO --
              
        Nome: {self.nome}
        Salário: R$ {self.salario:,.2f}
        Idade: {self.idade} anos
        Cargo: {self.cargo}
""")

    # método de classe
    @classmethod
    def criar_de_string(cls, dados_string):
        # construtor alternativo que recebe uma string formatada
        nome, salario, idade, cargo = dados_string.split(',')
        # 'cls' aqui cria uma nova instância de Funcionario(nome, salario, idade, cargo)
        return cls(nome, float(salario), int(idade), cargo)

# usando o construtor padrão
f1 = Funcionario("Ana", 5000.0)
f1.exibir_dados()

# usando o método de classe para instanciar a partir de uma string
dados = "Carlos,6000.0"
f2 = Funcionario.criar_de_string(dados)
f2.exibir_dados()
