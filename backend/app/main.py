from fastapi import FastAPI
from app.routes import products
from app.config.db import engine, SessionLocal, Base
from app.services.crawler import crawl_and_save_products

app = FastAPI()

# 데이터베이스 초기화 및 크롤링 실행
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)  # 데이터베이스 초기화
    db = SessionLocal()
    try:
        print("서버 시작: 최신 상품 데이터 갱신 중...")
        crawl_and_save_products(db)  # 서버 시작 시 크롤링 실행
    except Exception as e:
        print(f"크롤링 실행 중 오류 발생: {str(e)}")
    finally:
        db.close()

# 라우터 등록
app.include_router(products.router, prefix="/api", tags=["Products"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Shopping Mall API!"}