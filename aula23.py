#Tupla utiliza parenteses e listas usa colchetes
lista = ["Daniel", "Leticia", "Maria", "Paulo"]
lista2 = ["10", "20", "50", "60", "30", "40", "70", "80"]
print(lista)
print(lista[0])
print(lista[1:3])
print(lista[2:])
print(lista[2:4])

listaSoma = lista + lista2
for elemento in listaSoma:
    print(elemento)

listaSoma = lista + lista2
if "Daniel" in listaSoma:
    print("sim")
else:
    print("nao")

listaSoma = lista + lista2
if "João" in listaSoma:
    print("sim")
else:
    print("nao")

listaNmeros = [1, 100]
for elemento2 in listaNmeros:
    print(elemento2)