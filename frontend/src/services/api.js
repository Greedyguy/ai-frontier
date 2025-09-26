/**
 * API 클라이언트 서비스
 * FastAPI 백엔드와 통신하는 함수들을 제공합니다.
 */

import { API_BASE_URL, isStaticMode, getStaticResponse, createApiUrl } from '../config/api.js';

const API_BASE_URL_LEGACY = 'http://localhost:8080';

/**
 * API 응답 에러를 처리하는 함수
 */
const handleApiError = async (response) => {
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }));
    throw new Error(errorData.detail || `HTTP ${response.status}: ${response.statusText}`);
  }
  return response;
};

/**
 * 논문 수집을 시작하는 API 호출
 * @param {Object} requestData - 수집 요청 데이터
 * @returns {Promise<Object>} 작업 ID를 포함한 응답 객체
 */
export const startCollection = async (requestData) => {
  try {
    console.log('🚀 Starting collection with data:', requestData);

    // GitHub Pages 정적 모드에서는 실제 API 호출 대신 안내 메시지 반환
    if (isStaticMode) {
      console.log('📍 Static mode detected - GitHub Pages deployment');
      return {
        success: false,
        message: 'GitHub Pages는 정적 호스팅입니다.',
        instructions: [
          '실시간 논문 수집은 GitHub Actions 워크플로우를 사용하세요:',
          '1. Repository → Actions → "Collect ArXiv Papers" 선택',
          '2. "Run workflow" 버튼 클릭',
          '3. 파라미터 설정 후 실행',
          '',
          '또는 로컬 환경에서 백엔드 서버를 실행하세요:',
          'python -m ai_frontier.api.server'
        ],
        github_actions_url: 'https://github.com/Greedyguy/ai-frontier/actions/workflows/collect-papers.yml'
      };
    }

    console.log('🔗 API URL:', `${API_BASE_URL_LEGACY}/api/collect`);

    const response = await fetch(`${API_BASE_URL_LEGACY}/api/collect`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    });

    console.log('📥 Start collection response status:', response.status, response.statusText);
    console.log('📋 Response headers:', Object.fromEntries(response.headers.entries()));

    if (!response.ok) {
      const errorText = await response.text();
      console.error('❌ Response error text:', errorText);
      throw new Error(`HTTP ${response.status}: ${response.statusText} - ${errorText}`);
    }

    const data = await response.json();
    console.log('✅ Start collection response data:', data);
    console.log('🆔 Task ID received:', data.task_id);
    return data;
  } catch (error) {
    console.error('❌ Failed to start collection:', error);
    console.error('🔍 Error details:', {
      name: error.name,
      message: error.message,
      stack: error.stack
    });
    throw error;
  }
};

/**
 * 특정 작업의 상태를 조회하는 API 호출
 * @param {string} taskId - 작업 ID
 * @returns {Promise<Object>} 작업 상태 객체
 */
export const getCollectionStatus = async (taskId) => {
  try {
    const url = `${API_BASE_URL}/api/status/${taskId}`;
    console.log(`🔍 Requesting status for task: ${taskId} from ${url}`);
    const response = await fetch(url);
    console.log('📥 Status response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('📊 Status data:', data);
    return data;
  } catch (error) {
    console.error('❌ Failed to get collection status:', error);
    console.error('🔗 URL was:', `${API_BASE_URL}/api/status/${taskId}`);
    console.error('🆔 TaskId was:', taskId);
    throw error;
  }
};

/**
 * 모든 작업 목록을 조회하는 API 호출
 * @returns {Promise<Object>} 작업 목록 객체
 */
export const getAllTasks = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/tasks`);
    await handleApiError(response);
    return await response.json();
  } catch (error) {
    console.error('Failed to get all tasks:', error);
    throw error;
  }
};

/**
 * 보고서를 다운로드하는 함수
 * @param {string} taskId - 작업 ID
 * @returns {Promise<void>} 파일 다운로드 시작
 */
export const downloadReport = async (taskId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/download/${taskId}`);
    await handleApiError(response);

    // 파일을 blob으로 다운로드
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `arxiv_report_${taskId.slice(0, 8)}.md`;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
  } catch (error) {
    console.error('Failed to download report:', error);
    throw error;
  }
};

/**
 * 작업을 삭제하는 API 호출
 * @param {string} taskId - 작업 ID
 * @returns {Promise<Object>} 삭제 결과 객체
 */
export const deleteTask = async (taskId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/tasks/${taskId}`, {
      method: 'DELETE',
    });
    await handleApiError(response);
    return await response.json();
  } catch (error) {
    console.error('Failed to delete task:', error);
    throw error;
  }
};

/**
 * 서버 헬스 체크
 * @returns {Promise<Object>} 헬스 체크 결과
 */
export const healthCheck = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    await handleApiError(response);
    return await response.json();
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};

/**
 * 진행 상황을 실시간으로 모니터링하는 폴링 함수
 * @param {string} taskId - 작업 ID
 * @param {Function} onProgress - 진행 상황 업데이트 콜백
 * @param {number} interval - 폴링 간격 (밀리초, 기본: 2000)
 * @returns {Function} 폴링을 중단하는 함수
 */
export const monitorProgress = (taskId, onProgress, interval = 2000) => {
  console.log('🚀 MonitorProgress function called with:', { taskId, interval });
  let timeoutId;
  let isActive = true;

  const poll = async () => {
    if (!isActive) {
      console.log('⏹️ Poll function called but monitoring is not active');
      return;
    }

    try {
      console.log(`📡 Polling status for task: ${taskId}`);
      const status = await getCollectionStatus(taskId);
      console.log('✅ Received status:', status);
      onProgress(status);

      // 작업이 완료되지 않았다면 계속 폴링
      if (status.status !== 'completed' && status.status !== 'error' && status.status !== 'cancelled' && isActive) {
        console.log(`⏱️ Scheduling next poll in ${interval}ms`);
        timeoutId = setTimeout(poll, interval);
      } else {
        console.log(`🛑 Polling stopped. Status: ${status.status}, isActive: ${isActive}`);
      }
    } catch (error) {
      console.error('❌ Error while monitoring progress:', error);
      if (isActive) {
        console.log(`🔄 Retrying in ${interval}ms due to error`);
        timeoutId = setTimeout(poll, interval);
      }
    }
  };

  // 첫 번째 폴링을 약간 지연시켜 백엔드가 작업을 등록할 시간을 줍니다
  console.log('⏰ Starting first poll in 500ms...');
  timeoutId = setTimeout(poll, 500);

  // 폴링을 중단하는 함수 반환
  return () => {
    console.log('🛑 MonitorProgress cleanup called');
    isActive = false;
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
  };
};

/**
 * 수집된 논문 목록을 가져오는 API 호출
 * @param {string} taskId - 작업 ID
 * @returns {Promise<Array>} 수집된 논문 목록
 */
export const getCollectedPapers = async (taskId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/papers/${taskId}`);
    await handleApiError(response);
    return await response.json();
  } catch (error) {
    console.error('Failed to get collected papers:', error);
    throw error;
  }
};

/**
 * 논문 파일 목록을 가져오는 API 호출
 * @returns {Promise<Array>} 생성된 논문 파일 목록
 */
export const getPaperFiles = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/files`);
    await handleApiError(response);
    return await response.json();
  } catch (error) {
    console.error('Failed to get paper files:', error);
    throw error;
  }
};

/**
 * 프론트엔드 폼 데이터를 API 요청 형식으로 변환
 * @param {Object} formData - 프론트엔드 폼 데이터
 * @returns {Object} API 요청 형식의 데이터
 */
/**
 * 논문 수집 작업 중단 API 호출
 * @param {string} taskId - 작업 ID
 * @returns {Promise<Object>} 중단 결과 객체
 */
export const cancelCollection = async (taskId) => {
  try {
    console.log(`Cancelling task: ${taskId}`);
    const response = await fetch(`${API_BASE_URL}/api/cancel/${taskId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    console.log('Cancel response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('Cancel result:', data);
    return data;
  } catch (error) {
    console.error('Failed to cancel collection:', error);
    throw error;
  }
};

export const transformFormDataToApiRequest = (formData) => {
  const request = {
    keywords: formData.keywords || [],
    categories: formData.categories || [],
    search_mode: formData.searchMode || 'category',
    date_mode: formData.dateMode || 'recent',
    translation_provider: formData.translationProvider || 'openai',
    summarization_provider: formData.summarizationProvider || 'openai',
    target_language: formData.targetLanguage || 'ko',
    use_rss: formData.useRss || false,
  };

  // 날짜 모드에 따라 적절한 파라미터만 설정
  if (formData.dateMode === 'range') {
    // 범위 모드: start_date와 end_date 사용
    request.start_date = formData.startDate || null;
    request.end_date = formData.endDate || null;
    request.days_back = null; // 명시적으로 null 설정
  } else {
    // 최근 모드: days_back 사용
    request.days_back = formData.daysBack || 7;
    request.start_date = null; // 명시적으로 null 설정
    request.end_date = null; // 명시적으로 null 설정
  }

  return request;
};

/**
 * 일일 다이제스트 생성 API 호출
 * @param {string} date - 날짜 (YYYYMMDD 형식, 선택사항)
 * @returns {Promise<Object>} 다이제스트 생성 결과
 */
export const generateDailyDigest = async (date = null) => {
  try {
    console.log('🗓️ Generating daily digest for date:', date);

    const url = date
      ? `${API_BASE_URL}/api/digest/daily?date=${date}`
      : `${API_BASE_URL}/api/digest/daily`;

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    console.log('Daily digest response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('Daily digest result:', data);
    return data;
  } catch (error) {
    console.error('Failed to generate daily digest:', error);
    throw error;
  }
};

/**
 * 주간 다이제스트 생성 API 호출
 * @param {string} date - 날짜 (YYYYMMDD 형식, 선택사항)
 * @returns {Promise<Object>} 다이제스트 생성 결과
 */
export const generateWeeklyDigest = async (date = null) => {
  try {
    console.log('📅 Generating weekly digest for date:', date);

    const url = date
      ? `${API_BASE_URL}/api/digest/weekly?date=${date}`
      : `${API_BASE_URL}/api/digest/weekly`;

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    console.log('Weekly digest response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('Weekly digest result:', data);
    return data;
  } catch (error) {
    console.error('Failed to generate weekly digest:', error);
    throw error;
  }
};

/**
 * 생성된 다이제스트 목록 조회 API 호출
 * @returns {Promise<Object>} 다이제스트 목록
 */
export const getDigests = async () => {
  try {
    console.log('📋 Fetching digests list');

    const response = await fetch(`${API_BASE_URL}/api/digests`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    console.log('Get digests response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('Digests list:', data);
    return data;
  } catch (error) {
    console.error('Failed to get digests:', error);
    throw error;
  }
};

/**
 * 하이브리드 검색 API 호출
 * @param {Object} searchRequest - 검색 요청 데이터
 * @returns {Promise<Object>} 검색 결과
 */
export const hybridSearch = async (searchRequest) => {
  try {
    console.log('🔍 Performing hybrid search:', searchRequest);

    const response = await fetch(`${API_BASE_URL}/api/search/hybrid`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(searchRequest),
    });

    console.log('Hybrid search response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('Hybrid search results:', data);
    return data;
  } catch (error) {
    console.error('Failed to perform hybrid search:', error);
    throw error;
  }
};

/**
 * 하이브리드 검색 통계 조회 API 호출
 * @returns {Promise<Object>} 하이브리드 검색 통계
 */
export const getHybridSearchStats = async () => {
  try {
    console.log('📊 Fetching hybrid search stats');

    const response = await fetch(`${API_BASE_URL}/api/search/hybrid/stats`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    console.log('Hybrid search stats response:', response.status, response.statusText);
    await handleApiError(response);
    const data = await response.json();
    console.log('Hybrid search stats:', data);
    return data;
  } catch (error) {
    console.error('Failed to get hybrid search stats:', error);
    throw error;
  }
};