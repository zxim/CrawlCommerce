from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base 

class ProductCategory(Base):
    __tablename__ = "product_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    # Relationship: 하나의 카테고리에 여러 상품 연결
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    image_url = Column(String(255))  # 상품 이미지 URL
    details = Column(Text)  # 상세 설명
    category_id = Column(Integer, ForeignKey("product_category.id"))

    # Relationship: 상품이 카테고리에 속함
    category = relationship("ProductCategory", back_populates="products")
