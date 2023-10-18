import bcrypt
import sqlite3
import getpass
from  os import system

# Conectando-se ao Banco de Dados
CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

# Codigo de apoio para criar a tabela
'''cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario VARCHAR(60) NOT NULL UNIQUE,
        senha VARCHAR(60) NOT NULL,
        salt VARCHAR(60) NOT NULL
)
""")'''

def cadastrar_usuario() -> None:
    print("------CADASTRANDO NOVO USUARIO------")

    # Capturando a entrada do Usuario.
    nome:str = input("Insira seu nome: ")
    senha:str = input("Insira sua senha: ")

    # Gerando um salt aleatorio junto de um hash para a senha.
    salt:bytes = bcrypt.gensalt(rounds=12)
    senha_hash:bytes = bcrypt.hashpw(password=senha.encode("utf-8"), salt=salt)

    # Salvando os dados no banco.
    CURSOR.execute("""INSERT INTO Usuarios (usuario, senha, salt) VALUES (?, ?, ?)""", (nome, senha_hash, salt))
    CONN.commit()

    print(f"Usuario {nome} cadastrado com sucesso!")

    
# Verifica se o usuario é valido.
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


def menu():
    opc:str = ''
    while True:
        system("clear || cls")
        print("Insira seu usuario e sua senha")
        user:str = input("Usuario: ")
        senha:str = getpass.getpass("Senha: ")

        if verifica_usuario(user, senha):
            system("clear || cls")
            print("Usuario Valido!")

            input("\n\nDigite ENTER para continuar")

        else:
            system("clear || cls")
            print("Usuario invalido")

            input("\n\nDigite ENTER para continuar")


if __name__ == "__main__":
    menu()