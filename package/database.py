import sqlite3
from datetime import datetime

class Database:
    def __init__(self, dbpath: str):
        """
        Inicializa uma instância da classe Database e estabelece uma conexão com o banco de dados.

        Parameters:
            dbpath (str): O caminho para o arquivo do banco de dados SQLite.
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

    def criar_tabela(self):
        """
        Cria a tabela 'Funcionarios' no banco de dados, se ela não existir.
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Funcionarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    dataNascimento DATE NOT NULL,
                    cargo TEXT NOT NULL
                )''')
            self.conn.commit()
            print("Tabela 'Funcionarios' criada com sucesso.")

        except sqlite3.Error as e:
            print(f"Não foi possível criar a tabela: {e}")

    @staticmethod
    def _verifica_data_nascimento(data: str) -> bool:
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

    def inserir_valor(self, nome: str, data: str, cargo: str) -> int:
        """
        Insere valores na tabela 'Funcionários' do banco de dados e retorna o ID gerado.

        Parameters:
            nome (str): Nome do funcionário.
            data (str): Data de nascimento no formato 'dd-mm-yyyy'.
            cargo (str): Cargo do funcionário.

        Returns:
            int: O ID gerado para o novo registro inserido, ou -1 em caso de erro.
        """
        # Verifica se os campos obrigatórios estão vazios
        if not nome or not data or not cargo:
            print("Erro! Dados inseridos vazios!")
            return -1

        # Verifica o formato da data de nascimento
        if not self._verifica_data_nascimento(data):
            print("Erro! Formato de data de nascimento inválido!")
            return -1

        # Verifica se a data de nascimento é uma data válida
        try:
            dia, mes, ano = map(int, data.split('-'))
            datetime(ano, mes, dia)

        except ValueError:
            print("Erro! Data de nascimento inválida!")
            return -1

        try:
            self.cursor.execute("""
                INSERT INTO Funcionarios (nome, dataNascimento, cargo)
                VALUES (?, ?, ?)""", (nome, data, cargo))
            self.conn.commit()

            return self.cursor.lastrowid  # Retorna o ID gerado

        except sqlite3.Error as e:
            print(f"Falha ao inserir novos valores no banco: {e}")
            return -1

    def atualizar_valor(self, id: int, coluna: str, valor: str):
        """
        Atualiza valores na tabela 'Funcionários' do banco de dados.

        Parameters:
            id (int): O ID do registro a ser atualizado.
            coluna (str): O nome da coluna a ser atualizada.
            valor (str): O novo valor a ser definido para a coluna.
        """
        try:
            self.cursor.execute(f"""
                UPDATE Funcionarios SET {coluna} = ? WHERE id = ?
            """, (valor, id))
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Houve um problema ao tentar atualizar o valor: {e}")

    def mostrar_registro(self, id:int) -> tuple:
        """
        Recupera...

        Returns:
            list:.
        """
        try:
            self.cursor.execute("""SELECT * FROM Funcionarios WHERE id = ?""", (id))
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Erro ao acessar a base de dados: {e}")

    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.
        """
        try:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")

        except sqlite3.Error as e:
            print(f"Erro ao fechar a conexão: {e}")
