# Resumo da Vetorizacao - Fase 1

## Informacoes do Banco de Dados

**Tabela Principal:** movies
- **Total de registros:** 4,961 filmes
- **Total de colunas:** 20
- **Estimativa de tempo:** ~25 minutos (1488 segundos)

## Configuracao do Insomnia

Para evitar timeout, configure:

1. Abra o Insomnia
2. Va em: **Preferences** (ou Settings)
3. Navegue ate: **Request** → **Request timeout**
4. Configure para: **1800000ms** (30 minutos - para ter margem de seguranca)

## O que sera vetorizado?

Todos os 4,961 filmes com as seguintes colunas:
- id, tmdb_id, imdb_id
- title, original_title
- year, runtime
- genres, director, cast
- overview, tagline, keywords
- rating, vote_count, popularity
- budget, revenue
- production_companies, description

## Processo de Vetorizacao

1. Cada filme tera todos os campos combinados em um texto unico
2. O texto sera transformado em vetor usando SentenceTransformer
3. Os vetores serao armazenados no ChromaDB (pasta ./chroma_db)
4. Metadados de cada filme serao preservados para consultas futuras
5. Os dados ficam salvos em arquivo e podem ser reutilizados

## Arquivos Gerados

Apos a vetorizacao, sera criada a pasta:
- **./chroma_db/** - Contem todos os vetores e metadados

Para consultar os vetores salvos:
```bash
python consultar_vetores.py
```

## Como executar?

### Opcao 1: Via Insomnia (recomendado)
```
GET http://localhost:5000/fase_1
```

### Opcao 2: Via navegador
```
http://localhost:5000/fase_1
```

### Opcao 3: Via curl
```bash
curl http://localhost:5000/fase_1
```

## Acompanhamento

Voce pode acompanhar o progresso pelos logs no terminal onde a API esta rodando.
Mensagens que aparecerão:
- "Conectando ao banco de dados..."
- "Buscando dados da tabela..."
- "Tabela encontrada: movies"
- "Total de registros a vetorizar: 4961"
- "Carregando modelo de vetorizacao..."
- "Conectando ao ChromaDB..."
- "Iniciando vetorizacao..."
- "Vetorizacao concluida com sucesso!"

## Importante

- O processo pode demorar ate 30 minutos
- Nao feche o terminal durante a execucao
- Nao cancele a requisicao no Insomnia
- Aguarde ate receber a resposta JSON com status "sucesso"
