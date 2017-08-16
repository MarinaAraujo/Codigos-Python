class Pessoa:
    def __init__(self, nome):
        self.nome= nome

    def falar(self):
        print("fala de forma generica")
    def andar (self):
        print("anda de forma generica")
    def pagar (self):
        print("paga de forma generica")


class Cliente(Pessoa):
    def __init__(self, nome):
        Super(Cliente, self).__init__(nome)
    def pagar (self):
        print("pagando como cliente")

class Funcionario:
    def __init__(self, nome):
          Super(Funcionario, self).__init__(nome)


class Maratona():
    def correr(self, pessoa):
        pessoa.andar()
        passoa.pagar()

