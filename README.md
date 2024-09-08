# ToDo List Project

Um projeto de lista de tarefas que permite aos usuários criar, listar, editar e excluir tarefas, com filtros por data e status, além de uma barra de busca.

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite3
- **Estilização:** Bootstrap 4

## 🚀 Instruções para o Uso

### Pré-requisitos

- Python 3.x instalado
- Django instalado (pode ser instalado via `pip install django`)

### Configuração do Ambiente

1. Clone este repositório:

    ```bash
    git clone https://github.com/davimesquit/ToDoList-cbLab.git
    ```

2. Navegue até a pasta do projeto:

    ```bash
    cd ToDoList-cbLab
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Banco de dados: O projeto utiliza o SQLite3 por padrão. Não há necessidade de configuração adicional para o banco de dados.

5. Execute as migrações:

    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    A aplicação estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 📖 Funcionalidades

- **Criar Tarefas:** Utilize o formulário disponível para adicionar novas tarefas.
- **Listar Tarefas:** Visualize todas as tarefas cadastradas com opções de filtro por data e status.
- **Editar Tarefas:** Modifique detalhes de uma tarefa existente.
- **Excluir Tarefas:** Remova tarefas da lista.

## Endpoints

- `/ `: Página principal que lista todas as tarefas.
- `/create/`: Página para criar novas tarefas.
- `/manage_tarefa/<id>/`: Página para editar ou excluir uma tarefa existente.

## 🧪 Testes

Para verificar a cobertura de testes, siga as etapas,

1. Instale o coverage:

```bash
pip install coverage
```

2. Gere o relatório de cobertura

```bash
coverage report
```

3. Pra uma visualização detalhada, você pode gerar um relatório em HTML e mudar o diretório:

```bash
coverage html
cd htmlcov
```
4. Em seguida utilize o servidor python para vicualizar no seu navegador

```bash
python -m http.server
```
5. E então o relatório em HTML estará rodando na porta http://localhost:8000/


