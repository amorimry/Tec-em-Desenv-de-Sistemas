class Materiais():
    def __init__(self, titulo, autor, ano, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def exibir_informacao(self):
        print(f"""
== INFORMAÇÕES ==

        Título: {self.titulo}
        Autor: {self.autor}
        Ano: {self.ano}
        Quantidades: {self.disponivel}
""")

class Livro(Materiais):
    def __init__(self, titulo, autor, ano, disponivel, num_paginas):
        super().__init__(titulo, autor, ano, disponivel)
        self.num_paginas = num_paginas

    def emprestar(self):
        print(f"""
== EMPRÉSTIMO DE LIVRO ==

        Título: {self.titulo}
        Autor: {self.autor}
        Ano: {self.ano}
        Quantidades: {self.disponivel}

        Número de páginas: {self.num_paginas}

""")

class Revista(Materiais):
    def __init__(self, titulo, autor, ano, disponivel, edicao):
        super().__init__(titulo, autor, ano, disponivel)
        self.edicao = edicao

    def emprestar(self):
        print(f"""
== EMPRÉSTIMO DE REVISTA ==

        Título: {self.titulo}
        Autor: {self.autor}
        Ano: {self.ano}
        Quantidades: {self.disponivel}

        Edição: {self.edicao}

""")

class DVD(Materiais):
    def __init__(self, titulo, autor, ano, disponivel, duracao):
        super().__init__(titulo, autor, ano, disponivel)
        self.duracao = duracao

    def emprestar(self):
        print(f"""
== EMPRÉSTIMO DE DVD ==

        Título: {self.titulo}
        Autor: {self.autor}
        Ano: {self.ano}
        Quantidades: {self.disponivel}

        Duração: {self.duracao} minutos

""")
        

if __name__ == "__main__":

    livro1 = Livro("Viagem ao centro da Terra.", "Julio Verme", 2010, 5, 590)
    revista1 = Revista("Construções de Brasília", "Nicolas Nietch", 2011, 12, "Colecionador")
    dvd1 = DVD("Xuxa para baixinhos", "Xuxa", 2004, 25, 120)

    livro1.exibir_informacao()
    livro1.emprestar()