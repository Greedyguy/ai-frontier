---
keywords:
  - Zero-Shot Learning
  - Multimodal Learning
  - Interactive Retrieval
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16674
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:31:09.070064",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Multimodal Learning",
    "Interactive Retrieval",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.85,
    "Multimodal Learning": 0.8,
    "Interactive Retrieval": 0.78,
    "Vision-Language Model": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is crucial for understanding the framework's ability to generalize without prior examples, linking it to broader machine learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is central to the framework's ability to process and integrate different types of data, enhancing connectivity with related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.8
      },
      {
        "surface": "Interactive Retrieval",
        "canonical": "Interactive Retrieval",
        "aliases": [
          "Interactive Search"
        ],
        "category": "unique_technical",
        "rationale": "Interactive Retrieval is a unique aspect of the framework, emphasizing user engagement and adaptability in search processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are integral to the framework's ability to interpret and relate visual and textual data, linking it to advanced AI research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "Text-based Pedestrian Retrieval",
      "Feature Contrastive Decoding",
      "Incremental Semantic Mining",
      "Query-aware Hierarchical Retrieval"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Interactive Retrieval",
      "resolved_canonical": "Interactive Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# FitPro: A Zero-Shot Framework for Interactive Text-based Pedestrian Retrieval in Open World

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16674.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16674](https://arxiv.org/abs/2509.16674)

## 🔗 유사한 논문
- [[2025-09-19/Handle Object Navigation as Weighted Traveling Repairman Problem_20250919|Handle Object Navigation as Weighted Traveling Repairman Problem]] (80.9% similar)
- [[2025-09-23/Optimal Transport for Handwritten Text Recognition in a Low-Resource Regime_20250923|Optimal Transport for Handwritten Text Recognition in a Low-Resource Regime]] (80.8% similar)
- [[2025-09-23/ProReason_ Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom_20250923|ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom]] (80.0% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (79.6% similar)
- [[2025-09-23/KRAST_ Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models_20250923|KRAST: Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Interactive Retrieval|Interactive Retrieval]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16674v1 Announce Type: new 
Abstract: Text-based Pedestrian Retrieval (TPR) aims to retrieve specific target pedestrians in visual scenes according to natural language descriptions. Although existing methods have achieved progress under constrained settings, interactive retrieval in the open-world scenario still suffers from limited model generalization and insufficient semantic understanding. To address these challenges, we propose FitPro, an open-world interactive zero-shot TPR framework with enhanced semantic comprehension and cross-scene adaptability. FitPro has three innovative components: Feature Contrastive Decoding (FCD), Incremental Semantic Mining (ISM), and Query-aware Hierarchical Retrieval (QHR). The FCD integrates prompt-guided contrastive decoding to generate high-quality structured pedestrian descriptions from denoised images, effectively alleviating semantic drift in zero-shot scenarios. The ISM constructs holistic pedestrian representations from multi-view observations to achieve global semantic modeling in multi-turn interactions,thereby improving robustness against viewpoint shifts and fine-grained variations in descriptions. The QHR dynamically optimizes the retrieval pipeline according to query types, enabling efficient adaptation to multi-modal and multi-view inputs. Extensive experiments on five public datasets and two evaluation protocols demonstrate that FitPro significantly overcomes the generalization limitations and semantic modeling constraints of existing methods in interactive retrieval, paving the way for practical deployment. The code and data will be released at https://github.com/ lilo4096/FitPro-Interactive-Person-Retrieval.

## 📝 요약

이 논문은 자연어 설명을 기반으로 특정 보행자를 시각 장면에서 검색하는 텍스트 기반 보행자 검색(TPR)의 한계를 극복하기 위해 FitPro라는 프레임워크를 제안합니다. FitPro는 개방형 세계에서의 상호작용적 제로샷 TPR을 목표로 하며, 향상된 의미 이해와 장면 간 적응성을 제공합니다. 주요 구성 요소로는 특징 대조 디코딩(FCD), 점진적 의미 채굴(ISM), 쿼리 인식 계층적 검색(QHR)이 있습니다. FCD는 프롬프트 기반 대조 디코딩을 통해 고품질의 보행자 설명을 생성하여 의미 드리프트를 완화합니다. ISM은 다중 관찰을 통해 보행자 표현을 구축하여 견고성을 높입니다. QHR은 쿼리 유형에 따라 검색 파이프라인을 최적화하여 다중 모달 입력에 효율적으로 적응합니다. 실험 결과, FitPro는 기존 방법의 일반화 한계와 의미 모델링 제약을 극복하여 실용적 활용 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. FitPro는 자연어 설명을 기반으로 특정 보행자를 시각적 장면에서 검색하는 텍스트 기반 보행자 검색(TPR)을 위한 프레임워크입니다.
- 2. FitPro는 제로샷 시나리오에서 의미적 드리프트를 완화하기 위해 프롬프트 기반 대조 디코딩을 통합한 기능 대조 디코딩(FCD)을 도입합니다.
- 3. 증분적 의미 마이닝(ISM)은 다중 관찰을 통해 전체적인 보행자 표현을 구축하여 다중 턴 상호작용에서 전역 의미 모델링을 달성합니다.
- 4. FitPro의 쿼리 인식 계층적 검색(QHR)은 쿼리 유형에 따라 검색 파이프라인을 동적으로 최적화하여 효율적인 적응을 가능하게 합니다.
- 5. FitPro는 다섯 개의 공개 데이터셋과 두 개의 평가 프로토콜에서 기존 방법의 일반화 한계와 의미 모델링 제약을 극복하는 데 성공했습니다.


---

*Generated on 2025-09-24 04:31:09*