import sqlite3, os

def estrutura_db():
    # Tamanho do banco de dados
    tamanho_db = os.path.getsize("imdb.db")
    
    # Conexão com banco de dados
    con = sqlite3.connect("imdb.db")
    cursor = con.cursor()

    # Nome da Database 
    nome_database = cursor.execute("PRAGMA database_list").fetchall()
     
    # Nome da tabela no database imdb.db     
    nome_tabelas = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    
    # Exibir nome das colunas e tipos de todas as tabelas
    # Usando pragma_table_info em um JOIN para evitar loops em Python
    query_colunas = """
    SELECT m.name as tabela, p.name as coluna, p.type as tipo
    FROM sqlite_master m
    JOIN pragma_table_info(m.name) p
    WHERE m.type = 'table'
    """
    colunas_tipos = cursor.execute(query_colunas).fetchall()

    # Retorna os resultados
    return nome_database, nome_tabelas, colunas_tipos

# Ativar modulo
if __name__ == "__main__":
    print(estrutura_db())
    
    