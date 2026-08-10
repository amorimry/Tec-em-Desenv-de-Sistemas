class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def mostrar_dados(self):
        print(f"""
--- DADOS DO FUNCIONÁRIO --
    
    Nome: {self.nome}
    Salário: R$ {self.salario:,.2f}
    Cargo: {self.cargo}
""")
        
    def aumentar_salario(self, percentual):
        valor_percentual = (percentual / 100) * self.salario
        self.salario += valor_percentual
        print(f"""
    --- Salário aumentado com sucesso em {percentual}%
""")

    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        print(f"""
    --- Funcionário promovido!
""")

if __name__ == "__main__":

    pessoa1 = Funcionario("Pedro", 2200, "Marketing")
    pessoa2 = Funcionario("Gabriel", 1800, "Administrativo")

    pessoa1.mostrar_dados()
    pessoa1.aumentar_salario(50)
    pessoa1.mostrar_dados()
    pessoa1.promover("Diretor Artístico")
    pessoa1.mostrar_dados()
    print("-------------------------------------------------------------------")
    pessoa2.mostrar_dados()
    pessoa2.aumentar_salario(10)
    pessoa2.mostrar_dados()
    pessoa2.aumentar_salario(15)
    pessoa2.mostrar_dados()
    pessoa2.promover("Gerente")
    pessoa2.mostrar_dados()
    pessoa2.promover("Diretor Geral")
    pessoa2.mostrar_dados()