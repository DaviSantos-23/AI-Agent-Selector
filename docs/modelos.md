# Modelos Utilizados

## Objetivo

Cada funcionalidade utiliza um modelo especializado da Hugging Face.

---

# Gerador de Texto

Função:

Produzir novos textos a partir de um prompt.

Aplicações

- artigos
- histórias
- conteúdos
- ideias
- documentação

---

# Resumidor

Função

Gerar resumos automáticos.

Aplicações

- artigos científicos
- notícias
- documentos
- livros
- textos longos

---

# Chat

Função

Responder perguntas de forma conversacional.

Aplicações

- assistentes virtuais
- suporte
- educação
- atendimento

---

# Comparação

| Modelo          | Finalidade         |
| --------------- | ------------------ |
| Text Generation | Criar novos textos |
| Summarization   | Resumir conteúdos  |
| Chat Completion | Conversação        |

---

# Como adicionar um novo agente

1. Criar um novo arquivo em

```
src/agents/
```

Exemplo

```
hfapi_translation.py
```

2. Implementar a chamada da API.

3. Adicionar a opção na interface Streamlit.

4. Testar.

---

# Possíveis melhorias

- Tradução automática
- Correção gramatical
- Classificação de textos
- Extração de entidades
- Análise de sentimentos
- OCR
- Perguntas sobre documentos
