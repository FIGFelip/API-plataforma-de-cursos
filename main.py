from fastapi import FastAPI
from api.routes.curso import router as curso_router
from api.routes.aluno import router as aluno_router

app=FastAPI(title="plataforma cursos")



@app.get("/")
def home():
    return {"message":"Api rodando"}



app.include_router(curso_router)
app.include_router(aluno_router)

