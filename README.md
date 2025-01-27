# Sistema de Organização de Eventos

Este repositório contém a implementação de um sistema de gerenciamento de eventos e participantes utilizando FastAPI. O sistema permite criar, atualizar, listar e excluir eventos e participantes, com funcionalidades que seguem boas práticas de organização e divisão de responsabilidades.

---

## Estrutura do Projeto

- **Controllers**:
  - `event_controller.py`: Controlador para gerenciar endpoints relacionados aos eventos.
  - `participant_controller.py`: Controlador para gerenciar endpoints relacionados aos participantes.

- **Models**:
  - `event.py`: Classe representando o modelo de um evento.
  - `participant.py`: Classe representando o modelo de um participante.

- **DAOs**:
  - `event_dao.py`: Classe para gerenciar operações de persistência relacionadas aos eventos.
  - `participant_dao.py`: Classe para gerenciar operações de persistência relacionadas aos participantes.

- **Services**:
  - `event_service.py`: Contém a lógica de negócios relacionada aos eventos.
  - `participant_service.py`: Contém a lógica de negócios relacionada aos participantes.

- **Main**:
  - `main.py`: Arquivo principal que inicializa o servidor FastAPI e registra as rotas.

---

## Funcionalidades

### **Eventos**
- **Endpoints**:
  - **POST `/events/`**: Criação de novos eventos.
  - **GET `/events/listar`**: Listagem de todos os eventos.
  - **GET `/events/listar/{id}`**: Busca por evento específico com base no ID.
  - **PUT `/events/{id}/updated`**: Atualização de informações de um evento.
  - **DELETE `/events/{id}/delete`**: Exclusão de eventos com base no ID.

- **Atributos**:
  - `id` (int): Identificador único do evento.
  - `name` (str): Nome do evento.
  - `date` (str): Data do evento.

---

### **Participantes**
- **Endpoints**:
  - **POST `/participants/`**: Registro de novos participantes.
  - **GET `/participants/{event_id}`**: Listagem de participantes de um evento específico.
  - **GET `/participants/{id}/ola`**: Busca de participante pelo ID.
  - **PUT `/participants/{id}/updated`**: Atualização de informações de um participante.
  - **DELETE `/participants/{id}/delete`**: Exclusão de participantes com base no ID.

- **Atributos**:
  - `id` (int): Identificador único do participante.
  - `name` (str): Nome do participante.
  - `event_id` (int): ID do evento associado.

---

## Tecnologias Utilizadas
- **FastAPI**: Framework para criação de APIs rápidas e performáticas.
- **Python**: Linguagem principal utilizada no projeto.

---

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-eventos.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd sistema-eventos
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```

- **Exemplos de Uso:**
- Criação de um Evento

- Requisição (POST /events/):
   ```bash
   {
     "id": 1,
     "name": "Workshop de Python",
     "date": "2025-02-01"
   }
   ```
- Resposta:
   ```bash
   {
     "message": "Evento criado com sucesso!",
     "event": {
       "id": 1,
       "name": "Workshop de Python",
       "date": "2025-02-01"
     }
   }
   ```
## Finalização
- Feito por:
- Maria Carolina de Araújo de Sousa
- Taíssa Moreira da Silva
