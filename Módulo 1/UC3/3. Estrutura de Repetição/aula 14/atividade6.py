# 3. Em uma competição de corrida um programa deve receber quantos metros cada competidor correu. Execute o programa até que seja inserido 0 na quantidade de metros percorridos. Ao final mostre qual foi o maior percurso registrado.
# Bônus: Colete também o nome de cada competidor e exiba o nome do competidor com o maior percurso


colocacao = 1
maior = 0 #aqui nesse programa não faz sentido ter um valor abaixo de 0, então daria certo nesse cenario ter um 0 como inicio
menor = 100 #no caso eu sei quantos metros é o máximo da corrida

while True:
    metros = float(input(f"Digite quantros metros foram percorridos pelo {colocacao}° corredor (0 para finalizar): "))
    colocacao += 1
    #é importante essas vericações estarem no inicio pois vai protegendo e controlando o fluxo
    if metros < 0:
        print("Digite um valor válido novamente!")
        continue #pega uma info inválida e desconsidera, e volta para a próxima repetição
    if metros == 0:
        print("Encerrando cadastro de percurso!")
        break

    if maior < metros:
        maior = metros
    if menor > metros:
        menor = metros

print(f"Maior percurso: {maior} metros.")
print(f"Menor percurso: {menor} metros.")




    



maior_corrida = ""
menor_corrida = ""
maior = float("-inf")
menor = float("inf")

colocacao = 1
sair = 1

while True:
    corredor = input(f"Digite o nome do {colocacao}° corredor: ")
    colocacao += 1
    metros = float(input(f"Digite quantros metros foram percorridos: "))

    if metros < 0:
        print("Digite um valor válido novamente!")
        continue

    sair = int(input("Informações inseridas.\nQuer continuar? (S/N): "))

    if sair == "N":
        print("Encerrando cadastro de percurso!")
        break

    if maior < metros:
        maior = metros
        maior_corrida = corredor
    if menor > metros:
        menor = metros
        menor_corrida = corredor

print(f"""
Maior percurso: {maior} metros.
Menor percurso: {menor} metros.

Maior corredor: {maior_corrida}.
Menor corredor: {menor_corrida}.
""")