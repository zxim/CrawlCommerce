import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.db import Base, get_db
from app.models.product import Product, ProductCategory


TEST_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/testdb"

# 테스트용 엔진과 세션
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """
    각 테스트 함수마다 새로운 데이터베이스 세션을 제공합니다.
    """
    Base.metadata.create_all(bind=engine)  # 테이블 생성
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)  # 테스트 후 테이블 삭제
