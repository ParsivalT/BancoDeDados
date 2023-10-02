import sqlite3
from datetime import datetime

class dataBase:
    def __init__(self, dbpath: str):
        """
        Inicializa uma instância da classe dataBase e estabelece uma conexão com o banco de dados.

        Parameters:
            dbpath (str): O caminho para o arquivo do banco de dados SQLite.

        Atributos:
            online (bool): Indica se a conexão com o banco de dados foi estabelecida com sucesso.
            conn (sqlite3.Connection): Representa a conexão com o banco de dados.
            cursor (sqlite3.Cursor): Um objeto de cursor para executar consultas SQL no banco de dados.

        Exemplo de uso:
            db = dataBase("meu_banco_de_dados.db")
            if db.online:
                # A conexão foi estabelecida com sucesso, agora você pode executar consultas SQL.
                db.criar_tabela()
            else:
                print("Não foi possível conectar ao banco de dados.")
        """
        self.online = False

        try:
            # Tenta estabelecer uma conexão com o banco de dados SQLite usando o caminho fornecido.
            self.conn = sqlite3.connect(dbpath)
            self.cursor = self.conn.cursor()
            self.online = True

        except sqlite3.Error as e:
            # Se ocorrer um erro durante a conexão, imprime uma mensagem de erro.
            print(f"Não foi possível se conectar ao banco: {e}")

    @property
    def criar_tabela(self):
        """
        Cria a tabela 'Funcionarios' no banco de dados, se ela não existir.

        Exemplo de uso:
            db = dataBase("meu_banco_de_dados.db")
            if db.online:
                db.criar_tabela
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Funcionarios (
                    id INTEGER PRIMARY KEY,
                    nome VARCHAR(60) NOT NULL,
                    dataNascimento DATE NOT NULL,
                    cargo VARCHAR(30) NOT NULL
                )''')
            self.conn.commit()
            print("Tabela 'Funcionarios' criada com sucesso.")

        except sqlite3.Error as e:
            print(f"Não foi possível criar a tabela: {e}")

    def verifica_data_nascimento(self, data:str):
        """
        Valida a Data de Nascimento inserida.

        Parameters:
            data (str): Data de nascimento no formato 'dd-mm-yyyy'.

        Returns:
            bool: True se a data estiver no formato correto, False caso contrário.
        """
        formato = '%d-%m-%Y'
        try:
            datetime.strptime(data, formato)
            return True

        except ValueError:
            return False

    def inserir_valor(self, nome:str, data:str, cargo:str):
        """
        Insere valores na tabela 'Funcionarios' do banco de dados.

        Parameters:
            nome (str): Nome do funcionário.
            data (str): Data de nascimento no formato 'dd-mm-yyyy'.
            cargo (str): Cargo do funcionário.

        Returns:
            bool: True se a inserção for bem-sucedida, False em caso de erro.
        """
        if nome == '' or data == '' or cargo == '' or not self.verifica_data_nascimento(data):
            print("Erro! Dados inseridos vazios ou formato de data inválido!")
            return False

    @property
    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.

        Exemplo de uso:
            db = dataBase("meu_banco_de_dados.db")
            if db.online:
                # Realize operações no banco de dados aqui
                db.fechar_conexao
        """
        try:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")

        except sqlite3.Error as e:
            print(f"Erro ao fechar a conexão: {e}")
