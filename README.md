# 🎬 Sistema RAG de Recomendação de Filmes IMDB

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📚 Objetivo Didático

Este projeto foi desenvolvido com **fins educacionais** para ensinar e demonstrar na prática os conceitos de **RAG (Retrieval-Augmented Generation)**, uma das técnicas mais importantes em IA moderna.

### 🎓 O que você vai aprender:

1. **Embeddings e Vetorização**
   - Como transformar texto em vetores numéricos
   - Uso de modelos de linguagem (SentenceTransformers)
   - Conceito de espaço vetorial e similaridade semântica

2. **Bancos de Dados Vetoriais**
   - Diferença entre bancos relacionais e vetoriais
   - Como usar ChromaDB para armazenar e buscar vetores
   - Busca semântica vs busca por palavras-chave

3. **RAG (Retrieval-Augmented Generation)**
   - **R**etrieval: Recuperação de informações relevantes
   - **A**ugmented: Enriquecimento do contexto
   - **G**eneration: Geração de respostas pela LLM
   - Como evitar "alucinações" da IA

4. **APIs REST com Flask**
   - Criação de endpoints
   - Métodos HTTP (GET, POST)
   - Manipulação de JSON

5. **Integração com LLMs**
   - Como usar Google Gemini API
   - Engenharia de prompts
   - Controle de respostas da IA

---

## 🎯 Sobre o Projeto

Este sistema permite que usuários façam perguntas sobre filmes e recebam recomendações personalizadas baseadas em um banco de dados real do IMDB. A diferença é que **a IA responde APENAS com base nos dados do banco**, não inventando informações.

### ✨ Diferenciais:

- ✅ Respostas baseadas em dados reais
- ✅ Busca semântica inteligente
- ✅ Recomendações personalizadas
- ✅ Código didático e bem comentado
- ✅ Arquitetura modular e escalável

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    FASE 1: VETORIZAÇÃO                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  imdb.db (SQLite)                                          │
│       │                                                     │
│       ├─► SentenceTransformer (all-MiniLM-L6-v2)          │
│       │                                                     │
│       └─► ChromaDB (Banco Vetorial)                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                 FASE 2: RAG (Consulta)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Pergunta do Usuário                                        │
│       │                                                     │
│       ├─► 1. RETRIEVAL: Busca semântica no ChromaDB       │
│       │                                                     │
│       ├─► 2. AUGMENTED: Formata contexto + instruções     │
│       │                                                     │
│       └─► 3. GENERATION: LLM Gemini gera resposta         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta Google Cloud (para API Gemini)

### Passo 1: Clone o Repositório

```bash
git clone <seu-repositorio>
cd aula_rag
```

### Passo 2: Crie um Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instale as Dependências

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

### Passo 4: Configure a API do Gemini

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma API Key
3. Edite o arquivo `genai_api.py` e substitua pela sua chave:

```python
client = genai.Client(api_key="SUA_API_KEY_AQUI")
```

---

## 📖 Como Usar

### 1️⃣ Inicie a API

```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

### 2️⃣ Execute a Fase 1 (Vetorização)

**Primeira vez apenas** - Cria o banco vetorial:

```bash
curl http://localhost:5000/fase_1
```

Ou execute diretamente:

```bash
python vetorizacao_fase1.py
```

### 3️⃣ Use a Fase 2 (Consulta RAG)

#### Via cURL:

```bash
curl -X POST http://localhost:5000/fase_2 \
  -H "Content-Type: application/json" \
  -d "{\"pergunta\": \"Me recomende filmes de ação emocionantes\"}"
```

#### Via Insomnia/Postman:

```
POST http://localhost:5000/fase_2

Body (JSON):
{
  "pergunta": "Me recomende filmes de ação emocionantes",
  "contexto_adicional": "Gosto de filmes com muita adrenalina",
  "top_k": 5
}
```

#### Via Python (Teste Interativo):

```bash
python rag_fase2.py
```

#### Via Script de Teste:

```bash
python teste_fase2.py
```

---

## 📁 Estrutura do Projeto

```
aula_rag/
│
├── 📄 app.py                    # API principal (Flask)
├── 📄 genai_api.py             # Configuração Google Gemini
├── 📄 estrutura_database.py    # Estrutura do banco SQLite
│
├── 🔵 FASE 1: Vetorização
│   └── vetorizacao_fase1.py    # Converte DB tabular → vetorial
│
├── 🟢 FASE 2: RAG
│   ├── rag_fase2.py            # Lógica completa RAG
│   └── teste_fase2.py          # Script de teste
│
├── 📚 Documentação
│   ├── README.md               # Este arquivo
│   ├── README_FASE2.md         # Documentação detalhada Fase 2
│   └── FLUXO_RAG.md            # Diagramas e conceitos
│
├── 💾 Dados
│   ├── imdb.db                 # Banco SQLite original
│   └── chroma_db/              # Banco vetorial ChromaDB
│
└── 📦 Configuração
    ├── requirements.txt        # Dependências Python
    └── .gitignore             # Arquivos ignorados pelo Git
```

---

## 🎯 Endpoints da API

### 📍 GET/POST `/fase_1` - Vetorização

Cria o banco vetorial a partir do banco SQLite.

**Resposta:**
```json
{
  "status": "sucesso",
  "mensagem": "Vetorização concluída com sucesso!",
  "total_documentos": 1000,
  "modelo_usado": "all-MiniLM-L6-v2"
}
```

### 📍 POST `/fase_2` - Consulta RAG

Processa perguntas e retorna recomendações.

**Parâmetros:**
- `pergunta` (obrigatório): Sua pergunta sobre filmes
- `contexto_adicional` (opcional): Preferências adicionais
- `top_k` (opcional, padrão: 5): Número de filmes a buscar

**Exemplo de Requisição:**
```json
{
  "pergunta": "Quais são os melhores filmes de drama?",
  "contexto_adicional": "Prefiro filmes que me façam refletir",
  "top_k": 3
}
```

**Resposta:**
```json
{
  "status": "sucesso",
  "pergunta_original": "Quais são os melhores filmes de drama?",
  "total_filmes_encontrados": 3,
  "resposta": "Aqui estão os melhores filmes de drama...",
  "metadados_filmes": [...]
}
```

---

## 💡 Exemplos de Uso

### Exemplo 1: Recomendação por Gênero

```json
{
  "pergunta": "Me recomende filmes de ação emocionantes"
}
```

### Exemplo 2: Busca com Contexto

```json
{
  "pergunta": "Filmes de comédia para assistir com a família",
  "contexto_adicional": "Quero algo leve e divertido"
}
```

### Exemplo 3: Melhores Avaliações

```json
{
  "pergunta": "Me mostre os filmes com as melhores avaliações no IMDB",
  "top_k": 10
}
```

### Exemplo 4: Diretor Específico

```json
{
  "pergunta": "Filmes dirigidos por Christopher Nolan"
}
```

---

## 🧠 Conceitos Técnicos Explicados

### O que é RAG?

**RAG (Retrieval-Augmented Generation)** é uma técnica que combina:

1. **Retrieval (Recuperação)**: Busca informações relevantes em uma base de conhecimento
2. **Augmented (Aumento)**: Enriquece o prompt da IA com essas informações
3. **Generation (Geração)**: A LLM gera uma resposta baseada no contexto fornecido

### Por que usar RAG?

✅ **Respostas precisas**: Baseadas em dados reais, não em "conhecimento" da IA  
✅ **Reduz alucinações**: A IA não inventa informações  
✅ **Dados atualizados**: Você controla a fonte de informação  
✅ **Mais econômico**: Não precisa fazer fine-tuning da LLM  
✅ **Escalável**: Funciona com grandes bases de conhecimento  

### O que são Embeddings?

**Embeddings** são representações numéricas (vetores) de texto que capturam o significado semântico.

Exemplo:
```
"filme de ação"     → [0.8, 0.2, -0.1, 0.5, ...]
"action movie"      → [0.79, 0.21, -0.09, 0.51, ...] (similar!)
"romantic comedy"   → [-0.3, 0.9, 0.4, -0.2, ...]   (diferente!)
```

Textos com significados similares têm vetores próximos no espaço vetorial.

---

## 🔧 Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.8+ | Linguagem principal |
| **Flask** | 3.0 | Framework web para API REST |
| **ChromaDB** | 0.4 | Banco de dados vetorial |
| **SentenceTransformers** | 2.3 | Modelo de embeddings |
| **Google Gemini** | API | LLM para geração de respostas |
| **SQLite** | 3.x | Banco de dados tabular original |

---

## 📊 Fluxo de Dados Detalhado

### Fase 1: Vetorização

```
1. Lê dados do imdb.db (SQLite)
   ↓
2. Para cada filme:
   - Combina título, gênero, sinopse, etc.
   - Gera embedding usando SentenceTransformer
   ↓
3. Armazena vetores no ChromaDB
   - Vetor de 384 dimensões
   - Metadados do filme
```

### Fase 2: Consulta RAG

```
1. RETRIEVAL
   - Usuário faz pergunta: "Filmes de ação"
   - Sistema vetoriza a pergunta
   - Busca os top_k filmes mais similares no ChromaDB
   ↓
2. AUGMENTED
   - Formata informações dos filmes encontrados
   - Cria prompt especializado com instruções
   - Adiciona contexto do usuário
   ↓
3. GENERATION
   - Envia prompt para Gemini
   - LLM analisa APENAS os filmes fornecidos
   - Gera recomendação detalhada
   ↓
4. Retorna resposta ao usuário
```

---

## 🎓 Exercícios Propostos

Para aprofundar seu aprendizado, tente:

1. **Básico**
   - [ ] Adicionar mais filmes ao banco de dados
   - [ ] Testar diferentes tipos de perguntas
   - [ ] Modificar o número de resultados (top_k)

2. **Intermediário**
   - [ ] Adicionar filtro por ano de lançamento
   - [ ] Implementar filtro por nota mínima do IMDB
   - [ ] Criar endpoint para listar gêneros disponíveis

3. **Avançado**
   - [ ] Implementar cache de respostas
   - [ ] Adicionar histórico de conversas
   - [ ] Criar interface web com HTML/CSS/JS
   - [ ] Implementar sistema de feedback (like/dislike)

---

## 🐛 Troubleshooting

### Erro: "Connection refused"
**Solução**: Certifique-se de que a API está rodando (`python app.py`)

### Erro: "Nada encontrado no banco de dados"
**Solução**: Execute a Fase 1 primeiro (`curl http://localhost:5000/fase_1`)

### Erro: "API Key inválida"
**Solução**: Verifique se configurou corretamente a chave no `genai_api.py`

### Erro: "Module not found"
**Solução**: Instale as dependências (`pip install -r requirements.txt`)

---

## 📚 Recursos Adicionais

### Documentação Oficial:
- [ChromaDB](https://docs.trychroma.com/)
- [SentenceTransformers](https://www.sbert.net/)
- [Google Gemini API](https://ai.google.dev/)
- [Flask](https://flask.palletsprojects.com/)

### Artigos Recomendados:
- [O que é RAG?](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- [Embeddings Explicados](https://platform.openai.com/docs/guides/embeddings)
- [Bancos Vetoriais](https://www.pinecone.io/learn/vector-database/)

---

## 🤝 Contribuindo

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido como material didático para ensino de RAG e IA.

---

## 🙏 Agradecimentos

- Dataset IMDB
- Comunidade ChromaDB
- Google AI (Gemini)
- Comunidade Python

---

## 📞 Suporte

Dúvidas? Abra uma [issue](https://github.com/seu-usuario/seu-repo/issues) no GitHub!

---

**⭐ Se este projeto te ajudou a aprender, deixe uma estrela no GitHub!**

---

## 🗺️ Roadmap

- [x] Fase 1: Vetorização
- [x] Fase 2: RAG básico
- [ ] Fase 3: Interface web
- [ ] Fase 4: Sistema de cache
- [ ] Fase 5: Histórico de conversas
- [ ] Fase 6: Suporte a múltiplos idiomas

---

**Bons estudos! 🚀📚**
