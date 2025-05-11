from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_USER = "root" 
DB_PASSWORD = ""  
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "iot_database"

BASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
SQLALCHEMY_DATABASE_URL = f"{BASE_URL}{DB_NAME}"

def create_database():
    temp_engine = create_engine(BASE_URL)
    
    try:
        with temp_engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
            conn.commit()
            logger.info(f"Banco de dados '{DB_NAME}' verificado/criado com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao criar banco de dados: {e}")
        raise

create_database()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True, 
    echo=False  
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()