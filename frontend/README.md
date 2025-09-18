# AI Frontier Frontend

React 기반 ArXiv 논문 수집 서비스의 프론트엔드 인터페이스입니다.

## 주요 기능

### 🏷️ 키워드 해시태그 입력
- Enter, Tab, 쉼표로 키워드 추가
- 해시태그 형태로 시각화
- 드래그&드롭으로 순서 변경
- 일괄 붙여넣기 지원

### 📅 날짜 범위 선택
- **최근 N일**: 빠른 선택 버튼 제공
- **특정 날짜 범위**: 달력 인터페이스
- 실시간 날짜 범위 미리보기

### 📚 카테고리 선택
- 계층적 카테고리 구조
- 검색 및 필터링 기능
- 섹션별 일괄 선택/해제
- 인기 카테고리 빠른 선택

### 🔍 검색 모드
- **카테고리 기반**: 선택된 카테고리에서만 검색
- **카테고리 + 키워드**: 카테고리 내에서 키워드 검색
- **키워드 전용**: 모든 분야에서 키워드 검색

## 설치 및 실행

```bash
# 의존성 설치
cd frontend
npm install

# 개발 서버 실행
npm run dev

# 브라우저에서 접속
# http://localhost:3000
```

## 기술 스택

- **React 18**: 컴포넌트 기반 UI
- **Vite**: 빠른 개발 빌드 도구
- **Tailwind CSS**: 유틸리티 기반 스타일링
- **Lucide React**: 아이콘 라이브러리
- **date-fns**: 날짜 처리

## 프로젝트 구조

```
frontend/
├── src/
│   ├── components/          # 재사용 가능한 컴포넌트
│   │   ├── KeywordInput.jsx     # 키워드 해시태그 입력
│   │   ├── DateRangePicker.jsx  # 날짜 범위 선택
│   │   └── CategorySelector.jsx # 카테고리 선택
│   ├── App.jsx             # 메인 애플리케이션
│   ├── main.jsx           # 엔트리 포인트
│   └── index.css          # 글로벌 스타일
├── index.html
├── package.json
├── vite.config.js
└── tailwind.config.js
```

## 컴포넌트 사용법

### KeywordInput
```jsx
<KeywordInput
  keywords={keywords}
  setKeywords={setKeywords}
  placeholder="키워드를 입력하세요..."
/>
```

### DateRangePicker
```jsx
<DateRangePicker
  dateMode={dateMode}
  setDateMode={setDateMode}
  daysBack={daysBack}
  setDaysBack={setDaysBack}
  startDate={startDate}
  setStartDate={setStartDate}
  endDate={endDate}
  setEndDate={setEndDate}
/>
```

### CategorySelector
```jsx
<CategorySelector
  selectedCategories={selectedCategories}
  setSelectedCategories={setSelectedCategories}
/>
```

## 백엔드 연동

현재는 프론트엔드만 구현되어 있으며, 실제 논문 수집을 위해서는 Python 백엔드와 연동이 필요합니다.

### API 연동 예정 기능
- 논문 검색 요청
- 수집 진행 상황 모니터링
- 결과 다운로드
- 실시간 상태 업데이트

## 개발 가이드

### 스타일링
- Tailwind CSS 유틸리티 클래스 사용
- 커스텀 컴포넌트 스타일은 `@layer components`에 정의
- 반응형 디자인 지원 (모바일 우선)

### 상태 관리
- React hooks (useState) 사용
- 추후 복잡도 증가 시 Context API 또는 Redux 도입 예정

### 빌드
```bash
# 프로덕션 빌드
npm run build

# 빌드 미리보기
npm run preview
```