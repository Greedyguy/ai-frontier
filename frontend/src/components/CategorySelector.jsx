import React, { useState } from 'react';
import { Search, Check, X } from 'lucide-react';

const CategorySelector = ({ selectedCategories, setSelectedCategories }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const categories = {
    'cs.AI': 'Artificial Intelligence',
    'cs.LG': 'Machine Learning',
    'cs.CL': 'Computation and Language',
    'cs.CV': 'Computer Vision and Pattern Recognition',
    'cs.CR': 'Cryptography and Security',
    'cs.DC': 'Distributed, Parallel, and Cluster Computing',
    'cs.DM': 'Discrete Mathematics',
    'cs.DS': 'Data Structures and Algorithms',
    'cs.ET': 'Emerging Technologies',
    'cs.FL': 'Formal Languages and Automata Theory',
    'cs.GL': 'General Literature',
    'cs.GR': 'Graphics',
    'cs.GT': 'Computer Science and Game Theory',
    'cs.HC': 'Human-Computer Interaction',
    'cs.IR': 'Information Retrieval',
    'cs.IT': 'Information Theory',
    'cs.LO': 'Logic in Computer Science',
    'cs.MA': 'Multiagent Systems',
    'cs.MM': 'Multimedia',
    'cs.MS': 'Mathematical Software',
    'cs.NA': 'Numerical Analysis',
    'cs.NE': 'Neural and Evolutionary Computing',
    'cs.NI': 'Networking and Internet Architecture',
    'cs.OH': 'Other Computer Science',
    'cs.OS': 'Operating Systems',
    'cs.PF': 'Performance',
    'cs.PL': 'Programming Languages',
    'cs.RO': 'Robotics',
    'cs.SC': 'Symbolic Computation',
    'cs.SD': 'Sound',
    'cs.SE': 'Software Engineering',
    'cs.SI': 'Social and Information Networks',
    'cs.SY': 'Systems and Control'
  };

  const toggleCategory = (categoryId) => {
    if (selectedCategories.includes(categoryId)) {
      setSelectedCategories(selectedCategories.filter(id => id !== categoryId));
    } else {
      setSelectedCategories([...selectedCategories, categoryId]);
    }
  };

  const clearAll = () => {
    setSelectedCategories([]);
  };

  const selectPopular = () => {
    const popularCategories = ['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV'];
    setSelectedCategories(popularCategories);
  };

  const selectAll = () => {
    setSelectedCategories(Object.keys(categories));
  };

  // 검색 필터링
  const filteredCategories = Object.entries(categories).filter(([id, name]) =>
    searchTerm === '' ||
    id.toLowerCase().includes(searchTerm.toLowerCase()) ||
    name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <label className="block text-sm font-medium text-gray-700">
          CS 카테고리
        </label>
        <div className="text-sm text-gray-500">
          {selectedCategories.length}개 선택됨
        </div>
      </div>

      {/* 빠른 선택 버튼들 */}
      <div className="flex flex-wrap gap-2">
        <button
          type="button"
          onClick={selectPopular}
          className="px-3 py-1 text-xs bg-primary-100 text-primary-700 rounded-full hover:bg-primary-200 transition-colors"
        >
          인기 카테고리 (AI/ML/NLP/CV)
        </button>
        <button
          type="button"
          onClick={selectAll}
          className="px-3 py-1 text-xs bg-green-100 text-green-700 rounded-full hover:bg-green-200 transition-colors"
        >
          CS 전체 선택 (33개)
        </button>
        <button
          type="button"
          onClick={clearAll}
          className="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition-colors"
        >
          모두 해제
        </button>
      </div>

      {/* 검색 */}
      <div className="relative">
        <Search size={16} className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
        <input
          type="text"
          placeholder="카테고리 검색..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full pl-9 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent text-sm"
        />
      </div>

      {/* 카테고리 그리드 */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 max-h-64 overflow-y-auto border border-gray-200 rounded-lg p-2">
        {filteredCategories.map(([categoryId, categoryName]) => (
          <label
            key={categoryId}
            className="flex items-center gap-2 p-2 rounded-lg hover:bg-gray-50 cursor-pointer text-sm"
          >
            <div className="relative flex-shrink-0">
              <input
                type="checkbox"
                checked={selectedCategories.includes(categoryId)}
                onChange={() => toggleCategory(categoryId)}
                className="sr-only"
              />
              <div className={`w-4 h-4 border-2 rounded flex items-center justify-center transition-colors ${
                selectedCategories.includes(categoryId)
                  ? 'bg-primary-600 border-primary-600'
                  : 'border-gray-300'
              }`}>
                {selectedCategories.includes(categoryId) && (
                  <Check size={10} className="text-white" />
                )}
              </div>
            </div>
            <div className="flex-1 min-w-0">
              <div className="font-medium text-gray-900 truncate">
                {categoryId}
              </div>
              <div className="text-xs text-gray-600 truncate">
                {categoryName}
              </div>
            </div>
          </label>
        ))}
      </div>

      {/* 선택된 카테고리 요약 */}
      {selectedCategories.length > 0 && (
        <div className="p-3 bg-primary-50 rounded-lg">
          <div className="text-sm font-medium text-primary-900 mb-2">
            선택된 카테고리 ({selectedCategories.length}개):
          </div>
          <div className="flex flex-wrap gap-1">
            {selectedCategories.slice(0, 6).map((categoryId) => (
              <span
                key={categoryId}
                className="inline-flex items-center gap-1 px-2 py-1 bg-primary-100 text-primary-800 rounded text-xs"
              >
                {categoryId}
                <button
                  type="button"
                  onClick={() => toggleCategory(categoryId)}
                  className="hover:bg-primary-200 rounded-full p-0.5"
                >
                  <X size={10} />
                </button>
              </span>
            ))}
            {selectedCategories.length > 6 && (
              <span className="text-xs text-primary-700">
                +{selectedCategories.length - 6}개 더
              </span>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default CategorySelector;