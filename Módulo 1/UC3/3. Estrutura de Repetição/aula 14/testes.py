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

    sair = input("Informações inseridas.\nQuer continuar? (S/N): ")

    if sair == "N" or "n":
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