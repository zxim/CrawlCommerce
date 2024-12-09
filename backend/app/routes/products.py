from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.config.db import SessionLocal
from app.models.product import Product
from app.services.naver_api import fetch_products_from_naver

router = APIRouter()

# DB 세션 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 네이버 쇼핑 데이터를 가져와 DB에 저장하는 엔드포인트
@router.post("/products/crawl")
async def crawl_products(query: str, db: Session = Depends(get_db)):
    try:
        # 네이버 쇼핑 데이터 가져오기
        naver_data = fetch_products_from_naver(query=query)

        # 데이터 저장
        products = []
        for item in naver_data.get("items", []):
            product = Product(
                name=item["title"],
                price=int(item["lprice"]),
                description=item["link"],
            )
            db.add(product)
            products.append(product)

        db.commit()

        return {"message": f"{len(products)} products added successfully.", "products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
