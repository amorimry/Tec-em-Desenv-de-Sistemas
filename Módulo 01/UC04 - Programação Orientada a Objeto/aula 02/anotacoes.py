# Programação Orientada à Objetos (POO)

# iniciamos com o uso do dict, mas não tinha tanta mobilidade, como as validações que eram feitas de forma externa
# verificamos tudo na "classe", que é uma config que dis como funciona meu dict aluno, por exemplo
# a ideia é centralizar o armazenamento e a lógica dos dados, fazendo mais coisa com pouco código e verificando mais coisas tbm

# vamos organizar do modo MVC, uma forma de organizar melhor o código / Model View Control

# o código onde vai estar o projeto fica salvo, no python, como main, esse nome é meio que um modelo padrão, mas n é necessário
    # utils, main, class, connectDB...

# para criar uma classe:

# class NomeDaClasse(): # criando a entidade que representa o NomeDaClasse
#     def __init__(self, parâmetro):  /contrução/
#         self.atributo = parâmetro

# NomeDaClasse (começando em letra maiúscula, sem _)
# o init já vem como padrão, e o selft tem que deixar e junto com ele os parâmetros
# esse selft é uma maneira de se referir ao objeto que estou trabalhando, uma auto referência, mostrar que estou trabalhando com um dos objetos que escolhi

# aluno1.verMedia()
# aqui o selft vai virar, por atrás dos panos, o aluno1, isso no python, em outras linguagens é outro nome

# método é o nome da função que fica dentro de uma class
    # upper, apend.. tudo é método