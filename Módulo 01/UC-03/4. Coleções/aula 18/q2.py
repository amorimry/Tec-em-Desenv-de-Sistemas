# 2. Fila de atendimento
# Uma clínica tem uma fila com os nomes: ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]. Adicione "Tatiane" ao final da fila e remova "Fábio" porque ele desistiu. Exiba a fila atualizada e o total de pessoas.

nomes = ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]
print(nomes)

nomes.append("Tatiane")
nomes.pop(2)
# if "Fábio" in nomes:
#     nomes.remove("Fábio")

num = 1
for n in nomes:
    print(f"{num}. {n}")
    num += 1

print(f"Total de pacientes: {len(nomes)}")