# Script para verificar a quantidade de registros no banco IMDB
import sqlite3

def verificar_quantidade_registros():
    """Verifica quantos registros existem no banco de dados"""
    
    try:
        # Conectar ao banco
        conexao = sqlite3.connect("imdb.db")
        cursor = conexao.cursor()
        
        # Buscar todas as tabelas
        tabelas = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        
        print("Informacoes do Banco de Dados IMDB\n")
        print("=" * 60)
        
        for tabela in tabelas:
            nome_tabela = tabela[0]
            
            # Contar registros
            count = cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}").fetchone()[0]
            
            # Pegar nomes das colunas
            colunas = cursor.execute(f"PRAGMA table_info({nome_tabela})").fetchall()
            num_colunas = len(colunas)
            
            print(f"\nTabela: {nome_tabela}")
            print(f"   Total de registros: {count:,}")
            print(f"   Total de colunas: {num_colunas}")
            print(f"   Estimativa de tempo: ~{int(count/100 * 30)} segundos")
            
        print("\n" + "=" * 60)
        print("\nDica: Ajuste o timeout do Insomnia para pelo menos 5 minutos")
        print("   (Preferences -> Request -> Request timeout -> 300000ms)\n")
        
        conexao.close()
        
    except Exception as erro:
        print(f"Erro: {erro}")

if __name__ == "__main__":
    verificar_quantidade_registros()
