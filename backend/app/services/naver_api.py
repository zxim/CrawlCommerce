import requests
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

def fetch_products_from_naver(query: str, display: int = 10):
    """
    네이버 쇼핑 API를 사용하여 상품 데이터를 가져오는 함수.
    Args:
        query (str): 검색할 키워드.
        display (int): 가져올 상품 개수.

    Returns:
        dict: 상품 데이터 결과.
    """
    # 네이버 API 키 가져오기
    client_id = os.getenv("Client_ID")
    client_secret = os.getenv("Client_Secret")

    if not client_id or not client_secret:
        raise ValueError("Client_ID 또는 Client_Secret 환경 변수가 설정되지 않았습니다.")

    url = "https://openapi.naver.com/v1/search/shop.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    params = {
        "query": query,
        "display": display,
        "sort": "sim",  # 유사도 순 정렬
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        data = response.json()

        if "items" not in data:
            print("네이버 API 응답에 'items' 키가 없습니다.")
            return {"items": []}

        return data

    except requests.exceptions.RequestException as e:
        print(f"네이버 API 요청 중 오류 발생: {e}")
        return {"items": []}

    except ValueError as e:
        print(f"JSON 파싱 중 오류 발생: {e}")
        return {"items": []}