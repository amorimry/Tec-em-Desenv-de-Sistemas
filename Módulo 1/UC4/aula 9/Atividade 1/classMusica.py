class Musica():
    def __init__(self, nome, artista, genero, lancamento, album = "Não se enquadra"):
        self.nome = nome
        self.artista = artista
        self.genero = genero
        self.lacamento = lancamento
        self.album = album

    def detalhes_da_musica(self):
        print(f"""
--> Detalhes da Música
        
        Título: {self.nome}
        Artista: {self.artista}
        Gênero: {self.genero}
        Ano de Lançamento: {self.lacamento}
        Álbum: {self.album}

    {self.ver_plataforma()}
""")
        
    def ver_plataforma(self):
        if self.artista in ["Lana Del Rey", "Billie Eilish", "Mitski", "Grunge"]:
            return "Ouça a música em: Spotify"
        elif self.artista in ["Willow", "Conan Gray", "YUNGBLUD", "Harry Styles"]:
            return "Ouça a música em: Apple Music"
        elif self.artista in ["Olivia Rodrigo", "Kate Bush", "The Neighbourhood"]:
            return "Ouça a música em: YouTube Music"
        else:
            return "Música não encontrada."