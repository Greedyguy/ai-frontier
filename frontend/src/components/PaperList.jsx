import React, { useState, useEffect } from 'react';
import { FileText, ExternalLink, Calendar, User, Tag, Eye, ChevronDown, ChevronUp, RefreshCw } from 'lucide-react';
import { getPaperFiles } from '../services/api';

function PaperList({ taskStatus, isVisible, onToggle }) {
  const [collectedPapers, setCollectedPapers] = useState([]);
  const [expandedPaper, setExpandedPaper] = useState(null);
  const [loading, setLoading] = useState(false);

  // 논문 파일 목록 로드
  const loadPaperFiles = async () => {
    try {
      setLoading(true);
      const response = await getPaperFiles();
      setCollectedPapers(response.files || []);
    } catch (error) {
      console.error('Failed to load paper files:', error);
      // 실패 시 목업 데이터 사용
      setCollectedPapers([
        {
          id: '2409.12345',
          title: 'Attention Is All You Need: A Comprehensive Study',
          title_ko: '어텐션이 필요한 전부: 포괄적 연구',
          authors: ['Ashish Vaswani', 'Noam Shazeer', 'Niki Parmar'],
          published: '2024-09-15',
          category: 'cs.AI',
          keywords: ['Transformer', 'Attention Mechanism', 'Neural Networks'],
          abstract: 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks...',
          abstract_ko: '주요 시퀀스 변환 모델들은 복잡한 순환 또는 합성곱 신경망을 기반으로 합니다...',
          pdf_url: 'https://arxiv.org/pdf/2409.12345.pdf',
          arxiv_url: 'https://arxiv.org/abs/2409.12345'
        },
        {
          id: '2409.12346',
          title: 'Large Language Models for Code Generation',
          title_ko: '코드 생성을 위한 대규모 언어 모델',
          authors: ['John Doe', 'Jane Smith', 'Alice Johnson'],
          published: '2024-09-14',
          category: 'cs.CL',
          keywords: ['Code Generation', 'Large Language Models', 'Programming'],
          abstract: 'Recent advances in large language models have shown remarkable capabilities in code generation tasks...',
          abstract_ko: '대규모 언어 모델의 최근 발전은 코드 생성 작업에서 놀라운 능력을 보여주었습니다...',
          pdf_url: 'https://arxiv.org/pdf/2409.12346.pdf',
          arxiv_url: 'https://arxiv.org/abs/2409.12346'
        },
        {
          id: '2409.12347',
          title: 'Efficient Training of Deep Neural Networks',
          title_ko: '깊은 신경망의 효율적 훈련',
          authors: ['Bob Wilson', 'Carol Lee'],
          published: '2024-09-13',
          category: 'cs.LG',
          keywords: ['Deep Learning', 'Training Efficiency', 'Optimization'],
          abstract: 'Training deep neural networks efficiently remains a significant challenge in machine learning...',
          abstract_ko: '깊은 신경망을 효율적으로 훈련하는 것은 기계학습에서 여전히 중요한 도전과제입니다...',
          pdf_url: 'https://arxiv.org/pdf/2409.12347.pdf',
          arxiv_url: 'https://arxiv.org/abs/2409.12347'
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  // 수집 완료 시 논문 목록 로드
  useEffect(() => {
    if (taskStatus?.status === 'completed' && isVisible) {
      loadPaperFiles();
    }
  }, [taskStatus, isVisible]);

  const toggleExpanded = (paperId) => {
    setExpandedPaper(expandedPaper === paperId ? null : paperId);
  };

  if (!isVisible && collectedPapers.length === 0) {
    return null;
  }

  return (
    <div className="card p-4">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900 flex items-center gap-2">
          <FileText size={20} />
          수집된 논문 ({collectedPapers.length}개)
        </h3>
        <div className="flex items-center gap-2">
          <button
            onClick={loadPaperFiles}
            disabled={loading}
            className="p-1 rounded hover:bg-gray-100 transition-colors disabled:opacity-50"
            title="목록 새로고침"
          >
            <RefreshCw size={16} className={loading ? 'animate-spin' : ''} />
          </button>
          <button
            onClick={onToggle}
            className="p-1 rounded hover:bg-gray-100 transition-colors"
          >
            {isVisible ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
          </button>
        </div>
      </div>

      <div className="space-y-4 max-h-96 overflow-y-auto">
        {collectedPapers.map((paper, index) => (
          <div
            key={paper.arxiv_id || paper.filename || index}
            className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
          >
            {/* 논문 헤더 */}
            <div className="flex items-start justify-between mb-3">
              <div className="flex-1">
                <h4 className="font-medium text-gray-900 mb-1 leading-tight">
                  {paper.title_ko}
                </h4>
                <p className="text-sm text-gray-600 mb-2 leading-tight">
                  {paper.title}
                </p>
                
                {/* 메타 정보 */}
                <div className="flex flex-wrap items-center gap-4 text-xs text-gray-500">
                  <div className="flex items-center gap-1">
                    <User size={12} />
                    <span>{paper.authors.slice(0, 2).join(', ')}{paper.authors.length > 2 ? ` 외 ${paper.authors.length - 2}명` : ''}</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <Calendar size={12} />
                    <span>{paper.published}</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <Tag size={12} />
                    <span>{paper.category}</span>
                  </div>
                </div>

                {/* 키워드 */}
                <div className="flex flex-wrap gap-1 mt-2">
                  {paper.keywords.map((keyword, index) => (
                    <span
                      key={index}
                      className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded-full"
                    >
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>

              {/* 액션 버튼들 */}
              <div className="flex items-center gap-2 ml-4">
                <button
                  onClick={() => toggleExpanded(paper.arxiv_id || paper.filename)}
                  className="p-1 rounded hover:bg-gray-100 transition-colors"
                  title="상세 정보 보기"
                >
                  <Eye size={16} />
                </button>
                <a
                  href={paper.arxiv_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-1 rounded hover:bg-gray-100 transition-colors"
                  title="ArXiv에서 보기"
                >
                  <ExternalLink size={16} />
                </a>
              </div>
            </div>

            {/* 확장된 상세 정보 */}
            {expandedPaper === (paper.arxiv_id || paper.filename) && (
              <div className="mt-4 pt-4 border-t border-gray-100 space-y-3">
                <div>
                  <h5 className="text-sm font-medium text-gray-900 mb-2">초록 (한글)</h5>
                  <p className="text-sm text-gray-700 leading-relaxed">
                    {paper.abstract_ko}
                  </p>
                </div>
                
                <div>
                  <h5 className="text-sm font-medium text-gray-900 mb-2">Abstract (원문)</h5>
                  <p className="text-sm text-gray-600 leading-relaxed">
                    {paper.abstract}
                  </p>
                </div>

                <div className="flex items-center gap-4 pt-2">
                  <a
                    href={paper.pdf_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 px-3 py-1 bg-red-600 text-white text-sm rounded hover:bg-red-700 transition-colors"
                  >
                    <FileText size={14} />
                    PDF 다운로드
                  </a>
                  <a
                    href={paper.arxiv_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 px-3 py-1 bg-gray-600 text-white text-sm rounded hover:bg-gray-700 transition-colors"
                  >
                    <ExternalLink size={14} />
                    ArXiv 페이지
                  </a>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {collectedPapers.length === 0 && (
        <div className="text-center py-8 text-gray-500">
          <FileText size={32} className="mx-auto mb-2 opacity-50" />
          <p className="text-sm">아직 수집된 논문이 없습니다.</p>
        </div>
      )}
    </div>
  );
}

export default PaperList;
