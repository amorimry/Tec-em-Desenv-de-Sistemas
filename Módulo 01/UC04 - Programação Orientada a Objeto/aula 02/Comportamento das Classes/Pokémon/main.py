from classPokemon import Pokemon

pok1 = Pokemon("Sunflora", "Grama", "Johto", ["Fogo, Gelo, Veneno, Inseto, Voador"], ["Água, Terra, Rocha"])
pok2 = Pokemon("Mimikyu", "Fantasma / Fada", "Alola", ["Fantasma, Aço"], ["Dragão, Lutador, Inseto, Normal"])
pok3 = Pokemon("Jynx", "Gelo / Psíquico", "Kanto", ["Fogo, Inseto, Fantasma, Aço, Sombrio, Rocha"], ["Grama, Terra, Voador, Dragão, Lutador, Veneno"])
pok4 = Pokemon("Meowth", "Normal", "Kanto", ["Lutador"], ["Nenhuma"])
pok5 = Pokemon("Marill", "Água / Fada", "Johto", ["Elétrico, Grama, Veneno"], ["Fogo, Água, Gelo, Lutador, Inseto, Sombrio, Dragão"])


print(f"""
-- Pokémons preferidos --

    {pok1.nome}
    Tipo: {pok1.tipo}
    Região: {pok1.regiao}
        Fraqueza: {pok1.fraqueza}
        Vantagem: {pok1.vantagem}

    {pok2.nome}
    Tipo: {pok2.tipo}
    Região: {pok2.regiao}
        Fraqueza: {pok2.fraqueza}
        Vantagem: {pok2.vantagem}

    {pok3.nome}
    Tipo: {pok3.tipo}
    Região: {pok3.regiao}
        Fraqueza: {pok3.fraqueza}
        Vantagem: {pok3.vantagem}
""")