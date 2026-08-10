# DESAFIO 1
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    @property
    def idade(self):
        # Retorne a idade privada
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        # Valide se a nova idade é maior ou igual a zero
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("A idade não pode ser negativa.")

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.__idade}")


pessoa1 = Pessoa("Ana", 20)

pessoa1.apresentar()

pessoa1.idade = 21
pessoa1.apresentar()

pessoa1.idade = -5
pessoa1.apresentar()

# DESAFIO 2
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço alterado com sucesso.")
        else:
            print("O preço deve ser maior que zero.")

    def mostrar_produto(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.__preco:.2f}")


produto1 = Produto("Mouse", 80)

produto1.mostrar_produto()

produto1.preco = 95
produto1.mostrar_produto()

produto1.preco = -30
produto1.mostrar_produto()

# DESAFIO 3
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
            print("Nota alterada com sucesso.")
        else:
            print("A nota deve estar entre 0 e 10.")

    def mostrar_aluno(self):
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.__nota}")


aluno1 = Aluno("Carlos", 8)

aluno1.mostrar_aluno()

aluno1.nota = 9.5
aluno1.mostrar_aluno()

aluno1.nota = 15
aluno1.mostrar_aluno()

# DESAFIO 4
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
            print("Salário alterado com sucesso.")
        else:
            print("O salário deve ser maior que zero.")

    def mostrar_funcionario(self):
        print(f"Funcionário: {self.nome}")
        print(f"Salário: R$ {self.__salario:.2f}")


funcionario1 = Funcionario("Mariana", 2500)

funcionario1.mostrar_funcionario()

funcionario1.salario = 3000
funcionario1.mostrar_funcionario()

funcionario1.salario = -1000
funcionario1.mostrar_funcionario()

# DESAFIO 5
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def mostrar_conta(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta1 = ContaBancaria("João", 500)

conta1.mostrar_conta()

conta1.depositar(200)
conta1.sacar(100)

print(conta1.saldo)

conta1.sacar(1000)
conta1.mostrar_conta()

# DESAFIO 6
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    @property
    def senha(self):
        return "Senha protegida."

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("A senha deve ter pelo menos 6 caracteres.")

    def mostrar_usuario(self):
        print(f"Usuário: {self.nome}")
        print(self.senha)


usuario1 = Usuario("admin", "123456")

usuario1.mostrar_usuario()

usuario1.senha = "abc"
usuario1.mostrar_usuario()

usuario1.senha = "abc123"
usuario1.mostrar_usuario()

# DESAFIO 7
class Livro:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.__preco = preco

    @property
    def preco(self):
        return self.preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço do livro atualizado.")
        else:
            print("O preço do livro deve ser maior que zero.")

    def mostrar_livro(self):
        print(f"Livro: {self.titulo}")
        print(f"Preço: R$ {self.__preco:.2f}")


livro1 = Livro("Python para Iniciantes", 59.90)

livro1.mostrar_livro()

livro1.preco = 79.90
livro1.mostrar_livro()

livro1.preco = 0
livro1.mostrar_livro()

# DESAFIO 8
class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.__ano = ano

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        if novo_ano >= 1900:
            self.__ano = novo_ano
            print("Ano alterado com sucesso.")
        else:
            print("Ano inválido.")

    def mostrar_veiculo(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.__ano}")


veiculo1 = Veiculo("Civic", 2020)

veiculo1.mostrar_veiculo()

veiculo1.ano = 2024
veiculo1.mostrar_veiculo()

veiculo1.ano = 1800
veiculo1.mostrar_veiculo()

# DESAFIO 9
class Curso:
    def __init__(self, titulo, carga_horaria):
        self.titulo = titulo
        self.__carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga):
        if nova_carga > 0:
            self.__carga_horaria = nova_carga
            print("Carga horária alterada com sucesso.")
        else:
            print("A carga horária deve ser maior que zero.")

    def mostrar_curso(self):
        print(f"Curso: {self.titulo}")
        print(f"Carga horária: {self.__carga_horaria} horas")


curso1 = Curso("Python POO", 20)

curso1.mostrar_curso()

curso1.carga_horaria = 30
curso1.mostrar_curso()

curso1.carga_horaria = 0
curso1.mostrar_curso()

# DESAFIO 10
class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.__quantidade = quantidade

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
            print("Quantidade atualizada com sucesso.")
        else:
            print("A quantidade não pode ser negativa.")

    def mostrar_estoque(self):
        print(f"Produto: {self.produto}")
        print(f"Quantidade em estoque: {self.__quantidade}")


estoque1 = Estoque("Notebook", 10)

estoque1.mostrar_estoque()

estoque1.quantidade = 5
estoque1.mostrar_estoque()

estoque1.quantidade = -3
estoque1.mostrar_estoque()