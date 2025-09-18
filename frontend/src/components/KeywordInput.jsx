import React, { useState, useRef, useEffect } from 'react';
import { X, Plus, Save, RotateCcw } from 'lucide-react';
import { keywordStorage } from '../utils/storage';

const KeywordInput = ({ keywords, setKeywords, placeholder = "키워드를 입력하세요..." }) => {
  const [inputValue, setInputValue] = useState('');
  const [savedKeywords, setSavedKeywords] = useState([]);
  const inputRef = useRef(null);

  // 컴포넌트 마운트 시 저장된 키워드 불러오기
  useEffect(() => {
    const stored = keywordStorage.load();
    setSavedKeywords(stored);
    // 현재 키워드가 비어있고 저장된 키워드가 있으면 자동으로 불러오기
    if (keywords.length === 0 && stored.length > 0) {
      setKeywords(stored);
    }
  }, []);

  // 키워드가 변경될 때마다 자동 저장
  useEffect(() => {
    if (keywords.length > 0) {
      keywordStorage.save(keywords);
      setSavedKeywords(keywords);
    }
  }, [keywords]);

  const addKeyword = (keyword) => {
    const trimmed = keyword.trim();
    if (trimmed && !keywords.includes(trimmed)) {
      setKeywords([...keywords, trimmed]);
    }
    setInputValue('');
  };

  const removeKeyword = (keywordToRemove) => {
    setKeywords(keywords.filter(keyword => keyword !== keywordToRemove));
  };

  const handleKeyDown = (e) => {
    switch (e.key) {
      case 'Enter':
      case 'Tab':
      case ',':
        e.preventDefault();
        addKeyword(inputValue);
        break;
      case 'Backspace':
        if (inputValue === '' && keywords.length > 0) {
          removeKeyword(keywords[keywords.length - 1]);
        }
        break;
    }
  };

  const handlePaste = (e) => {
    e.preventDefault();
    const pastedText = e.clipboardData.getData('text');
    const pastedKeywords = pastedText
      .split(/[,\n\t]/)
      .map(keyword => keyword.trim())
      .filter(keyword => keyword);

    const newKeywords = [...keywords];
    pastedKeywords.forEach(keyword => {
      if (!newKeywords.includes(keyword)) {
        newKeywords.push(keyword);
      }
    });
    setKeywords(newKeywords);
  };

  // 저장된 키워드 불러오기
  const loadSavedKeywords = () => {
    const stored = keywordStorage.load();
    setKeywords(stored);
  };

  // 키워드 초기화
  const clearKeywords = () => {
    setKeywords([]);
    keywordStorage.clear();
    setSavedKeywords([]);
  };

  // 현재 키워드 수동 저장
  const saveCurrentKeywords = () => {
    if (keywords.length > 0) {
      keywordStorage.save(keywords);
      setSavedKeywords(keywords);
    }
  };

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between">
        <label className="block text-sm font-medium text-gray-700">
          키워드
        </label>

        {/* 키워드 관리 버튼들 */}
        <div className="flex items-center gap-2">
          {savedKeywords.length > 0 && (
            <button
              type="button"
              onClick={loadSavedKeywords}
              className="flex items-center gap-1 px-2 py-1 text-xs text-blue-600 hover:text-blue-700 hover:bg-blue-50 rounded transition-colors"
              title="저장된 키워드 불러오기"
            >
              <RotateCcw size={12} />
              저장된 것 불러오기
            </button>
          )}

          {keywords.length > 0 && (
            <button
              type="button"
              onClick={saveCurrentKeywords}
              className="flex items-center gap-1 px-2 py-1 text-xs text-green-600 hover:text-green-700 hover:bg-green-50 rounded transition-colors"
              title="현재 키워드 저장하기"
            >
              <Save size={12} />
              저장
            </button>
          )}

          {keywords.length > 0 && (
            <button
              type="button"
              onClick={clearKeywords}
              className="flex items-center gap-1 px-2 py-1 text-xs text-red-600 hover:text-red-700 hover:bg-red-50 rounded transition-colors"
              title="모든 키워드 초기화"
            >
              <X size={12} />
              초기화
            </button>
          )}
        </div>
      </div>

      <div className="relative">
        <div className="min-h-[42px] w-full px-3 py-2 border border-gray-300 rounded-lg focus-within:ring-2 focus-within:ring-primary-500 focus-within:border-transparent bg-white">
          <div className="flex flex-wrap gap-2 items-center">
            {/* 키워드 태그들 */}
            {keywords.map((keyword, index) => (
              <span
                key={index}
                className="inline-flex items-center gap-1 px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-sm font-medium group hover:bg-primary-200 transition-colors"
              >
                <span>#{keyword}</span>
                <button
                  type="button"
                  onClick={() => removeKeyword(keyword)}
                  className="p-0.5 rounded-full hover:bg-primary-300 transition-colors"
                  aria-label={`${keyword} 키워드 제거`}
                >
                  <X size={12} />
                </button>
              </span>
            ))}

            {/* 입력 필드 */}
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              onPaste={handlePaste}
              placeholder={keywords.length === 0 ? placeholder : ""}
              className="flex-1 min-w-[120px] bg-transparent border-none outline-none text-sm"
            />

            {/* 추가 버튼 */}
            {inputValue.trim() && (
              <button
                type="button"
                onClick={() => addKeyword(inputValue)}
                className="p-1 text-primary-600 hover:text-primary-700 transition-colors"
                aria-label="키워드 추가"
              >
                <Plus size={16} />
              </button>
            )}
          </div>
        </div>
      </div>

      {/* 도움말 텍스트 */}
      <div className="text-xs text-gray-500 space-y-1">
        <p>• Enter, Tab, 쉼표(,)로 키워드를 추가할 수 있습니다</p>
        <p>• Backspace로 마지막 키워드를 삭제할 수 있습니다</p>
        <p>• 여러 키워드를 한번에 붙여넣기할 수 있습니다</p>
      </div>

      {/* 키워드 상태 표시 */}
      <div className="flex items-center justify-between text-sm">
        {keywords.length > 0 && (
          <div className="text-gray-600">
            총 {keywords.length}개의 키워드
          </div>
        )}

        {savedKeywords.length > 0 && (
          <div className="text-xs text-gray-500">
            {JSON.stringify(keywords) === JSON.stringify(savedKeywords) ? (
              <span className="text-green-600">✓ 저장됨</span>
            ) : (
              <span className="text-orange-600">● 변경됨 (저장 필요)</span>
            )}
          </div>
        )}
      </div>

      {/* 저장된 키워드 미리보기 */}
      {savedKeywords.length > 0 && JSON.stringify(keywords) !== JSON.stringify(savedKeywords) && (
        <div className="p-2 bg-gray-50 rounded-lg">
          <div className="text-xs text-gray-600 mb-1">저장된 키워드:</div>
          <div className="flex flex-wrap gap-1">
            {savedKeywords.map((keyword, index) => (
              <span
                key={index}
                className="inline-block px-2 py-1 bg-gray-200 text-gray-700 rounded text-xs"
              >
                #{keyword}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default KeywordInput;