# 📚 Fase 1 - Vetorização do Banco IMDB

## 📝 O que foi criado?

### 1. **vetorizacao_fase1.py**
Arquivo responsável por vetorizar os dados do banco IMDB.

#### Como funciona:
1. **Conecta** ao banco SQLite (imdb.db)
2. **Busca** os dados da primeira tabela
3. **Vetoriza** os textos usando SentenceTransformer
4. **Armazena** os vetores no ChromaDB

### 2. **Endpoint /fase_1**
Adicionado ao arquivo `app.py`

- **URL**: `http://localhost:5000/fase_1`
- **Métodos**: GET ou POST
- **Função**: Executa o processo de vetorização

## 🚀 Como usar?

### Opção 1: Via GET (navegador ou Postman)
```
GET http://localhost:5000/fase_1
```

### Opção 2: Via POST (Postman ou código)
```
POST http://localhost:5000/fase_1
```

### Opção 3: Via Python (requests)
```python
import requests

resposta = requests.get("http://localhost:5000/fase_1")
print(resposta.json())
```

### Opção 4: Via curl (terminal)
```bash
curl http://localhost:5000/fase_1
```

## 📊 Resposta esperada

### Sucesso:
```json
{
  "status": "sucesso",
  "mensagem": "Vetorização concluída com sucesso!",
  "tabela_vetorizada": "nome_da_tabela",
  "total_documentos": 1234,
  "colunas": ["coluna1", "coluna2", "..."],
  "modelo_usado": "all-MiniLM-L6-v2"
}
```

### Erro:
```json
{
  "status": "erro",
  "mensagem": "Descrição do erro"
}
```

## 🔧 Testar localmente

Para testar apenas a função de vetorização (sem API):
```bash
python vetorizacao_fase1.py
```

## 📦 Dependências necessárias

Certifique-se de ter instalado:
- ✅ sentence-transformers
- ✅ chromadb
- ✅ sqlite3 (já vem com Python)
- ✅ flask (para a API)

## 💡 Observações

- O código está **simples e comentado** para fácil entendimento
- Vetoriza **todos os registros** da tabela do banco de dados
- Usa o modelo **all-MiniLM-L6-v2** (rápido e eficiente)
- Os vetores ficam armazenados no **ChromaDB em arquivo** (pasta `./chroma_db`)
- ✅ **Persistência**: Os vetores são salvos em disco e podem ser reutilizados
- ⚠️ **Importante**: Dependendo da quantidade de dados, o processo pode demorar alguns minutos
  - Ajuste o timeout do Insomnia em: **Preferences → Request → Request timeout** (recomendado: 300000ms = 5 minutos)

## 📁 Arquivos Gerados

Após a vetorização, será criada a pasta:
- `./chroma_db/` - Contém todos os vetores e metadados armazenados

Para consultar os vetores salvos:
```bash
python consultar_vetores.py
```
