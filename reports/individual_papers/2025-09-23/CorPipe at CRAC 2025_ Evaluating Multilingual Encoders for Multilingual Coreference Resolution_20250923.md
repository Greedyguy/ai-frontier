---
keywords:
  - Multilingual Coreference Resolution
  - Large Language Model
  - PyTorch
  - TensorFlow
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17858
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:34:14.625765",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multilingual Coreference Resolution",
    "Large Language Model",
    "PyTorch",
    "TensorFlow"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multilingual Coreference Resolution": 0.82,
    "Large Language Model": 0.8,
    "PyTorch": 0.7,
    "TensorFlow": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multilingual Coreference Resolution",
        "canonical": "Multilingual Coreference Resolution",
        "aliases": [
          "Cross-lingual Coreference Resolution"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and is a specific task within NLP, enhancing connectivity with related works.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "The paper introduces a new LLM track, linking it to broader discussions in NLP and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "PyTorch",
        "canonical": "PyTorch",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The migration to PyTorch is a significant technical detail that may connect with other works using or discussing this framework.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "TensorFlow",
        "canonical": "TensorFlow",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Mentioned as the previous framework, it provides context for technical evolution and links to other works using TensorFlow.",
        "novelty_score": 0.4,
        "connectivity_score": 0.72,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "Shared Task",
      "CRAC 2025",
      "CorPipe 25"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multilingual Coreference Resolution",
      "resolved_canonical": "Multilingual Coreference Resolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "PyTorch",
      "resolved_canonical": "PyTorch",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "TensorFlow",
      "resolved_canonical": "TensorFlow",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.72,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# CorPipe at CRAC 2025: Evaluating Multilingual Encoders for Multilingual Coreference Resolution

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17858.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17858](https://arxiv.org/abs/2509.17858)

## 🔗 유사한 논문
- [[2025-09-23/CorefInst_ Leveraging LLMs for Multilingual Coreference Resolution_20250923|CorefInst: Leveraging LLMs for Multilingual Coreference Resolution]] (83.5% similar)
- [[2025-09-23/Findings of the Fourth Shared Task on Multilingual Coreference Resolution_ Can LLMs Dethrone Traditional Approaches?_20250923|Findings of the Fourth Shared Task on Multilingual Coreference Resolution: Can LLMs Dethrone Traditional Approaches?]] (83.0% similar)
- [[2025-09-23/CLaC at DISRPT 2025_ Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification_20250923|CLaC at DISRPT 2025: Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification]] (80.1% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (79.3% similar)
- [[2025-09-23/AISTAT lab system for DCASE2025 Task6_ Language-based audio retrieval_20250923|AISTAT lab system for DCASE2025 Task6: Language-based audio retrieval]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/PyTorch|PyTorch]], [[keywords/TensorFlow|TensorFlow]]
**⚡ Unique Technical**: [[keywords/Multilingual Coreference Resolution|Multilingual Coreference Resolution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17858v1 Announce Type: new 
Abstract: We present CorPipe 25, the winning entry to the CRAC 2025 Shared Task on Multilingual Coreference Resolution. This fourth iteration of the shared task introduces a new LLM track alongside the original unconstrained track, features reduced development and test sets to lower computational requirements, and includes additional datasets. CorPipe 25 represents a complete reimplementation of our previous systems, migrating from TensorFlow to PyTorch. Our system significantly outperforms all other submissions in both the LLM and unconstrained tracks by a substantial margin of 8 percentage points. The source code and trained models are publicly available at https://github.com/ufal/crac2025-corpipe.

## 📝 요약

CorPipe 25는 CRAC 2025 다국어 코리퍼런스 해결 공유 과제에서 우승한 시스템입니다. 이번 과제는 새로운 LLM 트랙을 도입하고, 개발 및 테스트 세트를 축소하여 계산 요구 사항을 줄였으며, 추가 데이터셋을 포함합니다. CorPipe 25는 이전 시스템을 TensorFlow에서 PyTorch로 완전히 재구현한 것으로, LLM 및 비제한 트랙 모두에서 다른 제출물보다 8% 포인트 높은 성능을 보였습니다. 소스 코드와 학습된 모델은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. CorPipe 25는 CRAC 2025 다국어 코리퍼런스 해석 공유 과제에서 우승한 시스템입니다.
- 2. 이번 과제에서는 새로운 LLM 트랙이 도입되었으며, 개발 및 테스트 세트가 축소되어 계산 요구 사항이 낮아졌습니다.
- 3. CorPipe 25는 이전 시스템을 TensorFlow에서 PyTorch로 완전히 재구현한 것입니다.
- 4. 이 시스템은 LLM 및 비제한 트랙 모두에서 다른 제출물보다 8% 포인트 더 높은 성능을 보였습니다.
- 5. 소스 코드와 학습된 모델은 https://github.com/ufal/crac2025-corpipe에서 공개적으로 제공됩니다.


---

*Generated on 2025-09-24 03:34:14*