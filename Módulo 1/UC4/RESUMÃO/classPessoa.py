class Pessoa():
    ano_atual = 2026 # esse valor vai ser o mesmo para todos os objetos dessa classe

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def apresentar_pessoa(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    def comer(self, alimento = "algo"):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        
        if self.falar:
            print(f"{self.nome} está falando e não pode comer enquanto fala.")
        
        self.comendo = True
        print(f"{self.nome} está comendo {alimento}.")

    def parar_de_comer(self, alimento = "algo"):
        if not self.comendo: # se caso a variavel comendo não for True
            print(f"{self.nome} já não está comendo.")
            return
        
        self.comendo = False
        print(f"{self.nome} parou de comer {alimento}.")

    def falar(self, assunto = "algo"):
        if self.falando:
            print(f"{self.nome} já está falando.")
            return

        if self.comendo:
            print(f"{self.nome} está comendo e não pode falar enquanto come.")
            return

        self.falando = True
        print(f"{self.nome} está falando {assunto}.")

    def parar_de_falar(self):
        if not self.falando:
            print(f"{self.nome} já não está falando.")
            return
        
        self.falando = False
        print(f"{self.nome} parou de falar.")

    def ano_de_nascimento(self):
        return self.ano_atual - self.idade