from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):     #garantiza que los tipos de datos van a corresponder con el que hemos definido
    titulo : str
    autor: str
    paginas: int
    editorial: Optional[str]



@app.get("/")
def index():
    return {"mensaje": "Hola pythonianos"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return{"data":id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return{"message": f"libro {libro.titulo} insertado"}