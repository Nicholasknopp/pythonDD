nome = input("Digite com seu nome:")
idade = int(input("Digite com sua idade:"))

dadosClientes = (27.9, nome, idade)

indice = 0
while (indice < len(dadosClientes)):
    print(dadosClientes[indice])
    indice = indice + 1