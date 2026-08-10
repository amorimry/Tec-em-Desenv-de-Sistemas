class Pokemon():
    def __init__(self, nome, tipo, regiao, fraqueza, vantagem):
        self.nome = nome
        self.tipo = tipo
        self.regiao = regiao
        self.fraqueza = fraqueza
        self.vantagem = vantagem

    def mostrar_pokemon(self):
        print(f"""{"-"*60}
Pokémon:

    {self.nome}
    Tipo: {self.tipo}
    Região: {self.regiao}

        Fraqueza: {self.fraqueza}
        Vantagem: {self.vantagem}
{"-"*60}""")