# Daily Diet API

Uma API REST para controle de dieta diária, desenvolvida com Flask e MySQL. Esta API permite registrar refeições, marcar se estão dentro da dieta e consultar o histórico alimentar.

## 🚀 Tecnologias

- Python 3.13
- Flask
- MySQL
- Docker
- SQLAlchemy
- PyMySQL

## 📋 Pré-requisitos

- Python 3.13 ou superior
- Docker e Docker Compose
- Git

## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone [seu-repositorio]
cd daily-diet-api
```

### 2. Crie e ative um ambiente virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Inicie o container do MySQL
```bash
docker-compose up -d
```

### 5. Configure o banco de dados
```bash
# Entre no Flask shell
flask shell

# No shell do Flask, execute:
from app import db
db.create_all()
exit()
```

### 6. Inicie a aplicação
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## 📌 Endpoints

### Registrar Refeição
```http
POST /registerMeal
```
Body:
```json
{
    "name": "Café da manhã",
    "description": "Pão integral com ovo",
    "inDiet": true
}
```

### Listar Todas as Refeições
```http
GET /getAllMeals
```

### Buscar Refeição por ID
```http
GET /getMeal/<id>
```

### Atualizar Refeição
```http
PUT /updateMeal/<id>
```
Body:
```json
{
    "name": "Novo nome",
    "description": "Nova descrição",
    "inDiet": false
}
```

## 🗃️ Estrutura do Banco de Dados

### Tabela: Meal
- `id`: INT (Primary Key)
- `name`: VARCHAR(80)
- `description`: VARCHAR(200)
- `data_time`: DATETIME
- `inDiet`: BOOLEAN

## 🛠️ Configuração do Ambiente de Desenvolvimento

### Variáveis de Ambiente
O projeto usa as seguintes configurações de banco de dados:
- Host: localhost
- Porta: 3306
- Usuário: root
- Senha: admin123
- Banco de dados: daily_diet

### Docker
O arquivo `docker-compose.yml` configura:
- MySQL 8.0
- Porta exposta: 3306
- Volume persistente para dados

## ⚠️ Possíveis Erros e Soluções

### Erro de Conexão com MySQL
Se encontrar erro de conexão:
1. Verifique se o container está rodando:
```bash
docker ps
```
2. Verifique os logs do container:
```bash
docker logs [container-id]
```

### Erro ao Criar Tabelas
Se encontrar erro ao criar tabelas:
1. Verifique se o banco existe:
```bash
docker exec -it [container-id] mysql -u root -padmin123
SHOW DATABASES;
```
2. Recrie o banco se necessário:
```sql
CREATE DATABASE daily_diet CHARACTER SET utf8mb4;
```

## 🤝 Contribuindo

1. Faça o fork do projeto
2. Crie sua feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
