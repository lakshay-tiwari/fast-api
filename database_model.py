from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Float
from database import engine

class Base(DeclarativeBase):
    pass 

class Product(Base): 
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
    sell: Mapped[int] = mapped_column(server_default="0")
    shopkeeper_name: Mapped[str] = mapped_column(nullable=False, server_default="xyz")

    # id = Column( Integer, primary_key=True, index=True)
    # name = Column(String)
    # description = Column(String)
    # price = Column(Float)
    # quantity = Column(Integer)
