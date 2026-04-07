class Aluno:
    _seq=1
    def __init__(self, nome:str, email:str):
        self._codigo=Aluno._seq
        Aluno._seq+=1
        self.nome=nome
        self.email=email

    @property
    def codigo(self)->int:
        return self._codigo
    
    class Config:
        from_attributes=True
    
    