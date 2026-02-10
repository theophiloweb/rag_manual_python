# 📮 Como Testar o Endpoint da Fase 2 no Insomnia/Postman

## 🎯 Endpoint: `/fase_2`

### Método: `POST`

### URL: 
```
http://localhost:5000/fase_2
```

---

## 📝 Exemplo 1: Pergunta Simples

### Body (JSON):
```json
{
  "pergunta": "Me recomende filmes de ação emocionantes"
}
```

### Resposta Esperada:
```json
{
  "status": "sucesso",
  "pergunta_original": "Me recomende filmes de ação emocionantes",
  "contexto_adicional": "",
  "total_filmes_encontrados": 5,
  "resposta": "Aqui estão minhas recomendações de filmes de ação...",
  "metadados_filmes": [...]
}
```

---

## 📝 Exemplo 2: Pergunta com Contexto Adicional

### Body (JSON):
```json
{
  "pergunta": "Quais são os melhores filmes de drama?",
  "contexto_adicional": "Prefiro filmes que me façam refletir sobre a vida"
}
```

### Resposta Esperada:
```json
{
  "status": "sucesso",
  "pergunta_original": "Quais são os melhores filmes de drama?",
  "contexto_adicional": "Prefiro filmes que me façam refletir sobre a vida",
  "total_filmes_encontrados": 5,
  "resposta": "Excelente escolha! Aqui estão os melhores filmes de drama...",
  "metadados_filmes": [...]
}
```

---

## 📝 Exemplo 3: Pergunta com Top K Personalizado

### Body (JSON):
```json
{
  "pergunta": "Filmes de comédia para assistir com a família",
  "contexto_adicional": "Quero algo leve e divertido",
  "top_k": 3
}
```

### Resposta Esperada:
```json
{
  "status": "sucesso",
  "pergunta_original": "Filmes de comédia para assistir com a família",
  "contexto_adicional": "Quero algo leve e divertido",
  "total_filmes_encontrados": 3,
  "resposta": "Ótima escolha para assistir em família! Aqui estão 3 comédias...",
  "metadados_filmes": [...]
}
```

---

## ❌ Exemplo 4: Erro - Pergunta Vazia

### Body (JSON):
```json
{
  "pergunta": ""
}
```

### Resposta Esperada:
```json
{
  "status": "erro",
  "mensagem": "Por favor, envie uma pergunta no campo 'pergunta'",
  "detalhes": "A pergunta não pode estar vazia"
}
```

---

## ❌ Exemplo 5: Erro - Nada Encontrado

### Body (JSON):
```json
{
  "pergunta": "Filmes sobre viagem no tempo quântico interdimensional"
}
```

### Resposta Esperada (se não houver filmes correspondentes):
```json
{
  "status": "erro",
  "mensagem": "Nada encontrado no banco de dados. Tente outra pesquisa.",
  "detalhes": "Nenhum resultado relevante foi encontrado para sua pergunta."
}
```

---

## 🔧 Configuração no Insomnia

### Passo 1: Criar Nova Requisição
1. Clique em `+` para criar nova requisição
2. Nomeie como "Fase 2 - RAG"
3. Selecione método `POST`

### Passo 2: Configurar URL
```
http://localhost:5000/fase_2
```

### Passo 3: Configurar Headers
```
Content-Type: application/json
```

### Passo 4: Configurar Body
1. Selecione `JSON` no dropdown do Body
2. Cole um dos exemplos acima

### Passo 5: Enviar Requisição
1. Clique em `Send`
2. Veja a resposta na aba `Response`

---

## 🎬 Exemplos de Perguntas para Testar

### Ação:
```json
{"pergunta": "Me recomende filmes de ação emocionantes"}
```

### Drama:
```json
{"pergunta": "Quais são os melhores filmes de drama?"}
```

### Comédia:
```json
{"pergunta": "Filmes de comédia para assistir com a família"}
```

### Suspense:
```json
{"pergunta": "Quero assistir um filme de suspense psicológico"}
```

### Melhores Avaliações:
```json
{"pergunta": "Me mostre os filmes com as melhores avaliações no IMDB"}
```

### Diretor Específico:
```json
{"pergunta": "Filmes dirigidos por Christopher Nolan"}
```

### Época Específica:
```json
{"pergunta": "Filmes clássicos dos anos 90"}
```

---

## 🧪 Testando Diretamente pelo Terminal

### Usando cURL:
```bash
curl -X POST http://localhost:5000/fase_2 \
  -H "Content-Type: application/json" \
  -d "{\"pergunta\": \"Me recomende filmes de ação emocionantes\"}"
```

### Usando Python:
```python
import requests

response = requests.post('http://localhost:5000/fase_2', json={
    "pergunta": "Me recomende filmes de ação emocionantes",
    "contexto_adicional": "Gosto de adrenalina",
    "top_k": 5
})

print(response.json())
```

### Executando o arquivo diretamente:
```bash
python rag_fase2.py
```
*Isso abrirá um prompt interativo onde você pode digitar sua pergunta*

---

## 📊 Parâmetros Aceitos

| Parâmetro | Tipo | Obrigatório | Padrão | Descrição |
|-----------|------|-------------|--------|-----------|
| `pergunta` | string | ✅ Sim | - | A pergunta sobre filmes |
| `contexto_adicional` | string | ❌ Não | "" | Contexto adicional/preferências |
| `top_k` | integer | ❌ Não | 5 | Número de filmes a buscar |

---

## ✅ Checklist Antes de Testar

- [ ] API está rodando (`python app.py`)
- [ ] Fase 1 foi executada (banco vetorial criado)
- [ ] Insomnia/Postman configurado corretamente
- [ ] URL está correta: `http://localhost:5000/fase_2`
- [ ] Método é `POST`
- [ ] Header `Content-Type: application/json` está configurado
- [ ] Body está em formato JSON válido

---

## 🐛 Troubleshooting

### Erro: "Connection refused"
- Verifique se a API está rodando: `python app.py`

### Erro: "Nada encontrado no banco de dados"
- Execute a Fase 1 primeiro: `curl http://localhost:5000/fase_1`

### Erro: "Invalid JSON"
- Verifique se o JSON está válido (use um validador JSON online)
- Certifique-se de usar aspas duplas `"` e não simples `'`

### Resposta vazia ou erro 500
- Verifique os logs do terminal onde a API está rodando
- Certifique-se de que todas as dependências estão instaladas
