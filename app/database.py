from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DB_URL = 'sqlite:///./blog.db'

# sqlite_engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(bind=sqlite_engine, autocommit=False, autoflush=False)

Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

SQLALCHEMY_MYSQL_URL = 'mysql+pymysql://root@localhost:3306/fastapi_example'

mysql_engine = create_engine(SQLALCHEMY_MYSQL_URL)
mysql_SessionLocal = sessionmaker(bind=mysql_engine, autocommit=False, autoflush=False)

def get_mysql_db():
    db = mysql_SessionLocal()
    try:
        yield db
    finally:
        db.close()