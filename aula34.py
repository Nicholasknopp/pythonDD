def criarArquivo():
    arquivo = open("arquivo.txt", "w")
    arquivo.close()

def escreveArquivo():
    nome = input("Digite o seu nome: ")
    
    arquivo = open("arquivo.txt", "a")
    arquivo.write(nome)
    arquivo.write("\n(00)000000-0000\n")
    arquivo.close()

def lerArquivo():
    arquivo = open("arquivo.txt", "r")
    line = arquivo.readlines()
    
    while line != "":
        print(line)
        line = arquivo.readline()
    arquivo.close()
#criarArquivo()
escreveArquivo()
lerArquivo()
    
    