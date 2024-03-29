import sqlite3
import os

PATH = os.path.abspath('data/')
PATH_DB = os.path.join(PATH, 'Empresa.db')

# Crie ou conecte ao banco de dados
conn = sqlite3.connect(PATH_DB)
cursor = conn.cursor()

# Crie a tabela de funcionários (caso ela não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        dataNascimento TEXT,
        cargo TEXT
    )
''')

for _ in range(1000):
    cursor.execute("""INSERT INTO funcionarios (nome, dataNascimento, cargo)
    VALUES
        ('João Silva', '15-04-1985', 'Gerente de Vendas'),
        ('Maria Santos', '25-08-1990', 'Analista de Marketing'),
        ('Pedro Oliveira', '10-11-1982', 'Desenvolvedor de Software'),
        ('Ana Costa', '03-06-1995', 'Assistente Administrativo'),
        ('Rafael Pereira', '18-09-1987', 'Engenheiro de Projetos'),
        ('Mariana Vieira', '21-02-1992', 'Designer Gráfico'),
        ('Carlos Santos', '07-07-1980', 'Analista Financeiro'),
        ('Patrícia Rodrigues', '12-03-1988', 'Analista de Recursos Humanos'),
        ('Lucas Gomes', '29-01-1993', 'Analista de Sistemas'),
        ('Isabela Fernandes', '14-05-1986', 'Gerente de Marketing'),
        ('Eduardo Almeida', '08-12-1979', 'Diretor de Operações'),
        ('Camila Lima', '05-10-1991', 'Analista de Qualidade'),
        ('Gustavo Pereira', '19-07-1984', 'Gerente de Produção'),
        ('Luana Oliveira', '22-09-1994', 'Engenheiro de Software'),
        ('André Costa', '01-03-1983', 'Designer de UI/UX'),
        ('Juliana Martins', '09-11-1989', 'Analista de Compras'),
        ('Fernando Sousa', '26-06-1981', 'Coordenador de RH'),
        ('Amanda Castro', '17-12-1996', 'Desenvolvedor Front-End'),
        ('Roberto Ferreira', '23-08-1978', 'Diretor Financeiro'),
        ('Larissa Ribeiro', '30-04-1987', 'Analista de TI'),
        ('Marcelo Santos', '04-02-1990', 'Gerente de Operações'),
        ('Carolina Lima', '11-10-1985', 'Analista de Marketing Digital'),
        ('Rodrigo Pereira', '20-01-1982', 'Analista de Suporte Técnico'),
        ('Vanessa Rodrigues', '28-05-1993', 'Analista de RH'),
        ('Ricardo Gomes', '02-07-1979', 'Gerente de Vendas'),
        ('Beatriz Almeida', '13-03-1994', 'Analista de Produção'),
        ('José Fernandes', '06-09-1986', 'Engenheiro de Software'),
        ('Fernanda Oliveira', '24-11-1991', 'Designer Gráfico'),
        ('Antônio Castro', '31-08-1988', 'Analista de Finanças'),
        ('Luisa Santos', '16-02-1995', 'Analista de RH'),
        ('Felipe Costa', '03-05-1980', 'Desenvolvedor Back-End'),
        ('Cláudia Ribeiro', '21-07-1984', 'Gerente de Marketing'),
        ('Giovanni Martins', '08-12-1977', 'Diretor de Recursos Humanos'),
        ('Isabela Lima', '25-10-1992', 'Analista de Vendas'),
        ('Daniel Sousa', '09-04-1983', 'Analista de Comunicação'),
        ('Tatiana Ferreira', '29-09-1996', 'Gerente de Projetos'),
        ('Bruno Rodrigues', '14-01-1981', 'Designer de UI'),
        ('Mariana Gonçalves', '10-06-1989', 'Analista de Logística'),
        ('Renato Pereira', '27-03-1986', 'Analista de TI'),
        ('Laura Ribeiro', '12-05-1990', 'Coordenador de RH'),
        ('Vinícius Silva', '05-11-1987', 'Analista de Marketing Online'),
        ('Carla Alves', '18-02-1993', 'Gerente de Produção'),
        ('Rafaela Fernandes', '01-07-1984', 'Engenheiro de Software'),
        ('Gustavo Santos', '23-09-1980', 'Analista Financeiro'),
        ('Aline Costa', '30-01-1991', 'Analista de Recursos Humanos'),
        ('José Pedro Oliveira', '07-04-1978', 'Desenvolvedor Full Stack'),
        ('Amanda Gonçalves', '22-08-1994', 'Diretor Financeiro'),
        ('Marcos Lima', '04-12-1985', 'Analista de TI'),
        ('Fernanda Sousa', '13-06-1982', 'Gerente de Vendas'),
        ('Thiago Martins', '28-10-1987', 'Analista de Marketing Digital'),
        ('Luciana Ferreira', '15-03-1993', 'Analista de Suporte Técnico'),
        ('Paulo Rodrigues', '20-09-1979', 'Coordenador de RH'),
        ('Julia Almeida', '06-01-1990', 'Analista de Compras'),
        ('André Santos', '19-05-1986', 'Diretor de Operações'),
        ('Beatriz Oliveira', '02-07-1995', 'Desenvolvedor Front-End'),
        ('Ricardo Costa', '11-11-1981', 'Analista de Vendas'),
        ('Camila Rodrigues', '26-04-1988', 'Analista de Produção'),
        ('Marcelo Fernandes', '09-08-1984', 'Gerente de Marketing'),
        ('Larissa Castro', '18-02-1992', 'Analista de Finanças'),
        ('Rodrigo Silva', '29-06-1980', 'Engenheiro de Projetos'),
        ('Carolina Almeida', '07-12-1993', 'Designer Gráfico'),
        ('Lucas Pereira', '22-03-1987', 'Analista de Logística'),
        ('Patrícia Ribeiro', '03-05-1985', 'Analista de TI'),
        ('Eduardo Lima', '14-09-1990', 'Gerente de Produção'),
        ('Vanessa Oliveira', '25-01-1981', 'Analista de Recursos Humanos'),
        ('Luiz Costa', '10-07-1979', 'Desenvolvedor')
    """)
    conn.commit()
    
conn.close()

