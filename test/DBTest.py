from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:Password@localhost:5432/BPO"

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        print("Connected!")
except Exception as e:
    print("Connection failed:", e)
