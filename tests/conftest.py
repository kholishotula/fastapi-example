from config.database import get_db
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app

SQLALCHEMY_DB_TEST_URL = 'mysql+pymysql://root@localhost:3306/fastapi_example_test'
test_engine = create_engine(SQLALCHEMY_DB_TEST_URL)
test_session = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db_test = test_session()
    try:
        yield db_test
    finally:
        db_test.close()

Base.metadata.drop_all(test_engine)
Base.metadata.create_all(test_engine)

test_app = app
test_app.dependency_overrides[get_db] = override_get_db