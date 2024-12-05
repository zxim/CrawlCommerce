frontend/ <br>
├── public/             # 정적 파일 (이미지, 폰트 등)<br>
│   └── logo.png<br>
├── src/                # 소스 코드 디렉토리 (Next.js 13 이상 권장)<br>
│   ├── app/            # App Router 디렉토리<br>
│   │   ├── layout.tsx  # 공통 레이아웃 (모든 페이지에 적용)<br>
│   │   ├── page.tsx    # 메인 페이지<br>
│   │   ├── about/      # 중첩 라우팅<br>
│   │   │   └── page.tsx # 'about' 페이지<br>
│   │   ├── products/   # 중첩 및 동적 라우팅<br>
│   │   │   ├── page.tsx # 'products' 메인 페이지<br>
│   │   │   └── [id]/page.tsx # 동적 라우팅 (예: /products/123)<br>
│   ├── components/     # 재사용 가능한 컴포넌트<br>
│   │   ├── Header.tsx<br>
│   │   ├── Footer.tsx<br>
│   │   └── ProductCard.tsx<br>
│   ├── styles/         # CSS/SCSS 파일<br>
│   │   ├── globals.css # 전역 스타일<br>
│   │   ├── Home.module.css # 모듈 CSS (홈 페이지 전용)<br>
│   ├── utils/          # 공통 유틸리티 함수 (API 호출 등)<br>
│   │   └── api.ts<br>
│   ├── hooks/          # 커스텀 React Hook<br>
│   │   └── useAuth.ts<br>
│   ├── context/        # 전역 상태 관리 Context<br>
│   │   └── AuthContext.tsx<br>
│   ├── types/          # 전역 타입 정의 파일<br>
│   │   └── index.d.ts<br>
│   └── config/         # 설정 파일 (예: API URL 등)<br>
│       └── constants.ts<br>
├── .env.local          # 환경 변수 파일<br>
├── tsconfig.json       # TypeScript 설정 파일<br>
├── next.config.js      # Next.js 설정 파일<br>
├── package.json        # 프로젝트 메타 정보 및 의존성<br>
└── README.md           # 프로젝트 설명<br>


backend/<br>
├── app/<br>
│   ├── main.py            # FastAPI 애플리케이션 진입점<br>
│   ├── routes/            # 라우터 정의<br>
│   │   ├── products.py    # 상품 관련 API<br>
│   │   └── search.py      # 검색 관련 API<br>
│   ├── services/          # 비즈니스 로직 (크롤링, 데이터 처리)<br>
│   │   ├── naver_api.py   # 네이버 쇼핑 API 연동<br>
│   │   └── crawvler.py     # 상품 상세 크롤링<br>
│   ├── models/            # 데이터베이스 모델<br>
│   │   └── product.py     # 상품 모델<br>
│   ├── config/            # 설정 및 환경 변수<br>
│   │   ├── db.py          # 데이터베이스 연결 설정<br>
│   │   └── settings.py    # 앱 설정<br>
│   ├── schemas/           # 데이터 스키마 정의 (Pydantic)<br>
│   │   └── product.py     # 상품 데이터 스키마<br>
│   └── utils/             # 유틸리티 함수<br>
│       └── helpers.py     # 공통 유틸 함수<br>
├── tests/                 # 테스트 코드<br>
│   ├── test_products.py   # 상품 API 테스트<br>
│   └── test_search.py     # 검색 API 테스트<br>
├── requirements.txt       # Python 의존성<br>
├── .env                   # 환경 변수 파일<br>
└── README.md              # 프로젝트 설명<br>
