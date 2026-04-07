from fastapi import APIRouter, HTTPException
from schemas.aluno import AlunoCreate, AlunoOut
from domain.Aluno import Aluno
from services.plataforma_services import (
    criar_aluno,
    listar_alunos
)

router = APIRouter(prefix="/aluno", tags=["aluno"])

@router.post("/", response_model=AlunoOut)
def post_aluno(data:AlunoCreate):
    return criar_aluno(data)

@router.get("/", response_model=list[AlunoOut])
def get_alunos():
    return listar_alunos()

