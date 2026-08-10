from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nome, local, data, cap_max):
        self.nome = nome
        self.local = local
        self.data = data
        self.cap_max = cap_max

    @abstractmethod
    def realizar_inscricao(self):
        pass

    def __repr__(self):
        return f"""-- Visualizando evento
    Tipo: {self.__class__.__name__}
    Nome: {self.nome}
    Local: {self.local}
    Data: {self.data}
    Capacidade Máxima: {self.cap_max}
"""

class Show(Evento):

    def __init__(self, nome, local, data, cap_max):
        super().__init__(nome, local, data, cap_max)

    def __repr__(self):
         return super().__repr__()

    def realizar_inscricao(self, indice):
        pass

class Festa(Evento):

    def __init__(self, nome, local, data, cap_max):
        super().__init__(nome, local, data, cap_max)

    def __repr__(self):
             return super().__repr__()

    def realizar_inscricao(self, indice):
            pass

class Palestra(Evento):

    def __init__(self, nome, local, data, cap_max):
        super().__init__(nome, local, data, cap_max)

    def __repr__(self):
             return super().__repr__()

    def realizar_inscricao(self, indice):
            pass

class Feira(Evento):

    def __init__(self, nome, local, data, cap_max):
        super().__init__(nome, local, data, cap_max)

    def __repr__(self):
             return super().__repr__()

    def realizar_inscricao(self, indice):
            pass