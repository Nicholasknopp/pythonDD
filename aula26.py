#HELP - O que é help() faz é apenas exibir para você a docstring do objeto passado como argumento.
tupla = (2, 5, 8, 9, 3, 6, 5)
help(tupla)

#DIR - A função dir() retorna em uma lista todos os atributos e métodos daquela instanciância, e isso vale também para classes.
tupla2 = (2, 5, 8, 9, 3, 6, 5)
print(dir(tupla2))

#TYPE - Retorna o tipo que é a variavel
tupla3 = (5, 6, 5, 8, 6, 6, 6, 6)
print(type(tupla3))

def tupla4():
    print(" ")
print(type(tupla4))

#STR - Converte em qualquer variavel em uma string
numero = 5
print(type(str(numero)))

#INT - Converte variaveis recebidas em inteiro
numero = 6.9
print(int(numero))
print(type(int(numero)))
