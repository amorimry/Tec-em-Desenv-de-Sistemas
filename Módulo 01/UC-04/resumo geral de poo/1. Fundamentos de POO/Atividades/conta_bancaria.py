class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ver_informacoes(self):
        pass

    def depositar(self, deposito):
        self.saldo += deposito