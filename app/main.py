from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/libros/", response_model=schemas.Libro)
def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db=db, libro=libro)

@app.get("/libros/", response_model=list[schemas.Libro])
def read_libros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    libros = crud.get_libros(db, skip=skip, limit=limit)
    return libros

@app.get("/libros/{libro_id}", response_model=schemas.Libro)
def read_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = crud.get_libro(db, libro_id=libro_id)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro not found")
    return db_libro

@app.put("/libros/{libro_id}", response_model=schemas.Libro)
def update_libro(libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    db_libro = crud.update_libro(db, libro_id=libro_id, libro=libro)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro not found")
    return db_libro

@app.delete("/libros/{libro_id}", response_model=schemas.Libro)
def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = crud.delete_libro(db, libro_id=libro_id)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro not found")
    return db_libro
