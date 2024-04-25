from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 

#import os
#from dotenv import load_dotenv
#load_dotenv()
#DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine('postgresql://postgres:caqp1007239955@localhost/libreria') # debería estar guardada en un lugar secreto (quemada)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Ya estamos conectados 
# Ver la guía de como crear las bases de datos a travez de Sql Alchemy

# LISTO 