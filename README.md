# Aplicação Web com Docker - Documentação Completa

## Índice
1. [Descrição da Aplicação](#descrição-da-aplicação)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Detalhes da Implementação](#detalhes-da-implementação)
5. [Implantação no Docker](#implantação-no-docker)
6. [Como Executar](#como-executar)

---

## Descrição da Aplicação

Esta é uma **aplicação web simples** desenvolvida em Python utilizando o framework Flask. A aplicação consiste em uma página web que exibe informações sobre o container Docker em execução, confirmando que todos os requisitos da atividade foram atendidos.

### Funcionalidades:
- Página web acessível via navegador
- Exibe o nome/hostname do container Docker
- Interface responsiva com design moderno
- Confirma visualmente todos os requisitos da atividade

### Objetivo:
Demonstrar a criação, construção e execução de uma aplicação containerizada com Docker, incluindo mapeamento de portas e acesso remoto via navegador.

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.9 | Linguagem de programação |
| **Flask** | 2.3.3 | Framework web minimalista |
| **Docker** | Latest | Plataforma de containerização |
| **Git** | Latest | Controle de versão |

---

## Estrutura do Projeto

```
minha-app-docker/
│
├── Dockerfile              # Instruções para construir a imagem Docker
├── app.py                  # Código da aplicação Flask
├── requirements.txt        # Dependências Python
└── README.md              # Este documento
```

---

## 🔍 Detalhes da Implementação

### 1. **Dockerfile**

O Dockerfile define como a imagem Docker será construída:

```dockerfile
FROM python:3.9-slim        # Imagem base leve do Python
WORKDIR /app                # Define diretório de trabalho
COPY app.py .               # Copia arquivo da aplicação
COPY requirements.txt .     # Copia dependências
RUN pip install --no-cache-dir -r requirements.txt  # Instala dependências
EXPOSE 5000                 # Expõe a porta 5000
CMD ["python", "app.py"]    # Comando para executar a aplicação
```

**Escolhas técnicas:**
- `python:3.9-slim`: Imagem base otimizada (menor tamanho)
- `WORKDIR /app`: Organização e isolamento dos arquivos
- `EXPOSE 5000`: Documenta a porta utilizada pela aplicação
- `--no-cache-dir`: Reduz o tamanho da imagem final

### 2. **Aplicação Flask (app.py)**

Aplicação web minimalista que:
- Cria um servidor web na porta 5000
- Responde requisições HTTP com uma página HTML
- Captura e exibe o hostname do container
- Utiliza `host='0.0.0.0'` para aceitar conexões externas

**Endpoint:**
- `GET /` - Retorna página HTML com informações do container

### 3. **Dependências (requirements.txt)**

```
Flask==2.3.3
Werkzeug==2.3.7
```

---

## Implantação no Docker

### Passo 1: Construção da Imagem

```bash
docker build -t minha-app-web .
```

### Passo 2: Execução do Container

```bash
docker run -d -p 8080:5000 --name meu-container minha-app-web
```

**Mapeamento de Portas:**
```
Host (seu computador) → Container (Docker)
localhost:8080        → aplicação:5000
```
---

## Como Executar

### Passo a Passo:

1. **Clonar o repositório:**
```bash
git clone https://github.com/KaioMelo78/docker-ifto.git
cd minha-app-docker
```

2. **Construir a imagem Docker:**
```bash
docker build -t minha-app-web .
```

3. **Executar o container:**
```bash
docker run -d -p 8080:5000 --name meu-container minha-app-web
```

4. **Acessar no navegador:**
```
http://localhost:8080
```
