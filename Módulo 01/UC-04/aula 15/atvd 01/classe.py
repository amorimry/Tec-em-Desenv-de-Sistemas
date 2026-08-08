from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade, raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça

    @abstractmethod
    def cadastrar_animal(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raça})"

    def __str__(self):
        return f"Nome do animal: {self.nome} | Idade do animal: {self.idade} | Raça do animal: {self.raça}"

class Cachorro(Animal):
    animal = "Cachorro"

    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade, raça)

    def cadastrar_animal(self, nome, idade, raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça
        print(f"{self.animal}\nAnimal '{self.nome}', da raça '{self.raça}', cadastrado com sucesso.")

class Gato(Animal):
    animal = "Gato"

    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade, raça)

    def cadastrar_animal(self, nome, idade, raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça
        print(f"{self.animal}\nAnimal '{self.nome}', da raça '{self.raça}', cadastrado com sucesso.")

class Coelho(Animal):
    animal = "Coelho"

    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade, raça)

    def cadastrar_animal(self, nome, idade, raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça
        print(f"{self.animal}\nAnimal '{self.nome}', da raça '{self.raça}', cadastrado com sucesso.")

class Tutor():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Tutor(Nome: {self.nome}, Idade: {self.idade})"

    def __str__(self):
        return f"Tutor: {self.nome} | Idade: {self.idade}"
        
    def cadastrar_tutor(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Tutor '{self.nome}' cadastrado com sucesso.")
        return {self.nome, self.idade}