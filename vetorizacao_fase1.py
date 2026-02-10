# Arquivo responsável pela vetorização do banco de dados IMDB
import sqlite3
import chromadb
from sentence_transformers import SentenceTransformer

def vetorizar_banco():
    """
    Função que realiza a vetorização dos dados do banco IMDB.
    
    Passos:
    1. Conecta ao banco SQLite (imdb.db)
    2. Busca os dados da tabela
    3. Transforma os textos em vetores usando SentenceTransformer
    4. Armazena os vetores no ChromaDB
    
    Retorna: Mensagem de sucesso ou erro
    """
    
    try:
        # PASSO 1: Conectar ao banco de dados SQLite
        print("📂 Conectando ao banco de dados...")
        conexao = sqlite3.connect("imdb.db")
        cursor = conexao.cursor()
        
        # PASSO 2: Buscar dados da tabela (ajuste o nome da tabela conforme necessário)
        print("📊 Buscando dados da tabela...")
        # Primeiro, vamos descobrir qual tabela existe
        tabelas = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        
        if not tabelas:
            return {"erro": "Nenhuma tabela encontrada no banco de dados"}
        
        # Pega a primeira tabela (você pode ajustar isso depois)
        nome_tabela = tabelas[0][0]
        print(f"✅ Tabela encontrada: {nome_tabela}")
        
        # Busca todos os dados da tabela
        dados = cursor.execute(f"SELECT * FROM {nome_tabela}").fetchall()
        
        # Pega os nomes das colunas
        colunas = [descricao[0] for descricao in cursor.description]
        print(f"📋 Colunas: {colunas}")
        print(f"📈 Total de registros a vetorizar: {len(dados)}")
        
        # PASSO 3: Preparar o modelo de vetorização
        print("🤖 Carregando modelo de vetorização...")
        modelo = SentenceTransformer('all-MiniLM-L6-v2')
        
        # PASSO 4: Conectar ao ChromaDB com persistência em arquivo
        print("💾 Conectando ao ChromaDB (modo persistente)...")
        cliente_chroma = chromadb.PersistentClient(path="./chroma_db")
        
        # Criar ou obter a coleção (onde os vetores serão armazenados)
        colecao = cliente_chroma.get_or_create_collection(name="imdb_vetores")
        
        # Verificar se já existem vetores na coleção
        count_existente = colecao.count()
        if count_existente > 0:
            print(f"⚠️  Atenção: Já existem {count_existente} vetores na coleção.")
            print("   Deletando vetores antigos para re-vetorizar...")
            cliente_chroma.delete_collection(name="imdb_vetores")
            colecao = cliente_chroma.get_or_create_collection(name="imdb_vetores")
            print("✅ Coleção limpa e pronta para nova vetorização!")
        
        # PASSO 5: Vetorizar e armazenar os dados
        print("⚙️ Iniciando vetorização...")
        documentos = []
        metadados = []
        ids = []
        
        for indice, linha in enumerate(dados):
            # Combina todos os campos da linha em um texto único
            texto = " ".join([str(campo) for campo in linha if campo])
            documentos.append(texto)
            
            # Cria metadados com informações da linha
            metadata = {}
            for i, coluna in enumerate(colunas):
                if i < len(linha):
                    metadata[coluna] = str(linha[i])
            metadados.append(metadata)
            
            # Cria um ID único para cada documento
            ids.append(f"doc_{indice}")
        
        # Adiciona os documentos à coleção do ChromaDB
        # O ChromaDB automaticamente vetoriza usando o modelo padrão
        # Mas vamos usar nosso modelo SentenceTransformer
        embeddings = modelo.encode(documentos).tolist()
        
        colecao.add(
            embeddings=embeddings,
            documents=documentos,
            metadatas=metadados,
            ids=ids
        )
        
        # PASSO 6: Fechar conexão com o banco
        conexao.close()
        
        print("✅ Vetorização concluída com sucesso!")
        
        return {
            "status": "sucesso",
            "mensagem": "Vetorização concluída com sucesso!",
            "tabela_vetorizada": nome_tabela,
            "total_documentos": len(dados),
            "colunas": colunas,
            "modelo_usado": "all-MiniLM-L6-v2"
        }
        
    except Exception as erro:
        print(f"❌ Erro durante a vetorização: {erro}")
        return {
            "status": "erro",
            "mensagem": f"Erro durante a vetorização: {str(erro)}"
        }


# Teste local (apenas para desenvolvimento)
if __name__ == "__main__":
    resultado = vetorizar_banco()
    print("\n📊 Resultado:")
    print(resultado)
