import dados
from classes import Show, Festa, Palestra, Feira

# def visualizar_eventos(tipo, lista):
#     classes_map = {1: Show, 2: Festa, 3: Palestra, 4: Feira}
#     classe_escolhida = classes_map.get(tipo)
#     if classe_escolhida is None:
#         print("Tipo inválido!")
#         return []
#     eventos_filtrados = [evento for evento in lista if isinstance(evento, classe_escolhida)]
#     for i, event in enumerate(eventos_filtrados):
#         print(f"{i+1}. {event.nome}")
#     return eventos_filtrados

def visualizar_eventos(lista):
    for i, event in enumerate(lista):
        print(f"{i+1}. {event.nome}")

print("     --Visualizar eventos")
tipo = input("""Digite o tipo de evento que deseja visualizar
1. Show
2. Festa
3. Palestra
4. Feira
--> """)
match tipo:
    case "1":
        visualizar_eventos(dados.shows_lista)
    case "2":
        visualizar_eventos(dados.festas_lista)
    case "3":
        visualizar_eventos(dados.palestra_lista)
    case "4":
        visualizar_eventos(dados.feiras_lista)

print("     --Realizar incrição")
indice = int(input("Digite o número do evento que deseja se inscrever: "))
indice = indice - 1

lista_escolhida = None
if tipo == "1":
    lista_escolhida = dados.shows_lista
elif tipo == "2":
    lista_escolhida = dados.festas_lista
elif tipo == "3":
    lista_escolhida = dados.palestra_lista
elif tipo == "4":
    lista_escolhida = dados.feiras_lista

print(lista_escolhida[indice])

print("     --Cancelar participação")

print("     --Registrar avaliação")
