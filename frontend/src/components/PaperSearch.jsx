import React, { useState, useEffect } from 'react';
import { Search, Filter, ChevronDown, ChevronUp, ExternalLink, Calendar, Tag, Star } from 'lucide-react';

const PaperSearch = () => {
  // Search state
  const [query, setQuery] = useState('');
  const [searchResults, setSearchResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Filter state
  const [showFilters, setShowFilters] = useState(false);
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [minSimilarity, setMinSimilarity] = useState(0.5);
  const [pageSize, setPageSize] = useState(10);

  // Search mode and hybrid weights
  const [searchMode, setSearchMode] = useState('vector'); // 'vector', 'keyword', 'hybrid'
  const [keywordWeight, setKeywordWeight] = useState(0.3);
  const [vectorWeight, setVectorWeight] = useState(0.7);

  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);

  // Database stats
  const [dbStats, setDbStats] = useState(null);

  // Available categories (will be populated from database stats)
  const [availableCategories, setAvailableCategories] = useState([]);

  useEffect(() => {
    fetchDatabaseStats();
  }, []);

  const fetchDatabaseStats = async () => {
    try {
      const response = await fetch('http://localhost:8080/api/search/stats');
      if (response.ok) {
        const stats = await response.json();
        setDbStats(stats);
        // Extract categories from stats
        const categories = Object.keys(stats.categories || {}).sort();
        setAvailableCategories(categories);
      }
    } catch (error) {
      console.error('Failed to fetch database stats:', error);
    }
  };

  const handleSearch = async (page = 1) => {
    if (!query.trim()) {
      setError('검색어를 입력해주세요.');
      return;
    }

    setLoading(true);
    setError('');
    setCurrentPage(page);

    try {
      let searchRequest;
      let apiEndpoint;

      // Select API endpoint and request format based on search mode
      if (searchMode === 'hybrid') {
        apiEndpoint = 'http://localhost:8080/api/search/hybrid';
        searchRequest = {
          query: query.trim(),
          keyword_weight: keywordWeight,
          vector_weight: vectorWeight,
          top_k: 100,
          min_similarity: minSimilarity,
          categories: selectedCategories.length > 0 ? selectedCategories : null,
          start_date: startDate || null,
          end_date: endDate || null,
          page: page,
          page_size: pageSize
        };
      } else {
        // Use existing vector search endpoint for both vector and keyword modes
        apiEndpoint = 'http://localhost:8080/api/search/papers';
        searchRequest = {
          query: query.trim(),
          top_k: 100,
          min_similarity: minSimilarity,
          categories: selectedCategories.length > 0 ? selectedCategories : null,
          start_date: startDate || null,
          end_date: endDate || null,
          page: page,
          page_size: pageSize
        };
      }

      const response = await fetch(apiEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(searchRequest),
      });

      if (response.ok) {
        const results = await response.json();
        setSearchResults(results);
      } else {
        try {
          const errorData = await response.json();
          setError(errorData.detail || '검색 중 오류가 발생했습니다.');
        } catch (jsonError) {
          setError(`서버 응답 오류 (${response.status}): 서버에서 유효하지 않은 응답을 받았습니다.`);
        }
      }
    } catch (error) {
      console.error('Search error:', error);
      if (error.name === 'SyntaxError' && error.message.includes('JSON')) {
        setError('서버 응답을 처리하는 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.');
      } else {
        setError('검색 중 오류가 발생했습니다: ' + error.message);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryToggle = (category) => {
    setSelectedCategories(prev =>
      prev.includes(category)
        ? prev.filter(c => c !== category)
        : [...prev, category]
    );
  };

  const clearFilters = () => {
    setSelectedCategories([]);
    setStartDate('');
    setEndDate('');
    setMinSimilarity(0.5);
    setSearchMode('vector');
    setKeywordWeight(0.3);
    setVectorWeight(0.7);
  };

  const handleWeightChange = (newKeywordWeight) => {
    const newVectorWeight = 1.0 - newKeywordWeight;
    setKeywordWeight(newKeywordWeight);
    setVectorWeight(newVectorWeight);
  };

  const handlePageChange = (page) => {
    handleSearch(page);
  };

  const getSimilarityColor = (score) => {
    if (score >= 0.8) return 'text-green-600 bg-green-50';
    if (score >= 0.6) return 'text-yellow-600 bg-yellow-50';
    return 'text-red-600 bg-red-50';
  };

  const getScoreLabel = (searchMode, score) => {
    if (searchMode === 'hybrid') {
      return `하이브리드 점수: ${score.toFixed(3)}`;
    }
    return `유사도: ${score.toFixed(3)}`;
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'Unknown';
    try {
      return new Date(dateString).toLocaleDateString();
    } catch {
      return dateString;
    }
  };

  return (
    <div className="space-y-6">
      {/* Database Stats */}
      {dbStats && (
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
          <h3 className="font-medium text-blue-800 mb-2">📊 검색 가능한 논문 정보</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div>
              <span className="font-medium">총 논문 수:</span> {dbStats.total_papers.toLocaleString()}개
            </div>
            <div>
              <span className="font-medium">카테고리:</span> {Object.keys(dbStats.categories).length}개
            </div>
            <div>
              <span className="font-medium">기간:</span> {dbStats.date_range.earliest} ~ {dbStats.date_range.latest}
            </div>
            <div>
              <span className="font-medium">임베딩 차원:</span> {dbStats.embedding_dimension}차원
            </div>
          </div>
        </div>
      )}

      {/* Search Input */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">🔍 논문 검색</h2>

        <div className="space-y-4">
          <div className="flex gap-3">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="검색할 키워드나 문장을 입력하세요 (예: 'transformer attention mechanism')"
              className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
            />
            <button
              onClick={() => handleSearch()}
              disabled={loading}
              className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-lg disabled:opacity-50 flex items-center gap-2"
            >
              <Search size={20} />
              {loading ? '검색 중...' : '검색'}
            </button>
          </div>

          {/* Filters Toggle */}
          <button
            onClick={() => setShowFilters(!showFilters)}
            className="flex items-center gap-2 text-gray-600 hover:text-gray-800"
          >
            <Filter size={16} />
            고급 필터
            {showFilters ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          </button>

          {/* Filters Panel */}
          {showFilters && (
            <div className="border border-gray-200 rounded-lg p-4 space-y-4">
              <div className="flex justify-between items-center">
                <h3 className="font-medium">검색 조건</h3>
                <button
                  onClick={clearFilters}
                  className="text-sm text-blue-500 hover:text-blue-700"
                >
                  필터 초기화
                </button>
              </div>

              {/* Search Mode Selection */}
              <div>
                <label className="block text-sm font-medium mb-2">검색 모드</label>
                <div className="flex gap-4">
                  <label className="flex items-center space-x-2">
                    <input
                      type="radio"
                      value="vector"
                      checked={searchMode === 'vector'}
                      onChange={(e) => setSearchMode(e.target.value)}
                      className="border-gray-300"
                    />
                    <span>벡터 검색 (의미 기반)</span>
                  </label>
                  <label className="flex items-center space-x-2">
                    <input
                      type="radio"
                      value="hybrid"
                      checked={searchMode === 'hybrid'}
                      onChange={(e) => setSearchMode(e.target.value)}
                      className="border-gray-300"
                    />
                    <span>하이브리드 검색 (키워드 + 벡터)</span>
                  </label>
                </div>
              </div>

              {/* Hybrid Search Weight Control */}
              {searchMode === 'hybrid' && (
                <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
                  <label className="block text-sm font-medium mb-3">검색 가중치 조정</label>

                  <div className="space-y-3">
                    <div className="flex items-center justify-between text-sm">
                      <span>키워드 검색 (BM25)</span>
                      <span className="font-medium">{(keywordWeight * 100).toFixed(0)}%</span>
                    </div>

                    <input
                      type="range"
                      min="0"
                      max="1"
                      step="0.1"
                      value={keywordWeight}
                      onChange={(e) => handleWeightChange(parseFloat(e.target.value))}
                      className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                    />

                    <div className="flex items-center justify-between text-sm">
                      <span>벡터 검색 (의미 기반)</span>
                      <span className="font-medium">{(vectorWeight * 100).toFixed(0)}%</span>
                    </div>

                    <div className="text-xs text-gray-600 mt-2">
                      💡 키워드 검색은 정확한 용어 매칭에, 벡터 검색은 의미적 유사성에 강합니다.
                    </div>
                  </div>
                </div>
              )}

              {/* Categories */}
              <div>
                <label className="block text-sm font-medium mb-2">카테고리</label>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-2 max-h-32 overflow-y-auto">
                  {availableCategories.map((category) => (
                    <label key={category} className="flex items-center space-x-2 text-sm">
                      <input
                        type="checkbox"
                        checked={selectedCategories.includes(category)}
                        onChange={() => handleCategoryToggle(category)}
                        className="rounded border-gray-300"
                      />
                      <span title={category}>{category}</span>
                      {dbStats?.categories[category] && (
                        <span className="text-gray-500">({dbStats.categories[category]})</span>
                      )}
                    </label>
                  ))}
                </div>
              </div>

              {/* Date Range */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-1">시작 날짜</label>
                  <input
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">종료 날짜</label>
                  <input
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              </div>

              {/* Similarity Threshold */}
              <div>
                <label className="block text-sm font-medium mb-1">
                  최소 유사도: {minSimilarity.toFixed(2)}
                </label>
                <input
                  type="range"
                  min="0"
                  max="1"
                  step="0.05"
                  value={minSimilarity}
                  onChange={(e) => setMinSimilarity(parseFloat(e.target.value))}
                  className="w-full"
                />
                <div className="flex justify-between text-xs text-gray-500 mt-1">
                  <span>0.0 (낮음)</span>
                  <span>1.0 (높음)</span>
                </div>
              </div>

              {/* Page Size */}
              <div>
                <label className="block text-sm font-medium mb-1">페이지당 결과 수</label>
                <select
                  value={pageSize}
                  onChange={(e) => setPageSize(parseInt(e.target.value))}
                  className="px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value={10}>10개</option>
                  <option value={20}>20개</option>
                  <option value={50}>50개</option>
                  <option value={100}>100개</option>
                </select>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Error Message */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
          {error}
        </div>
      )}

      {/* Search Results */}
      {searchResults && (
        <div className="bg-white rounded-lg shadow">
          {/* Results Header */}
          <div className="p-6 border-b border-gray-200">
            <div className="flex justify-between items-center">
              <div>
                <h3 className="text-lg font-semibold">검색 결과</h3>
                <div className="space-y-1">
                  <p className="text-gray-600">
                    "{searchResults.query}"에 대한 {searchResults.total_results}개 결과
                    (페이지 {searchResults.page}/{searchResults.total_pages})
                  </p>
                  {searchResults.search_type === 'hybrid' && searchResults.weights && (
                    <div className="space-y-1">
                      <p className="text-sm text-blue-600">
                        🔄 하이브리드 검색: 키워드 {(searchResults.weights.keyword_weight * 100).toFixed(0)}% + 벡터 {(searchResults.weights.vector_weight * 100).toFixed(0)}%
                      </p>
                      {searchResults.search_stats?.extracted_keywords && searchResults.search_stats.extracted_keywords.length > 0 && (
                        <p className="text-xs text-gray-600">
                          🔍 추출된 키워드: {searchResults.search_stats.extracted_keywords.join(', ')}
                        </p>
                      )}
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* Applied Filters */}
            {(searchResults.applied_filters.categories ||
              searchResults.applied_filters.start_date ||
              searchResults.applied_filters.end_date) && (
              <div className="mt-3 flex flex-wrap gap-2">
                {searchResults.applied_filters.categories?.map(cat => (
                  <span key={cat} className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm">
                    📂 {cat}
                  </span>
                ))}
                {searchResults.applied_filters.start_date && (
                  <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                    📅 {searchResults.applied_filters.start_date} 이후
                  </span>
                )}
                {searchResults.applied_filters.end_date && (
                  <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                    📅 {searchResults.applied_filters.end_date} 이전
                  </span>
                )}
              </div>
            )}
          </div>

          {/* Results List */}
          <div className="divide-y divide-gray-200">
            {searchResults.results.length === 0 ? (
              <div className="p-6 text-center text-gray-500">
                검색 조건에 맞는 논문을 찾을 수 없습니다.
              </div>
            ) : (
              searchResults.results.map((paper, index) => (
                <div key={paper.arxiv_id} className="p-6 hover:bg-gray-50">
                  <div className="space-y-3">
                    {/* Title and Similarity Score */}
                    <div className="flex justify-between items-start">
                      <h4 className="text-lg font-medium text-gray-900 flex-1 mr-4">
                        {paper.title}
                      </h4>
                      <div className={`px-3 py-1 rounded-full text-sm font-medium ${getSimilarityColor(paper.similarity_score || paper.hybrid_score)}`}>
                        <Star size={14} className="inline mr-1" />
                        {searchResults.search_type === 'hybrid' ?
                          (paper.hybrid_score * 100).toFixed(1) + '%' :
                          (paper.similarity_score * 100).toFixed(1) + '%'
                        }
                      </div>
                    </div>

                    {/* Metadata */}
                    <div className="flex flex-wrap gap-4 text-sm text-gray-600">
                      <span className="flex items-center gap-1">
                        <Tag size={14} />
                        {paper.category}
                      </span>
                      <span className="flex items-center gap-1">
                        <Calendar size={14} />
                        {formatDate(paper.published_date)}
                      </span>
                      <span>
                        📄 {paper.arxiv_id}
                      </span>
                    </div>

                    {/* Abstract */}
                    <p className="text-gray-700 text-sm leading-relaxed">
                      {paper.abstract.length > 300
                        ? paper.abstract.substring(0, 300) + '...'
                        : paper.abstract
                      }
                    </p>

                    {/* Summary */}
                    {paper.summary && (
                      <div className="bg-blue-50 p-3 rounded border-l-4 border-blue-200">
                        <p className="text-sm text-blue-800">
                          <strong>AI 요약:</strong> {paper.summary}
                        </p>
                      </div>
                    )}

                    {/* Key Points */}
                    {paper.key_points && paper.key_points.length > 0 && (
                      <div className="bg-green-50 p-3 rounded">
                        <p className="text-sm font-medium text-green-800 mb-2">주요 포인트:</p>
                        <ul className="text-sm text-green-700 space-y-1">
                          {paper.key_points.slice(0, 3).map((point, idx) => (
                            <li key={idx} className="flex items-start">
                              <span className="mr-2">•</span>
                              <span>{point}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Links */}
                    <div className="flex gap-3 pt-2">
                      <a
                        href={`https://arxiv.org/abs/${paper.arxiv_id}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 hover:text-blue-800 text-sm flex items-center gap-1"
                      >
                        <ExternalLink size={14} />
                        ArXiv 보기
                      </a>
                      <a
                        href={paper.pdf_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-red-600 hover:text-red-800 text-sm flex items-center gap-1"
                      >
                        <ExternalLink size={14} />
                        PDF 다운로드
                      </a>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>

          {/* Pagination */}
          {searchResults && searchResults.total_pages > 1 && (
            <div className="p-6 border-t border-gray-200 flex justify-center">
              <div className="flex gap-2">
                <button
                  onClick={() => handlePageChange(Math.max(1, currentPage - 1))}
                  disabled={currentPage === 1 || loading}
                  className="px-3 py-2 border border-gray-300 rounded disabled:opacity-50 hover:bg-gray-50"
                >
                  이전
                </button>

                {/* Page Numbers */}
                {Array.from({ length: Math.min(5, searchResults.total_pages) }, (_, i) => {
                  const pageNum = Math.max(1, currentPage - 2) + i;
                  if (pageNum > searchResults.total_pages) return null;

                  return (
                    <button
                      key={pageNum}
                      onClick={() => handlePageChange(pageNum)}
                      disabled={loading}
                      className={`px-3 py-2 border rounded ${
                        pageNum === currentPage
                          ? 'bg-blue-500 text-white border-blue-500'
                          : 'border-gray-300 hover:bg-gray-50'
                      }`}
                    >
                      {pageNum}
                    </button>
                  );
                })}

                <button
                  onClick={() => handlePageChange(Math.min(searchResults.total_pages, currentPage + 1))}
                  disabled={currentPage === searchResults.total_pages || loading}
                  className="px-3 py-2 border border-gray-300 rounded disabled:opacity-50 hover:bg-gray-50"
                >
                  다음
                </button>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default PaperSearch;