from app.services.crawler import crawl_and_save_products
from app.models.product import Product, ProductCategory

def test_crawl_and_save_products(db_session):
    """
    크롤링한 데이터를 데이터베이스에 저장하는 기능 테스트
    """
    query = "운동화"
    display = 5

    # 크롤링 및 데이터 저장
    crawl_and_save_products(db=db_session, query=query, display=display)

    # 데이터베이스 검증
    category = db_session.query(ProductCategory).filter(ProductCategory.name == query).first()
    assert category is not None, "카테고리가 데이터베이스에 저장되지 않았습니다."

    products = db_session.query(Product).filter(Product.category_id == category.id).all()
    assert len(products) == display, f"저장된 상품 개수가 {display}와 일치하지 않습니다."

    for product in products:
        assert product.name, "상품 이름이 비어 있습니다."
        assert product.price > 0, "상품 가격이 유효하지 않습니다."
        assert product.description, "상품 설명이 비어 있습니다."
