# API Plataforma de Cursos
 ativiade feita em sala de api rest com fastapi

## Configurando o ambiente
### Ativando o venv
"""
python3 venv .venv
source .venv/bin/activate
"""

## Instalando bibliotecas necessárias
"""
pip install uvicorn fastapi[standard]
"""

## Utilizando a API
Para iniciar a API utilize o comando:
"""
uvicorn main:app --reload
"""

## Endpoints:
### Aluno
"""
POST/aluno
GET/alunos
"""

### Curso
"""
POST/ curso
GET/ cursos
GET/{codigo}/ curso
PUT/{codigo}/preco/ curso
GET/{codigo}/preco_final/ curso
"""