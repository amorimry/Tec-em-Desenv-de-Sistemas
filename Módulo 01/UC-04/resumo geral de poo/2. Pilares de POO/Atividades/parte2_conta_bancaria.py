from abc import ABC, abstractmethod

class BancoAbstracao(ABC):
    pass

    @abstractmethod
    def fazer_login(self):
        pass

class ContaBancaria(BancoAbstracao):
    def __init__(self, titular, saldo, senha, status = False):
        self._titular = titular
        self.__saldo = saldo
        self.__senha = senha
        self.status = status

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("O saldo não pode ser negativo.")
        elif novo_saldo > 20*self.__saldo:
            print("Saldo ultrapassou o valor para altereação.")
        else:
            self.__saldo = novo_saldo
            print("Saldo atualizado.")

    def fazer_login(self):
        while True:
            senha = input("Digite sua senha: ")
            if senha == self.__senha:
                print("Senha correta, acesso liberado.")
                self.status = True
                break
            else:
                print("Senha incorreta.")
                self.status = False

    def ver_informacoes(self):
        if self.status:
            print(f"""
== INFORMAÇÕES DA CONTA ==

        Titular: {self._titular}
        Saldo: R$ {self.__saldo:,.2f}
""")
        else:
            print("""
    == FAÇA LOGIN NA SUA CONTA ==
""")
        
    def depositar(self, valor):
        if self.status:
            if valor <= 0:
                print("Valor inválido para deposito.")

            else:
                self.__saldo += valor
                print(f"Deposito de R$ {valor:,.2f} efetuado com sucesso.")
        else:
            print("""
    == FAÇA LOGIN NA SUA CONTA ==
""")

    def sacar(self, valor):
        if self.status:
            if valor > self.__saldo:
                print("Saldo insuficiente.")
            
            elif valor <= 0:
                print("Valor inválido para saque.")

            else:
                self.__saldo -= valor
                print(f"Saque de R$ {valor:,.2f} efetuado com sucesso.")
        else:
            print("""
    == FAÇA LOGIN NA SUA CONTA ==
""")

if __name__ == "__main__":

    conta1 = ContaBancaria("Pedro", 1200, "pedropokemon")
    