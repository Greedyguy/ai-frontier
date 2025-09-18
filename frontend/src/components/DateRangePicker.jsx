import React, { useState, useEffect } from 'react';
import { Calendar, Clock, ChevronDown } from 'lucide-react';

const DateRangePicker = ({
  dateMode,
  setDateMode,
  daysBack,
  setDaysBack,
  startDate,
  setStartDate,
  endDate,
  setEndDate
}) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  // 오늘 날짜를 YYYY-MM-DD 형식으로 가져오기
  const today = new Date().toISOString().split('T')[0];

  // 기본값 설정
  useEffect(() => {
    if (!startDate || !endDate) {
      const todayDate = new Date();
      const weekAgo = new Date(todayDate);
      weekAgo.setDate(todayDate.getDate() - 7);

      if (!startDate) setStartDate(weekAgo.toISOString().split('T')[0]);
      if (!endDate) setEndDate(today);
    }
  }, []);

  // 최근 N일 옵션들
  const daysBackOptions = [
    { value: 1, label: '최근 1일' },
    { value: 3, label: '최근 3일' },
    { value: 7, label: '최근 7일' },
    { value: 14, label: '최근 2주' },
    { value: 30, label: '최근 30일' },
    { value: 90, label: '최근 3개월' }
  ];

  const handleDateModeChange = (mode) => {
    setDateMode(mode);
    setIsDropdownOpen(false);
  };

  const formatDateForDisplay = (dateStr) => {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('ko-KR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  const calculateDateRange = () => {
    if (dateMode === 'recent') {
      const endDate = new Date();
      const startDate = new Date();
      startDate.setDate(endDate.getDate() - daysBack);
      return `${formatDateForDisplay(startDate.toISOString().split('T')[0])} ~ ${formatDateForDisplay(today)}`;
    } else {
      return `${formatDateForDisplay(startDate)} ~ ${formatDateForDisplay(endDate)}`;
    }
  };

  return (
    <div className="space-y-4">
      <label className="block text-sm font-medium text-gray-700">
        수집 기간
      </label>

      {/* 날짜 모드 선택 */}
      <div className="relative">
        <button
          type="button"
          onClick={() => setIsDropdownOpen(!isDropdownOpen)}
          className="w-full flex items-center justify-between px-3 py-2 border border-gray-300 rounded-lg hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent bg-white"
        >
          <div className="flex items-center gap-2">
            <Clock size={16} className="text-gray-500" />
            <span className="text-sm">
              {dateMode === 'recent' ? '최근 일수 기준' : '특정 날짜 범위'}
            </span>
          </div>
          <ChevronDown
            size={16}
            className={`text-gray-400 transition-transform ${isDropdownOpen ? 'rotate-180' : ''}`}
          />
        </button>

        {isDropdownOpen && (
          <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-200 rounded-lg shadow-lg z-10">
            <button
              type="button"
              onClick={() => handleDateModeChange('recent')}
              className={`w-full text-left px-3 py-2 hover:bg-gray-50 ${
                dateMode === 'recent' ? 'bg-primary-50 text-primary-700' : ''
              }`}
            >
              <div className="flex items-center gap-2">
                <Clock size={16} />
                <span>최근 일수 기준</span>
              </div>
            </button>
            <button
              type="button"
              onClick={() => handleDateModeChange('range')}
              className={`w-full text-left px-3 py-2 hover:bg-gray-50 rounded-b-lg ${
                dateMode === 'range' ? 'bg-primary-50 text-primary-700' : ''
              }`}
            >
              <div className="flex items-center gap-2">
                <Calendar size={16} />
                <span>특정 날짜 범위</span>
              </div>
            </button>
          </div>
        )}
      </div>

      {/* 최근 N일 선택 */}
      {dateMode === 'recent' && (
        <div className="space-y-3">
          <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
            {daysBackOptions.map((option) => (
              <button
                key={option.value}
                type="button"
                onClick={() => setDaysBack(option.value)}
                className={`px-3 py-2 text-sm rounded-lg border transition-colors ${
                  daysBack === option.value
                    ? 'bg-primary-100 border-primary-300 text-primary-700'
                    : 'bg-white border-gray-300 text-gray-700 hover:bg-gray-50'
                }`}
              >
                {option.label}
              </button>
            ))}
          </div>

          <div className="flex items-center gap-2">
            <label htmlFor="custom-days" className="text-sm text-gray-600">
              또는 직접 입력:
            </label>
            <input
              id="custom-days"
              type="number"
              min="1"
              max="365"
              value={daysBack}
              onChange={(e) => setDaysBack(parseInt(e.target.value) || 1)}
              className="w-20 px-2 py-1 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-primary-500"
            />
            <span className="text-sm text-gray-600">일</span>
          </div>
        </div>
      )}

      {/* 특정 날짜 범위 선택 */}
      {dateMode === 'range' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label htmlFor="start-date" className="block text-sm font-medium text-gray-600 mb-1">
              시작 날짜
            </label>
            <input
              id="start-date"
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              max={endDate || today}
              className="input-field"
            />
          </div>
          <div>
            <label htmlFor="end-date" className="block text-sm font-medium text-gray-600 mb-1">
              종료 날짜
            </label>
            <input
              id="end-date"
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              min={startDate}
              max={today}
              className="input-field"
            />
          </div>
        </div>
      )}

      {/* 선택된 날짜 범위 표시 */}
      <div className="p-3 bg-gray-50 rounded-lg">
        <div className="text-sm text-gray-600 mb-1">선택된 기간:</div>
        <div className="text-sm font-medium text-gray-900">
          {calculateDateRange()}
        </div>
      </div>

      {/* 도움말 */}
      <div className="text-xs text-gray-500">
        <p>• 논문 발행일 기준으로 수집됩니다</p>
        <p>• 최대 1년까지 설정 가능합니다</p>
      </div>
    </div>
  );
};

export default DateRangePicker;