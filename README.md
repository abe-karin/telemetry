# 📡 Telemetry Mini Service

> Serviço minimalista orientado a eventos, projetado para demonstrar **modelagem de domínio**, **observabilidade** e **análise de dados**, com foco em **engenharia de plataformas e operações**.

---

## 🎯 Objetivo do projeto

Este projeto tem como objetivo demonstrar **como projetar um sistema observável desde a concepção**, priorizando:

- Modelagem correta de eventos
- Separação clara entre domínio e infraestrutura
- Observabilidade real (logs, métricas e dados históricos)
- Operabilidade via containers
- Extração de conhecimento a partir de dados

> O foco **não é a complexidade funcional**, mas a **qualidade arquitetural**.

---

## 🧠 Conceito central

O sistema é orientado a um único conceito:

> **Toda ação de usuário é registrada como um evento imutável.**

Esses eventos:
- Geram logs estruturados
- Alimentam métricas agregadas
- São persistidos para análise posterior

---

## 🏗️ Arquitetura (visão lógica)
```
Cliente
↓
API (FastAPI)
↓
Evento de Domínio
↓
Logs estruturados
↓
Métricas (Prometheus)
↓
Persistência (SQLite)
↓
Análise (Jupyter Notebook)
```
---

## 📦 Estrutura do projeto

```text
telemetry-mini-service/
│
├── app/
│   ├── main.py                  # API FastAPI
│   ├── models.py                # Evento de domínio
│   ├── logging_config.py        # Logs estruturados (JSON)
│   │
│   ├── services/
│   │   └── event_service.py     # Coordenação de domínio
│   │
│   ├── repository/
│   │   └── events_repository.py # Persistência (SQLite)
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   └── observability/
│       └── metrics.py           # Métricas Prometheus
│
├── notebooks/
│   └── telemetry_analysis.ipynb # Análise de eventos
│
├── monitoring/
│   └── prometheus.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

```

🧩 Evento de domínio
UserActionEvent
event_id   : UUID
user_id    : string
action     : string
timestamp  : datetime (UTC)
source     : string
metadata   : JSON (livre)


Princípios adotados

Eventos são imutáveis

Eventos descrevem fatos, não interpretações

metadata é flexível por design

O evento não depende de banco ou framework

🔍 Observabilidade
Logs

Formato JSON

Um log para cada evento criado

Facilmente integrável a stacks de logging

Métricas (Prometheus)

Métricas técnicas:

Total de requisições

Latência por endpoint

Métricas de domínio:

Total de ações

Ações por tipo

Ações por origem

Métricas são usadas para padrões e alertas, não para análise detalhada.

📊 Análise de dados

Os eventos persistidos em SQLite são analisados via Jupyter Notebook, permitindo:

Identificação de padrões de uso

Análise temporal

Exploração de metadata

Geração de insights sem alterar o código do serviço

Essa separação demonstra a diferença entre:

Observabilidade em tempo real

Análise histórica de dados

🐳 Execução com Docker
Subir o ambiente completo
```
docker compose up --build
```

Serviços disponíveis

API: http://localhost:8000/docs

Métricas: http://localhost:8000/metrics

Prometheus: http://localhost:9090



