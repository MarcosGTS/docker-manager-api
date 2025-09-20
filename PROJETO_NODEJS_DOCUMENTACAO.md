# Docker Manager API - Documentação Completa do Projeto Node.js

## Visão Geral do Projeto
O Docker Manager API é um sistema de gerenciamento de contêineres Docker que permite criar, executar e gerenciar aplicações containerizadas com diferentes configurações de backend e banco de dados. O projeto inclui uma API principal de gerenciamento e aplicações Node.js de exemplo.

## Arquitetura do Sistema

### 1. Aplicação Principal (Docker Manager API)
**Localização**: `/app.js` (raiz do projeto)
**Porta**: 8000
**Framework**: Express.js

#### Tecnologias Utilizadas:
- **Node.js**: Ambiente de runtime
- **Express.js**: Framework web (v4.18.2)
- **CORS**: Middleware para Cross-Origin Resource Sharing (v2.8.5)
- **Mustache Express**: Template engine (v1.3.2)
- **UUID**: Geração de identificadores únicos (v9.0.1)

#### Endpoints da API Principal:

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Página inicial com informações do sistema |
| GET | `/options` | Lista configurações disponíveis |
| GET | `/applications` | Lista aplicações ativas |
| POST | `/up` | Cria e executa uma aplicação containerizada |
| POST | `/down` | Remove uma aplicação containerizada |
| GET | `/script` | Gera e baixa scripts de teste |

### 2. Aplicação Node.js (Backend de Exemplo)
**Localização**: `/applications/node/`
**Porta**: 3000
**Framework**: Express.js

#### Dependências:
- **Express.js**: Framework web (v4.18.2)
- **CORS**: Cross-Origin Resource Sharing (v2.8.5)
- **Sequelize**: ORM para banco de dados (v6.33.0)
- **MySQL2**: Driver MySQL (v3.6.1)
- **pg/pg-hstore**: Driver PostgreSQL (v8.11.0/v2.3.4)
- **Sequelize-CLI**: Ferramenta CLI (v6.6.1) - dev dependency

#### Endpoints da API Node.js (CRUD de Usuários):

| Método | Endpoint | Descrição | Resposta |
|--------|----------|-----------|----------|
| GET | `/` | Informações da API | `{"info": "Basic users API", "paths": ["/users", "/users/:id"]}` |
| GET | `/users` | Lista todos os usuários | Array de usuários |
| GET | `/users/:id` | Busca usuário por ID | Objeto do usuário |
| POST | `/users` | Cria novo usuário | Usuário criado |
| PUT | `/users/:id` | Atualiza usuário | Usuário atualizado |
| DELETE | `/users/:id` | Remove usuário | Resultado da operação |

#### Modelo de Dados (Usuário):
```javascript
{
  id: INTEGER (auto-increment, primary key),
  name: STRING,
  username: STRING,
  email: STRING,
  gender: STRING,
  dateOfBirth: STRING,
  location: STRING,
  createdAt: TIMESTAMP,
  updatedAt: TIMESTAMP
}
```

## Configurações de Banco de Dados

### Configurações Suportadas:
1. **PostgreSQL**: `postgresEnv`
2. **MySQL**: `mysqlEnv`
3. **Test**: Ambiente de teste local
4. **Production**: Ambiente de produção

### Variáveis de Ambiente:
```env
# Node.js
DB_NAME=postgres
DB_PASSWORD=db
DB_PORT=5432
DB_HOST=database
NODE_ENV=postgresEnv

# PostgreSQL
POSTGRES_DB=postgres
POSTGRES_PASSWORD=db

# MySQL
MYSQL_DATABASE=postgres
MYSQL_ROOT_PASSWORD=db
```

## Configurações Docker

### Versões de Imagens:
- **Node.js**: `node:21-alpine3.17`
- **PostgreSQL**: `postgres:16-alpine3.18`
- **MySQL**: `mysql:5.7`

### Configurações de Recursos:
```env
# CPU (aceita frações, ex: 0.5)
BK_CPUS=0.8  # Backend CPU
DB_CPUS=0.8  # Database CPU

# Memória (valores com unidade, ex: 4M)
BK_MEMORY=453M  # Backend Memory
DB_MEMORY=484M  # Database Memory
```

### Composições Docker Disponíveis:
1. `node-postgres` - Node.js + PostgreSQL
2. `node-mysql` - Node.js + MySQL
3. `java-postgres` - Java + PostgreSQL
4. `java-mysql` - Java + MySQL
5. `java-mongo` - Java + MongoDB
6. `python-postgres` - Python + PostgreSQL

## Framework de Testes de Performance (K6)

### Tipos de Teste Disponíveis:
1. **Smoke Test**: 5 usuários por 10 segundos
2. **Load Test**: 100→1000→100 usuários em 16 minutos
3. **Stress Test**: Escalamento gradual até limites
4. **Spike Test**: Picos de 500→5000→500 usuários
5. **Breakpoint Test**: 10.000 usuários por 2 horas
6. **Soak Test**: Teste de resistência prolongado

### Configuração dos Testes:
- **Endpoint Base**: `${__ENV.HOSTNAME}/users`
- **Operações Testadas**: GET, POST, PUT, DELETE
- **Payload**: Objetos de usuário com campos aleatórios
- **Headers**: `Content-Type: application/json`

## Estrutura de Arquivos

```
docker-manager-api/
├── app.js                          # Aplicação principal
├── package.json                    # Dependências da API principal
├── config.env                      # Configurações de recursos
├── api_description.yaml            # Especificação OpenAPI
├── src/                            # Código fonte principal
│   ├── config.js                   # Configurações do sistema
│   ├── dockerManager.js            # Gerenciador de Docker
│   ├── dockerAPI.js                # API Docker
│   ├── application.js              # Classe Application
│   ├── scriptManager.js            # Gerador de scripts
│   └── validation.js               # Validações
├── applications/
│   └── node/                       # Aplicação Node.js exemplo
│       ├── app.js                  # Aplicação Express
│       ├── package.json            # Dependências Node.js
│       ├── queries.js              # Operações CRUD
│       ├── models/                 # Modelos Sequelize
│       │   ├── index.js
│       │   ├── users.js
│       │   └── movies.js
│       └── config/
│           └── config.js           # Configurações BD
├── composers/                      # Docker Compose files
│   ├── node-postgres/
│   ├── node-mysql/
│   └── ...
├── test_files/                     # Scripts de teste K6
│   ├── smoke.js
│   ├── load.js
│   ├── stress.js
│   ├── spike.js
│   ├── breakpoint.js
│   └── soak.js
└── views/                          # Templates Mustache
    └── index.mustache
```

## Informações do Sistema

### Hardware Detectado:
- **CPU**: Modelo e quantidade de cores detectados automaticamente
- **RAM**: Total e disponível em MB
- **Limites configuráveis**: CPU (0.1 - cores disponíveis), RAM (100MB - 1GB)

### URL e Porta:
- **API Principal**: `http://localhost:8000`
- **Aplicações Node.js**: Porta 3000 (mapeada dinamicamente)

## Funcionalidades Principais

### 1. Gerenciamento de Aplicações:
- Criação dinâmica de ambientes containerizados
- Configuração flexível de recursos (CPU/RAM)
- Suporte a múltiplos bancos de dados
- Remoção controlada de aplicações

### 2. Geração de Scripts:
- Scripts de teste personalizados
- Diferentes tipos de carga de trabalho
- Download automático de arquivos de teste

### 3. Interface Web:
- Dashboard com informações do sistema
- Formulários para criação de aplicações
- Monitoramento de recursos

### 4. API RESTful:
- Endpoints bem documentados (OpenAPI 3.0)
- Operações CRUD completas
- Tratamento de erros padronizado

## Como Usar

### 1. Instalar Dependências:
```bash
npm install
```

### 2. Executar API Principal:
```bash
node app.js
# Servidor rodando em http://localhost:8000
```

### 3. Criar Aplicação Node.js:
```bash
# POST /up
{
  "conf": "node-postgres",
  "backend": {"cpu": 0.5, "ram": "200M"},
  "database": {"cpu": 0.3, "ram": "300M"}
}
```

### 4. Executar Testes de Performance:
```bash
k6 run --env HOSTNAME=http://localhost:3000 test_files/smoke.js
```

## Observações Técnicas

- O projeto usa Sequelize com sincronização forçada (`force: true`)
- Retry automático para conexão com banco de dados (delay de 5s)
- Templates Mustache para renderização de páginas
- Validação de dados implementada
- Sistema de logs para depuração
- Arquitetura modular e extensível

Esta documentação cobre todas as configurações Node.js, versões, endpoints, operações e estrutura do projeto Docker Manager API.