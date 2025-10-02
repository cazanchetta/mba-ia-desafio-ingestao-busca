# Desafio MBA Engenharia de Software com IA - Full Cycle

Descreva abaixo como executar a sua solução.

Este projeto permite fazer perguntas a partir de um **PDF ingerido e vetorizado** em um banco **Postgres com PGVector**.  
As respostas vêm somente do conteúdo do PDF. Se a informação não existir, retorna:  
`Não tenho informações necessárias para responder sua pergunta.`

---

## ⚙️ Configuração

1. Crie um arquivo `.env` na raiz com as variáveis:

```env
GOOGLE_API_KEY=
GOOGLE_EMBEDDING_MODEL='models/embedding-001'

OPENAI_API_KEY=
OPENAI_EMBEDDING_MODEL='text-embedding-3-small'

DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/meubanco
PG_VECTOR_COLLECTION_NAME=gpt5_collection

PDF_PATH=/caminho/para/arquivo.pdf
```

2. Suba um banco Postgres com PGVector (exemplo com Docker):

```bash
docker run --name pgvector -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -p 5432:5432 ankane/pgvector
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Execução

### 1. Ingerir o PDF
```bash
python ingest.py
```

### 2. Fazer perguntas
- **Interativo:**
```bash
python chat.py
```

### 3. Encerrar
Para sair do modo interativo do sistema basta digitar 'sair' e o sistema se encerrará.

---

## 📋 Exemplos

Pergunta dentro do contexto:
```
PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.
```

Pergunta fora do contexto:
```
PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```
