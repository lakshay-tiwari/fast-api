from database import session, engine
from database_model import Product, Base
from fastapi import FastAPI, Request, Response, Depends
from sqlalchemy.orm import Session
from pydantic_model import ProductDict 
app = FastAPI() 

Base.metadata.create_all(bind=engine)
db = session()


def get_db(): 
    db = session()
    try: 
        yield db 
    finally: 
        db.close()

# create product 
@app.post("/products")
def create_product(product: ProductDict, db: Session = Depends(get_db)): 
    db_product = Product(**product.model_dump())
    try: 
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return {
            "message": "Created Successfully",
            "products": db_product
        }

    except Exception as Error:
        db.rollback()
        print(Error)
        raise


