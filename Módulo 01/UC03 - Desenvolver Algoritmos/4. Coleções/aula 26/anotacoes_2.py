def somar (num1, num2): # função usada para me mostrar algo
    soma = num1 + num2
    print(f"Resultado da soma: {soma}")

somar(20,50)

# print(soma) --> nenhuma dessas variaveis existe
# print(num1)
# print(num2)

def dividir(num1, num2): # função usada para me devolver algo
    resultado = num1 / num2

    return resultado # aqui vc retorna o resultado que tiver dentro da função

# dividir(10, 2) # não vai rodar
print(dividir(10,2))

print(f"Resultado da função Somar: {somar}")
print(f"Resultado da função Dividir: {dividir}")