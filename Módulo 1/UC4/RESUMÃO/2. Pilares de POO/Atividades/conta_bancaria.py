class ContaBancaria():
    def __init__(self, titular, saldo):
        self._titular = titular
        self.__saldo = saldo

# GETTER (ermite ler o saldo de fora com: conta1.saldo)
    @property
    def ver_saldo(self):
        return self.__saldo
    
# SETTER (permite alterar o saldo de fora com: conta1.saldo = valor)
    @ver_saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("O saldo não pode ser negativo.")
        else:
            self.__saldo = novo_saldo
            print("Saldo atualizado.")

    def ver_informacoes(self):
        print(f"""
== INFORMAÇÕES DA CONTA ==

        Titular: {self._titular}
        Saldo: R$ {self.__saldo:,.2f}
""")
        
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para deposito.")

        else:
            self.__saldo += valor
            print(f"Deposito de R$ {valor:,.2f} efetuado com sucesso.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        
        elif valor <= 0:
            print("Valor inválido para saque.")

        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:,.2f} efetuado com sucesso.")

if __name__ == "__main__":

    conta1 = ContaBancaria("Pedro", 2000)

    conta1.ver_informacoes()

    conta1._titular = "Ryan"
    conta1.__saldo = 5000000000
    conta1.ver_informacoes()

    conta1.depositar(0)
    conta1.depositar(100)

    conta1.ver_informacoes()

    conta1.sacar(10000)
    conta1.sacar(1000)

    conta1.ver_informacoes()