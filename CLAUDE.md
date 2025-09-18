# CLAUDE.md

이 파일은 Claude Code (claude.ai/code)가 이 저장소의 코드 작업 시 참고할 가이드를 제공합니다.

## 프로젝트 개요

AI Frontier는 arxiv.org에서 최신 논문을 자동으로 수집하고, AI를 이용해 초록을 번역 및 요약하여 종합 보고서를 생성하는 자동화된 리포팅 서비스입니다. `src/` 레이아웃의 현대적인 Python 패키지 구조와 포괄적인 개발 도구를 사용합니다.

## 주요 기능

### 핵심 기능
- **ArXiv 논문 자동 수집**: 지정된 카테고리와 기간에 따른 논문 검색
- **키워드 기반 검색**: 제목, 초록, 코멘트에서 키워드 검색 지원
- **AI 번역**: OpenAI/Claude를 이용한 다국어 번역 (기본: 한국어)
- **요약 생성**: AI 기반 논문 초록 요약 및 핵심 포인트 추출
- **마크다운 보고서 생성**: 일별 보고서 자동 생성 및 저장

### 검색 옵션
- **카테고리 기반 검색**: ArXiv 카테고리 지정 (기본: cs.AI, cs.LG, cs.CL, cs.CV)
- **기간 설정**: days-back 옵션으로 수집 기간 조정 (기본: 1일)
- **키워드 검색**: 특정 키워드가 포함된 논문 검색
- **키워드 전용 검색**: 카테고리 제한 없이 키워드로만 검색

## 설치 및 실행

### 환경 설정
```bash
# 패키지를 editable 모드로 설치
pip install -e .

# 개발 의존성 포함 설치
pip install -e ".[dev]"

# 환경 변수 설정
cp .env.example .env
# .env 파일에 API 키와 설정값 입력
```

### 필수 환경 변수
`.env` 파일에 다음 설정이 필요합니다:
- `OPENAI_API_KEY`: OpenAI API 접근 키
- `ANTHROPIC_API_KEY`: Claude API 접근 키 (선택사항)
- `MODEL_NAME`: 사용할 기본 모델명
- `DEVICE`: 연산 장치 (auto/cpu/cuda)
- `DATA_DIR`: 데이터 저장 디렉토리
- `LOG_LEVEL`: 로깅 레벨

## 현재 구현 상태 (2025-09-17)

### ✅ 완료된 기능

#### 1. 웹 인터페이스 (React + FastAPI)
- **React 프론트엔드**: 사용자 친화적인 논문 수집 인터페이스
- **FastAPI 백엔드**: RESTful API 서버로 논문 수집 작업 관리
- **실시간 진행률 추적**: 작업 상태와 진행률 실시간 모니터링
- **작업 중단 기능**: 논문 수집 중단 및 재시작 지원

#### 2. 논문 수집 시스템
- **ArXiv API 통합**: 카테고리 및 키워드 기반 논문 검색
- **멀티 쓰레드 처리**: Thread Pool을 활용한 비블로킹 백그라운드 작업
- **유연한 파라미터 처리**: 날짜 범위 모드와 최근 일수 모드 지원
- **정확한 검색 결과**: 사용자 설정에 따른 다양한 논문 수집 결과

#### 3. AI 기반 처리
- **다국어 번역**: OpenAI/Claude API를 통한 논문 초록 번역
- **요약 생성**: AI 기반 논문 요약 및 핵심 포인트 추출
- **키워드 추출**: 자동 키워드 분석 및 추출

#### 4. 데이터 관리
- **개별 논문 저장**: `reports/individual_papers/` 디렉토리에 논문별 마크다운 파일
- **작업 상태 추적**: Task ID 기반 작업 관리 및 상태 조회
- **파일 다운로드**: 생성된 보고서 다운로드 기능

### 🔧 최근 해결된 주요 이슈

#### 1. 파라미터 처리 버그 수정 (2025-09-17)
- **문제**: 다른 수집 설정에도 불구하고 항상 69개 논문만 수집되는 문제
- **원인**:
  - 프론트엔드에서 `dateMode`와 관계없이 모든 날짜 파라미터 전송
  - 백엔드에서 `days_back` 재계산으로 사용자 설정 무시
- **해결**:
  - `frontend/src/services/api.js:274-299`: 조건부 파라미터 전송 구현
  - `src/ai_frontier/main.py:249-253`: 날짜 범위 우선 처리 로직 수정

#### 2. 실시간 모니터링 개선
- **Progress 추적**: 실시간 진행률 업데이트 및 상태 변경 알림
- **중단 기능**: 안전한 작업 중단 및 상태 관리
- **Thread Pool**: 비블로킹 백그라운드 작업 처리

### 🚀 웹 인터페이스 실행 방법

#### FastAPI 백엔드 서버
```bash
# 백엔드 API 서버 실행 (포트: 8080)
python -m ai_frontier.api.server
```

#### React 프론트엔드
```bash
# 프론트엔드 개발 서버 실행 (포트: 3000)
cd frontend
npm install  # 최초 실행시에만
npm run dev
```

#### 통합 실행
- 백엔드: http://localhost:8080
- 프론트엔드: http://localhost:3000
- API 문서: http://localhost:8080/docs

### Streamlit 웹 인터페이스 (레거시)
```bash
# Streamlit 웹 UI 실행
python run_streamlit.py

# 또는 직접 실행
streamlit run src/ai_frontier/streamlit_app.py

# 브라우저에서 http://localhost:8501 접속
```

### 기본 실행 (CLI)
```bash
# 기본 설정으로 실행 (cs.AI, cs.LG, cs.CL, cs.CV 카테고리, 최근 1일)
python -m ai_frontier.main

# 특정 카테고리 지정
python -m ai_frontier.main --categories cs.AI cs.CV cs.NI

# 수집 기간 지정 (최근 3일)
python -m ai_frontier.main --days-back 3

# 특정 날짜 범위 지정 (YYYYMMDD 형태)
python -m ai_frontier.main --start-date 20241201 --end-date 20241207

# 키워드 검색
python -m ai_frontier.main --keywords "transformer" "attention" "neural network"

# 키워드 전용 검색 (카테고리 제한 없음)
python -m ai_frontier.main --keywords "machine learning" --keyword-only

# 특정 기간의 키워드 검색
python -m ai_frontier.main --keywords "GPT" --start-date 20241201 --end-date 20241207

# 번역/요약 제공자 변경
python -m ai_frontier.main --translation-provider claude --summarization-provider claude

# 출력 디렉토리 지정
python -m ai_frontier.main --output-dir custom_reports
```

### 실행 옵션 상세

#### 필수 매개변수
- 없음 (모든 옵션에 기본값 존재)

#### 선택적 매개변수
- `--categories`: ArXiv 카테고리 목록 (기본: cs.AI cs.LG cs.CL cs.CV)
- `--days-back`: 검색할 과거 일수 (기본: 1)
- `--start-date`: 수집 시작 날짜 (YYYYMMDD 형식)
- `--end-date`: 수집 종료 날짜 (YYYYMMDD 형식)
- `--translation-provider`: 번역 서비스 제공자 (openai/claude, 기본: openai)
- `--summarization-provider`: 요약 서비스 제공자 (openai/claude, 기본: openai)
- `--output-dir`: 보고서 출력 디렉토리 (기본: reports)
- `--keywords`: 검색할 키워드 목록
- `--keyword-only`: 키워드 전용 검색 모드 (카테고리 제한 해제)

#### 날짜 범위 사용법
- `--start-date`와 `--end-date`는 함께 사용해야 함
- 날짜 형식: YYYYMMDD (예: 20241215)
- 날짜 범위가 지정되면 `--days-back` 옵션은 무시됨
- 페이지네이션을 통해 해당 기간의 **모든 논문** 수집

#### 사용 예시
```bash
# 최근 7일간 딥러닝 관련 논문 수집
python -m ai_frontier.main --categories cs.LG cs.CV --days-back 7

# 2024년 12월 1일~7일 기간의 모든 AI 논문 수집
python -m ai_frontier.main --start-date 20241201 --end-date 20241207

# 특정 기간의 키워드 검색
python -m ai_frontier.main --keywords "GPT" "BERT" "transformer" --start-date 20241201 --end-date 20241207

# 모든 분야에서 특정 기간의 "quantum computing" 관련 논문 검색
python -m ai_frontier.main --keywords "quantum computing" --keyword-only --start-date 20241201 --end-date 20241207

# 일주일간의 전체 컴퓨터 사이언스 논문 수집
python -m ai_frontier.main --categories cs.AI cs.LG cs.CV cs.CL cs.CR cs.DC --start-date 20241201 --end-date 20241207
```

## 프로젝트 구조

### 패키지 구조
- `src/ai_frontier/`: 메인 패키지 (src-layout 구조)
- `src/ai_frontier/main.py`: 메인 실행 파일 및 CLI 인터페이스
- `src/ai_frontier/api/`: FastAPI 웹 서버
  - `server.py`: RESTful API 서버 및 엔드포인트
- `src/ai_frontier/arxiv/`: ArXiv API 연동 및 논문 수집
  - `client.py`: ArXiv 클라이언트 및 논문 검색 로직
- `src/ai_frontier/translation/`: AI 기반 번역 서비스
  - `translator.py`: OpenAI/Claude 번역 인터페이스
- `src/ai_frontier/summarization/`: 초록 요약 로직
  - `summarizer.py`: AI 기반 요약 및 핵심 포인트 추출
- `src/ai_frontier/reporting/`: 보고서 생성 및 포맷팅
  - `generator.py`: 마크다운 보고서 생성기
- `src/ai_frontier/utils/`: 유틸리티 함수 및 헬퍼
- `frontend/`: React 프론트엔드 애플리케이션
  - `src/`: React 컴포넌트 및 서비스
  - `src/services/api.js`: 백엔드 API 클라이언트
- `tests/`: pytest 테스트 파일

### 핵심 설계 패턴
- **Source Layout**: 패키지 격리를 위한 `src/` 레이아웃 사용
- **Pydantic Models**: 데이터 검증 및 설정을 위한 Pydantic 사용
- **환경 설정**: 민감한 설정을 위한 `.env` 파일 사용
- **타입 힌트**: mypy를 통한 완전한 타입 주석 지원

### 의존성
- **핵심**: torch, transformers, numpy, pandas, pydantic, requests
- **ArXiv**: arxiv (API 연동), feedparser (RSS 피드)
- **번역**: openai, anthropic (AI 서비스)
- **보고서**: jinja2 (템플릿), markdown (포맷팅)
- **웹 서버**: fastapi, uvicorn (RESTful API 서버)
- **스케줄링**: schedule (자동화)
- **개발**: pytest, black, isort, flake8, mypy
- **설정**: python-dotenv (환경 관리)
- **프론트엔드**: React, Vite, TailwindCSS (사용자 인터페이스)

## 출력 결과

### 보고서 형태
- **파일명**: `arxiv_report_YYYYMMDD.md` (예: arxiv_report_20241217.md)
- **저장 위치**: `reports/` 디렉토리 (또는 지정된 출력 디렉토리)
- **포맷**: 마크다운 형식

### 보고서 내용
각 논문별로 다음 정보 포함:
- 원본 제목 및 번역된 제목
- 저자 정보
- ArXiv ID 및 PDF 링크
- 원본 초록 및 번역된 초록
- AI 생성 요약
- 핵심 포인트
- 발행일

## 개발 관련

### 테스트
```bash
# 모든 테스트 실행
pytest

# 커버리지 포함 테스트
pytest --cov=src/ai_frontier

# 특정 테스트 파일 실행
pytest tests/test_basic.py
```

### 코드 품질 관리
```bash
# 코드 포맷팅
black src/ tests/

# import 정렬
isort src/ tests/

# 타입 체킹
mypy src/

# 린팅
flake8 src/ tests/

# 모든 품질 검사 실행
black src/ tests/ && isort src/ tests/ && flake8 src/ tests/ && mypy src/
```

## 개발 워크플로우
1. 기능 브랜치 생성
2. 타입 힌트와 함께 변경사항 구현
3. 테스트 추가/업데이트
4. 품질 검사 실행: `black && isort && flake8 && mypy`
5. 테스트 실행: `pytest`
6. 커밋 및 풀 리퀘스트 생성

## 최신 기능 (2025-09-18 업데이트)

### 🔗 Obsidian 링크 자동 생성
- **자동 키워드 추출**: 논문 제목과 초록에서 AI/ML 관련 키워드 자동 추출
- **Obsidian 링크 포맷**: `[[daily/2025-09-18|2025-09-18]] [[keywords/GraphRAG|GraphRAG]] [[authors/Zirui Guo|Zirui Guo]]` 형태
- **메타데이터 섹션**: 각 논문 파일에 Links 섹션 자동 추가
- **카테고리별 분류**: 날짜, 키워드, 저자, 카테고리별 체계적 링크 구성

### 🤖 자동화 도구 지원 (n8n, Zapier 등)
새로운 webhook API 엔드포인트 추가:

#### 비동기 수집 (추천)
- `POST /webhook/collect`: 백그라운드에서 논문 수집 시작
- `GET /webhook/status/{task_id}`: 작업 진행 상황 모니터링
- `DELETE /webhook/task/{task_id}`: 작업 삭제
- `GET /webhook/tasks`: 모든 작업 목록 조회

#### 동기 수집 (간단한 자동화용)
- `POST /webhook/collect-sync`: 완료까지 대기하고 결과 직접 반환

#### 사용 예시 (n8n)
```json
{
  "keywords": ["transformer", "attention"],
  "categories": ["cs.AI", "cs.LG"],
  "days_back": 7,
  "callback_url": "https://your-webhook.com/arxiv-complete"
}
```

### 📊 일일/주간 다이제스트 생성
수집된 논문들의 스마트 요약 기능:

#### CLI 사용법
```bash
# 오늘 날짜 일일 다이제스트
python -m ai_frontier.main --generate-digest daily

# 특정 날짜 일일 다이제스트
python -m ai_frontier.main --generate-digest daily --digest-date 20250915

# 이번 주 주간 다이제스트
python -m ai_frontier.main --generate-digest weekly

# 특정 주 다이제스트
python -m ai_frontier.main --generate-digest weekly --digest-date 20250915
```

#### API 엔드포인트
- `POST /api/digest/daily?date=20250915`: 일일 다이제스트 생성
- `POST /api/digest/weekly?date=20250915`: 주간 다이제스트 생성
- `GET /api/digests`: 생성된 다이제스트 목록 조회

#### 다이제스트 내용
- **AI 생성 요약**: 전체 논문 동향과 주요 연구 방향 분석
- **카테고리별 분류**: 연구 분야별 논문 그룹핑
- **주목할 만한 논문**: AI가 선별한 중요 논문 하이라이트
- **키워드 트렌드**: 빈도 분석 기반 연구 트렌드 파악
- **통계 정보**: 일별/주별 수집 통계

### 🔄 키워드 검색 개선
- **OR 검색 지원**: 여러 키워드 중 하나라도 매칭되면 수집
- **자동 키워드 추출**: 더 이상 수동 입력 불필요, AI가 논문에서 자동 추출
- **스마트 키워드**: 기술 용어, 약어, 인용구 등 포괄적 추출

## 알려진 제한사항

### ArXiv 카테고리
- `cs`만 입력하면 컴퓨터 사이언스 전체 수집 불가
- 정확한 하위 카테고리 명시 필요 (예: `cs.AI`, `cs.LG` 등)
- 모든 CS 분야 수집 시 모든 하위 카테고리를 명시적으로 지정해야 함

### API 제한
- OpenAI/Claude API 사용량 제한 고려 필요
- ArXiv API rate limiting 적용
- 대량 논문 처리 시 시간 소요 발생

## 기술 스택 상세

### 백엔드 (Python)
- **FastAPI**: RESTful API 서버 프레임워크
- **Uvicorn**: ASGI 서버
- **Pydantic**: 데이터 검증 및 직렬화
- **Thread Pool**: 비동기 백그라운드 작업 처리
- **Logging**: 구조화된 로깅 시스템
- **Obsidian Formatter**: 링크 생성 및 메타데이터 포맷팅
- **Digest Generator**: AI 기반 논문 요약 및 분석

### 프론트엔드 (React)
- **React 18**: 사용자 인터페이스 라이브러리
- **Vite**: 번들링 및 개발 서버
- **TailwindCSS**: 유틸리티 기반 CSS 프레임워크
- **Fetch API**: HTTP 클라이언트
- **실시간 폴링**: 작업 상태 모니터링

### 자동화 도구 통합
- **Webhook API**: n8n, Zapier 등 자동화 플랫폼 지원
- **비동기 처리**: 백그라운드 작업으로 논문 수집
- **콜백 지원**: 작업 완료 시 외부 URL 호출
- **진행률 모니터링**: 실시간 작업 상태 추적

### 데이터 플로우
1. **사용자 입력**: React UI 또는 자동화 도구에서 논문 수집 파라미터 설정
2. **API 요청**: Frontend/Automation Tool → Backend API 호출
3. **백그라운드 작업**: Thread Pool에서 논문 수집 실행
4. **실시간 모니터링**: 폴링을 통한 진행률 업데이트
5. **Obsidian 링크 생성**: 자동 키워드 추출 및 링크 포맷팅
6. **결과 저장**: 마크다운 파일로 개별 논문 저장
7. **다이제스트 생성**: AI 기반 일일/주간 요약 생성
8. **다운로드**: 생성된 보고서 파일 다운로드

## 주요 API 엔드포인트

### 논문 수집 관련
- `POST /api/collect`: 논문 수집 작업 시작
- `GET /api/status/{task_id}`: 작업 상태 조회
- `POST /api/cancel/{task_id}`: 작업 중단
- `GET /api/tasks`: 전체 작업 목록 조회
- `DELETE /api/tasks/{task_id}`: 작업 삭제

### 자동화 도구용 Webhook API
- `POST /webhook/collect`: 비동기 논문 수집 시작
- `POST /webhook/collect-sync`: 동기 논문 수집 (완료까지 대기)
- `GET /webhook/status/{task_id}`: Webhook 작업 상태 조회
- `DELETE /webhook/task/{task_id}`: Webhook 작업 삭제
- `GET /webhook/tasks`: Webhook 작업 목록 조회

### 다이제스트 생성
- `POST /api/digest/daily?date=YYYYMMDD`: 일일 다이제스트 생성
- `POST /api/digest/weekly?date=YYYYMMDD`: 주간 다이제스트 생성
- `GET /api/digests`: 생성된 다이제스트 목록 조회

### 파일 관리
- `GET /api/download/{task_id}`: 보고서 다운로드
- `GET /api/papers/{task_id}`: 수집된 논문 목록 조회
- `GET /api/files`: 생성된 파일 목록 조회

### 시스템
- `GET /health`: 서버 상태 확인