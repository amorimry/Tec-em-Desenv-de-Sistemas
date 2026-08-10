class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Cliente(Pessoa):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)

    def apresentar(self):
        return (f"Cliente: {self.nome} | Telefone: {self.telefone}")

    def total_gasto(self, lista):
        total = 0
        for v in lista:
            total += v.preco
        return (f"R$ {total:,.2f}")

class Profissional(Pessoa):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)

    def apresentar(self):
        print(f"Profissional: {self.nome} | Telefone: {self.telefone}")

    def agenda_do_dia(self, data):
        return [ag.resumo() for ag in self.agendamentos
                if ag.data_hora.startswith(data)]

# ------------------------------------------------------------

class Agendamento:
    agendamentos = []

    def __init__(self, cliente, profissional, servico, data_hora):
        self.cliente = cliente
        self.profissional = profissional
        self.servico = servico
        self.data_hora = data_hora
        cliente.agendamento.append(self)
        profissional.agendamento.append(self)

    def resumo(self):
        return (f"{self.data_hora} | {self.cliente.nome} com"
                f"{self.profissional.nome} - {self.servico.nome}"
                f"R$ {self.servico.get_preco():.2f}")

class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo):
        if novo > 0:
            self.__preco = novo
        else:
            print("Preço inválido.")


if __name__ == "__main__":
    pass