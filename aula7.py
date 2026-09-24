# AND  Verdade se ambas as variáveis forem verdadeiras.
idade = 18

if (idade >=18 and idade <= 20):
    print("Verdade.")
else:
    print("Falso.")


if (idade >=18 and idade == 20):
    print("Verdade.")
else:
    print("Falso.")


if (idade ==18 and idade == 20):
    print("Verdade.")
else:
    print("Falso.")

# OR Verdade se pelo menos uma das variáveis forem verdadeiras.
if (idade >=18 or idade == 20):
    print("O carro está funcionando,então vou usar o carro.")
else:
    print("O carro NÃO está funcionando,então vou andar a pé.")

# NOT Verdade se a variável for falsa.
if (not (idade >= 18 and idade <= 20)):
    print("Verdade!")
else:
    print("Falso!")