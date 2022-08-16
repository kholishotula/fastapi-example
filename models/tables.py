from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean

class Table(Base):
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(10))
    status = Column(Boolean)