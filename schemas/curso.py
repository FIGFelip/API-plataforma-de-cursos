from pydantic import BaseModel


class CursoCreate(BaseModel):
    titulo:str
    preco:float
    tipo:int
    desconto_percentual:float=0.0


class AlterarPrecoInput(BaseModel):
    preco: float


class CursoOut(BaseModel):
    codigo:int
    titulo:str
    preco:float
    tipo:int
    desconto_percentual:float=0.0
    
    class Config:
        from_attributes=True
