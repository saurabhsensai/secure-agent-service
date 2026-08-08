from sqlalchemy import text 
from app.db.session import engine, SessionLocal

def test_engine_exist():
    assert engine is not None 

def test_create_session():
    db = SessionLocal()
    try: 
        assert db is not None
    finally: 
        db.close() 

def test_database_connection():
    db = SessionLocal()
    try: 
        result = db.execute(text("SELECT 1"))
        assert result.scalar() == 1
    finally: 
        db.close()