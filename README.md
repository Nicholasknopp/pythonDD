# Python DD - Estudos de Python e Agenda Telefônica

Repositório com os exercícios desenvolvidos durante o curso de **Programação em Python** e o projeto final **Agenda Telefônica**, uma aplicação de terminal (CLI) para gerenciar contatos.

## Projeto Final - Agenda Telefônica

Aplicação de linha de comando que permite cadastrar, listar, buscar, editar e excluir contatos. Os dados são persistidos em um arquivo de texto (`contatos.txt`), sem necessidade de banco de dados.

### Funcionalidades
- **Adicionar contato**: nome, telefone e e-mail (opcional)
- **Listar contatos**: exibe todos os contatos com índice
- **Buscar contato**: busca por parte do nome (ignorando maiúsculas/minúsculas)
- **Editar contato**: alteração dos dados, mantendo os campos deixados em branco
- **Excluir contato**: com confirmação antes de remover
- **Persistência em arquivo**: leitura e gravação automática em `contatos.txt`

### Como Executar
1. Tenha o Python 3 instalado.
2. Execute o arquivo:

   ```
   python agenda.py
   ```

3. Utilize o menu numérico para navegar pelas opções.

## Exercícios (aulas)

A pasta raiz contém os arquivos `aula1.py` a `aula34.py`, com os exercícios práticos do curso, abordando:
- Variáveis, tipos de dados e operadores
- Estruturas condicionais e de repetição
- Listas, tuplas, dicionários e conjuntos
- Funções e modularização
- Classes e Programação Orientada a Objetos
- Manipulação de arquivos

## Estrutura do Projeto

```
pythonDD/
├── ProjetoDD.py/
│   └── agenda.py          # Projeto final - Agenda Telefônica
├── aula1.py ... aula34.py # Exercícios das aulas
└── contatos.txt           # Base de dados gerada em tempo de execução
```

## Tecnologias Utilizadas
- Python 3
- Programação Orientada a Objetos
- Manipulação de arquivos (`.txt`)

## Autor
Desenvolvido por **Nicholas Knopp Seferin da Silva**.
