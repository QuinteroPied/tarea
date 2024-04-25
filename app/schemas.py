from pydantic import BaseModel

class LibroBase(BaseModel):
    titulo: str
    autor: str
    descripcion: str

class LibroCreate(LibroBase):
    pass

class Libro(LibroBase):
    id: int

    class Config:
        orm_mode = True # mapeando las relaciones a traves de objetos

# Esto es lo que se va a ver en la web.

# La librería Sql alchemy es la librería de orm que estamos usando (object relational maping)
 
# Listo