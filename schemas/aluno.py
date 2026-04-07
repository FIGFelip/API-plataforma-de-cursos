from pydantic import EmailStr
from pydantic import BaseModel
from uuid import uuid4

class AlunoCreate(BaseModel):
    nome:str
    email: EmailStr


class AlunoOut(BaseModel):
    codigo:int
    nome:str
    email: EmailStr