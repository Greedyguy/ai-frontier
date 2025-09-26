# GitHub Pages + GitHub Actions 설정 가이드

AI Frontier 프로젝트를 GitHub Pages와 GitHub Actions를 사용해 완전 자동화된 시스템으로 구축하는 방법입니다.

## 🚀 시스템 구조

```
GitHub Repository
├── GitHub Pages (프론트엔드 호스팅)
│   ├── React 앱 자동 배포
│   └── 생성된 논문 보고서 정적 서빙
├── GitHub Actions (자동화)
│   ├── 매일 논문 수집 (09:00 KST)
│   ├── 일간 다이제스트 생성 (10:00 KST)
│   ├── 주간 다이제스트 생성 (월요일 11:00 KST)
│   └── Slack/Email 알림 자동 발송
└── 수동 실행도 가능
```

## 📋 1단계: Repository 설정

### 1.1 Repository Settings
1. GitHub Repository → **Settings** 이동
2. **Pages** 섹션에서:
   - Source: "GitHub Actions" 선택
   - Branch: main (기본값)

### 1.2 필요한 디렉토리 구조 확인
```
.github/workflows/
├── deploy-pages.yml      # GitHub Pages 배포
├── collect-papers.yml    # 논문 수집 자동화
└── generate-digest.yml   # 다이제스트 생성 자동화
```

## 🔐 2단계: Secrets 설정

GitHub Repository → **Settings** → **Secrets and variables** → **Actions**에서 다음 환경 변수들을 설정:

### 2.1 필수 API Keys
```
OPENAI_API_KEY=sk-...                    # OpenAI API 키 (필수)
ANTHROPIC_API_KEY=sk-ant-...            # Claude API 키 (옵션)
MODEL_NAME=gpt-4o-mini                  # 기본 모델 (옵션, 기본값: gpt-4o-mini)
```

### 2.2 Slack 알림 설정 (옵션)
```
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
SLACK_CHANNEL=#ai-frontier              # 기본값: #ai-frontier
SLACK_BOT_NAME=AI Frontier Bot          # 기본값: AI Frontier Bot
```

### 2.3 Email 알림 설정 (옵션)
```
# Gmail 예시
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587                     # 기본값: 587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password        # Gmail 앱 비밀번호
EMAIL_TO=recipient@example.com
```

### 2.4 기타 설정 (옵션)
```
EMAIL_FROM_NAME=AI Frontier Reports
EMAIL_USE_TLS=true
```

## ⚙️ 3단계: 워크플로우 활성화

### 3.1 자동 스케줄
워크플로우가 자동으로 다음 시간에 실행됩니다:

- **매일 09:00 KST**: 논문 수집
- **매일 10:00 KST**: 일간 다이제스트 생성
- **월요일 11:00 KST**: 주간 다이제스트 생성

### 3.2 수동 실행
GitHub Repository → **Actions** → 원하는 워크플로우 → **Run workflow**

#### 논문 수집 옵션:
- **keywords**: 검색 키워드 (쉼표로 구분)
- **categories**: ArXiv 카테고리 (쉼표로 구분)
- **days_back**: 과거 며칠간 검색
- **start_date/end_date**: 특정 날짜 범위
- **keyword_only**: 키워드만으로 검색

#### 다이제스트 생성 옵션:
- **digest_type**: daily 또는 weekly
- **target_date**: 대상 날짜 (YYYYMMDD)
- **send_notifications**: 알림 발송 여부

## 📱 4단계: GitHub Pages 접속

설정이 완료되면 다음 URL에서 접속 가능:
```
https://[사용자명].github.io/[저장소명]/
```

예시: `https://johndoe.github.io/ai_frontier/`

## 🔧 5단계: 프론트엔드 설정 조정

### 5.1 API URL 설정
`frontend/package.json`에서 build 스크립트 확인:

```json
{
  "scripts": {
    "build": "vite build",
    "build:github": "VITE_API_BASE_URL=/[저장소명]/api vite build"
  }
}
```

### 5.2 GitHub Pages용 라우팅 설정
`frontend/vite.config.js`:

```javascript
export default defineConfig({
  plugins: [react()],
  base: process.env.NODE_ENV === 'production' ? '/[저장소명]/' : '/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
  }
})
```

## 📊 6단계: 모니터링 및 로그

### 6.1 워크플로우 실행 상태 확인
- GitHub Repository → **Actions** 탭
- 각 워크플로우의 실행 로그 확인

### 6.2 생성된 파일 확인
- `reports/individual_papers/`: 개별 논문 파일
- `reports/digests/`: 생성된 다이제스트

### 6.3 알림 확인
- Slack 채널에서 자동 알림 수신
- 이메일로 다이제스트 첨부 파일 수신

## 🛠️ 고급 설정

### 7.1 커스텀 스케줄 변경
`.github/workflows/`의 각 파일에서 `cron` 값을 수정:

```yaml
schedule:
  - cron: '0 0 * * *'  # 매일 09:00 KST (UTC 0:00)
```

### 7.2 수집 파라미터 기본값 변경
`collect-papers.yml`에서 기본 키워드나 카테고리 수정:

```yaml
default: 'transformer,attention,large language model'
```

### 7.3 리소스 제한 고려
- GitHub Actions 무료 플랜: 월 2,000분
- 매일 실행시 약 10-20분 소요 예상
- 필요시 스케줄 조정 (격일, 주 2회 등)

## 🚨 문제 해결

### 8.1 API 키 오류
- Secrets에 정확한 API 키가 설정되었는지 확인
- OpenAI/Anthropic API 사용량 한도 확인

### 8.2 GitHub Pages 배포 실패
- Repository Settings → Pages에서 소스가 "GitHub Actions"로 설정되었는지 확인
- 워크플로우 권한이 충분한지 확인

### 8.3 스케줄 실행 안됨
- Repository가 활성 상태인지 확인 (60일 이상 비활성 시 중단)
- 워크플로우 파일 문법 오류 확인

### 8.4 알림 발송 실패
- Slack Webhook URL과 이메일 설정이 정확한지 확인
- 로그에서 구체적인 오류 메시지 확인

## ✨ 장점

### 💰 비용 효율성
- **GitHub Pages**: 무료 호스팅
- **GitHub Actions**: 무료 플랜 2,000분/월
- **서버 비용 없음**: VPS나 클라우드 인스턴스 불필요

### 🔄 완전 자동화
- 코드 푸시만으로 자동 배포
- 스케줄링된 논문 수집과 다이제스트 생성
- 자동 알림 발송

### 🔒 보안성
- GitHub Secrets로 API 키 안전 보관
- HTTPS 자동 적용
- 버전 관리와 백업 자동화

### 📱 접근성
- 웹 브라우저로 어디서든 접근
- 모바일 친화적 인터페이스
- 정적 파일로 빠른 로딩

이제 GitHub에 푸시하기만 하면 완전 자동화된 AI 논문 수집 및 분석 시스템이 구동됩니다!