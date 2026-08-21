import os 
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

# print(DATABASE_URL)
if not DATABASE_URL: 
    raise ValueError("Database_url is not set")


engine = create_engine(DATABASE_URL)

session = sessionmaker(
    autocommit=False,
    autoflush=False, 
    bind=engine
)