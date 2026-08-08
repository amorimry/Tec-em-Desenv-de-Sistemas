from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf, matricula, salario):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, cpf, matricula, salario, bonus):
        super().__init__(nome, cpf, matricula, salario)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario + (self.salario * self.bonus/100)

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, matricula, salario, comissao):
        super().__init__(nome, cpf, matricula, salario)
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario + self.comissao

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, matricula, salario, auxilio, carga_horaria):
        super().__init__(nome, cpf, matricula, salario)
        self.auxilio = auxilio
        self.carga_horaria = carga_horaria

    def calcular_salario(self):
        return self.salario + self.auxilio

teste1 = Gerente("Pedro", "02145632587", "1144", 2500, 10)
teste2 = Vendedor("Liz", "85695748523", "5565", 1800, 200)
teste3 = Estagiario("Tomas", "56481235778", "8547", 900, 60, 6)

print(f"R$ {teste1.calcular_salario():.2f}")
print(f"R$ {teste2.calcular_salario():.2f}")
print(f"R$ {teste3.calcular_salario():.2f}")