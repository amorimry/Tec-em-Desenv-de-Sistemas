# PetMatch: Sistema para Encontros entre Pets

import classe

def mostrar_animais(lista):
    for i, animal in enumerate(lista):
        print(f"{i+1}. {animal.nome}")

def mostrar_encontros(lista):
    for i, encont in enumerate(lista):
            print(f"{i+1}. {encont.nome}")

tutores_lista = []
animais_lista = [
    classe.Cachorro("Rex", 3, "Vira-lata"),
    classe.Gato("Whiskas", 2, "Persa"),
    classe.Cachorro("Mel", 5, "Poodle")
]
encontros_lista = []

print("Cadastrar Tutor")
nome = input("Digite o nome do tutor: ")
idade = int(input("Digite a idade do tutor: "))

novo_tutor = classe.Tutor(nome, idade)
tutores_lista.append(novo_tutor)

print(tutores_lista)

print("Cadastrar Animal")
escolha = print(f"""Qual animal deseja cadastrar?
1. Cachorro
2. Gato
3. Coelho
""")
match escolha:
    case "1":
        pass
    case "2":
        pass
    case "3":
        pass
    case _:
        print("Opção inválida.")

print("Inscrever animais em encontros")
mostrar_animais(animais_lista)
escolha = int(input("Digite o número do animal que deseja inscrever em um encontro: "))
indice = escolha - 1


# print("Cancelar inscrição")


# print("Informações dos animais cadastrados")
mostrar_animais(animais_lista)