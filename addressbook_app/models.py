from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from .database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)