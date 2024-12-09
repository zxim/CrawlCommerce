from sqlalchemy import Column, Integer, String
from app.config.db import Base

# Product 테이블 모델 정의
class Product(Base):
    __tablename__ = "products"  #테이블 이름

    id = Column(Integer, primary_key=True, index=True)  #기본키
    name = Column(String, index=True)   #상품명
    price = Column(Integer)
    description = Column(String)