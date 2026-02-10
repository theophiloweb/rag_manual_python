# Script para consultar os vetores armazenados no ChromaDB
import chromadb

def consultar_vetores():
    """Consulta informações sobre os vetores armazenados"""
    
    try:
        # Conectar ao ChromaDB persistente
        print("Conectando ao ChromaDB...")
        cliente = chromadb.PersistentClient(path="./chroma_db")
        
        # Listar todas as coleções
        colecoes = cliente.list_collections()
        
        print("\n" + "=" * 60)
        print("INFORMACOES DOS VETORES ARMAZENADOS")
        print("=" * 60)
        
        if not colecoes:
            print("\nNenhuma colecao encontrada!")
            print("Execute o endpoint /fase_1 para criar os vetores.\n")
            return
        
        for colecao in colecoes:
            print(f"\nColecao: {colecao.name}")
            print(f"   Total de vetores: {colecao.count()}")
            
            # Pegar um exemplo de vetor
            if colecao.count() > 0:
                resultado = colecao.get(limit=1, include=['documents', 'metadatas'])
                
                if resultado['documents']:
                    print(f"\n   Exemplo de documento:")
                    doc = resultado['documents'][0]
                    print(f"   {doc[:200]}..." if len(doc) > 200 else f"   {doc}")
                    
                if resultado['metadatas']:
                    print(f"\n   Metadados disponiveis:")
                    metadata = resultado['metadatas'][0]
                    for chave in list(metadata.keys())[:5]:  # Mostra apenas 5 primeiras chaves
                        print(f"      - {chave}: {metadata[chave][:50] if len(str(metadata[chave])) > 50 else metadata[chave]}")
        
        print("\n" + "=" * 60)
        print(f"\nLocal de armazenamento: ./chroma_db")
        print("Os vetores estao salvos em arquivo e podem ser reutilizados!\n")
        
    except Exception as erro:
        print(f"\nErro ao consultar vetores: {erro}")
        print("Certifique-se de que a vetorizacao foi executada.\n")

if __name__ == "__main__":
    consultar_vetores()
