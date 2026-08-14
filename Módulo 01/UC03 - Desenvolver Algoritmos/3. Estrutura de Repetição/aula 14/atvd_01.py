qtd_notas = int(input("Digite quantas notas serão digitadas: "))
soma = 0
for i in range(qtd_notas):
    nota = float(input(f"Digite a {i+1}° nota: "))
    
    if nota < 0 or nota > 10:
        print("Nota inválida, não será calculada.") #aqui implementa uma operação até sair o certo, por isso usamos o _while_, que vai rodar uma repetição até o valor for certo
    else:
        soma += nota

media = soma/qtd_notas

print(f"Média das notas: {media:.2f}")


qtd_notas = int(input("Digite quantas notas serão digitadas: "))
soma = 0
for i in range(qtd_notas):

    while True:
        nota = float(input(f"Digite a {i+1}° nota: "))
    
        if nota < 0 or nota > 10:
            print("Nota inválida, não será calculada.") 
        else:
            soma += nota
            break #aqui vai parar a repetição

media = soma/qtd_notas

print(f"Média das notas: {media:.2f}")