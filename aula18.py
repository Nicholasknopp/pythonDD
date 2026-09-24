def soma (n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao (n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicacao (n1, n2):
    resultado = n1 * n2
    return resultado

def divisao (n1, n2):
    resultado = n1 / n2
    return resultado 

print("Seja Bem Vindo ao Programa da Calculadora")

control = True
while (control == True):
    n1 = float(input("Digite o primeiro número:"))
    n2 = float(input("Digite o segundo número:"))

    print("Selecione a operação desejada:")
    operador = int(input("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\nReposta:"))

    if operador == 1:
        resultado = soma(n1, n2)
        print("O resultado da soma é:", resultado)
    elif operador == 2:
        resultado = subtracao(n1, n2)
        print("O resultado da subtração é:", resultado)
    elif operador == 3:
        resultado = multiplicacao(n1, n2)
        print("O resultado da multiplicação é:", resultado)
    elif operador == 4:
        resultado = divisao(n1, n2)
        print("O resultado da divisão é:", resultado)       
    else:
        print("Operação inválida")

    control = input("Deseja continuar? (s/n)")
    if control == "s":
        control = True
    else:
        control = False
        print("Programa encerrado")
