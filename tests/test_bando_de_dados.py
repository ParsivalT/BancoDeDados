# test_database.py
import sqlite3
import pytest
from package.database import dataBase

# Fixture para criar uma instância do banco de dados em memória
@pytest.fixture
def memory_db():
    db = dataBase(dbpath=':memory:')
    db.criar_tabela()
    
    yield db
    db.conn.close()

# Teste para verificar a criação da tabela
def test_create_table(memory_db):
    memory_db.criar_tabela()
    assert 'Funcionarios' in memory_db.conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()[0]

# Teste para verificar a validação de data de nascimento
def test_verify_date_format():
    db = dataBase(dbpath=':memory:')
    assert db.verifica_data_nascimento('31-12-2000') == True
    assert db.verifica_data_nascimento('12/31/2000') == False

# Teste para inserir valores na tabela

def test_insert_values(memory_db):
    assert memory_db.inserir_valor('João','31-12-2000', 'Analista') == True
    assert memory_db.inserir_valor('', '31-12-2000', 'Analista') == False
    assert memory_db.inserir_valor('Maria', '31/12/2000', 'Analista') == False

# Teste para verificar o fechamento da conexão
def test_close_connection(memory_db):
    memory_db.fechar_conexao()
    with pytest.raises(sqlite3.ProgrammingError):
        memory_db.conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

if __name__ == '__main__':
    pytest.main()
