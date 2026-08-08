class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        valor_deposito = valor + self.saldo
        print(f"O valor de R$ {valor:.2f} foi depositado com sucesso na conta bancária: {self.titular}.")

        self.saldo = valor_deposito

        # self.saldo += valor
        # print(f"O valor de R$ {valor:.2f} foi depositado com sucesso na conta bancária: {self.titular}.")

    def sacar(self, valor):
        valor_saque = self.saldo - valor
        if valor_saque <= 0:
            print(f"Não foi possivel sacar o valor de R$ {valor:.2f}, saldo insuficiente.")
        else:
            print(f"O valor de R$ {valor:.2f} foi sacado com sucesso da conta bancária: {self.titular}.")
            self.saldo = valor_saque

        # if self.saldo >= valor:
        #     self.saldo -= valor
        #     print(f"O valor de R$ {valor:.2f} foi sacado com sucesso da conta bancária: {self.titular}.")
        # else:
        #     print(f"Não foi possivel sacar o valor de R$ {valor:.2f}, saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"""
-- INFORMAÇÕES DA CONTA --
    Titular: {self.titular}
    Saldo: R$ {self.saldo:,.2f}
""")


if __name__ == "__main__":

    teste1 = ContaBancaria("Alexandre", 1500)

    teste1.mostrar_saldo()
    print("----------------------------------------")
    teste1.depositar(50)

    teste1.mostrar_saldo()
    print("----------------------------------------")
    teste1.sacar(2000)

    teste1.mostrar_saldo()
    print("----------------------------------------")
    teste1.sacar(500)

    teste1.mostrar_saldo()
    print("----------------------------------------")