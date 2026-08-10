# um método estático é uma função vinculada à classe, e não a uma instância específica

# ele não recebe os parâmetros implícitos self ou cls, não podendo acessar ou modificar estados da classe ou do objeto

# é definido usando o decorador @staticmethod

# geralmente, métodos estáticos são utilizados para agrupar funções utilitárias que logicamente pertencem à classe, mas que não dependem de nenhum dado do objeto para funcionar

# eles se comportam como funções normais, mas ficam organizados dentro do escopo da classe

class Matematica:
    
    @staticmethod
    def potencia(base, expoente):
        return base ** expoente

    def multiplicar(self, a, b):
        return a * b

# Chamando o método estático diretamente pela classe (sem instanciar)
resultado = Matematica.potencia(2, 3)
print(f"Resultado estático: {resultado}") # Saída: 8

# Também é possível chamar o método estático a partir de um objeto, se preferir
objeto_mat = Matematica()
print(f"Objeto potência: {objeto_mat.potencia(3, 2)}") # Saída: 9

# O método comum 'multiplicar' exige uma instância para ser chamado
print(f"Multiplicação: {objeto_mat.multiplicar(4, 5)}") # Saída: 20
