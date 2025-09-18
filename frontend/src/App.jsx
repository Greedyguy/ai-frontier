import React, { useState, useEffect } from 'react';
import { Search, Settings, Download, Play, Pause, RotateCcw, Trash2, AlertCircle, CheckCircle } from 'lucide-react';
import KeywordInput from './components/KeywordInput';
import DateRangePicker from './components/DateRangePicker';
import CategorySelector from './components/CategorySelector';
import PaperList from './components/PaperList';
import { loadAllSettings, categoryStorage, searchModeStorage, dateStorage, aiServiceStorage, rssStorage, clearAllSettings } from './utils/storage';
import { startCollection, getCollectionStatus, monitorProgress, transformFormDataToApiRequest, downloadReport, cancelCollection } from './services/api';

function App() {
  // 키워드 상태
  const [keywords, setKeywords] = useState([]);

  // 날짜 상태
  const [dateMode, setDateMode] = useState('recent'); // 'recent' 또는 'range'
  const [daysBack, setDaysBack] = useState(7);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  // 카테고리 상태
  const [selectedCategories, setSelectedCategories] = useState(['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV']);

  // 검색 모드 상태
  const [searchMode, setSearchMode] = useState('category'); // 'category', 'keyword', 'keyword-only'

  // AI 서비스 설정
  const [translationProvider, setTranslationProvider] = useState('openai');
  const [summarizationProvider, setSummarizationProvider] = useState('openai');

  // 검색 방식 설정
  const [useRss, setUseRss] = useState(false);

  // UI 상태 - 새로운 변수명으로 충돌 방지
  const [isProcessing, setIsProcessingState] = useState(false);

  // setIsProcessing wrapper for debugging
  const setIsProcessing = (value) => {
    console.log('🔧 setIsProcessing called with:', value);
    console.trace('📍 Stack trace:');
    setIsProcessingState(value);
  };

  const [showAdvanced, setShowAdvanced] = useState(false);
  const [showPaperList, setShowPaperList] = useState(true); // 기본적으로 표시

  // API 관련 상태
  const [currentTask, setCurrentTask] = useState(null);
  const [taskStatus, setTaskStatus] = useState(null);
  const [error, setError] = useState(null);

  // 호환성을 위한 alias
  const isCollecting = isProcessing;
  const setIsCollecting = setIsProcessing;

  // 디버깅: isCollecting 상태 로그
  useEffect(() => {
    console.log('🔄 isCollecting state changed to:', isCollecting);
    console.log('🔄 isProcessing state:', isProcessing);
    console.log('🔄 All states:', {
      isCollecting,
      isProcessing,
      currentTask,
      taskStatus: taskStatus?.status
    });
    console.trace('📍 Stack trace for isCollecting change:');
  }, [isCollecting, isProcessing, currentTask, taskStatus]);

  // 컴포넌트 마운트 시 저장된 설정 불러오기
  useEffect(() => {
    console.log('🚀 App component mounted, initializing...');
    const settings = loadAllSettings();

    // 키워드는 KeywordInput 컴포넌트에서 처리
    setSelectedCategories(settings.categories);
    setSearchMode(settings.searchMode);
    setDateMode(settings.dateMode);
    setDaysBack(settings.daysBack);
    setTranslationProvider(settings.translationProvider);
    setSummarizationProvider(settings.summarizationProvider);
    setUseRss(settings.useRss);

    // 수집 상태 명시적 초기화
    setIsCollecting(false);
    setCurrentTask(null);
    setTaskStatus(null);
    setError(null);

    console.log('✅ App component initialized');
  }, []);

  // 설정 변경 시 자동 저장
  useEffect(() => {
    categoryStorage.save(selectedCategories);
  }, [selectedCategories]);

  useEffect(() => {
    searchModeStorage.save(searchMode);
  }, [searchMode]);

  useEffect(() => {
    dateStorage.saveMode(dateMode);
  }, [dateMode]);

  useEffect(() => {
    dateStorage.saveDaysBack(daysBack);
  }, [daysBack]);

  useEffect(() => {
    aiServiceStorage.saveTranslation(translationProvider);
  }, [translationProvider]);

  useEffect(() => {
    aiServiceStorage.saveSummarization(summarizationProvider);
  }, [summarizationProvider]);

  useEffect(() => {
    rssStorage.save(useRss);
  }, [useRss]);

  // 설정 관리 함수들
  const resetToDefaults = () => {
    if (confirm('모든 설정을 기본값으로 초기화하시겠습니까?')) {
      clearAllSettings();
      // 기본값으로 재설정
      setKeywords([]);
      setSelectedCategories(['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV']);
      setSearchMode('category');
      setDateMode('recent');
      setDaysBack(7);
      setTranslationProvider('openai');
      setSummarizationProvider('openai');
      setUseRss(false);
    }
  };

  // 디버깅: isCollecting 강제 리셋 함수
  const forceResetCollecting = () => {
    console.log('🔧 Force resetting isProcessing to false');
    setIsProcessing(false);
    setCurrentTask(null);
    setTaskStatus(null);
  };

  // 개발 모드에서 전역으로 접근 가능하게 만들기
  if (typeof window !== 'undefined') {
    window.forceResetCollecting = forceResetCollecting;
  }

  const reloadSettings = () => {
    const settings = loadAllSettings();
    setKeywords(settings.keywords);
    setSelectedCategories(settings.categories);
    setSearchMode(settings.searchMode);
    setDateMode(settings.dateMode);
    setDaysBack(settings.daysBack);
    setTranslationProvider(settings.translationProvider);
    setSummarizationProvider(settings.summarizationProvider);
  };

  // 폼 검증
  const canSubmit = () => {
    console.log('🔍 canSubmit called with:', { searchMode, keywords: keywords.length, selectedCategories: selectedCategories.length, dateMode, startDate, endDate });

    if (searchMode === 'keyword-only' && keywords.length === 0) {
      console.log('❌ canSubmit: false - keyword-only mode but no keywords');
      return false;
    }
    if (searchMode === 'category' && selectedCategories.length === 0) {
      console.log('❌ canSubmit: false - category mode but no categories');
      return false;
    }
    if (dateMode === 'range' && (!startDate || !endDate)) {
      console.log('❌ canSubmit: false - range mode but missing dates');
      return false;
    }
    console.log('✅ canSubmit: true');
    return true;
  };

  // 수집 시작
  const handleStartCollection = async () => {
    console.log('🎯 handleStartCollection function called!');
    console.log('🔍 canSubmit():', canSubmit());
    console.log('📊 Current state:', { isCollecting, keywords, selectedCategories, searchMode });

    if (!canSubmit()) {
      console.log('❌ Cannot submit - validation failed');
      return;
    }

    const formData = {
      keywords,
      categories: selectedCategories,
      searchMode,
      dateMode,
      daysBack,
      startDate,
      endDate,
      translationProvider,
      summarizationProvider,
      targetLanguage: 'ko',
      useRss
    };

    setError(null);
    setIsCollecting(true);

    try {
      // API 요청 형식으로 변환
      const apiRequest = transformFormDataToApiRequest(formData);
      console.log('🚀 Starting collection with config:', apiRequest);

      // 수집 시작
      console.log('📞 Calling startCollection API...');
      console.log('⏰ Current time:', new Date().toISOString());

      const response = await startCollection(apiRequest);

      console.log('✅ StartCollection completed successfully');
      console.log('📋 Response object:', response);
      console.log('🆔 Task ID from response:', response?.task_id);

      const taskId = response.task_id;

      if (!taskId) {
        console.error('❌ No task ID in response:', response);
        throw new Error('No task ID received from server');
      }

      setCurrentTask(taskId);
      console.log('✅ Collection started successfully, task ID:', taskId);
      console.log('🔄 Starting progress monitoring...');

      // 진행 상황 모니터링 시작
      const stopMonitoring = monitorProgress(taskId, (status) => {
        console.log('Progress callback called with status:', status);
        setTaskStatus(status);

        // 완료, 에러, 중단 시 수집 상태 업데이트
        if (status.status === 'completed' || status.status === 'error' || status.status === 'cancelled') {
          console.log('Task finished with status:', status.status);
          setIsCollecting(false);
          // 수집 완료 시 논문 목록 자동 표시
          if (status.status === 'completed') {
            setShowPaperList(true);
          }
        }
      });

      console.log('MonitorProgress started, stopFunction:', typeof stopMonitoring);

      // 컴포넌트 언마운트 시 모니터링 정리를 위해 저장
      window.currentStopMonitoring = stopMonitoring;

    } catch (err) {
      console.error('❌ Failed to start collection - Error details:');
      console.error('📛 Error name:', err.name);
      console.error('💬 Error message:', err.message);
      console.error('📚 Error stack:', err.stack);
      console.error('🔍 Full error object:', err);
      console.error('⏰ Error occurred at:', new Date().toISOString());

      setError(err.message);
      setIsCollecting(false);
    }
  };

  // 진행 중인 작업 취소
  const handleStopCollection = async () => {
    console.log('🛑 handleStopCollection function called!');
    console.log('📊 Current state:', { isCollecting, currentTask });
    console.log('🔍 currentTask:', currentTask);
    if (!currentTask) {
      console.log('❌ No current task to cancel');
      return;
    }

    try {
      console.log('Sending cancel request for task:', currentTask);
      // 백엔드에 중단 요청
      await cancelCollection(currentTask);
      console.log('Collection cancelled successfully');

      // 프론트엔드 모니터링 중단
      if (window.currentStopMonitoring) {
        console.log('Stopping monitoring');
        window.currentStopMonitoring();
        window.currentStopMonitoring = null;
      }

      // 모든 관련 상태를 즉시 리셋
      setIsCollecting(false);
      setIsProcessing(false);
      setCurrentTask(null);
      setTaskStatus(null);
      console.log('UI state completely reset after successful cancel');
    } catch (err) {
      console.error('Failed to cancel collection:', err);
      setError(err.message);

      // 실패해도 프론트엔드 상태는 리셋
      if (window.currentStopMonitoring) {
        console.log('Stopping monitoring after error');
        window.currentStopMonitoring();
        window.currentStopMonitoring = null;
      }
      // 에러가 발생해도 모든 상태 리셋
      setIsCollecting(false);
      setIsProcessing(false);
      setCurrentTask(null);
      console.log('UI state reset after error');
    }
  };

  // 보고서 다운로드
  const handleDownloadReport = async () => {
    if (!currentTask) return;

    try {
      await downloadReport(currentTask);
    } catch (err) {
      console.error('Failed to download report:', err);
      setError(err.message);
    }
  };

  // 설정 요약 생성
  const getConfigSummary = () => {
    const parts = [];

    if (searchMode === 'category') {
      parts.push(`카테고리: ${selectedCategories.length}개`);
    }

    if (keywords.length > 0) {
      parts.push(`키워드: ${keywords.length}개`);
    }

    if (dateMode === 'recent') {
      parts.push(`최근 ${daysBack}일`);
    } else {
      parts.push(`${startDate} ~ ${endDate}`);
    }

    return parts.join(' | ');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* 헤더 */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
                <Search size={20} className="text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">AI Frontier</h1>
                <p className="text-sm text-gray-500">ArXiv 논문 자동 수집 & 번역 서비스</p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={reloadSettings}
                className="p-2 rounded-lg text-gray-500 hover:text-gray-700 hover:bg-gray-100 transition-colors"
                title="저장된 설정 다시 불러오기"
              >
                <RotateCcw size={18} />
              </button>
              <button
                type="button"
                onClick={resetToDefaults}
                className="p-2 rounded-lg text-gray-500 hover:text-red-600 hover:bg-red-50 transition-colors"
                title="모든 설정 초기화"
              >
                <Trash2 size={18} />
              </button>
              <button
                type="button"
                onClick={() => setShowAdvanced(!showAdvanced)}
                className={`p-2 rounded-lg transition-colors ${
                  showAdvanced ? 'bg-primary-100 text-primary-700' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-100'
                }`}
                title="고급 설정 토글"
              >
                <Settings size={18} />
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* 메인 컨텐츠 */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* 전체 설정을 한 줄에 배치 */}
        <div className="space-y-6">
          {/* 첫 번째 행: 검색 모드 + 키워드 */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* 검색 모드 선택 */}
            <div className="card p-4">
              <h2 className="text-base font-semibold text-gray-900 mb-3">검색 모드</h2>
              <div className="grid grid-cols-3 gap-2">
                <button
                  type="button"
                  onClick={() => setSearchMode('category')}
                  className={`p-3 rounded-lg border-2 transition-colors text-xs ${
                    searchMode === 'category'
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <div className="font-medium">카테고리</div>
                  <div className="text-gray-500 mt-1">CS 카테고리</div>
                </button>
                <button
                  type="button"
                  onClick={() => setSearchMode('keyword')}
                  className={`p-3 rounded-lg border-2 transition-colors text-xs ${
                    searchMode === 'keyword'
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <div className="font-medium">카테고리+키워드</div>
                  <div className="text-gray-500 mt-1">조합 검색</div>
                </button>
                <button
                  type="button"
                  onClick={() => setSearchMode('keyword-only')}
                  className={`p-3 rounded-lg border-2 transition-colors text-xs ${
                    searchMode === 'keyword-only'
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <div className="font-medium">키워드 전용</div>
                  <div className="text-gray-500 mt-1">전 분야</div>
                </button>
              </div>
            </div>

            {/* 키워드 입력 */}
            <div className="card p-4">
              <KeywordInput
                keywords={keywords}
                setKeywords={setKeywords}
                placeholder="transformer, attention, neural network 등..."
              />
            </div>

          </div>

          {/* 두 번째 행: 카테고리 + 날짜 */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* 카테고리 선택 */}
            {(searchMode === 'category' || searchMode === 'keyword') && (
              <div className="card p-4">
                <CategorySelector
                  selectedCategories={selectedCategories}
                  setSelectedCategories={setSelectedCategories}
                />
              </div>
            )}

            {/* 날짜 범위 선택 */}
            <div className={`card p-4 ${(searchMode !== 'category' && searchMode !== 'keyword') ? 'lg:col-span-2' : ''}`}>
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
            </div>
          </div>

          {/* 세 번째 행: 실행 버튼 + 고급 설정 + 상태 */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* 실행 및 설정 요약 */}
            <div className="card p-4">
              <h3 className="text-base font-semibold text-gray-900 mb-3">실행</h3>

              {/* 설정 요약 */}
              <div className="space-y-2 mb-4 text-xs">
                <div className="flex justify-between">
                  <span className="text-gray-600">모드:</span>
                  <span className="font-medium">
                    {searchMode === 'category' && '카테고리'}
                    {searchMode === 'keyword' && '카테고리+키워드'}
                    {searchMode === 'keyword-only' && '키워드 전용'}
                  </span>
                </div>
                {selectedCategories.length > 0 && (
                  <div className="flex justify-between">
                    <span className="text-gray-600">카테고리:</span>
                    <span className="font-medium">{selectedCategories.length}개</span>
                  </div>
                )}
                {keywords.length > 0 && (
                  <div className="flex justify-between">
                    <span className="text-gray-600">키워드:</span>
                    <span className="font-medium">{keywords.length}개</span>
                  </div>
                )}
                <div className="flex justify-between">
                  <span className="text-gray-600">기간:</span>
                  <span className="font-medium">
                    {dateMode === 'recent' ? `최근 ${daysBack}일` : `선택된 범위`}
                  </span>
                </div>
              </div>

              {/* 실행 버튼 */}
              <div className="space-y-2">
                <button
                  type="button"
                  onClick={() => {
                    console.log('🖱️ Button clicked! Current isCollecting:', isCollecting);
                    console.log('🖱️ Button clicked! Current currentTask:', currentTask);

                    // 만약 isCollecting이 true인데 currentTask가 null이면 강제 리셋
                    if (isCollecting && !currentTask) {
                      console.log('⚠️ Invalid state detected! Forcing reset...');
                      setIsCollecting(false);
                      setIsProcessing(false);
                      return;
                    }

                    if (isCollecting) {
                      console.log('➡️ Calling handleStopCollection');
                      handleStopCollection();
                    } else {
                      console.log('➡️ Calling handleStartCollection');
                      handleStartCollection();
                    }
                  }}
                  disabled={!canSubmit() && !isCollecting}
                  className={`w-full flex items-center justify-center gap-2 py-3 px-4 rounded-lg font-medium transition-colors ${
                    isCollecting
                      ? 'bg-orange-600 text-white hover:bg-orange-700'
                      : canSubmit()
                      ? 'bg-primary-600 text-white hover:bg-primary-700'
                      : 'bg-gray-300 text-gray-500 cursor-not-allowed'
                  }`}
                >
                  {isCollecting ? (
                    <>
                      <Pause size={16} />
                      중단하기
                    </>
                  ) : (
                    <>
                      <Play size={16} />
                      논문 수집 시작
                    </>
                  )}
                </button>

                {/* 다운로드 버튼 */}
                {taskStatus?.status === 'completed' && taskStatus.result?.success && (
                  <button
                    type="button"
                    onClick={handleDownloadReport}
                    className="w-full flex items-center justify-center gap-2 py-2 px-4 rounded-lg font-medium bg-green-600 text-white hover:bg-green-700 transition-colors"
                  >
                    <Download size={16} />
                    보고서 다운로드
                  </button>
                )}
              </div>

              {!canSubmit() && (
                <div className="mt-2 text-xs text-red-600">
                  {searchMode === 'keyword-only' && keywords.length === 0 && '키워드를 입력해주세요.'}
                  {searchMode === 'category' && selectedCategories.length === 0 && '카테고리를 선택해주세요.'}
                  {dateMode === 'range' && (!startDate || !endDate) && '날짜 범위를 설정해주세요.'}
                </div>
              )}
            </div>

            {/* 고급 설정 */}
            <div className="card p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-base font-semibold text-gray-900">고급 설정</h3>
                <button
                  type="button"
                  onClick={() => setShowAdvanced(!showAdvanced)}
                  className={`p-1 rounded transition-colors ${
                    showAdvanced ? 'text-primary-600' : 'text-gray-400 hover:text-gray-600'
                  }`}
                >
                  <Settings size={16} />
                </button>
              </div>

              {showAdvanced ? (
                <div className="space-y-3">
                  <div>
                    <label className="block text-xs font-medium text-gray-700 mb-1">
                      번역 서비스
                    </label>
                    <select
                      value={translationProvider}
                      onChange={(e) => setTranslationProvider(e.target.value)}
                      className="w-full px-2 py-1 text-xs border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-primary-500"
                    >
                      <option value="openai">OpenAI</option>
                      <option value="claude">Claude</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-700 mb-1">
                      요약 서비스
                    </label>
                    <select
                      value={summarizationProvider}
                      onChange={(e) => setSummarizationProvider(e.target.value)}
                      className="w-full px-2 py-1 text-xs border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-primary-500"
                    >
                      <option value="openai">OpenAI</option>
                      <option value="claude">Claude</option>
                    </select>
                  </div>
                  <div>
                    <label className="flex items-center space-x-2 text-xs">
                      <input
                        type="checkbox"
                        checked={useRss}
                        onChange={(e) => setUseRss(e.target.checked)}
                        className="w-3 h-3 text-primary-600 border-gray-300 rounded focus:ring-primary-500"
                      />
                      <span className="font-medium text-gray-700">
                        RSS 피드 사용
                      </span>
                    </label>
                    <p className="mt-1 text-xs text-gray-500">
                      ArXiv API 대신 RSS 피드를 사용합니다. 최신 논문에 대해 더 정확한 날짜 기준으로 검색됩니다.
                    </p>
                    {useRss && (
                      <p className="mt-1 text-xs text-amber-600 bg-amber-50 p-2 rounded">
                        ⚠️ RSS 모드는 최신 발표 논문만 검색 가능합니다. 과거 날짜 검색은 ArXiv API를 사용해주세요.
                      </p>
                    )}
                  </div>
                </div>
              ) : (
                <div className="text-xs text-gray-500">
                  <p>번역: {translationProvider}</p>
                  <p>요약: {summarizationProvider}</p>
                  <p>검색: {useRss ? 'RSS 피드' : 'ArXiv API'}</p>
                  <p className="mt-2 text-gray-400">설정 아이콘을 클릭하여 변경</p>
                </div>
              )}
            </div>

            {/* 진행 상태 */}
            <div className="card p-4">
              <h3 className="text-base font-semibold text-gray-900 mb-3">
                {isCollecting ? '수집 진행 상황' : '상태'}
              </h3>

              {/* 에러 표시 */}
              {error && (
                <div className="mb-3 p-2 bg-red-50 border border-red-200 rounded-lg">
                  <div className="flex items-center gap-2 text-red-700">
                    <AlertCircle size={14} />
                    <span className="text-xs font-medium">오류 발생</span>
                  </div>
                  <p className="text-xs text-red-600 mt-1">{error}</p>
                </div>
              )}

              {isCollecting || taskStatus ? (
                <div className="space-y-3">
                  {/* 진행률 바 */}
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className={`h-2 rounded-full transition-all duration-300 ${
                        taskStatus?.status === 'error' ? 'bg-red-500' : 'bg-primary-600'
                      }`}
                      style={{
                        width: `${taskStatus?.progress?.progress_percentage || 0}%`
                      }}
                    ></div>
                  </div>

                  {/* 현재 단계 */}
                  <div className="flex items-center gap-2">
                    {taskStatus?.status === 'completed' ? (
                      <CheckCircle size={14} className="text-green-500" />
                    ) : taskStatus?.status === 'error' ? (
                      <AlertCircle size={14} className="text-red-500" />
                    ) : (
                      <div className="w-3.5 h-3.5 border-2 border-primary-600 border-t-transparent rounded-full animate-spin"></div>
                    )}
                    <span className="text-xs text-gray-600">
                      {taskStatus?.progress?.current_step || '작업을 시작하고 있습니다...'}
                    </span>
                  </div>

                  {/* 상세 정보 */}
                  {taskStatus?.progress && (
                    <div className="text-xs text-gray-500 space-y-1">
                      {taskStatus.progress.papers_found > 0 && (
                        <div className="flex justify-between">
                          <span>발견된 논문:</span>
                          <span className="font-medium">{taskStatus.progress.papers_found}개</span>
                        </div>
                      )}
                      {taskStatus.progress.total_papers > 0 && (
                        <div className="flex justify-between">
                          <span>진행률:</span>
                          <span className="font-medium">
                            {taskStatus.progress.papers_processed}/{taskStatus.progress.total_papers} 
                            ({taskStatus.progress.progress_percentage}%)
                          </span>
                        </div>
                      )}
                      {taskStatus.progress.current_step && taskStatus.progress.current_step.includes('논문') && (
                        <div className="mt-2 p-2 bg-blue-50 rounded border-l-2 border-blue-300">
                          <div className="text-blue-700 font-medium text-xs">처리 중:</div>
                          <div className="text-blue-600 text-xs mt-1 truncate" title={taskStatus.progress.current_step}>
                            {taskStatus.progress.current_step}
                          </div>
                        </div>
                      )}
                    </div>
                  )}

                  {/* 완료 메시지 */}
                  {taskStatus?.status === 'completed' && (
                    <div className="p-2 bg-green-50 border border-green-200 rounded-lg">
                      <p className="text-xs text-green-700 font-medium">
                        ✅ 수집이 완료되었습니다!
                      </p>
                      {taskStatus.result && (
                        <p className="text-xs text-green-600 mt-1">
                          {taskStatus.result.papers_collected}개의 논문이 수집되었습니다.
                        </p>
                      )}
                    </div>
                  )}

                  {/* 중단 메시지 */}
                  {taskStatus?.status === 'cancelled' && (
                    <div className="p-2 bg-orange-50 border border-orange-200 rounded-lg">
                      <p className="text-xs text-orange-700 font-medium">
                        ⏹️ 수집이 중단되었습니다
                      </p>
                      <p className="text-xs text-orange-600 mt-1">
                        사용자 요청에 의해 작업이 중단되었습니다.
                      </p>
                    </div>
                  )}

                  {/* 에러 메시지 */}
                  {taskStatus?.status === 'error' && (
                    <div className="p-2 bg-red-50 border border-red-200 rounded-lg">
                      <p className="text-xs text-red-700 font-medium">
                        ❌ 수집 중 오류가 발생했습니다
                      </p>
                      {taskStatus.progress?.error_message && (
                        <p className="text-xs text-red-600 mt-1">
                          {taskStatus.progress.error_message}
                        </p>
                      )}
                    </div>
                  )}
                </div>
              ) : (
                <div className="space-y-2">
                  <div className="flex items-center gap-2 text-xs">
                    <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                    <span className="text-gray-600">대기 중</span>
                  </div>
                  <div className="text-xs text-gray-500">
                    <p>• 설정을 확인하고 수집을 시작하세요</p>
                    <p>• 결과는 마크다운 파일로 저장됩니다</p>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* 수집된 논문 목록 */}
          <PaperList 
            taskStatus={taskStatus}
            isVisible={showPaperList}
            onToggle={() => setShowPaperList(!showPaperList)}
          />
        </div>
      </main>
    </div>
  );
}

export default App;