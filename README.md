# Projeto de API com Django Rest Framework

Este projeto foi desenvolvido como parte de um curso da Alura, utilizando a versão mais recente do Django Rest Framework.

## Informações Técnicas

- **Framework**: Django Rest Framework (versão mais atual)
- **Linguagem**: Python

## Funcionalidades da API

A API gerencia três modelos principais:
- **Estudantes**
- **Cursos**
- **Matrículas**

### Rotas Disponíveis

- **Estudantes**: Endpoints para listar, criar, atualizar e deletar estudantes.
- **Cursos**: Endpoints para gerenciamento dos cursos disponíveis.
- **Matrículas**: Controle das matrículas dos estudantes em cursos específicos.
- **Matrículas por Estudante**: Exibe as matrículas de um estudante específico.
- **Matrícula por Cursos**: Exibe os estudantes matriculados em um curso específico.

## Instalação e Uso

1. Clone este repositório:
    ```bash
    git clone https://https://github.com/RaphaelMatias/DRF-Escola.git
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows: `venv\Scripts\activate`
    - No Mac/Linux: `source venv/bin/activate`

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

## Link para o Trello

Todas as informações adicionais sobre o andamento do projeto estão disponíveis no Trello. Acesse o quadro [aqui](https://trello.com/b/WPxbvI0c/django-rest-framework-escola-curso-01).

## Créditos

Este projeto faz parte de um curso oferecido pela **Alura**.

