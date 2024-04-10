# Librería API

Una API RESTful para gestionar una librería, construida con FastAPI y SQLAlchemy.

## Características

- CRUD para libros (crear, leer, actualizar, eliminar)
- Conexión con base de datos PostgreSQL
- Validación de datos con Pydantic

## Requisitos

- Python 3.8 o superior
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

## Instalación

Clona el repositorio

```bash
git clone git@github.com:santiecheva/ApiLibreria.git
cd ApiLibreria
```
#Instala las dependencias

```bash
pip install -r requirements.txt
```

# Configuración de la base de datos

en el archivo .env agrega

```
DATABASE_URL=postgresql://username:password@localhost/libreria
```

# ejecución
```
uvicorn app.main:app --reload
```

