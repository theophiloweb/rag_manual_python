# 📦 Guia: Como Gerar requirements.txt

## 🎯 Objetivo

O arquivo `requirements.txt` lista todas as dependências do projeto Python, facilitando a instalação em outros ambientes.

---

## 📝 Métodos para Gerar requirements.txt

### Método 1: pip freeze (Ambiente Virtual Recomendado)

Este é o método mais comum e recomendado quando você usa um **ambiente virtual**.

#### Passo a Passo:

1. **Ative seu ambiente virtual:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Gere o requirements.txt:**
   ```bash
   pip freeze > requirements.txt
   ```

3. **Verifique o arquivo:**
   ```bash
   cat requirements.txt  # Linux/Mac
   type requirements.txt # Windows
   ```

#### ✅ Vantagens:
- Lista TODAS as dependências instaladas
- Inclui versões exatas
- Garante reprodutibilidade

#### ❌ Desvantagens:
- Pode incluir pacotes desnecessários se não usar ambiente virtual
- Arquivo pode ficar muito grande

---

### Método 2: pipreqs (Apenas Dependências Usadas)

Este método analisa seu código e lista **apenas** as dependências que você realmente usa.

#### Instalação:
```bash
pip install pipreqs
```

#### Uso:
```bash
# Gera requirements.txt analisando o código
pipreqs . --force

# Ou especifique o diretório
pipreqs /caminho/do/projeto --force
```

#### ✅ Vantagens:
- Lista apenas o que é realmente usado
- Arquivo mais limpo e enxuto
- Não precisa de ambiente virtual

#### ❌ Desvantagens:
- Pode não detectar todas as dependências
- Precisa instalar ferramenta extra

---

### Método 3: Manual (Recomendado para Projetos Didáticos)

Crie o arquivo manualmente listando apenas as dependências principais.

#### Exemplo:
```txt
# requirements.txt

# Framework Web
Flask==3.0.0

# Banco de Dados Vetorial
chromadb==0.4.22

# Modelo de Embeddings
sentence-transformers==2.3.1

# LLM - Google Gemini
google-genai==0.2.2

# Utilitários
requests==2.31.0
```

#### ✅ Vantagens:
- Controle total sobre o que incluir
- Arquivo limpo e organizado
- Fácil de documentar

#### ❌ Desvantagens:
- Trabalhoso para projetos grandes
- Pode esquecer alguma dependência

---

## 🔄 Como Instalar Dependências

Depois de ter o `requirements.txt`, instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 📋 Boas Práticas

### 1. Use Ambiente Virtual

Sempre crie um ambiente virtual antes de instalar dependências:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt
```

### 2. Especifique Versões

Sempre especifique versões para garantir compatibilidade:

```txt
# ✅ BOM
Flask==3.0.0

# ❌ EVITE (pode instalar versão incompatível)
Flask
```

### 3. Organize por Categoria

Agrupe dependências por função:

```txt
# Web Framework
Flask==3.0.0
Werkzeug==3.0.1

# Database
chromadb==0.4.22

# ML/AI
sentence-transformers==2.3.1
torch==2.1.2
```

### 4. Adicione Comentários

Explique para que serve cada dependência:

```txt
# Flask - Framework web para criar a API REST
Flask==3.0.0

# ChromaDB - Banco de dados vetorial para armazenar embeddings
chromadb==0.4.22
```

---

## 🔍 Verificar Dependências Instaladas

### Listar todas as dependências:
```bash
pip list
```

### Verificar versão específica:
```bash
pip show Flask
```

### Verificar dependências desatualizadas:
```bash
pip list --outdated
```

---

## 🆙 Atualizar Dependências

### Atualizar uma dependência específica:
```bash
pip install --upgrade Flask
```

### Atualizar todas:
```bash
pip install --upgrade -r requirements.txt
```

---

## 🐛 Troubleshooting

### Erro: "pip: command not found"
**Solução**: Certifique-se de que Python e pip estão instalados:
```bash
python --version
pip --version
```

### Erro: "Permission denied"
**Solução**: Use ambiente virtual ou adicione `--user`:
```bash
pip install --user -r requirements.txt
```

### Erro: "No matching distribution found"
**Solução**: Verifique se a versão especificada existe:
```bash
pip search nome-do-pacote
```

---

## 📚 Recursos Adicionais

- [Documentação pip](https://pip.pypa.io/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [pipreqs no GitHub](https://github.com/bndr/pipreqs)

---

## 💡 Dica Final

Para este projeto RAG, o `requirements.txt` já está criado e pronto para uso:

```bash
pip install -r requirements.txt
```

Isso instalará todas as dependências necessárias! 🚀
