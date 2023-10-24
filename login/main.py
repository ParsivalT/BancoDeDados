# Importando a biblioteca bcrypt para geração de hashes a partir de senhas informadas pelos usuários.
import bcrypt
# Importando a biblioteca sqlite3 para trabalhar com o banco de dados SQLite.
import sqlite3
# Importando a função getpass para receber senhas do usuário sem exibi-las na tela.
import getpass
# Importando a função system do módulo os para limpar a tela.
from os import system


# Conectando-se ao Banco de Dados SQLite.
CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

# Codigo de apoio para criar a tabela
CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario VARCHAR(60) NOT NULL UNIQUE,
        senha VARCHAR(60) NOT NULL,
        salt VARCHAR(60) NOT NULL
)
""")

# Definindo uma função para cadastrar um novo usuário.
def cadastrar_usuario() -> None:
    print("------CADASTRANDO NOVO USUARIO------")

    # Capturando a entrada do usuário para nome e senha.
    nome:str = input("Insira seu nome: ")
    senha:str = input("Insira sua senha: ")

    # Gerando um salt aleatório junto com um hash para a senha.

    """
    Salt é uma sequência de dados aleatórios que é gerada e usada em conjunto 
    com uma senha antes de calcular seu hash.
    """
    salt:bytes = bcrypt.gensalt(rounds=12)
    senha_hash:bytes = bcrypt.hashpw(password=senha.encode("utf-8"), salt=salt)

    # Salvando os dados no banco de dados.
    CURSOR.execute("""INSERT INTO Usuarios (usuario, senha, salt) VALUES (?, ?, ?)""", (nome, senha_hash, salt))
    CONN.commit()

    print(f"Usuário {nome} cadastrado com sucesso!")

# Verificando se o usuário é válido.
def verifica_usuario(usuario, senha):
    CURSOR.execute("SELECT senha, salt FROM Usuarios WHERE usuario = ?", (usuario, ))
    resultado = CURSOR.fetchone()

    if resultado:
        hash_armazenado:str = resultado[0]
        salt:str = resultado[1]

        hash_inserido: bytes = bcrypt.hashpw(password=senha.encode("utf-8"), salt=salt)

        if hash_armazenado == hash_inserido:
            return True

    return False

# Definindo uma função para o menu principal.
def menu():
    # TODO: Criar o menu.
    ...

if __name__ == "__main__":
    menu()  # Inicia o menu quando o programa é executado diretamente.
