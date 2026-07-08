class Cliente():
    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

class Servico():
    def __init__(self, nome, valor, duracao):
        self.nome = nome
        self.valor = valor
        self.duracao = duracao

class Agendamento():
    def __init__(self, cliente, servico, data, horario):
        self.cliente = cliente
        self.servico = servico
        self.data = data
        self.horario = horario
