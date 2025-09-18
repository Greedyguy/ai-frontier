#!/bin/bash

# AI Frontier Frontend 실행 스크립트

echo "🚀 AI Frontier Frontend를 시작합니다..."

# frontend 디렉토리로 이동
cd frontend

# node_modules가 없으면 의존성 설치
if [ ! -d "node_modules" ]; then
    echo "📦 의존성을 설치합니다..."
    npm install
fi

# 개발 서버 시작
echo "🌐 개발 서버를 시작합니다..."
echo "📱 브라우저에서 http://localhost:3000 에 접속하세요"
echo "🛑 Ctrl+C로 서버를 종료할 수 있습니다"
echo "----------------------------------------"

npm run dev