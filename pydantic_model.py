from pydantic import BaseModel


class ProductDict(BaseModel): 
    id: int
    name: str 
    description: str
    price: float 
    quantity: int