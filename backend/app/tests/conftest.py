import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.db import Base

# 테스트 데이터베이스 URL
TEST_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/testdb"

# SQLAlchemy 엔진 및 세션 설정
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """
    각 테스트 함수마다 새로운 데이터베이스 세션을 제공합니다.
    """
    # 데이터베이스 테이블 생성
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # 테스트 후 데이터베이스 테이블 삭제
        Base.metadata.drop_all(bind=engine)
