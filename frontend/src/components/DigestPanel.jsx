import React, { useState, useEffect } from 'react';
import { generateDailyDigest, generateWeeklyDigest, getDigests } from '../services/api';

const DigestPanel = () => {
  const [digestDate, setDigestDate] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [generationResult, setGenerationResult] = useState(null);
  const [digestsList, setDigestsList] = useState([]);
  const [loadingDigests, setLoadingDigests] = useState(false);

  // 오늘 날짜를 YYYYMMDD 형식으로 가져오기
  const getTodayDate = () => {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}${month}${day}`;
  };

  // 컴포넌트 마운트 시 오늘 날짜로 초기화
  useEffect(() => {
    setDigestDate(getTodayDate());
    loadDigestsList();
  }, []);

  // 다이제스트 목록 로드
  const loadDigestsList = async () => {
    try {
      setLoadingDigests(true);
      const response = await getDigests();
      setDigestsList(response.digests || []);
    } catch (error) {
      console.error('Failed to load digests:', error);
    } finally {
      setLoadingDigests(false);
    }
  };

  // 일일 다이제스트 생성
  const handleGenerateDaily = async () => {
    try {
      setIsGenerating(true);
      setGenerationResult(null);

      const result = await generateDailyDigest(digestDate || null);
      setGenerationResult({
        type: 'daily',
        success: true,
        ...result
      });

      // 생성 후 목록 새로고침
      await loadDigestsList();
    } catch (error) {
      setGenerationResult({
        type: 'daily',
        success: false,
        error: error.message
      });
    } finally {
      setIsGenerating(false);
    }
  };

  // 주간 다이제스트 생성
  const handleGenerateWeekly = async () => {
    try {
      setIsGenerating(true);
      setGenerationResult(null);

      const result = await generateWeeklyDigest(digestDate || null);
      setGenerationResult({
        type: 'weekly',
        success: true,
        ...result
      });

      // 생성 후 목록 새로고침
      await loadDigestsList();
    } catch (error) {
      setGenerationResult({
        type: 'weekly',
        success: false,
        error: error.message
      });
    } finally {
      setIsGenerating(false);
    }
  };

  // 날짜 포맷팅 (YYYYMMDD -> YYYY-MM-DD)
  const formatDateForInput = (dateStr) => {
    if (!dateStr || dateStr.length !== 8) return '';
    return `${dateStr.slice(0, 4)}-${dateStr.slice(4, 6)}-${dateStr.slice(6, 8)}`;
  };

  // 날짜 포맷팅 (YYYY-MM-DD -> YYYYMMDD)
  const formatDateForAPI = (dateStr) => {
    if (!dateStr) return '';
    return dateStr.replace(/-/g, '');
  };

  // 다이제스트 파일명에서 날짜 추출
  const extractDateFromFilename = (filename) => {
    const match = filename.match(/(\d{8})/);
    return match ? match[1] : '';
  };

  // 다이제스트 타입 표시
  const getDigestTypeDisplay = (filename) => {
    if (filename.includes('daily')) return '일일';
    if (filename.includes('weekly')) return '주간';
    return '알 수 없음';
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-bold text-gray-800 mb-6">📊 다이제스트 생성</h2>

      {/* 날짜 선택 */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          생성할 날짜 선택
        </label>
        <input
          type="date"
          value={formatDateForInput(digestDate)}
          onChange={(e) => setDigestDate(formatDateForAPI(e.target.value))}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={isGenerating}
        />
        <p className="text-xs text-gray-500 mt-1">
          비워두면 오늘 날짜로 생성됩니다.
        </p>
      </div>

      {/* 생성 버튼들 */}
      <div className="flex gap-4 mb-6">
        <button
          onClick={handleGenerateDaily}
          disabled={isGenerating}
          className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
        >
          {isGenerating ? (
            <span className="flex items-center justify-center">
              <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              생성 중...
            </span>
          ) : (
            '📄 일일 다이제스트 생성'
          )}
        </button>

        <button
          onClick={handleGenerateWeekly}
          disabled={isGenerating}
          className="flex-1 bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
        >
          {isGenerating ? (
            <span className="flex items-center justify-center">
              <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              생성 중...
            </span>
          ) : (
            '📅 주간 다이제스트 생성'
          )}
        </button>
      </div>

      {/* 생성 결과 표시 */}
      {generationResult && (
        <div className={`p-4 rounded-md mb-6 ${
          generationResult.success
            ? 'bg-green-50 border border-green-200'
            : 'bg-red-50 border border-red-200'
        }`}>
          {generationResult.success ? (
            <div>
              <p className="text-green-800 font-medium">
                ✅ {generationResult.type === 'daily' ? '일일' : '주간'} 다이제스트가 성공적으로 생성되었습니다!
              </p>
              <p className="text-green-700 text-sm mt-1">
                📁 경로: {generationResult.digest_path}
              </p>
              {generationResult.date && (
                <p className="text-green-700 text-sm">
                  📅 날짜: {generationResult.date}
                </p>
              )}
            </div>
          ) : (
            <div>
              <p className="text-red-800 font-medium">
                ❌ {generationResult.type === 'daily' ? '일일' : '주간'} 다이제스트 생성에 실패했습니다.
              </p>
              <p className="text-red-700 text-sm mt-1">
                오류: {generationResult.error}
              </p>
            </div>
          )}
        </div>
      )}

      {/* 생성된 다이제스트 목록 */}
      <div>
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-lg font-semibold text-gray-800">📋 생성된 다이제스트 목록</h3>
          <button
            onClick={loadDigestsList}
            disabled={loadingDigests}
            className="px-3 py-1 text-sm bg-gray-100 text-gray-600 rounded-md hover:bg-gray-200 disabled:opacity-50"
          >
            {loadingDigests ? '로딩...' : '🔄 새로고침'}
          </button>
        </div>

        {digestsList.length === 0 ? (
          <p className="text-gray-500 text-center py-8">
            아직 생성된 다이제스트가 없습니다.
          </p>
        ) : (
          <div className="space-y-2">
            {digestsList.map((digest, index) => (
              <div
                key={index}
                className="flex justify-between items-center p-3 bg-gray-50 rounded-md hover:bg-gray-100 transition-colors"
              >
                <div>
                  <p className="font-medium text-gray-800">
                    {getDigestTypeDisplay(digest.filename)} 다이제스트
                  </p>
                  <p className="text-sm text-gray-600">
                    📅 {extractDateFromFilename(digest.filename) || '날짜 불명'}
                  </p>
                  <p className="text-xs text-gray-500">
                    📁 {digest.filename}
                  </p>
                </div>
                <div className="text-right">
                  <p className="text-sm text-gray-600">
                    {new Date(digest.modified_at).toLocaleString('ko-KR')}
                  </p>
                  <p className="text-xs text-gray-500">
                    {(digest.size / 1024).toFixed(1)} KB
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* n8n/자동화 도구용 URL 안내 */}
      <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-md">
        <h4 className="font-medium text-blue-800 mb-2">🔗 자동화 도구 연동 (n8n, Zapier 등)</h4>
        <div className="text-sm text-blue-700 space-y-1">
          <p><strong>일일 다이제스트:</strong> <code>POST http://localhost:8080/api/digest/daily</code></p>
          <p><strong>주간 다이제스트:</strong> <code>POST http://localhost:8080/api/digest/weekly</code></p>
          <p><strong>날짜 지정:</strong> <code>?date=20251201</code> 파라미터 추가</p>
          <p><strong>다이제스트 목록:</strong> <code>GET http://localhost:8080/api/digests</code></p>
        </div>
      </div>
    </div>
  );
};

export default DigestPanel;