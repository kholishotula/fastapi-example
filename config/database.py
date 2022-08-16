from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

SQLALCHEMY_MYSQL_URL = 'mysql+pymysql://root@localhost:3306/fastapi_example'

mysql_engine = create_engine(SQLALCHEMY_MYSQL_URL)
mysql_SessionLocal = sessionmaker(bind=mysql_engine, autocommit=False, autoflush=False)

def get_mysql_db():
    db = mysql_SessionLocal()
    try:
        yield db
    finally:
        db.close()