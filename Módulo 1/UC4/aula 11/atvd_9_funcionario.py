class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def mostrar_dados(self):
        print(f"""
--- DADOS DO FUNCIONÁRIO --
    
    Nome: {self.nome}
    Salário: R$ {self.salario:.2f}
    Cargo: {self.cargo}
""")
        
    def aumentar_salario(self, percentual):
        valor_percentual = (percentual / 100) * self.salario
        self.salario += valor_percentual

    def promover(self, novo_cargo):
        self.cargo = novo_cargo

if __name__ == "__main__":

    pessoa1 = Funcionario()
    pessoa2 = Funcionario()