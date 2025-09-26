# n8n Integration Examples

이 문서는 AI Frontier를 n8n에서 사용하는 두 가지 방법을 설명합니다:
1. **스크립트 직접 실행** (서버 불필요)
2. **웹훅 API 사용** (백엔드 서버 필요)

## 방법 1: 스크립트 직접 실행 (추천)

### 장점
- 백엔드 서버를 따로 띄울 필요 없음
- 설정이 간단함
- n8n 워크플로우가 독립적으로 실행됨
- 리소스 사용량이 적음

### n8n 노드 설정

#### 1. Execute Command 노드
```json
{
  "command": "python",
  "arguments": [
    "/path/to/ai_frontier/automation_script.py",
    "collect",
    "--keywords",
    "transformer",
    "attention",
    "--days-back",
    "7"
  ],
  "options": {
    "cwd": "/path/to/ai_frontier"
  }
}
```

#### 2. 동적 파라미터 사용 예시
```json
{
  "command": "python",
  "arguments": [
    "/path/to/ai_frontier/automation_script.py",
    "collect",
    "--keywords",
    "{{ $json.keywords.join('" "') }}",
    "--days-back",
    "{{ $json.days_back || 1 }}"
  ]
}
```

#### 3. 일일 다이제스트 생성
```json
{
  "command": "python",
  "arguments": [
    "/path/to/ai_frontier/automation_script.py",
    "digest",
    "daily"
  ]
}
```

#### 4. 특정 날짜의 주간 다이제스트
```json
{
  "command": "python",
  "arguments": [
    "/path/to/ai_frontier/automation_script.py",
    "digest",
    "weekly",
    "--date",
    "20250926"
  ]
}
```

### 출력 결과 처리

스크립트는 JSON 형태로 결과를 출력합니다:

```json
{
  "success": true,
  "message": "논문 수집 완료: 25개 논문 수집됨",
  "timestamp": "2025-09-26T10:30:00",
  "papers_collected": 25,
  "individual_files_count": 25,
  "report_path": "reports/arxiv_report_20250926.md",
  "individual_files": ["paper1.md", "paper2.md", "..."],
  "collection_params": {
    "keywords": ["transformer", "attention"],
    "categories": ["cs.AI", "cs.LG"],
    "days_back": 7
  }
}
```

### n8n 워크플로우 예시

```json
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.cron",
      "position": [250, 300],
      "parameters": {
        "rule": {
          "hour": 9,
          "minute": 0
        }
      }
    },
    {
      "name": "Collect Papers",
      "type": "n8n-nodes-base.executeCommand",
      "position": [450, 300],
      "parameters": {
        "command": "python",
        "arguments": [
          "/path/to/ai_frontier/automation_script.py",
          "collect",
          "--keywords",
          "transformer",
          "attention",
          "GPT",
          "--days-back",
          "1"
        ],
        "options": {
          "cwd": "/path/to/ai_frontier"
        }
      }
    },
    {
      "name": "Check Result",
      "type": "n8n-nodes-base.if",
      "position": [650, 300],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ JSON.parse($node['Collect Papers'].json.stdout).success }}",
              "value2": true
            }
          ]
        }
      }
    },
    {
      "name": "Send Success Notification",
      "type": "n8n-nodes-base.slack",
      "position": [850, 200],
      "parameters": {
        "channel": "#ai-papers",
        "text": "📚 {{ JSON.parse($node['Collect Papers'].json.stdout).message }}\n\n수집된 논문: {{ JSON.parse($node['Collect Papers'].json.stdout).papers_collected }}개"
      }
    },
    {
      "name": "Send Error Notification",
      "type": "n8n-nodes-base.slack",
      "position": [850, 400],
      "parameters": {
        "channel": "#ai-papers",
        "text": "❌ 논문 수집 실패: {{ JSON.parse($node['Collect Papers'].json.stdout).message }}"
      }
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Collect Papers",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Collect Papers": {
      "main": [
        [
          {
            "node": "Check Result",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Result": {
      "main": [
        [
          {
            "node": "Send Success Notification",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send Error Notification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

## 방법 2: 웹훅 API 사용

### 장점
- 백엔드 서버에서 작업 큐 관리
- 실시간 진행률 모니터링 가능
- 동시 작업 처리 제한 가능

### 단점
- 백엔드 서버를 항상 실행해야 함
- 설정이 복잡함

### 1. 백엔드 서버 실행
```bash
cd /path/to/ai_frontier
python -m ai_frontier.api.server
```

### 2. n8n HTTP Request 노드 설정

#### 비동기 논문 수집
```json
{
  "method": "POST",
  "url": "http://localhost:8080/webhook/collect",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "keywords": ["transformer", "attention"],
    "days_back": 7,
    "callback_url": "https://your-n8n-webhook.com/completion"
  }
}
```

#### 작업 상태 확인
```json
{
  "method": "GET",
  "url": "http://localhost:8080/webhook/status/{{ $json.task_id }}"
}
```

#### 동기 논문 수집 (완료까지 대기)
```json
{
  "method": "POST",
  "url": "http://localhost:8080/webhook/collect-sync",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "keywords": ["transformer", "attention"],
    "days_back": 7
  }
}
```

## 스크립트 사용법 상세

### 기본 명령어들

```bash
# 키워드로 논문 수집
python automation_script.py collect --keywords "transformer" "attention" --days-back 7

# 특정 카테고리에서 수집
python automation_script.py collect --categories "cs.AI" "cs.CV" --days-back 3

# 특정 날짜 범위 수집
python automation_script.py collect --start-date 20250920 --end-date 20250926

# 키워드만으로 수집 (카테고리 제한 없음)
python automation_script.py collect --keywords "quantum computing" --keyword-only

# 일일 다이제스트 생성
python automation_script.py digest daily

# 특정 날짜의 주간 다이제스트
python automation_script.py digest weekly --date 20250926

# 최근 파일 목록 조회
python automation_script.py list --limit 10

# 도움말 보기
python automation_script.py --help
python automation_script.py collect --help
```

### 환경 변수 설정

스크립트 실행 전에 필요한 환경 변수들을 설정하세요:

```bash
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-claude-key"  # Claude 사용시에만
```

또는 `.env` 파일을 사용:

```env
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-claude-key
MODEL_NAME=gpt-4o-mini
DEVICE=auto
DATA_DIR=data
LOG_LEVEL=INFO
```

## 결론

**스크립트 직접 실행 방식**을 추천합니다:
- 설정이 간단하고 유지보수가 쉬움
- 서버 리소스를 절약할 수 있음
- n8n 워크플로우가 독립적으로 실행됨
- JSON 출력으로 결과 처리가 용이함

웹훅 방식은 복잡한 작업 큐 관리나 실시간 모니터링이 필요할 때만 사용하시면 됩니다.