from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.schema.model import Base

DATABASE_URL = "mysql+pymysql://root:12345@localhost/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)