print ("_____Cadastramento de Notas_____")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

media_notas = (nota1 + nota2 + nota3 + nota4)/4

print (f"A média do aluno é de {media_notas:.1f} pontos.")

if media_notas >= 7 and media_notas <= 10:
    print ("--> Aluno aprovado!")
elif media_notas < 7 and media_notas >= 4:
    print ("--> Aluno de recuperação!")
elif media_notas < 4 and media_notas >= 0:
    print ("--> Aluno reprovado!")
else:
    print ("_ Erro no cálculo _")