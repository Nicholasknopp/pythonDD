class Contato:
    def __init__(self, nome, telefone, email=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def formatar_para_arquivo(self):
        return self.nome + "|" + self.telefone + "|" + self.email + "\n"

    def exibir(self):
        print("Nome: " + self.nome)
        print("Telefone: " + self.telefone)
        if self.email != "":
            print("Email: " + self.email)
        print("-" * 30)


def criar_arquivo():
    arquivo = open("contatos.txt", "w")
    arquivo.close()


def adicionar_contato():
    print("\n--- Adicionar Contato ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email (opcional): ")

    contato = Contato(nome, telefone, email)

    arquivo = open("contatos.txt", "a")
    arquivo.write(contato.formatar_para_arquivo())
    arquivo.close()

    print("\nContato adicionado com sucesso!")


def ler_contatos():
    contatos = []
    try:
        arquivo = open("contatos.txt", "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip()
            if linha != "":
                partes = linha.split("|")
                if len(partes) == 3:
                    contato = Contato(partes[0], partes[1], partes[2])
                    contatos.append(contato)
                elif len(partes) == 2:
                    contato = Contato(partes[0], partes[1])
                    contatos.append(contato)
        arquivo.close()
    except FileNotFoundError:
        criar_arquivo()
    return contatos


def listar_contatos():
    print("\n--- Lista de Contatos ---")
    contatos = ler_contatos()
    if len(contatos) == 0:
        print("Nenhum contato cadastrado.")
    else:
        for i in range(len(contatos)):
            print("Índice: " + str(i))
            contatos[i].exibir()


def buscar_contato():
    print("\n--- Buscar Contato ---")
    nome_busca = input("Digite o nome para buscar: ").lower()
    contatos = ler_contatos()
    encontrados = []

    for contato in contatos:
        if nome_busca in contato.nome.lower():
            encontrados.append(contato)

    if len(encontrados) == 0:
        print("Nenhum contato encontrado.")
    else:
        print("\nContatos encontrados:")
        for contato in encontrados:
            contato.exibir()


def salvar_contatos(contatos):
    arquivo = open("contatos.txt", "w")
    for contato in contatos:
        arquivo.write(contato.formatar_para_arquivo())
    arquivo.close()


def editar_contato():
    print("\n--- Editar Contato ---")
    listar_contatos()
    contatos = ler_contatos()

    if len(contatos) == 0:
        return

    indice = int(input("Digite o índice do contato que deseja editar: "))

    if indice < 0 or indice >= len(contatos):
        print("Índice inválido!")
        return

    print("\nDados atuais:")
    contatos[indice].exibir()

    print("\nDigite os novos dados (pressione Enter para manter o atual):")
    novo_nome = input("Nome (" + contatos[indice].nome + "): ")
    novo_telefone = input("Telefone (" + contatos[indice].telefone + "): ")
    novo_email = input("Email (" + contatos[indice].email + "): ")

    if novo_nome != "":
        contatos[indice].nome = novo_nome
    if novo_telefone != "":
        contatos[indice].telefone = novo_telefone
    if novo_email != "":
        contatos[indice].email = novo_email

    salvar_contatos(contatos)
    print("\nContato editado com sucesso!")


def excluir_contato():
    print("\n--- Excluir Contato ---")
    listar_contatos()
    contatos = ler_contatos()

    if len(contatos) == 0:
        return

    indice = int(input("Digite o índice do contato que deseja excluir: "))

    if indice < 0 or indice >= len(contatos):
        print("Índice inválido!")
        return

    print("\nContato a ser excluído:")
    contatos[indice].exibir()

    confirmacao = input("Tem certeza que deseja excluir? (S/N): ").upper()

    if confirmacao == "S":
        contatos.pop(indice)
        salvar_contatos(contatos)
        print("\nContato excluído com sucesso!")
    else:
        print("\nOperação cancelada.")


def menu():
    try:
        arquivo = open("contatos.txt", "r")
        arquivo.close()
    except FileNotFoundError:
        criar_arquivo()

    while True:
        print("\n" + "=" * 30)
        print("      AGENDA TELEFÔNICA")
        print("=" * 30)
        print("1 - Adicionar contato")
        print("2 - Listar todos os contatos")
        print("3 - Buscar contato")
        print("4 - Editar contato")
        print("5 - Excluir contato")
        print("0 - Sair")
        print("=" * 30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            editar_contato()
        elif opcao == "5":
            excluir_contato()
        elif opcao == "0":
            print("\nSaindo da agenda... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


menu()
