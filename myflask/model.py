from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class ToDo(Base):
    __tablename__ = 'ToDo'
    id = Column(Integer, primary_key = True)
    content = Column(String)
    date = Column(String)

