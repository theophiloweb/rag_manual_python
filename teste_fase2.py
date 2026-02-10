"""
Script de teste para o endpoint da Fase 2 - RAG
Demonstra como fazer requisições ao sistema de recomendação de filmes
"""

import requests
import json

# URL base da API
BASE_URL = "http://localhost:5000"

def testar_fase2(pergunta, contexto_adicional="", top_k=5):
    """
    Testa o endpoint da Fase 2 com uma pergunta
    """
    print(f"\n{'='*80}")
    print(f"🎬 PERGUNTA: {pergunta}")
    if contexto_adicional:
        print(f"📝 CONTEXTO: {contexto_adicional}")
    print(f"🔢 Buscando top {top_k} filmes...")
    print(f"{'='*80}\n")
    
    try:
        # Fazer requisição POST
        response = requests.post(
            f"{BASE_URL}/fase_2",
            json={
                "pergunta": pergunta,
                "contexto_adicional": contexto_adicional,
                "top_k": top_k
            },
            timeout=60  # Timeout de 60 segundos
        )
        
        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            resultado = response.json()
            
            if resultado.get('status') == 'sucesso':
                print("✅ STATUS: Sucesso!\n")
                print(f"📊 Total de filmes encontrados: {resultado.get('total_filmes_encontrados')}\n")
                print("🤖 RESPOSTA DA IA:")
                print("-" * 80)
                print(resultado.get('resposta'))
                print("-" * 80)
                
                # Mostrar metadados dos filmes (opcional)
                if resultado.get('metadados_filmes'):
                    print("\n📋 FILMES ENCONTRADOS:")
                    for i, filme in enumerate(resultado['metadados_filmes'], 1):
                        titulo = filme.get('Series_Title', 'N/A')
                        ano = filme.get('Released_Year', 'N/A')
                        nota = filme.get('IMDB_Rating', 'N/A')
                        print(f"  {i}. {titulo} ({ano}) - Nota: {nota}")
            else:
                print(f"❌ ERRO: {resultado.get('mensagem')}")
                if resultado.get('detalhes'):
                    print(f"   Detalhes: {resultado.get('detalhes')}")
        else:
            print(f"❌ Erro HTTP {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ ERRO: Não foi possível conectar à API.")
        print("   Certifique-se de que a API está rodando: python app.py")
    except requests.exceptions.Timeout:
        print("❌ ERRO: Timeout - A requisição demorou muito.")
    except Exception as e:
        print(f"❌ ERRO: {e}")


def main():
    """
    Função principal com exemplos de testes
    """
    print("\n" + "="*80)
    print("🎬 TESTE DO SISTEMA RAG - RECOMENDAÇÃO DE FILMES IMDB")
    print("="*80)
    
    # Verificar se a API está rodando
    try:
        response = requests.get(f"{BASE_URL}/fase_2", timeout=5)
        print("\n✅ API está rodando!")
    except:
        print("\n❌ ERRO: API não está rodando!")
        print("   Execute: python app.py")
        return
    
    # Teste 1: Filmes de ação
    testar_fase2(
        pergunta="Me recomende filmes de ação emocionantes",
        contexto_adicional="Gosto de filmes com muita adrenalina e efeitos especiais",
        top_k=3
    )
    
    input("\n\nPressione ENTER para o próximo teste...")
    
    # Teste 2: Filmes de drama
    testar_fase2(
        pergunta="Quais são os melhores filmes de drama?",
        contexto_adicional="Prefiro filmes que me façam refletir sobre a vida",
        top_k=3
    )
    
    input("\n\nPressione ENTER para o próximo teste...")
    
    # Teste 3: Filmes de comédia
    testar_fase2(
        pergunta="Filmes de comédia para assistir com a família",
        contexto_adicional="",
        top_k=3
    )
    
    input("\n\nPressione ENTER para o próximo teste...")
    
    # Teste 4: Melhores avaliações
    testar_fase2(
        pergunta="Me mostre os filmes com as melhores avaliações no IMDB",
        contexto_adicional="Quero assistir apenas os melhores filmes de todos os tempos",
        top_k=5
    )
    
    print("\n\n" + "="*80)
    print("✅ TESTES CONCLUÍDOS!")
    print("="*80)


if __name__ == "__main__":
    main()
