---
keywords:
  - Retrieval Augmented Generation
  - Large Language Model
  - Reinforcement Learning
  - Lossless Compression
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2508.19282
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:09:02.529687",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Large Language Model",
    "Reinforcement Learning",
    "Lossless Compression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.88,
    "Large Language Model": 0.8,
    "Reinforcement Learning": 0.82,
    "Lossless Compression": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that enhances LLMs by integrating external knowledge, making it a strong candidate for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.88
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus and are a key component in many NLP applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "specific_connectable",
        "rationale": "Reinforcement Learning is crucial for the proposed method, CORE, optimizing the compression process.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Lossless Compression",
        "canonical": "Lossless Compression",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, aiming to maintain performance while reducing input size.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Lossless Compression",
      "resolved_canonical": "Lossless Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning

**Korean Title:** CORE-RAG: 강화 학습을 통한 검색 증강 대형 언어 모델의 무손실 압축

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.19282.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2508.19282](https://arxiv.org/abs/2508.19282)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (86.5% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (85.8% similar)
- [[2025-09-22/CodeRAG_ Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion_20250922|CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion]] (85.7% similar)
- [[2025-09-19/GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA: Graph-based Reranking against Adversarial Documents Attack]] (85.7% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Lossless Compression|Lossless Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.19282v2 Announce Type: replace-cross 
Abstract: Retrieval-Augmented Generation (RAG) has emerged as a promising approach to enhance the timeliness of knowledge and the factual accuracy of responses in Large Language Models (LLMs). However, the inclusion of excessive retrieved documents substantially increases the input length, leading to higher computational costs. Previous studies have attempted to compress retrieved documents into shorter texts before in-context integration, but such methods often compromise end-task performance. The lack of well-defined compression targets forces many approaches to rely on fixed heuristics, which cannot guarantee that the compressed content will effectively support the end task. To address these limitations, we propose CORE, a novel method designed to achieve lossless context compression for RAG. CORE employs reinforcement learning to optimize the compression process without relying on predefined compression labels, which enables the compressor to generate summaries that maximize the accuracy of answers generated by the LLM. Extensive experiments on four datasets demonstrate the superiority of our approach. With a high compression ratio of 3\%, our method not only avoids performance degradation compared to prepending full documents across all datasets but also improves the average Exact Match (EM) score by 3.3 points. The code will be released soon.

## 🔍 Abstract (한글 번역)

arXiv:2508.19282v2 발표 유형: 교체-크로스  
초록: Retrieval-Augmented Generation (RAG)은 대형 언어 모델(LLM)에서 지식의 적시성과 응답의 사실적 정확성을 향상시키기 위한 유망한 접근법으로 부상하고 있습니다. 그러나 과도한 검색 문서의 포함은 입력 길이를 상당히 증가시켜 계산 비용을 높입니다. 이전 연구에서는 맥락 내 통합 전에 검색된 문서를 더 짧은 텍스트로 압축하려고 시도했지만, 이러한 방법은 종종 최종 작업 성능을 저하시킵니다. 잘 정의된 압축 목표의 부재로 인해 많은 접근법이 고정된 휴리스틱에 의존하게 되며, 이는 압축된 내용이 최종 작업을 효과적으로 지원할 것이라는 보장을 제공하지 못합니다. 이러한 제한점을 해결하기 위해, 우리는 RAG를 위한 무손실 맥락 압축을 달성하기 위해 설계된 새로운 방법인 CORE를 제안합니다. CORE는 강화 학습을 활용하여 사전 정의된 압축 레이블에 의존하지 않고 압축 과정을 최적화하여, LLM이 생성하는 답변의 정확성을 극대화하는 요약을 생성할 수 있도록 합니다. 네 개의 데이터셋에 대한 광범위한 실험은 우리의 접근법의 우수성을 입증합니다. 3%의 높은 압축 비율로, 우리의 방법은 모든 데이터셋에서 전체 문서를 첨부하는 것과 비교하여 성능 저하를 피할 뿐만 아니라 평균 정확 일치(EM) 점수를 3.3점 향상시킵니다. 코드는 곧 공개될 예정입니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 정보 정확성과 시의성을 향상시키기 위한 검색 증강 생성(RAG) 접근법의 문제점을 해결하고자 합니다. 기존 방법은 검색된 문서를 짧게 압축하려 했으나, 이는 종종 성능 저하를 초래했습니다. 이를 해결하기 위해, 저자들은 강화 학습을 활용한 새로운 방법인 CORE를 제안합니다. CORE는 사전 정의된 압축 기준 없이도 문맥을 손실 없이 압축할 수 있으며, LLM의 응답 정확성을 극대화하는 요약을 생성합니다. 네 개의 데이터셋에 대한 실험 결과, CORE는 3%의 높은 압축 비율을 유지하면서도 성능 저하 없이 평균 정확도(EM) 점수를 3.3점 향상시켰습니다. 코드도 곧 공개될 예정입니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation (RAG)는 대형 언어 모델의 지식 최신성과 사실적 정확성을 향상시키는 유망한 접근법으로 부상하고 있다.
- 2. 기존 연구들은 문서 압축을 시도했으나, 고정된 휴리스틱에 의존하여 최종 작업 성능을 저하시킬 수 있다.
- 3. CORE는 강화 학습을 활용하여 사전 정의된 압축 라벨 없이 압축 과정을 최적화하고, LLM의 답변 정확성을 극대화하는 요약을 생성한다.
- 4. CORE는 3%의 높은 압축 비율로 성능 저하 없이 평균 정확 일치(EM) 점수를 3.3점 향상시킨다.
- 5. CORE의 우수성은 네 개의 데이터셋을 통한 광범위한 실험에서 입증되었으며, 코드가 곧 공개될 예정이다.


---

*Generated on 2025-09-23 10:09:02*