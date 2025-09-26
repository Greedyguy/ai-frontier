---
keywords:
  - Disaster Management
  - Information Retrieval
  - Retrieval Models
  - Benchmark
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.15856
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:00:27.601506",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Disaster Management",
    "Information Retrieval",
    "Retrieval Models",
    "Benchmark"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Disaster Management": 0.88,
    "Information Retrieval": 0.8,
    "Retrieval Models": 0.72,
    "Benchmark": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Disaster Management",
        "canonical": "Disaster Management",
        "aliases": [
          "Crisis Management",
          "Emergency Management"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, it connects various IR tasks to real-world applications in disaster scenarios.",
        "novelty_score": 0.75,
        "connectivity_score": 0.85,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Information Retrieval",
        "canonical": "Information Retrieval",
        "aliases": [
          "IR"
        ],
        "category": "broad_technical",
        "rationale": "A core concept in the paper, linking to various retrieval models and benchmarks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Retrieval Models",
        "canonical": "Retrieval Models",
        "aliases": [
          "IR Models"
        ],
        "category": "specific_connectable",
        "rationale": "Key to understanding the performance evaluation aspect of the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Benchmark",
        "canonical": "Benchmark",
        "aliases": [
          "Evaluation Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "Essential for linking the evaluation framework presented in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Disaster Management",
      "resolved_canonical": "Disaster Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.85,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Information Retrieval",
      "resolved_canonical": "Information Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Retrieval Models",
      "resolved_canonical": "Retrieval Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Benchmark",
      "resolved_canonical": "Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# DisastIR: A Comprehensive Information Retrieval Benchmark for Disaster Management

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.15856.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.15856](https://arxiv.org/abs/2505.15856)

## 🔗 유사한 논문
- [[2025-09-22/Efficient and Versatile Model for Multilingual Information Retrieval of Islamic Text_ Development and Deployment in Real-World Scenarios_20250922|Efficient and Versatile Model for Multilingual Information Retrieval of Islamic Text: Development and Deployment in Real-World Scenarios]] (79.5% similar)
- [[2025-09-22/Database-Augmented Query Representation for Information Retrieval_20250922|Database-Augmented Query Representation for Information Retrieval]] (79.3% similar)
- [[2025-09-19/Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (78.9% similar)
- [[2025-09-18/Large Language Models for Information Retrieval_ A Survey_20250918|Large Language Models for Information Retrieval: A Survey]] (78.3% similar)
- [[2025-09-22/RSCC_ A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events_20250922|RSCC: A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events]] (78.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Information Retrieval|Information Retrieval]]
**🔗 Specific Connectable**: [[keywords/Retrieval Models|Retrieval Models]]
**⚡ Unique Technical**: [[keywords/Disaster Management|Disaster Management]], [[keywords/Benchmark|Benchmark]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.15856v3 Announce Type: replace-cross 
Abstract: Effective disaster management requires timely access to accurate and contextually relevant information. Existing Information Retrieval (IR) benchmarks, however, focus primarily on general or specialized domains, such as medicine or finance, neglecting the unique linguistic complexity and diverse information needs encountered in disaster management scenarios. To bridge this gap, we introduce DisastIR, the first comprehensive IR evaluation benchmark specifically tailored for disaster management. DisastIR comprises 9,600 diverse user queries and more than 1.3 million labeled query-passage pairs, covering 48 distinct retrieval tasks derived from six search intents and eight general disaster categories that include 301 specific event types. Our evaluations of 30 state-of-the-art retrieval models demonstrate significant performance variances across tasks, with no single model excelling universally. Furthermore, comparative analyses reveal significant performance gaps between general-domain and disaster management-specific tasks, highlighting the necessity of disaster management-specific benchmarks for guiding IR model selection to support effective decision-making in disaster management scenarios. All source codes and DisastIR are available at https://github.com/KaiYin97/Disaster_IR.

## 📝 요약

이 논문은 재난 관리에 특화된 정보 검색(IR) 평가 기준인 DisastIR을 소개합니다. 기존 IR 벤치마크는 일반 또는 특정 분야에 집중하여 재난 관리의 복잡한 언어적 특성과 다양한 정보 요구를 충분히 반영하지 못했습니다. DisastIR은 9,600개의 사용자 쿼리와 130만 개 이상의 쿼리-패시지 쌍을 포함하며, 6가지 검색 의도와 8개의 일반 재난 범주에서 파생된 48개의 검색 과제를 다룹니다. 30개의 최신 검색 모델을 평가한 결과, 과제별로 성능 차이가 크고, 모든 과제에서 뛰어난 모델은 없었습니다. 일반 도메인과 재난 관리 특정 과제 간의 성능 격차가 커, 재난 관리에 특화된 벤치마크의 필요성을 강조합니다. DisastIR의 소스 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 재난 관리에는 정확하고 맥락에 맞는 정보에 대한 신속한 접근이 필수적이다.
- 2. 기존 정보 검색 벤치마크는 재난 관리의 독특한 언어적 복잡성과 다양한 정보 요구를 간과하고 있다.
- 3. DisastIR은 재난 관리에 특화된 최초의 포괄적인 정보 검색 평가 벤치마크로, 9,600개의 사용자 쿼리와 130만 개 이상의 쿼리-패시지 쌍을 포함한다.
- 4. 30개의 최첨단 검색 모델 평가 결과, 모든 작업에서 뛰어난 성능을 보이는 단일 모델은 없었다.
- 5. 일반 도메인과 재난 관리 특화 작업 간의 성능 격차가 커서, 재난 관리 특화 벤치마크의 필요성이 강조된다.


---

*Generated on 2025-09-24 01:00:27*