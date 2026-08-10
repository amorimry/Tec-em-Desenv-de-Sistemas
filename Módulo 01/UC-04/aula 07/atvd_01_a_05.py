# ATIVIDADE 1
class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    def alterar_nota(self, nova_nota):
        if nova_nota >= 0 and nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Erro: A nota deve estar entre 0 e 10.")

# ATIVIDADE 2
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento
            print(f"Aumento aplicado! Novo salário: R$ {self.__salario}")
        else:
            print("Aumento inválido, o valor do aumento deve ser maior que zero.")

# ATIVIDADE 3
class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.__preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco
    
    @property
    def estoque(self):
        return self.__estoque
    
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @estoque.setter
    def estoque(self, novo_estoque):
        self.__estoque = novo_estoque

# ATIVIDADE 4
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def transferir(self, valor, conta_destino):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            conta_destino.__saldo += valor
            print(f"Trandferência de R$ {valor:,.2f} realizada com sucesso para a conta {conta_destino}")
        else:
            print(f"Transação inválida! Tente novamente.")

# ATIVIDADE 5
class Usuario():
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    def alterar_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Mudança inválida, a nova senha deve ter pelo menos 6 caracteres.")