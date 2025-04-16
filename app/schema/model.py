from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
    __tablename__='product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    phone = Column(String(50))
    city = Column(String(50))