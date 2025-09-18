# AI Frontier

ArXiv 논문 자동 번역 및 요약 리포팅 서비스

AI Frontier는 arxiv.org에서 최신 AI/ML 논문들을 자동으로 수집하고, AI를 활용해 초록을 번역 및 요약하여 일일 리포트를 생성하는 자동화 서비스입니다.

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

- **ArXiv 논문 수집**: 지정된 카테고리의 최신 논문 자동 검색
- **AI 번역**: OpenAI/Claude를 활용한 고품질 한국어 번역
- **자동 요약**: 논문 초록의 핵심 내용 요약 및 주요 포인트 추출
- **리포트 생성**: Markdown/HTML 형식의 일일 리포트 자동 생성
- **다중 AI 제공자**: OpenAI, Claude 등 여러 AI 서비스 지원

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
│       ├── utils/           # 유틸리티 함수
│       └── main.py          # 메인 애플리케이션
├── tests/                   # 테스트 파일
└── reports/                 # 생성된 리포트 저장
```

## Usage

### CLI 사용법

```bash
# 기본 실행 (최근 1일간의 AI 논문들)
python -m src.ai_frontier.main

# 키워드로 검색 (카테고리 + 키워드 조합)
python -m src.ai_frontier.main \
  --keywords "multimodal" "attention" "transformer" \
  --categories cs.AI cs.CV

# 키워드만으로 검색 (카테고리 제한 없음)
python -m src.ai_frontier.main \
  --keywords "large language model" "GPT" "BERT" \
  --keyword-only \
  --days-back 7

# 전체 옵션
python -m src.ai_frontier.main \
  --categories cs.AI cs.LG cs.CL cs.CV \
  --keywords "neural network" "deep learning" \
  --days-back 3 \
  --translation-provider openai \
  --summarization-provider claude \
  --output-dir ./reports
```

### Python 코드에서 사용

```python
from src.ai_frontier.main import ArxivReportingService

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