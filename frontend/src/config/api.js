// API configuration for different environments
const getApiBaseUrl = () => {
  // Production (GitHub Pages)
  if (process.env.NODE_ENV === 'production') {
    // GitHub Pages에서는 정적 파일만 서빙 가능
    // 실제 API는 GitHub Actions 워크플로우로 처리
    return '';
  }

  // Development
  return '';
};

export const API_BASE_URL = getApiBaseUrl();

// GitHub Pages용 정적 API 응답 처리
export const isStaticMode = process.env.NODE_ENV === 'production';

// 정적 모드에서 사용할 mock API 응답들
export const staticApiResponses = {
  '/api/files': {
    files: [],
    total: 0,
    message: 'GitHub Pages에서는 정적 파일만 제공됩니다. 실시간 데이터는 GitHub Actions 워크플로우를 사용하세요.'
  },

  '/api/tasks': {
    total_tasks: 0,
    tasks: [],
    active_tasks: [],
    message: 'GitHub Pages에서는 백그라운드 작업을 지원하지 않습니다. GitHub Actions 워크플로우를 사용하세요.'
  },

  '/api/digests': {
    digests: [],
    total: 0,
    message: '다이제스트는 GitHub Actions로 자동 생성됩니다.'
  }
};

// API URL 생성 헬퍼
export const createApiUrl = (endpoint) => {
  return `${API_BASE_URL}${endpoint}`;
};

// 정적 모드에서 API 응답 처리
export const getStaticResponse = (endpoint) => {
  return staticApiResponses[endpoint] || {
    error: 'GitHub Pages에서는 이 기능을 사용할 수 없습니다.',
    message: '실시간 기능은 로컬 개발 환경에서 사용하세요.'
  };
};