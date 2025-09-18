/**
 * 로컬 스토리지 유틸리티 함수들
 */

const STORAGE_KEYS = {
  KEYWORDS: 'ai_frontier_keywords',
  CATEGORIES: 'ai_frontier_categories',
  DATE_MODE: 'ai_frontier_date_mode',
  DAYS_BACK: 'ai_frontier_days_back',
  SEARCH_MODE: 'ai_frontier_search_mode',
  TRANSLATION_PROVIDER: 'ai_frontier_translation_provider',
  SUMMARIZATION_PROVIDER: 'ai_frontier_summarization_provider',
  USE_RSS: 'ai_frontier_use_rss'
};

/**
 * 로컬 스토리지에서 데이터 가져오기
 * @param {string} key - 스토리지 키
 * @param {any} defaultValue - 기본값
 * @returns {any} 저장된 값 또는 기본값
 */
export const getStorageItem = (key, defaultValue = null) => {
  try {
    const item = localStorage.getItem(key);
    return item ? JSON.parse(item) : defaultValue;
  } catch (error) {
    console.warn(`Error reading from localStorage for key "${key}":`, error);
    return defaultValue;
  }
};

/**
 * 로컬 스토리지에 데이터 저장하기
 * @param {string} key - 스토리지 키
 * @param {any} value - 저장할 값
 */
export const setStorageItem = (key, value) => {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    console.warn(`Error writing to localStorage for key "${key}":`, error);
  }
};

/**
 * 키워드 관련 스토리지 함수들
 */
export const keywordStorage = {
  // 키워드 불러오기
  load: () => getStorageItem(STORAGE_KEYS.KEYWORDS, []),

  // 키워드 저장하기
  save: (keywords) => setStorageItem(STORAGE_KEYS.KEYWORDS, keywords),

  // 키워드 추가 (중복 제거)
  add: (newKeyword) => {
    const keywords = keywordStorage.load();
    if (!keywords.includes(newKeyword)) {
      const updatedKeywords = [...keywords, newKeyword];
      keywordStorage.save(updatedKeywords);
      return updatedKeywords;
    }
    return keywords;
  },

  // 키워드 제거
  remove: (keywordToRemove) => {
    const keywords = keywordStorage.load();
    const updatedKeywords = keywords.filter(keyword => keyword !== keywordToRemove);
    keywordStorage.save(updatedKeywords);
    return updatedKeywords;
  },

  // 키워드 전체 업데이트
  update: (newKeywords) => {
    keywordStorage.save(newKeywords);
    return newKeywords;
  },

  // 키워드 초기화
  clear: () => {
    keywordStorage.save([]);
    return [];
  }
};

/**
 * 카테고리 관련 스토리지 함수들
 */
export const categoryStorage = {
  load: () => getStorageItem(STORAGE_KEYS.CATEGORIES, ['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV']),
  save: (categories) => setStorageItem(STORAGE_KEYS.CATEGORIES, categories)
};

/**
 * 검색 모드 관련 스토리지 함수들
 */
export const searchModeStorage = {
  load: () => getStorageItem(STORAGE_KEYS.SEARCH_MODE, 'category'),
  save: (searchMode) => setStorageItem(STORAGE_KEYS.SEARCH_MODE, searchMode)
};

/**
 * 날짜 설정 관련 스토리지 함수들
 */
export const dateStorage = {
  loadMode: () => getStorageItem(STORAGE_KEYS.DATE_MODE, 'recent'),
  saveMode: (dateMode) => setStorageItem(STORAGE_KEYS.DATE_MODE, dateMode),

  loadDaysBack: () => getStorageItem(STORAGE_KEYS.DAYS_BACK, 7),
  saveDaysBack: (daysBack) => setStorageItem(STORAGE_KEYS.DAYS_BACK, daysBack)
};

/**
 * AI 서비스 관련 스토리지 함수들
 */
export const aiServiceStorage = {
  loadTranslation: () => getStorageItem(STORAGE_KEYS.TRANSLATION_PROVIDER, 'openai'),
  saveTranslation: (provider) => setStorageItem(STORAGE_KEYS.TRANSLATION_PROVIDER, provider),

  loadSummarization: () => getStorageItem(STORAGE_KEYS.SUMMARIZATION_PROVIDER, 'openai'),
  saveSummarization: (provider) => setStorageItem(STORAGE_KEYS.SUMMARIZATION_PROVIDER, provider)
};

/**
 * RSS 옵션 관련 스토리지 함수들
 */
export const rssStorage = {
  load: () => getStorageItem(STORAGE_KEYS.USE_RSS, false),
  save: (useRss) => setStorageItem(STORAGE_KEYS.USE_RSS, useRss)
};

/**
 * 모든 설정을 한번에 불러오기
 */
export const loadAllSettings = () => {
  return {
    keywords: keywordStorage.load(),
    categories: categoryStorage.load(),
    searchMode: searchModeStorage.load(),
    dateMode: dateStorage.loadMode(),
    daysBack: dateStorage.loadDaysBack(),
    translationProvider: aiServiceStorage.loadTranslation(),
    summarizationProvider: aiServiceStorage.loadSummarization(),
    useRss: rssStorage.load()
  };
};

/**
 * 전체 스토리지 초기화
 */
export const clearAllSettings = () => {
  Object.values(STORAGE_KEYS).forEach(key => {
    try {
      localStorage.removeItem(key);
    } catch (error) {
      console.warn(`Error removing localStorage key "${key}":`, error);
    }
  });
};