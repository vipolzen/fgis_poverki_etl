import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
try:
    load_dotenv()
    db_url = os.getenv("DB_URL")
    engine = create_engine(db_url)
    with engine.begin() as connection:
        pass
    print(engine)
except Exception as e:
    print(f"[ERROR INFO] Ошибка подключения: {e}")
