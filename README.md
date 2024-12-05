frontend/
├── public/             # 정적 파일 (이미지, 폰트 등)
│   └── logo.png
├── src/                # 소스 코드 디렉토리 (Next.js 13 이상 권장)
│   ├── app/            # App Router 디렉토리
│   │   ├── layout.tsx  # 공통 레이아웃 (모든 페이지에 적용)
│   │   ├── page.tsx    # 메인 페이지
│   │   ├── about/      # 중첩 라우팅
│   │   │   └── page.tsx # 'about' 페이지
│   │   ├── products/   # 중첩 및 동적 라우팅
│   │   │   ├── page.tsx # 'products' 메인 페이지
│   │   │   └── [id]/page.tsx # 동적 라우팅 (예: /products/123)
│   ├── components/     # 재사용 가능한 컴포넌트
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── ProductCard.tsx
│   ├── styles/         # CSS/SCSS 파일
│   │   ├── globals.css # 전역 스타일
│   │   ├── Home.module.css # 모듈 CSS (홈 페이지 전용)
│   ├── utils/          # 공통 유틸리티 함수 (API 호출 등)
│   │   └── api.ts
│   ├── hooks/          # 커스텀 React Hook
│   │   └── useAuth.ts
│   ├── context/        # 전역 상태 관리 Context
│   │   └── AuthContext.tsx
│   ├── types/          # 전역 타입 정의 파일
│   │   └── index.d.ts
│   └── config/         # 설정 파일 (예: API URL 등)
│       └── constants.ts
├── .env.local          # 환경 변수 파일
├── tsconfig.json       # TypeScript 설정 파일
├── next.config.js      # Next.js 설정 파일
├── package.json        # 프로젝트 메타 정보 및 의존성
└── README.md           # 프로젝트 설명


backend/
├── app/
│   ├── main.py            # FastAPI 애플리케이션 진입점
│   ├── routes/            # 라우터 정의
│   │   ├── products.py    # 상품 관련 API
│   │   └── search.py      # 검색 관련 API
│   ├── services/          # 비즈니스 로직 (크롤링, 데이터 처리)
│   │   ├── naver_api.py   # 네이버 쇼핑 API 연동
│   │   └── crawvler.py     # 상품 상세 크롤링
│   ├── models/            # 데이터베이스 모델
│   │   └── product.py     # 상품 모델
│   ├── config/            # 설정 및 환경 변수
│   │   ├── db.py          # 데이터베이스 연결 설정
│   │   └── settings.py    # 앱 설정
│   ├── schemas/           # 데이터 스키마 정의 (Pydantic)
│   │   └── product.py     # 상품 데이터 스키마
│   └── utils/             # 유틸리티 함수
│       └── helpers.py     # 공통 유틸 함수
├── tests/                 # 테스트 코드
│   ├── test_products.py   # 상품 API 테스트
│   └── test_search.py     # 검색 API 테스트
├── requirements.txt       # Python 의존성
├── .env                   # 환경 변수 파일
└── README.md              # 프로젝트 설명
