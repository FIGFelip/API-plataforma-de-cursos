from fastapi import APIRouter, HTTPException
from schemas.curso import CursoCreate, CursoOut, AlterarPrecoInput
from services.plataforma_services import (
    criar_curso,
    listar_cursos,
    buscar_curso,
    atualizar_preco
)

router = APIRouter(prefix="/curso", tags=["curso"])



@router.post("/", response_model=CursoOut)
def post_curso(data:CursoCreate):
    return criar_curso(data)

@router.get("/", response_model=list[CursoOut])
def get_cursos():
    return listar_cursos()

@router.get("/{codigo}", response_model=CursoOut)
def get_curso_by_id(codigo:int):
    curso = buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code = 404, detail = "curso não encontrado")
    return  curso

@router.put("/{codigo}/preco", response_model = CursoOut)
def put_curso(codigo:int, data:AlterarPrecoInput):
    curso = atualizar_preco(codigo, data.preco)
    if not curso:
        raise HTTPException(status_code = 404, detail = "curso não encontrado")
    return {"codigo": curso.codigo,
            "titulo": curso.titulo,
            "preco": curso.preco,
            "tipo": curso.tipo,
            "desconto_percentual": curso.desconto_percentual
            }



@router.get("/{codigo}/preco_final", response_model=CursoOut)
def get_preco_final(codigo: int):
    curso= buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code = 404, detail = "curso não encontrado")
    return {"codigo": curso.codigo,
            "titulo": curso.titulo,
            "preco": curso.preco_final(),
            "tipo": curso.tipo,
            "desconto_percentual": curso.desconto_percentual
            }