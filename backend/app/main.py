from fastapi import FastAPI
from app.routes import products
from app.config.db import engine, SessionLocal
from app.models.product import Base, Product
from app.services.naver_api import fetch_products_from_naver

# FastAPI 인스턴스 생성
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)  # 데이터베이스 초기화
    db = SessionLocal()

    # 데이터베이스 상품 확인
    product_count = db.query(Product).count()
    if product_count == 0:
        print("데이터베이스가 비어 있습니다. 상품 데이터를 크롤링합니다.")
        await crawl_and_save_products(db)
    else:
        print(f"데이터베이스에 {product_count}개의 상품이 있습니다.")
        # 사용자에게 CLI로 크롤링 여부를 묻기
        while True:
            should_crawl = input("추가 크롤링을 실행하시겠습니까? (y/n): ").strip().lower()
            if should_crawl in ["y", "n"]:
                break
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력하세요.")

        if should_crawl == "y":
            await crawl_and_save_products(db)

    db.close()

async def crawl_and_save_products(db):
    """
    네이버 쇼핑 데이터를 크롤링하고 데이터베이스에 저장하는 함수.
    중복 데이터는 저장하지 않음.
    """
    try:
        print("크롤링 작업을 시작합니다...")
        naver_data = fetch_products_from_naver(query="노트북", display=10)

        for item in naver_data.get("items", []):
            # 중복 확인: 같은 이름의 상품이 이미 있는 경우 건너뛰기
            existing_product = db.query(Product).filter(Product.name == item["title"]).first()
            if existing_product:
                print(f"중복된 상품 발견: {item['title']} - 저장 건너뜀")
                continue

            # 새로운 상품 추가
            product = Product(
                name=item["title"],
                price=int(item["lprice"]),
                description=item["link"],
            )
            db.add(product)

        db.commit()
        print("크롤링 작업이 완료되었습니다.")
    except Exception as e:
        print(f"크롤링 중 오류 발생: {str(e)}")

# 라우터 등록
app.include_router(products.router, prefix="/api", tags=["Products"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Shopping Mall API!"}
