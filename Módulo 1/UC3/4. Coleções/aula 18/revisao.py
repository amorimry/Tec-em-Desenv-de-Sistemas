perfil = ["Ryan", 22, True, ["Pedro", "Áurea", "Ingrid"], "Aluno"]

#mostrando
print(perfil[0]) #Ryan
print(perfil[0][0]) #R
print(perfil[3][2]) #Ingrid
print(perfil[3][2][5]) #d

#adicionando
perfil.append("Desen. de Sistemas")
# perfil = ["Ryan", 22, True, ["Pedro", "Áurea", "Ingrid"], "Aluno", "Desen. de Sistemas"]
print(perfil[5]) #Desen. de Sistemas

#modificando
perfil[1] = 30
perfil[2] = False
# perfil = ["Ryan", 30, False, ["Pedro", "Áurea", "Ingrid"], "Aluno", "Desen. de Sistemas"]
print(perfil)

#removendo
perfil.pop(5) #remove o "Desen. de Sistemas"
# perfil = ["Ryan", 30, False, ["Pedro", "Áurea", "Ingrid"], "Aluno"]
print(perfil)

perfil.remove(30) #vai procurar e remover o que foi anotado
# perfil = ["Ryan", False, ["Pedro", "Áurea", "Ingrid"], "Aluno"]
print(perfil)