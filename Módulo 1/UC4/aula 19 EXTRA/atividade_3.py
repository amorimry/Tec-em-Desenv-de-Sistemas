# Atividade 3: Classe Carro
# • Descrição: Crie uma classe chamada Carro com atributos marca e modelo. Adicione um método chamado descrever que imprime a marca e o modelo do carro. Crie dois objetos dessa classe e chame o método. Crie os métodos fechar_porta e metodo abri_porta.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.porta = False
    
    def __str__(self):
        return f"Carro modelo {self.modelo}, fabricante {self.marca}"
    
    def descrever(self):
        print(f"""
    Marca: {self.marca}
    Modelo: {self.modelo}
""")
    
    def abrir_porta(self):
        if not self.porta:
            self.porta = True
            return f"Abrindo a porta do {self.modelo}..."
        else:
            return f"A porta do {self.modelo} já está aberta!"
            
    def fechar_porta(self):
        if self.porta:
            self.porta = False
            return f"Fechando a porta do {self.modelo}..."
        else:
            return f"A porta do {self.modelo} já está fechada!"


carro1 = Carro("Volkswagen", "Fusca")
carro2 = Carro("Volkswagen", "Kombi")

carro1.descrever()
carro2.descrever()

print(carro1.abrir_porta())
print(carro1.abrir_porta())
print(carro1.fechar_porta())
print(carro1.fechar_porta())