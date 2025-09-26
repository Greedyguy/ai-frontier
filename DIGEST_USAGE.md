# 📊 다이제스트 생성 가이드

AI Frontier에서 일일/주간 다이제스트를 생성하는 방법을 안내합니다.

## 🎯 다이제스트란?

다이제스트는 수집된 논문들을 자동으로 분석하고 요약하여 주요 연구 동향과 트렌드를 파악할 수 있도록 해주는 보고서입니다.

### 📝 다이제스트 내용
- **전체 논문 요약**: 해당 기간의 논문 동향 분석
- **카테고리별 분류**: 연구 분야별 논문 그룹핑
- **주목할 만한 논문**: AI가 선별한 중요 논문 하이라이트
- **키워드 트렌드**: 빈도 분석 기반 연구 트렌드
- **통계 정보**: 일별/주별 수집 통계

## 🖥️ 웹 UI 사용법

### 1. 프론트엔드 접속
```bash
# 백엔드 서버 실행
python -m ai_frontier.api.server

# 프론트엔드 실행
cd frontend
npm run dev

# 브라우저에서 접속
http://localhost:3000
```

### 2. 다이제스트 패널 사용
1. **날짜 선택**: 다이제스트를 생성할 날짜 선택 (기본: 오늘)
2. **버튼 클릭**:
   - `📄 일일 다이제스트 생성`: 해당 날짜의 일일 다이제스트 생성
   - `📅 주간 다이제스트 생성`: 해당 주간의 주간 다이제스트 생성
3. **결과 확인**: 생성된 다이제스트 목록에서 확인

## ⌨️ CLI 사용법

### 일일 다이제스트
```bash
# 오늘 날짜 일일 다이제스트
python -m ai_frontier.main --generate-digest daily

# 특정 날짜 일일 다이제스트
python -m ai_frontier.main --generate-digest daily --digest-date 20250915

# Claude를 사용한 다이제스트
python -m ai_frontier.main --generate-digest daily --translation-provider claude --summarization-provider claude
```

### 주간 다이제스트
```bash
# 이번 주 주간 다이제스트
python -m ai_frontier.main --generate-digest weekly

# 특정 주 다이제스트 (해당 날짜가 포함된 주)
python -m ai_frontier.main --generate-digest weekly --digest-date 20250915
```

## 🔗 API 사용법

### 일반 API 엔드포인트

#### 일일 다이제스트 생성
```http
POST http://localhost:8080/api/digest/daily
```

날짜 지정:
```http
POST http://localhost:8080/api/digest/daily?date=20250915
```

#### 주간 다이제스트 생성
```http
POST http://localhost:8080/api/digest/weekly
```

날짜 지정:
```http
POST http://localhost:8080/api/digest/weekly?date=20250915
```

#### 다이제스트 목록 조회
```http
GET http://localhost:8080/api/digests
```

### Webhook API (n8n, Zapier 등)

#### 일일 다이제스트
```http
POST http://localhost:8080/webhook/digest/daily
Content-Type: application/json

{
  "date": "20250915",
  "translation_provider": "openai",
  "summarization_provider": "openai",
  "callback_url": "https://your-webhook.com/digest-complete"
}
```

#### 주간 다이제스트
```http
POST http://localhost:8080/webhook/digest/weekly
Content-Type: application/json

{
  "date": "20250915",
  "translation_provider": "claude",
  "summarization_provider": "claude",
  "callback_url": "https://your-webhook.com/digest-complete"
}
```

#### 다이제스트 목록 조회
```http
GET http://localhost:8080/webhook/digests
```

## 🤖 자동화 도구 연동

### n8n 워크플로 예시

1. **HTTP Request 노드**:
   - Method: POST
   - URL: `http://localhost:8080/webhook/digest/daily`
   - Body:
     ```json
     {
       "date": "{{ $now.format('YYYYMMDD') }}",
       "callback_url": "{{ $webhook.url }}"
     }
     ```

2. **스케줄 트리거**:
   - 매일 오전 9시에 실행
   - Cron: `0 9 * * *`

### Zapier 연동

1. **Webhook by Zapier** 트리거
2. **POST 요청**:
   - URL: `http://localhost:8080/webhook/digest/daily`
   - Payload Type: JSON
   - Data:
     ```json
     {
       "date": "{{ date__format:YYYYMMDD }}",
       "translation_provider": "openai"
     }
     ```

## 📁 출력 파일

### 파일 위치
```
reports/
└── digests/
    ├── daily_digest_20250915.md
    ├── weekly_digest_20250910-20250916.md
    └── ...
```

### 파일명 규칙
- **일일**: `daily_digest_YYYYMMDD.md`
- **주간**: `weekly_digest_YYYYMMDD-YYYYMMDD.md`

## ⚙️ 설정 옵션

### 번역/요약 제공자
- `openai`: OpenAI GPT-4o (기본)
- `claude`: Claude Sonnet 4

### 환경 변수
```bash
# .env 파일에 설정
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key
```

## 🔍 문제 해결

### 다이제스트가 생성되지 않는 경우
1. **논문 데이터 확인**: 해당 날짜/주에 수집된 논문이 있는지 확인
   ```bash
   ls reports/individual_papers/
   ```

2. **API 키 확인**: 환경 변수가 올바르게 설정되었는지 확인
   ```bash
   echo $OPENAI_API_KEY
   echo $ANTHROPIC_API_KEY
   ```

3. **로그 확인**: 백엔드 서버 로그에서 오류 메시지 확인

### API 응답 예시

성공:
```json
{
  "success": true,
  "message": "Daily digest generated successfully",
  "digest_path": "reports/digests/daily_digest_20250915.md",
  "date": "2025-09-15"
}
```

실패:
```json
{
  "detail": "No papers found for the specified date range"
}
```

## 📈 활용 사례

1. **일일 연구 동향 파악**: 매일 생성되는 다이제스트로 최신 AI 연구 동향 추적
2. **주간 보고서**: 팀 미팅용 주간 AI 연구 동향 보고서
3. **자동화된 뉴스레터**: n8n/Zapier를 통한 자동 뉴스레터 발송
4. **연구 기획**: 트렌드 분석을 통한 연구 방향 기획

## 🎯 Pro Tips

1. **정기적 실행**: 스케줄러를 사용해 매일/매주 자동 생성
2. **콜백 활용**: callback_url을 사용해 생성 완료 시 알림 받기
3. **다양한 모델 테스트**: OpenAI와 Claude를 번갈아가며 사용해 결과 비교
4. **날짜 범위 조정**: 주간 다이제스트는 월요일 날짜로 지정하면 해당 주 전체 분석