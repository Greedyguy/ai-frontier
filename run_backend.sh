#!/bin/bash

# AI Frontier 백엔드 서버 실행 스크립트
# 작성일: 2025-09-17

echo "🚀 AI Frontier 백엔드 서버를 시작합니다..."
echo "📁 작업 디렉토리: $(pwd)"
echo "🐍 Python 가상환경 활성화 중..."

# 가상환경 활성화
source .venv/bin/activate

# Python 경로 확인
echo "✅ Python 경로: $(which python)"
echo "✅ Python 버전: $(python --version)"

# 필요한 환경 변수 설정 (필요시)
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

echo "🌐 백엔드 서버 시작 중..."
echo "📍 서버 주소: http://localhost:8080"
echo "🔗 Health Check: http://localhost:8080/health"
echo "📚 API 문서: http://localhost:8080/docs"
echo ""
echo "⏹️  서버를 종료하려면 Ctrl+C를 누르세요"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 백엔드 서버 실행
python -c "from src.ai_frontier.api.server import run_server; run_server()"
