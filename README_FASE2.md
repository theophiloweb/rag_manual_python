# Projeto RAG - Sistema de Recomendação de Filmes IMDB

## 📋 Visão Geral

Este projeto implementa um sistema completo de **RAG (Retrieval-Augmented Generation)** para recomendação de filmes usando o banco de dados IMDB.

## 🎯 Fases do Projeto

### ✅ Fase 1: Vetorização (CONCLUÍDA)
Transforma o banco de dados tabular SQLite em um banco vetorial usando ChromaDB.

**Endpoint:** `/fase_1` (GET ou POST)

**O que faz:**
1. Conecta ao banco `imdb.db`
2. Extrai os dados dos filmes
3. Vetoriza usando SentenceTransformer (modelo: all-MiniLM-L6-v2)
4. Armazena no ChromaDB (`chroma.sqlite3`)

### ✅ Fase 2: RAG - Consulta Inteligente (IMPLEMENTADA)
Permite ao usuário fazer perguntas e receber recomendações baseadas no banco vetorial.

**Endpoint:** `/fase_2` (GET ou POST)

**Fluxo RAG:**
1. **RETRIEVAL (Recuperação):**
   - Recebe a pergunta do usuário
   - Vetoriza a pergunta usando o mesmo modelo
   - Busca semanticamente no ChromaDB os filmes mais relevantes

2. **AUGMENTED (Aumento de Contexto):**
   - Formata os filmes encontrados
   - Cria um prompt especializado com instruções para a LLM
   - Adiciona contexto adicional do usuário (se fornecido)

3. **GENERATION (Geração):**
   - Envia o prompt aumentado para a LLM Gemini
   - A LLM gera uma resposta baseada APENAS nos filmes encontrados
   - Retorna a recomendação detalhada

## 🚀 Como Usar

### 1. Executar a Fase 1 (Vetorização)

Primeiro, certifique-se de que o banco vetorial foi criado:

```bash
# Via API
curl http://localhost:5000/fase_1
```

Ou execute diretamente:
```bash
python vetorizacao_fase1.py
```

### 2. Usar a Fase 2 (Consulta RAG)

#### Opção A: Via API (POST)

```bash
curl -X POST http://localhost:5000/fase_2 \
  -H "Content-Type: application/json" \
  -d '{
    "pergunta": "Me recomende filmes de ação emocionantes",
    "contexto_adicional": "Gosto de filmes com muita adrenalina",
    "top_k": 5
  }'
```

#### Opção B: Via Python

```python
import requests

response = requests.post('http://localhost:5000/fase_2', json={
    "pergunta": "Quais são os melhores filmes de drama?",
    "contexto_adicional": "Prefiro filmes mais recentes",
    "top_k": 3
})

print(response.json()['resposta'])
```

#### Opção C: Usar o script de teste

```bash
python teste_fase2.py
```

## 📊 Parâmetros da Fase 2

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `pergunta` | string | ✅ Sim | A pergunta/requisição do usuário |
| `contexto_adicional` | string | ❌ Não | Contexto adicional sobre preferências |
| `top_k` | integer | ❌ Não | Número de filmes a buscar (padrão: 5) |

## 📤 Resposta da Fase 2

```json
{
  "status": "sucesso",
  "pergunta_original": "Me recomende filmes de ação",
  "contexto_adicional": "Gosto de adrenalina",
  "total_filmes_encontrados": 5,
  "resposta": "Aqui estão minhas recomendações...",
  "metadados_filmes": [...]
}
```

## 🎬 Exemplos de Perguntas

- "Me recomende filmes de ação emocionantes"
- "Quais são os melhores filmes de drama?"
- "Filmes de comédia para assistir com a família"
- "Me mostre filmes com nota acima de 8 no IMDB"
- "Filmes dirigidos por Christopher Nolan"
- "Quero assistir um filme de suspense psicológico"

## 🔒 Regras Importantes

1. **A LLM responde APENAS com base nos filmes encontrados no banco**
2. Se nenhum filme for encontrado, retorna: "Nada encontrado no banco de dados. Tente outra pesquisa."
3. A LLM NÃO usa conhecimento próprio, apenas o contexto fornecido
4. As respostas são detalhadas, entusiastas e persuasivas

## 🛠️ Tecnologias Utilizadas

- **Flask**: API REST
- **ChromaDB**: Banco de dados vetorial
- **SentenceTransformer**: Modelo de embeddings (all-MiniLM-L6-v2)
- **Google Gemini**: LLM para geração de respostas
- **SQLite**: Banco de dados tabular original

## 📁 Estrutura de Arquivos

```
aula_rag/
├── app.py                    # API principal com endpoints
├── genai_api.py             # Configuração da API Gemini
├── estrutura_database.py    # Estrutura do banco SQLite
├── vetorizacao_fase1.py     # Fase 1: Vetorização
├── rag_fase2.py             # Fase 2: RAG completo
├── teste_fase2.py           # Script de teste
├── imdb.db                  # Banco SQLite original
└── chroma_db/               # Banco vetorial ChromaDB
    └── chroma.sqlite3
```

## 🐛 Troubleshooting

### Erro: "Nada encontrado no banco de dados"
- Execute a Fase 1 primeiro: `curl http://localhost:5000/fase_1`
- Verifique se o arquivo `chroma_db/chroma.sqlite3` existe

### Erro: "O banco vetorial está vazio"
- Delete a pasta `chroma_db` e execute a Fase 1 novamente

### Erro de importação
- Instale as dependências:
```bash
pip install flask chromadb sentence-transformers google-genai
```

## 📝 Próximos Passos

- [ ] Adicionar filtros por gênero, ano, nota
- [ ] Implementar cache de respostas
- [ ] Criar interface web
- [ ] Adicionar histórico de conversas
- [ ] Melhorar formatação das respostas

## 👨‍💻 Desenvolvido por

Projeto de estudo sobre RAG (Retrieval-Augmented Generation)
