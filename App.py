from Model import *
def main():
    Funcionario= Funcionario("maria")
    Cliente= Cliente("jose")
    Maratona= Maratona()
    Maratona.correr(Cliente)
    Maratona.correr(Funcionario)
if __name__ == '__main__':
     main()
