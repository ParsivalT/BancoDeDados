from crud.database import Database
from utils import aniLoad, Sistema
import os

SISTEMA = Sistema()
PATH = os.path.abspath('data/')
PATH_DB = os.path.join(PATH, 'Empresa.db')


def main():
    os.system('clear || cls')

   # Inciando a conexão com o banco.
    aniLoad(value="Conectando-se ao Banco de dados", time=2)
    SISTEMA.conectar(dbpath=PATH_DB)
    SISTEMA.menu()

if __name__ == '__main__':
    main()