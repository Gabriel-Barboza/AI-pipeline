# 🌸 AI Pipeline - Iris Classification

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green.svg)](https://scikit-learn.org/)
[![ONNX](https://img.shields.io/badge/ONNX-Optimized-orange.svg)](https://onnx.ai/)
[![GCP](https://img.shields.io/badge/Deploy-GCP-4285F4.svg)](https://cloud.google.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

## 📋 Sobre o Projeto

Este repositório contém um estudo sobre  **pipeline de Inteligência Artificial** para classificação de espécies da flor Íris (Setosa, Versicolor e Virginica). O projeto implementa um modelo de
Machine Learning utilizando Random Forest Classifier, treinado com o clássico dataset Iris e exportado para o formato ONNX para otimização de inferência em produção.

O modelo foi desenvolvido seguindo as melhores práticas de MLOps, inclui uma API REST completa com FastAPI e está deployado no Google Cloud Platform (GCP) com CI/CD automatizado, permitindo inferências rápidas e escaláveis.

## 🎯 Objetivos

- Classificar espécies de flores Íris com base em características morfológicas
- Implementar um pipeline de ML reproduzível e escalável
- Criar uma API REST profissional com FastAPI
- Otimizar o modelo para inferência em produção usando ONNX
- Deploy automatizado em ambiente cloud (GCP) com CI/CD

## 🌟 Características Principais

- **Modelo**: Random Forest Classifier
- **Dataset**: Iris Dataset (150 amostras, 4 features)
- **API**: FastAPI com documentação automática (Swagger/OpenAPI)
- **Formato de Exportação**: ONNX (Open Neural Network Exchange)
- **Deploy**: Google Cloud Run (serverless)
- **CI/CD**: Google Cloud Build com deploy automático
- **Containerização**: Docker com imagem otimizada
- **Tracking**: MLflow para rastreamento de experimentos
- **Testes**: Pytest para testes automatizados



## 📁 Estrutura do Projeto

```
AI-pipeline/
├── src/                        # Código fonte principal
│   ├── api/                    # API FastAPI
│   │   ├── __init__.py
│   │   ├── app.py              # Endpoints e lógica da API
│   │   └── baseModel.py        # modelo apra o JSON
│   │
│   └── training/               # Scripts de ML
│       ├── __init__.py
│       ├── pipeline_data.py    # Preparação dos dados
│       └── train_model.py      # Treinamento do modelo
│
├── data/                       # Dados processados (criado automaticamente)
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
│
├── models/                     # Modelos treinados
│   ├── model.onnx              # Modelo otimizado para API
│   └── model.pkl               # Modelo Scikit-learn original
│
├── tests/                      # Testes automatizados
│   ├── __init__.py
│   └── test_app.py             # Testes da API
│
├── .dockerignore               # Exclusões do Docker
├── .gitignore                  # Exclusões do Git
├── cloudbuild.yaml             # Pipeline CI/CD (Cloud Build)
├── Dockerfile                  # Imagem Docker da API
├── README.md                   # Este arquivo
├── requirements.txt            # Dependências (desenvolvimento/treino)
└── requirements-api.txt        # Dependências mínimas (API/produção)
```

## 📦 Configuração do Ambiente Local

### Pré-requisitos

- **Python 3.11 ou superior**: [Instalar Python](https://www.python.org/downloads/)
- **pip**: Gerenciador de pacotes Python (vem com Python)
- **Docker Desktop**: [Instalar Docker](https://www.docker.com/products/docker-desktop/)
- **(Opcional) Google Cloud SDK**: Para deploy no GCP - [Instalar gcloud](https://cloud.google.com/sdk/install)

### Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/Gabriel-Barboza/AI-pipeline.git
cd AI-pipeline
```

2. **Crie e ative um ambiente virtual:**

```bash
# Criar o ambiente virtual 
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (CMD):
venv\Scripts\activate.bat

# Linux/macOS:
source venv/bin/activate
```

3. **Instale as dependências de desenvolvimento:**

```bash
pip install -r requirements.txt -r requirements-api.txt
```


## 💻 Executando Localmente

Certifique-se de que seu ambiente virtual está ativado antes de executar os comandos.

### 1. Preparar os Dados

Este script cria os arquivos CSV na pasta `data/` (a pasta é criada automaticamente).

```bash
cd src/training
python pipeline_data.py
```

### 2. Treinar o Modelo

Este script treina o modelo, salva `model.pkl` e `model.onnx` na pasta `models/`, e registra no MLflow (pasta `mlruns/`).

```bash
python train_model.py
cd ../..  # Voltar para a raiz
```

### 3. Rodar os Testes da API

Verifica se a API carrega o modelo ONNX e responde corretamente.

```bash
python -m pytest
```

### 4. Rodar a API Localmente

Inicia o servidor FastAPI na sua máquina.

```bash
uvicorn src.api.app:app --reload
```

Acesse a documentação interativa em: **http://127.0.0.1:8000/docs**

## 🐳 Executando com Docker

### 1. Construir a Imagem Docker

```bash
docker build -t ai-pipeline-super-slim:latest .
```

### 2. Rodar o Container

```bash
docker run --rm -it -p 8000:8080 ai-pipeline-super-slim:latest
```

Acesse a API em: **http://127.0.0.1:8000/docs**


### Deploy Automático (CI/CD com Cloud Build)

Este projeto está configurado para **deploy automático** via Google Cloud Build.

#### Configuração:

1. O arquivo `cloudbuild.yaml` define os passos de build, push e deploy
2. Um **Gatilho (Trigger)** no Cloud Build monitora a branch `main` do repositório GitHub



## 🔌 Como Usar a API


**Resposta Esperada:**

```json
{"prediction":"setosa"}
```

### Exemplo com Python
url = https://iris-ml-api-783760059487.us-central1.run.app/docs
Acesse `/docs` na URL da sua API para explorar a documentação Swagger/OpenAPI interativa
```python
import requests


data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

response = requests.post(url, json=data)
print(response.json())  # {'prediction': 'setosa'}
```


## 👤 Autor

**Gabriel Barboza**

- GitHub: [@Gabriel-Barboza](https://github.com/Gabriel-Barboza)




⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Made with ❤️by Gabriel Barboza**
