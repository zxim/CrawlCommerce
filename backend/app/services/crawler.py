from sqlalchemy.orm import Session
from app.models.product import Product, ProductCategory
from app.services.naver_api import fetch_products_from_naver

def crawl_and_save_products(db: Session, query: str = "운동화", display: int = 10):
    """
    네이버 쇼핑 데이터를 크롤링하고 데이터베이스에 저장하는 함수.
    기존 카테고리에 해당하는 데이터가 있으면 삭제 후 새로 저장.
    """
    try:
        print(f"'{query}' 카테고리에 대한 크롤링을 시작합니다...")

        # 카테고리 확인 및 생성
        try:
            category = db.query(ProductCategory).filter(ProductCategory.name == query).first()
            if not category:
                category = ProductCategory(name=query)
                db.add(category)
                db.commit()
                db.refresh(category)
            else:
                # 기존 카테고리의 상품 삭제
                db.query(Product).filter(Product.category_id == category.id).delete()
                db.commit()
                print(f"'{query}' 카테고리의 기존 데이터를 삭제했습니다.")
        except Exception as e:
            print(f"카테고리 생성 또는 삭제 중 오류 발생: {str(e)}")
            db.rollback()
            return

        # 네이버 API를 통해 크롤링
        try:
            naver_data = fetch_products_from_naver(query=query, display=display)
        except Exception as e:
            print(f"네이버 API 요청 중 오류 발생: {str(e)}")
            return

        # 크롤링한 데이터 저장
        try:
            for item in naver_data.get("items", []):
                # 새로운 상품 추가
                product = Product(
                    name=item["title"],
                    price=int(item["lprice"]),
                    description=item["link"],
                    image_url=item["image"],
                    details=item.get("description", ""),
                    category_id=category.id  # 카테고리 ID 연결
                )
                db.add(product)

            db.commit()
            print("크롤링 작업이 완료되었습니다.")
        except Exception as e:
            print(f"데이터 저장 중 오류 발생: {str(e)}")
            db.rollback()
    except Exception as e:
        print(f"알 수 없는 오류 발생: {str(e)}")