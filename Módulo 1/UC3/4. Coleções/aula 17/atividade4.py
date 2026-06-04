print("--- LISTA DE ANIMAIS ---")
animais = ["pavão", "porco", "abelha", "cavalo", "golfinho"]
print(animais)

animal1 = "macaco"
animais = ["pavão", "porco", "abelha", "cavalo", "golfinho", animal1]
print(animais)

animais.append("tartaruga") #adicionar um novo elemento na lista
print(animais)

animais.insert(0, "gato") #adicionar na posição que vc deseja e as outras coisas serão empurradas
print(animais)

# animais.pop() #se deixar vazio, o último elemento é removido; 
# print(animais)

# animais.pop(3) #posição para ser removida; 
# print(animais)

# animais.pop("golfinho") #remove o que vc quer; 
# print(animais)

animais += ["peixe", "ouriço", "baleira"] #adicionar uma lista dentro da lista
print(animais)

print(animais[0][0]) #primeira letra da primeira palavra

animais[2] = "abelha rainha"
print(animais)