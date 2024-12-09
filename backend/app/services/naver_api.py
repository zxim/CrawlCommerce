import os
from dotenv import load_dotenv
import requests

# .env 파일 로드
load_dotenv()

# 네이버 API 설정
Client_ID = os.getenv("Client_ID")
Client_SECRET = os.getenv("Client_SECRET")

def fetch_products_from_naver(query: str, display: int = 10):
    """
    네이버 쇼핑 API를 통해 데이터를 가져오는 함수
    """
    url = "https://openapi.naver.com/v1/search/shop.json"
    headers = {
        "X-Naver-Client-Id": Client_ID,
        "X-Naver-Client-Secret": Client_SECRET,
    }
    params = {"query": query, "display": display}
    response = requests.get(url, headers=headers, params=params)

    # 응답 처리
    if response.status_code == 200:
        return response.json()  # JSON 데이터를 반환
    else:
        response.raise_for_status()  # 오류 발생 시 예외 발생
