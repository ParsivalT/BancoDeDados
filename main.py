from package.database import Database

dados = {'nome': 'Thiago',
         'cargo': 'Gerente',
         'data': '24-02-2092'}

if __name__ == '__main__':
    db = Database(dbpath="Empresa.db") 
    novo_id = db.inserir_valor(**dados)
    if novo_id > 0:
        print(f"novo id inserido com sucesso: {novo_id}")
    db.fechar_conexao()