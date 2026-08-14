print(f"Bem vindo(a) a página para calcular as médias dos alunos da escola!")

aluno = input("Digite o nome do aluno(a): ")

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

print(f"A média do aluno(a) {aluno} foi de {media:.1f} pontos.")
# para poder organizar a casa decimal coloca :, depois um ., a quantidade de casa decimal e termina com um f