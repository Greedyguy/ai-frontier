---
keywords:
  - BM25
  - Position Bias
  - Position Sensitivity Index
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2505.13950
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:56:49.867570",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "BM25",
    "Position Bias",
    "Position Sensitivity Index"
  ],
  "rejected_keywords": [
    "Dense Embedding Models",
    "ColBERT-style Models"
  ],
  "similarity_scores": {
    "BM25": 0.8,
    "Position Bias": 0.78,
    "Position Sensitivity Index": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# An Empirical Study of Position Bias in Modern Information Retrieval

**Korean Title:** 현대 정보 검색에서 위치 편향에 대한 실증적 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/BM25|BM25]]
**⚡ Unique Technical**: [[keywords/Position Bias|position bias]], [[keywords/Position Sensitivity Index|Position Sensitivity Index]]

## 🔗 유사한 논문
- [[Position Bias Mitigates Position BiasMitigate Position Bias Through Inter-Position Knowledge Distillation]] (84.7% similar)
- [[GASLITEing the Retrieval Exploring Vulnerabilities in Dense Embedding-based Search]] (79.4% similar)
- [[Judging with Many Minds Do More Perspectives Mean Less Prejudice On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (78.9% similar)
- [[Large Language Models for Information Retrieval A Survey]] (78.4% similar)
- [[What's the Best Way to Retrieve Slides_ A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.13950v5 Announce Type: replace 
Abstract: This study investigates the position bias in information retrieval, where models tend to overemphasize content at the beginning of passages while neglecting semantically relevant information that appears later. To analyze the extent and impact of position bias, we introduce a new evaluation framework consisting of two position-aware retrieval benchmarks (SQuAD-PosQ, FineWeb-PosQ) and an intuitive diagnostic metric, the Position Sensitivity Index (PSI), for quantifying position bias from a worst-case perspective. We conduct a comprehensive evaluation across the full retrieval pipeline, including BM25, dense embedding models, ColBERT-style late-interaction models, and full-interaction reranker models. Our experiments show that when relevant information appears later in the passage, dense embedding models and ColBERT-style models suffer significant performance degradation (an average drop of 15.6%). In contrast, BM25 and reranker models demonstrate greater robustness to such positional variation. These findings provide practical insights into model sensitivity to the position of relevant information and offer guidance for building more position-robust retrieval systems. Code and data are publicly available at: https://github.com/NovaSearch-Team/position-bias-in-IR.

## 🔍 Abstract (한글 번역)

arXiv:2505.13950v5 발표 유형: 교체  
초록: 본 연구는 정보 검색에서 발생하는 위치 편향(position bias)을 조사합니다. 이는 모델이 구문의 시작 부분에 있는 내용을 과도하게 강조하면서, 이후에 나타나는 의미적으로 관련 있는 정보를 간과하는 경향을 말합니다. 위치 편향의 정도와 영향을 분석하기 위해, 우리는 두 가지 위치 인식 검색 벤치마크(SQuAD-PosQ, FineWeb-PosQ)와 최악의 경우를 고려한 위치 편향을 정량화하는 직관적인 진단 지표인 위치 민감도 지수(Position Sensitivity Index, PSI)를 포함하는 새로운 평가 프레임워크를 도입합니다. 우리는 BM25, 밀집 임베딩 모델, ColBERT 스타일의 후기 상호작용 모델, 그리고 완전 상호작용 재순위 모델을 포함하는 전체 검색 파이프라인에 걸쳐 포괄적인 평가를 수행합니다. 실험 결과, 관련 정보가 구문의 후반부에 나타날 때, 밀집 임베딩 모델과 ColBERT 스타일 모델은 성능이 크게 저하되는 것으로 나타났으며(평균 15.6% 감소), 반면 BM25와 재순위 모델은 이러한 위치 변화에 대해 더 큰 견고성을 보여주었습니다. 이러한 결과는 관련 정보의 위치에 대한 모델의 민감성에 대한 실질적인 통찰을 제공하며, 보다 위치에 강건한 검색 시스템을 구축하기 위한 지침을 제시합니다. 코드와 데이터는 다음에서 공개적으로 이용 가능합니다: https://github.com/NovaSearch-Team/position-bias-in-IR.

## 📝 요약

이 연구는 정보 검색에서 발생하는 위치 편향을 조사합니다. 위치 편향이란 모델이 문서의 초반부 내용을 과도하게 강조하고 후반부에 나타나는 의미 있는 정보를 간과하는 현상입니다. 이를 분석하기 위해 두 가지 위치 인식 검색 벤치마크(SQuAD-PosQ, FineWeb-PosQ)와 위치 민감도 지수(PSI)를 도입했습니다. BM25, 밀집 임베딩 모델, ColBERT 스타일의 상호작용 모델, 전체 상호작용 재순위 모델을 포함한 검색 파이프라인 전반에 걸쳐 평가를 수행했습니다. 실험 결과, 관련 정보가 문서 후반부에 있을 때 밀집 임베딩 모델과 ColBERT 스타일 모델은 성능이 크게 저하되었으나(평균 15.6% 감소), BM25와 재순위 모델은 이러한 위치 변화에 더 강인함을 보였습니다. 이 연구는 위치에 대한 모델의 민감성을 이해하고, 보다 강인한 검색 시스템 구축에 대한 지침을 제공합니다. 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 정보 검색에서 위치 편향은 문서의 시작 부분에 있는 내용을 과대평가하고 후반부의 의미 있는 정보를 간과하는 경향이 있다.

- 2. 위치 편향의 영향을 분석하기 위해 새로운 평가 프레임워크와 위치 인식 검색 벤치마크(SQuAD-PosQ, FineWeb-PosQ) 및 위치 민감도 지수(PSI)를 도입했다.

- 3. 실험 결과, 관련 정보가 문서 후반부에 있을 때 밀집 임베딩 모델과 ColBERT 스타일 모델의 성능이 평균 15.6% 감소했다.

- 4. BM25 및 재순위 모델은 위치 변화에 대해 더 큰 강건성을 보여준다.

- 5. 연구 결과는 검색 시스템을 구축할 때 위치에 강건한 모델을 개발하는 데 실질적인 통찰력을 제공한다.

---

*Generated on 2025-09-19 16:26:07*