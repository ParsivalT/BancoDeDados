from crud.database import Database
from utils import aniLoad, Sistema
import os


SISTEMA = Sistema()

def main():
    os.system('clear || cls')

    # Inciando a conexão com o banco.
    aniLoad(value="Conectando-se ao Banco de dados", time=2)
    SISTEMA.conectar(dbpath='./database/Empresa.db')
    SISTEMA.menu()
    
if __name__ == '__main__':
    main()