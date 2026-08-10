# 3. Boletim simples
# Dada a lista notas = [7.0, 5.5, 8.5, 4.0, 9.0, 6.5], exiba a maior nota, a menor nota e a média da turma usando max(), min(), sum() e len().

notas = [7.0, 5.5, 8.5, 4.0, 9.0, 6.5]
print("- NOTAS -")
for i in notas:
    print(i)
print(f"""
MAIOR: {max(notas)}
MENOR: {min(notas)}
MÉDIA: {sum(notas)/len(notas)}
""")