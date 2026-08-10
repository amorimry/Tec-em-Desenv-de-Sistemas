# 4. Crie um programa que pede a idade de uma pessoa e imprima a faixa etária dessa pessoa seguindo as regras:

# 0 - 17  -> Criança
# 18 - 59  -> Adulto
# 60+ -> Sênior
# Idade Inválida -> Alienígena 👽

print ("== Faixa etária ==")
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 17:
    print ("Criança.")
elif idade >=18 and idade <= 59:
    print ("Adulto.")
elif idade >= 60 and idade <= 120:
    print ("Sênior.")
else:
    print ("Idade Inválida -> Alienígena 👽")