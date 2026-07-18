# Arquitetura do Sistema

## Objetivo

Disponibilizar uma única interface capaz de acessar diferentes modelos de Inteligência Artificial da Hugging Face.

---

# Arquitetura

```
                Usuário
                    │
                    ▼
           Interface Streamlit
                    │
                    ▼
          Seleção do Agente IA
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
 Gerar Texto   Resumir Texto    Chat
     │              │              │
     └──────────────┼──────────────┘
                    ▼
           Hugging Face API
                    │
                    ▼
          Modelo de Linguagem
                    │
                    ▼
             Resposta Final
```

---

## Componentes

### Interface

Responsável pela interação com o usuário.

---

### Agentes

Cada agente executa uma tarefa específica.

- Geração de Texto
- Resumo
- Chat

---

### API

Responsável pela comunicação com a Hugging Face.

---

### Modelos

Executam a inferência de Inteligência Artificial.

---

## Benefícios

- Arquitetura modular
- Fácil manutenção
- Fácil expansão
- Reutilização de código
- Baixo acoplamento
