# DESAFIO 1 — Sistema de animais

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Cachorro: au au")
class Gato(Animal):
    def emitir_som(self):
        print("Gato: miauuu")
class Vaca(Animal):
    def emitir_som(self):
        # Complete o som da vaca
        print("Vaca: muuuuu")

animais = [
    Cachorro(),
    Gato(),
    Vaca()
]

for animal in animais:
    animal.emitir_som()