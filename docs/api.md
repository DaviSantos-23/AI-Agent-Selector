# API da Hugging Face

## Visão Geral

Este projeto utiliza a API Inference da Hugging Face para executar diferentes tarefas de Inteligência Artificial.

Cada funcionalidade utiliza um endpoint específico da API.

---

## Funcionalidades Disponíveis

### 📝 Geração de Texto

Responsável por produzir textos a partir de um prompt informado pelo usuário.

Exemplo:

Entrada

```
Explique a Teoria da Relatividade.
```

Saída

```
A Teoria da Relatividade foi proposta por Albert Einstein...
```

---

### 📚 Resumo de Texto

Recebe um texto longo e retorna um resumo.

Exemplo

Entrada

```
Texto com várias páginas...
```

Saída

```
Resumo do conteúdo.
```

---

### 💬 Chat Conversacional

Permite ao usuário conversar com um modelo de linguagem.

Exemplo

Usuário:

```
O que é Machine Learning?
```

Resposta:

```
Machine Learning é uma área da Inteligência Artificial...
```

---

## Autenticação

A autenticação é realizada utilizando um Token da Hugging Face.

A chave é armazenada no arquivo:

```
.env
```

Exemplo

```
HF_API_KEY=xxxxxxxxxxxxxxxx
```

---

## Bibliotecas Utilizadas

- requests
- python-dotenv

---

## Fluxo da API

Usuário

↓

Interface Streamlit

↓

Requisição HTTP

↓

API Hugging Face

↓

Modelo Selecionado

↓

Resposta
