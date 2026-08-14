# DESAFIO 6 — Sistema de notificações

from abc import ABC, abstractmethod

class Notificacao(ABC):

    @abstractmethod
    def enviar(self, mensagem):
        pass

class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"E-mail enviado: {mensagem}")
class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")
class WhatsApp(Notificacao):
    def enviar(self, mensagem):
        print(f"WhatsApp enviado: {mensagem}")

notificacoes = [
    Email(),
    SMS(),
    WhatsApp()
]
for notificacao in notificacoes:
    notificacao.enviar("Seu pedido foi aprovado.")