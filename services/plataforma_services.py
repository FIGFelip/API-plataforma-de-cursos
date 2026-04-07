from domain.Aluno import Aluno
from domain.Curso import Curso
from repositories.memory import db


def criar_aluno(data):
    aluno = Aluno(nome=data.nome, email=data.nome)
    db.alunos[data.id]=aluno
    return aluno

def listar_alunos():
    return db.alunos.values()


def criar_curso(data)->Curso:
    curso = Curso(
        id=data.id,
        titulo=data.titulo,
        preco=data.preco,
        tipo=data.tipo
    )
    db.cursos[data.id]=curso
    return curso

def listar_cursos():
    return list(db.cursos.values())

def buscar_curso(id:int):
    curso=db.cursos.get(id)
    if not curso:
        raise ValueError("Curso não encontrado")
    return curso

def atualizar_preco(id:int, novo_preco:float):
    curso=db.cursos.get(id)
    if not curso:
        return None
    if novo_preco<0:
        raise ValueError("Preço deve ser maior que zero(0)")
    curso.preco=novo_preco
    return curso
