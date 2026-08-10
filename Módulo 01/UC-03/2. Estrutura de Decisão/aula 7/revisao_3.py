# 3. Crie um programa que pede o nome de uma fruta e imprime uma mensagem específica para cada fruta. Crie mensagens para 5 frutas à sua escolha e exiba somente a mensagem da fruta correta quando o programa for executado.

fruta = input("Digite o nome de uma fruta: ")
match fruta:
    case "Banana"|"banana":
        print ("Essa fruta é amarela.")
    case "Limão"|"limão":
        print ("Essa fruta é verde.")
    case "Uva"|"uva":
        print ("Essa fruta é roxa.")
    case "Maça"|"maça":
        print ("Essa fruta é vermelha.")
    case _:
        print ("Fruta não catalogada.")

fruta = input("Digite o nome de uma fruta: ")
if fruta == "Banana" or "banana":
    print ("Essa fruta é amarela.")
elif fruta == "Limão" or "limão":
    print ("Essa fruta é verde.")
elif fruta == "Uva" or "uva":
    print ("Essa fruta é roxa.")
elif fruta == "Maça" or "maça":
    print ("Essa fruta é vermelha.")
else:
    print ("Fruta não catalogada.")