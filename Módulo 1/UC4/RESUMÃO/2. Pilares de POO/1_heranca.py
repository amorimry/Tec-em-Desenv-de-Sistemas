# herança em POO é criar novas classes a partir de classes existentes para reaproveitar código.

# classe pai (Superclasse)
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome # Atributo genérico
        self.idade = idade
        self.cpf = cpf

    def apresentar_pessoa(self):
        print(f"""
-- DADOS DA PESSOA --
              
        Nome: {self.nome}
        Idade: {self.idade} anos
        CPF: {self.cpf}
""")

# classe filha (Subclasse)
    # herda os recursos da classe pai
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, salario, cargo):
        super().__init__(nome, idade, cpf)
        self.salario = salario
        self.cargo = cargo

# A função super() chama o construtor da classe Pai para reaproveitar 'nome', 'idade' e 'cpf'
# o super() serve para evitar repetir a criação dos atributos que já existem na classe pai

    def apresentar_func(self):
        print(f"""
-- DADOS GERAL DO FUNCIONÁRIO --
              
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

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, item_comprado):
        super().__init__(nome, idade, cpf)
        self.item_comprado = item_comprado

    def apresentar_cliente(self):
        print(f"""
-- DADOS GERAL DO CLIENTE --
              
        Nome: {self.nome}
        Idade: {self.idade} anos
        CPF: {self.cpf}

        Item comprado: {self.item_comprado}
""")

if __name__ == "__main__":

    func1 = Funcionario("Paulo", 25, "02145695875", 1800, "Vendedor")
    cliente1 = Cliente("Luiza", 32, "36547885232", "Notebook")

    func1.apresentar_pessoa()
    cliente1.apresentar_pessoa()

    func1.apresentar_func()
    cliente1.apresentar_cliente()