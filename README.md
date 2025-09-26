# AI Frontier

ArXiv 논문 자동 번역 및 요약 리포팅 서비스 + RAG 검색 시스템

AI Frontier는 arxiv.org에서 최신 AI/ML 논문들을 자동으로 수집하고, AI를 활용해 요약하여 일일 리포트를 생성하는 자동화 서비스입니다. 또한 수집된 논문들에 대한 시맨틱 검색 기능과 키워드 기반 맞춤형 알림 시스템을 제공하는 종합 연구 플랫폼입니다.

## Installation

```bash
# Install the package
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Development

```bash
# Run tests
pytest

# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Type checking
mypy src/

# Linting
flake8 src/ tests/
```

## 주요 기능

### 논문 수집 & 리포팅
- **ArXiv 논문 수집**: 지정된 카테고리의 최신 논문 자동 검색
- **자동 요약**: AI 기반 논문 초록 요약 및 핵심 포인트 추출
- **Obsidian 호환**: Properties 메타데이터와 자동 링크 생성 지원
- **리포트 생성**: Markdown 형식의 개별 논문 파일 자동 생성
- **다중 AI 제공자**: OpenAI, Claude 등 여러 AI 서비스 지원

### RAG 검색 시스템 🔍 (2025-09-19 추가)
- **시맨틱 검색**: OpenAI 임베딩을 이용한 의미 기반 논문 검색
- **고급 필터링**: 카테고리, 날짜 범위, 유사도 임계값으로 정밀 검색
- **유사 논문 발견**: 특정 논문과 유사한 연구 자동 추천
- **페이지네이션**: 10개씩 페이지 단위로 최대 100개 결과 표시
- **검색어 제안**: AI 기반 검색어 개선 제안

### 알림 시스템 📧 (2025-09-25 업데이트)
- **일간/주간 다이제스트**: AI 생성 스마트 요약 보고서
- **키워드 기반 알림**: 관심 키워드 논문만 맞춤형 알림
- **일간+주간 통합 구독**: 하나의 구독으로 모든 다이제스트 수신
- **다양한 채널 지원**: 이메일, 슬랙, 웹훅(n8n/Zapier) 알림
- **실시간 구독 관리**: 웹 UI에서 구독 정보 실시간 편집

## Environment Setup

1. API 키 설정:
```bash
cp .env.example .env
```

2. `.env` 파일에 API 키 입력:
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Project Structure

```
ai_frontier/
├── src/
│   └── ai_frontier/
│       ├── arxiv/           # ArXiv API 연동
│       ├── translation/     # AI 번역 서비스
│       ├── summarization/   # AI 요약 서비스
│       ├── reporting/       # 리포트 생성
│       ├── search/          # RAG 검색 시스템 (NEW)
│       ├── embeddings/      # 벡터 임베딩 관리 (NEW)
│       ├── api/             # FastAPI 웹 서버
│       ├── notification/    # 알림 시스템
│       ├── utils/           # 유틸리티 함수
│       └── main.py          # 메인 애플리케이션
├── frontend/                # React 웹 인터페이스 (NEW)
│   ├── src/
│   │   ├── components/      # React 컴포넌트
│   │   └── services/        # API 클라이언트
│   └── package.json
├── tests/                   # 테스트 파일
├── reports/                 # 생성된 리포트 저장
└── data/                    # 벡터 DB 및 데이터 저장
    └── embeddings/          # FAISS 벡터 데이터베이스
```

## Usage

### 웹 인터페이스 사용법 (권장)

#### 1. 서버 실행
```bash
# 백엔드 API 서버 (포트: 8080)
python -m ai_frontier.api.server

# 프론트엔드 개발 서버 (포트: 3000)
cd frontend
npm install  # 최초 실행시에만
npm run dev
```

#### 2. 웹 인터페이스 접속
- **메인 서비스**: http://localhost:3000
- **API 문서**: http://localhost:8080/docs

#### 3. 기능별 사용법
- **논문 수집**: "논문 수집" 탭에서 키워드, 카테고리, 날짜 범위 설정 후 수집
- **RAG 검색**: "논문 검색" 탭에서 자연어/키워드로 시맨틱 검색
- **다이제스트**: "다이제스트" 탭에서 일간/주간 요약 보고서 생성
- **알림 설정**: "알림 설정" 탭에서 다음 기능들 사용:
  - 일반 이메일 구독 (일간/주간/일간+주간)
  - 키워드 기반 맞춤 구독
  - 구독자 정보 실시간 편집/삭제
  - 이메일/슬랙 연결 테스트

### CLI 사용법

```bash
# 기본 실행 (최근 1일간의 AI 논문들)
python -m ai_frontier.main

# 키워드로 검색 (카테고리 + 키워드 조합)
python -m ai_frontier.main \
  --keywords "multimodal" "attention" "transformer" \
  --categories cs.AI cs.CV

# 키워드만으로 검색 (카테고리 제한 없음)
python -m ai_frontier.main \
  --keywords "large language model" "GPT" "BERT" \
  --keyword-only \
  --days-back 7

# 전체 옵션
python -m ai_frontier.main \
  --categories cs.AI cs.LG cs.CL cs.CV \
  --keywords "neural network" "deep learning" \
  --days-back 3 \
  --translation-provider openai \
  --summarization-provider claude \
  --output-dir ./reports
```

### Python 코드에서 사용

```python
from ai_frontier.main import ArxivReportingService

# 서비스 초기화
service = ArxivReportingService(
    translation_provider="openai",
    summarization_provider="claude"
)

# 키워드 기반 리포트 생성
import asyncio
report_path = asyncio.run(
    service.process_papers(
        categories=["cs.AI", "cs.LG"],
        days_back=3,
        keywords=["transformer", "attention", "multimodal"],
        keyword_only=False  # 카테고리 + 키워드 조합
    )
)
print(f"Report generated: {report_path}")

# 키워드만으로 검색
report_path = asyncio.run(
    service.process_papers(
        keywords=["large language model", "GPT", "BERT"],
        days_back=7,
        keyword_only=True  # 키워드만으로 검색
    )
)
print(f"Report generated: {report_path}")
```

### RAG 검색 시스템 사용법

#### API를 통한 검색

```python
import requests

# 시맨틱 검색
search_payload = {
    "query": "transformer attention mechanism",
    "top_k": 10,
    "min_similarity": 0.7,
    "categories": ["cs.AI", "cs.LG"],
    "page": 1,
    "page_size": 10
}

response = requests.post(
    "http://localhost:8080/api/search/papers",
    json=search_payload
)
results = response.json()

# 유사 논문 검색
similar_payload = {
    "arxiv_id": "2023.12345",
    "top_k": 5,
    "min_similarity": 0.8
}

response = requests.post(
    "http://localhost:8080/api/search/similar",
    json=similar_payload
)
similar_papers = response.json()

# 데이터베이스 통계
stats = requests.get("http://localhost:8080/api/search/stats").json()
print(f"총 논문 수: {stats['total_papers']}")
```

### 알림 시스템 사용법

#### 키워드 기반 구독 설정

```python
import requests

# 키워드 기반 구독 추가 (일간+주간 모두)
requests.post("http://localhost:8080/api/notifications/keywords/subscribe", json={
    "email": "user@example.com",
    "keywords": ["transformer", "attention", "multimodal"],
    "digest_type": "daily"  # 일간
})

requests.post("http://localhost:8080/api/notifications/keywords/subscribe", json={
    "email": "user@example.com",
    "keywords": ["transformer", "attention", "multimodal"],
    "digest_type": "weekly"  # 주간
})

# 구독자 목록 조회
subscribers = requests.get("http://localhost:8080/api/notifications/keywords/subscribers").json()
print(f"키워드 구독자: {len(subscribers)} 명")
```

#### 주요 API 엔드포인트

**검색 관련**
- `POST /api/search/papers`: 시맨틱 논문 검색
- `POST /api/search/similar`: 유사 논문 검색
- `GET /api/search/stats`: 벡터 데이터베이스 통계
- `GET /api/search/suggestions`: 검색어 개선 제안

**알림 관련**
- `POST /api/notifications/email/subscribe`: 이메일 구독 추가
- `POST /api/notifications/keywords/subscribe`: 키워드 기반 구독 추가
- `GET /api/notifications/email/subscribers`: 구독자 목록 조회
- `POST /api/notifications/test`: 연결 테스트

## 기술 스택

### 백엔드
- **Python 3.8+**: 메인 언어
- **FastAPI**: RESTful API 서버
- **FAISS**: 벡터 검색 엔진
- **OpenAI API**: 임베딩 및 AI 서비스
- **Anthropic Claude**: 대안 AI 서비스

### 프론트엔드
- **React 18**: 사용자 인터페이스
- **Vite**: 빌드 도구
- **TailwindCSS**: 스타일링
- **Lucide React**: 아이콘

### 데이터 처리
- **Pydantic**: 데이터 검증
- **Pandas**: 데이터 처리
- **NumPy**: 수치 연산