# Arquivo responsável pela Fase 2: RAG (Retrieval-Augmented Generation)
import chromadb
from sentence_transformers import SentenceTransformer
from genai_api import client

def processar_pergunta_rag(pergunta, contexto_adicional="", top_k=5):
    """
    Função que implementa o fluxo completo de RAG:
    1. RETRIEVAL: Busca semântica no banco vetorial
    2. AUGMENTED: Incrementa a pergunta com contexto recuperado
    3. GENERATION: Envia para a LLM e gera resposta
    
    Args:
        pergunta (str): Pergunta do usuário
        contexto_adicional (str): Contexto adicional opcional do usuário
        top_k (int): Número de resultados a recuperar do banco vetorial
        
    Retorna: Dicionário com a resposta e metadados
    """
    
    # Validar se a pergunta foi enviada
    if not pergunta or pergunta.strip() == "":
        return {
            "status": "erro",
            "mensagem": "Por favor, envie uma pergunta no campo 'pergunta'",
            "detalhes": "A pergunta não pode estar vazia"
        }
    
    try:
        # ========== ETAPA 1: RETRIEVAL (Recuperação) ==========
        print("🔍 Iniciando busca semântica no banco vetorial...")
        
        # Carregar o modelo de vetorização (mesmo usado na Fase 1)
        modelo = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Conectar ao ChromaDB
        cliente_chroma = chromadb.PersistentClient(path="./chroma_db")
        colecao = cliente_chroma.get_or_create_collection(name="imdb_vetores")
        
        # Verificar se há dados no banco vetorial
        total_documentos = colecao.count()
        if total_documentos == 0:
            return {
                "status": "erro",
                "mensagem": "Nada encontrado no banco de dados. Tente outra pesquisa.",
                "detalhes": "O banco vetorial está vazio. Execute a Fase 1 primeiro."
            }
        
        print(f"📊 Total de documentos no banco: {total_documentos}")
        
        # Vetorizar a pergunta do usuário
        print("🤖 Vetorizando pergunta do usuário...")
        vetor_pergunta = modelo.encode([pergunta]).tolist()
        
        # Realizar busca semântica
        print(f"🔎 Buscando os {top_k} resultados mais relevantes...")
        resultados = colecao.query(
            query_embeddings=vetor_pergunta,
            n_results=top_k
        )
        
        # Verificar se encontrou resultados
        if not resultados['documents'] or len(resultados['documents'][0]) == 0:
            return {
                "status": "erro",
                "mensagem": "Nada encontrado no banco de dados. Tente outra pesquisa.",
                "detalhes": "Nenhum resultado relevante foi encontrado para sua pergunta."
            }
        
        print(f"✅ Encontrados {len(resultados['documents'][0])} resultados relevantes!")
        
        # ========== ETAPA 2: AUGMENTED (Aumento de Contexto) ==========
        print("📝 Formatando contexto para a LLM...")
        
        # Formatar os filmes encontrados
        filmes_encontrados = []
        for i, (doc, metadata) in enumerate(zip(resultados['documents'][0], resultados['metadatas'][0])):
            filme_info = f"\n**Filme {i+1}:**\n"
            
            # Extrair informações dos metadados
            if 'Series_Title' in metadata:
                filme_info += f"- Título: {metadata['Series_Title']}\n"
            if 'Released_Year' in metadata:
                filme_info += f"- Ano: {metadata['Released_Year']}\n"
            if 'Genre' in metadata:
                filme_info += f"- Gênero: {metadata['Genre']}\n"
            if 'IMDB_Rating' in metadata:
                filme_info += f"- Nota IMDB: {metadata['IMDB_Rating']}\n"
            if 'Director' in metadata:
                filme_info += f"- Diretor: {metadata['Director']}\n"
            if 'Star1' in metadata or 'Star2' in metadata:
                estrelas = []
                if 'Star1' in metadata:
                    estrelas.append(metadata['Star1'])
                if 'Star2' in metadata:
                    estrelas.append(metadata['Star2'])
                if estrelas:
                    filme_info += f"- Elenco: {', '.join(estrelas)}\n"
            if 'Overview' in metadata:
                filme_info += f"- Sinopse: {metadata['Overview']}\n"
            
            filmes_encontrados.append(filme_info)
        
        contexto_formatado = "\n".join(filmes_encontrados)
        
        # Criar o prompt aumentado (AUGMENTED)
        prompt_augmented = f"""Você é um especialista em cinema com vasto conhecimento sobre filmes e séries.

**INSTRUÇÕES IMPORTANTES:**
- Use APENAS as informações dos filmes fornecidas abaixo
- Seja entusiasta, detalhista e persuasivo nas recomendações
- Explique POR QUE cada filme é interessante
- Destaque aspectos únicos de cada título
- Use um tom amigável e conversacional
- Se a pergunta for sobre recomendação, ordene do melhor para o menos indicado
- Se a pergunta for sobre um filme específico, dê análises profundas

**CONTEXTO ADICIONAL DO USUÁRIO:**
{contexto_adicional if contexto_adicional else 'Nenhum contexto adicional fornecido.'}

**FILMES DISPONÍVEIS PARA ANÁLISE:**
{contexto_formatado}

**PERGUNTA DO USUÁRIO:**
{pergunta}

**SUA RESPOSTA (seja detalhada, entusiasmada e útil):**"""

        # ========== ETAPA 3: GENERATION (Geração) ==========
        print("🚀 Enviando para a LLM Gemini...")
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt_augmented
        )
        
        print("✅ Resposta gerada com sucesso!")
        
        # Retornar resultado completo
        return {
            "status": "sucesso",
            "pergunta_original": pergunta,
            "contexto_adicional": contexto_adicional,
            "total_filmes_encontrados": len(resultados['documents'][0]),
            "resposta": response.text,
            "metadados_filmes": resultados['metadatas'][0]
        }
        
    except Exception as erro:
        print(f"❌ Erro durante o processamento RAG: {erro}")
        return {
            "status": "erro",
            "mensagem": f"Erro durante o processamento: {str(erro)}"
        }


# Teste local (apenas para desenvolvimento)
if __name__ == "__main__":
    print("=== TESTE DA FASE 2: RAG ===\n")
    
    # Solicita a pergunta do usuário
    print("Digite sua pergunta sobre filmes:")
    print("Exemplos:")
    print("  - Me recomende filmes de ação emocionantes")
    print("  - Quais são os melhores filmes de drama?")
    print("  - Filmes de comédia para assistir com a família")
    print()
    
    pergunta_teste = input("Sua pergunta: ").strip()
    
    if not pergunta_teste:
        print("❌ Erro: Você precisa digitar uma pergunta!")
    else:
        # Pergunta opcional por contexto adicional
        print("\nDeseja adicionar contexto adicional? (pressione ENTER para pular)")
        contexto_teste = input("Contexto adicional: ").strip()
        
        # Pergunta opcional por número de filmes
        print("\nQuantos filmes deseja buscar? (padrão: 5)")
        top_k_input = input("Top K: ").strip()
        top_k_teste = int(top_k_input) if top_k_input.isdigit() else 5
        
        print("\n" + "="*80)
        print("🔄 Processando sua pergunta...")
        print("="*80 + "\n")
        
        resultado = processar_pergunta_rag(
            pergunta=pergunta_teste,
            contexto_adicional=contexto_teste,
            top_k=top_k_teste
        )
        
        print("\n📊 RESULTADO:")
        print(f"Status: {resultado['status']}")
        if resultado['status'] == 'sucesso':
            print(f"\n💬 RESPOSTA DA IA:\n{resultado['resposta']}")
        else:
            print(f"Mensagem: {resultado['mensagem']}")

