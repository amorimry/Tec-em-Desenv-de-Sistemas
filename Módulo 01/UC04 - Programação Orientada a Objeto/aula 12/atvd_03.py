# Crie uma classe que modele uma pessoa:
# ● Atributos: nome, idade, peso e altura
# ● Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.anos_envelhecidos = 0

    def envelhecer(self, qtd_ano):
        self.idade += qtd_ano
        self.anos_envelhecidos += qtd_ano
        print(f"{self.nome} envelheceu {qtd_ano} ano(s).")
        print(f"Idade atual: {self.idade} anos")

    def engordar(self, valor_peso):
        self.peso += valor_peso
        print(f"{self.nome} engordou {valor_peso} Kg.")
        print(f"Peso atual: {self.peso} Kg")

    def emagrecer(self, valor_peso):
        self.peso -= valor_peso
        print(f"{self.nome} emagreceu {valor_peso} Kg.")
        print(f"Peso atual: {self.peso} Kg")

    def crescer(self):
        if self.anos_envelhecidos == 0:
            print(f"Não foi resgistrado envelhecimento para {self.nome}")
        else:
            idade_anterior = self.idade - self.anos_envelhecidos
            if self.idade >= 21:
                print(f"{self.nome} já tem 21 anos e não cresce mais.")
            else:
                idade_limite = min(self.idade, 21) #aqui vai pegar até onde a pessoa pode crescer, se ela tinha 19 e cresceu 5 anos de uma vez, ela vai passar a ter 24, mas por não poder crescer até os 24 ela só cresce até os 21, então de 19 para 21 são dois anos, ou seja, ela só cresce por 2 anos
                anos_para_crescer = idade_limite - idade_anterior #aqui descobrimos quantos anos dentro do "período de crescimento" realmente se passaram, se ela tinha 19 (idade_anterior) e vai crescer até os 21 (idade_limite), ela pode crescer por 2 anos (anos_para_crescer), fazendo a subtração
                crescimento = anos_para_crescer * 0.05
                self.altura += crescimento
                self.anos_envelhecidos = 0
                print(f"{self.nome} cresceu {crescimento:.2f} m!")
                print(f"Altura atual: {self.altura:.2f} m.")