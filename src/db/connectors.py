import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DB_URL")
engine = create_engine(db_url,  pool_size = 5, max_overflow = 10, pool_pre_ping = True)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, blind = engine)

Base = declarative_base()

def get_db():
    '''Генерация сессий'''
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def test_connection():
    try:
        with engine.connect() as conn:
            print("Соединение с базой данных успешно произведено")
        return True
    except SQLAlchemyError as e:
        print(f'Ошибка соединения с базой данных: {e}')
        return False

def init_db():
    Base.metadata.create_all(bind= engine)