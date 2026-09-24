#Herança é um mecanismo que a orientação a objetos permite provê, com objetivo de facilitar o reaproveitamento de código. A ideia é que as classes sejam construídad formando uma hierarquia de classes.
#Uma classe pode herdar de outra, e esta pode herdar de outra, e assim por diante.

class pessoa:
    cidade = "Padrão"
    carro = "Padrão"
    moto = "Padrão"

    def estado(self):
        self.estado = (int(input("Digite com um numero: ")))

class homem(pessoa):
    nome = "Padrão"
    sexo = "M"
    corCabelo = "Padrão"

class mulher(pessoa):
    nome = "Padrão"
    sexo = "F"
    corCabelo = "Padrão"

    Nicholas = homem()
    Nicholas.estado()
    print(Nicholas.estado)

