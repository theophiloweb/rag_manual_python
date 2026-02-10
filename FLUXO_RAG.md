# 🎬 FLUXO COMPLETO DO SISTEMA RAG - FASE 2

## 📊 Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FASE 1: VETORIZAÇÃO                          │
│                           (Concluída ✅)                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  imdb.db (SQLite)  ──────────────────────────────────────────────┐  │
│       │                                                            │  │
│       │ 1. Lê dados dos filmes                                    │  │
│       ▼                                                            │  │
│  SentenceTransformer                                               │  │
│  (all-MiniLM-L6-v2)                                               │  │
│       │                                                            │  │
│       │ 2. Converte texto em vetores                              │  │
│       ▼                                                            │  │
│  ChromaDB (chroma.sqlite3)  ◄──────────────────────────────────┘  │
│  [Banco Vetorial]                                                  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                      FASE 2: RAG (Implementada ✅)                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  👤 USUÁRIO                                                          │
│       │                                                              │
│       │ "Me recomende filmes de ação"                               │
│       ▼                                                              │
│  ┌─────────────────────────────────────────────────────────┐        │
│  │  ETAPA 1: RETRIEVAL (Recuperação)                       │        │
│  ├─────────────────────────────────────────────────────────┤        │
│  │  1. Vetoriza a pergunta do usuário                      │        │
│  │  2. Busca semanticamente no ChromaDB                    │        │
│  │  3. Retorna top_k filmes mais relevantes                │        │
│  └─────────────────────────────────────────────────────────┘        │
│       │                                                              │
│       │ [Filmes encontrados]                                        │
│       ▼                                                              │
│  ┌─────────────────────────────────────────────────────────┐        │
│  │  ETAPA 2: AUGMENTED (Aumento de Contexto)               │        │
│  ├─────────────────────────────────────────────────────────┤        │
│  │  1. Formata informações dos filmes                      │        │
│  │  2. Cria prompt especializado                           │        │
│  │  3. Adiciona instruções para a LLM                      │        │
│  │  4. Inclui contexto adicional do usuário                │        │
│  └─────────────────────────────────────────────────────────┘        │
│       │                                                              │
│       │ [Prompt aumentado]                                          │
│       ▼                                                              │
│  ┌─────────────────────────────────────────────────────────┐        │
│  │  ETAPA 3: GENERATION (Geração)                          │        │
│  ├─────────────────────────────────────────────────────────┤        │
│  │  1. Envia prompt para LLM Gemini                        │        │
│  │  2. LLM analisa APENAS os filmes fornecidos             │        │
│  │  3. Gera resposta detalhada e entusiasta                │        │
│  └─────────────────────────────────────────────────────────┘        │
│       │                                                              │
│       │ [Resposta gerada]                                           │
│       ▼                                                              │
│  👤 USUÁRIO recebe recomendação personalizada                        │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## 🔄 Exemplo Prático do Fluxo

### Entrada do Usuário:
```json
{
  "pergunta": "Me recomende filmes de ação emocionantes",
  "contexto_adicional": "Gosto de filmes com muita adrenalina",
  "top_k": 3
}
```

### 1️⃣ RETRIEVAL (Recuperação):
```
🔍 Vetorizando pergunta...
   Vetor: [0.123, -0.456, 0.789, ...]

🔎 Buscando no ChromaDB...
   Encontrados 3 filmes relevantes:
   
   ✅ Filme 1: The Dark Knight (2008)
      Similaridade: 0.92
      
   ✅ Filme 2: Inception (2010)
      Similaridade: 0.89
      
   ✅ Filme 3: Mad Max: Fury Road (2015)
      Similaridade: 0.87
```

### 2️⃣ AUGMENTED (Aumento de Contexto):
```
📝 Formatando contexto...

Prompt gerado:
┌────────────────────────────────────────────────────────────┐
│ Você é um especialista em cinema com vasto conhecimento    │
│ sobre filmes e séries.                                     │
│                                                             │
│ **INSTRUÇÕES IMPORTANTES:**                                │
│ - Use APENAS as informações dos filmes fornecidas abaixo   │
│ - Seja entusiasta, detalhista e persuasivo                 │
│ - Explique POR QUE cada filme é interessante               │
│ ...                                                         │
│                                                             │
│ **CONTEXTO ADICIONAL DO USUÁRIO:**                         │
│ Gosto de filmes com muita adrenalina                       │
│                                                             │
│ **FILMES DISPONÍVEIS PARA ANÁLISE:**                       │
│                                                             │
│ **Filme 1:**                                               │
│ - Título: The Dark Knight                                  │
│ - Ano: 2008                                                │
│ - Gênero: Action, Crime, Drama                             │
│ - Nota IMDB: 9.0                                           │
│ - Diretor: Christopher Nolan                               │
│ - Elenco: Christian Bale, Heath Ledger                     │
│ - Sinopse: When the menace known as the Joker...          │
│                                                             │
│ [... mais 2 filmes ...]                                    │
│                                                             │
│ **PERGUNTA DO USUÁRIO:**                                   │
│ Me recomende filmes de ação emocionantes                   │
└────────────────────────────────────────────────────────────┘
```

### 3️⃣ GENERATION (Geração):
```
🚀 Enviando para LLM Gemini...

💬 Resposta gerada:
┌────────────────────────────────────────────────────────────┐
│ Excelente escolha! Aqui estão 3 filmes de ação que vão    │
│ te deixar grudado na tela:                                 │
│                                                             │
│ 🎬 **1. The Dark Knight (2008) - Nota 9.0**               │
│                                                             │
│ Este é simplesmente IMPERDÍVEL! Christopher Nolan criou    │
│ uma obra-prima que transcende o gênero de super-heróis.    │
│ A performance icônica de Heath Ledger como Coringa é       │
│ perturbadora e fascinante. As cenas de ação são            │
│ espetaculares, especialmente a perseguição de caminhão     │
│ que vai te deixar sem fôlego...                            │
│                                                             │
│ [... continua com análises detalhadas ...]                 │
└────────────────────────────────────────────────────────────┘
```

## 🎯 Regras Importantes da LLM

### ✅ O que a LLM DEVE fazer:
- Usar APENAS informações dos filmes fornecidos
- Ser entusiasta e detalhista
- Explicar POR QUE cada filme é interessante
- Destacar aspectos únicos
- Usar tom amigável e conversacional
- Ordenar do melhor para o menos indicado

### ❌ O que a LLM NÃO DEVE fazer:
- Usar conhecimento próprio sobre outros filmes
- Recomendar filmes que não estão no contexto
- Dar respostas genéricas
- Ignorar o contexto adicional do usuário

### 🚫 Caso especial:
Se nenhum filme for encontrado:
```json
{
  "status": "erro",
  "mensagem": "Nada encontrado no banco de dados. Tente outra pesquisa."
}
```

## 📊 Métricas de Qualidade

### Busca Semântica (Retrieval):
- **Modelo**: all-MiniLM-L6-v2
- **Dimensão dos vetores**: 384
- **Métrica de similaridade**: Cosine similarity
- **Top-K padrão**: 5 filmes

### Geração (Generation):
- **LLM**: Google Gemini 3 Flash Preview
- **Temperatura**: Padrão (controlada pelo modelo)
- **Max tokens**: Sem limite (resposta completa)

## 🔐 Segurança e Validação

1. **Validação de entrada**:
   - Pergunta é obrigatória
   - top_k deve ser > 0
   - Contexto adicional é opcional

2. **Tratamento de erros**:
   - Banco vetorial vazio
   - Nenhum resultado encontrado
   - Erro na LLM
   - Timeout de conexão

3. **Limitações**:
   - Responde APENAS com dados do banco
   - Não inventa informações
   - Não usa conhecimento externo

## 📈 Próximas Melhorias

- [ ] Cache de embeddings para perguntas similares
- [ ] Filtros avançados (gênero, ano, nota mínima)
- [ ] Histórico de conversas
- [ ] Feedback do usuário (like/dislike)
- [ ] Reranking dos resultados
- [ ] Interface web interativa
- [ ] Suporte a múltiplos idiomas
- [ ] Análise de sentimento nas perguntas

## 🎓 Conceitos Técnicos

### RAG (Retrieval-Augmented Generation)
Técnica que combina:
- **Retrieval**: Busca de informações relevantes em uma base de conhecimento
- **Augmented**: Enriquecimento do prompt com contexto recuperado
- **Generation**: Geração de resposta pela LLM usando o contexto

### Vantagens do RAG:
✅ Respostas baseadas em dados reais e atualizados
✅ Reduz alucinações da LLM
✅ Permite controle sobre a fonte de informação
✅ Escalável para grandes bases de conhecimento
✅ Mais econômico que fine-tuning

### Embeddings (Vetores):
Representação numérica de texto que captura significado semântico.
Textos similares têm vetores próximos no espaço vetorial.

Exemplo:
```
"filme de ação"     → [0.8, 0.2, -0.1, ...]
"action movie"      → [0.79, 0.21, -0.09, ...]  (similar!)
"romantic comedy"   → [-0.3, 0.9, 0.4, ...]     (diferente!)
```
