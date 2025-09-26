---
keywords:
  - Large Language Model
  - Cross-Lingual Interaction-aware Multilingual Balancing
  - Cross-Lingual Interaction
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15556
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:03:26.311437",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cross-Lingual Interaction-aware Multilingual Balancing",
    "Cross-Lingual Interaction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cross-Lingual Interaction-aware Multilingual Balancing": 0.8,
    "Cross-Lingual Interaction": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus, connecting with existing discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Climb",
        "canonical": "Cross-Lingual Interaction-aware Multilingual Balancing",
        "aliases": [
          "Climb framework"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework specifically developed for optimizing multilingual data allocation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "cross-lingual interactions",
        "canonical": "Cross-Lingual Interaction",
        "aliases": [
          "inter-language dependencies"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for understanding multilingual data allocation and its impact on model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "multilingual capabilities",
      "language proportions",
      "training corpora"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Climb",
      "resolved_canonical": "Cross-Lingual Interaction-aware Multilingual Balancing",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cross-lingual interactions",
      "resolved_canonical": "Cross-Lingual Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining

**Korean Title:** 다중언어 조화 탐구: 대형 언어 모델 사전 훈련을 위한 다중언어 데이터 할당

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15556.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15556](https://arxiv.org/abs/2509.15556)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (86.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (85.9% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (85.3% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (84.9% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Cross-Lingual Interaction|Cross-Lingual Interaction]]
**⚡ Unique Technical**: [[keywords/Cross-Lingual Interaction-aware Multilingual Balancing|Cross-Lingual Interaction-aware Multilingual Balancing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15556v1 Announce Type: cross 
Abstract: Large language models (LLMs) have become integral to a wide range of applications worldwide, driving an unprecedented global demand for effective multilingual capabilities. Central to achieving robust multilingual performance is the strategic allocation of language proportions within training corpora. However, determining optimal language ratios is highly challenging due to intricate cross-lingual interactions and sensitivity to dataset scale. This paper introduces Climb (Cross-Lingual Interaction-aware Multilingual Balancing), a novel framework designed to systematically optimize multilingual data allocation. At its core, Climb introduces a cross-lingual interaction-aware language ratio, explicitly quantifying each language's effective allocation by capturing inter-language dependencies. Leveraging this ratio, Climb proposes a principled two-step optimization procedure--first equalizing marginal benefits across languages, then maximizing the magnitude of the resulting language allocation vectors--significantly simplifying the inherently complex multilingual optimization problem. Extensive experiments confirm that Climb can accurately measure cross-lingual interactions across various multilingual settings. LLMs trained with Climb-derived proportions consistently achieve state-of-the-art multilingual performance, even achieving competitive performance with open-sourced LLMs trained with more tokens.

## 🔍 Abstract (한글 번역)

arXiv:2509.15556v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)은 전 세계적으로 다양한 응용 프로그램에 필수적인 요소가 되었으며, 효과적인 다국어 기능에 대한 전례 없는 글로벌 수요를 촉진하고 있습니다. 강력한 다국어 성능을 달성하기 위해서는 훈련 코퍼스 내에서 언어 비율의 전략적 할당이 중요합니다. 그러나 최적의 언어 비율을 결정하는 것은 복잡한 언어 간 상호작용과 데이터셋 규모에 대한 민감성 때문에 매우 어렵습니다. 본 논문에서는 다국어 데이터 할당을 체계적으로 최적화하기 위해 설계된 새로운 프레임워크인 Climb (Cross-Lingual Interaction-aware Multilingual Balancing)을 소개합니다. Climb의 핵심은 언어 간 종속성을 포착하여 각 언어의 효과적인 할당을 명시적으로 정량화하는 언어 간 상호작용 인식 언어 비율을 도입하는 것입니다. 이 비율을 활용하여 Climb은 원칙적인 두 단계 최적화 절차를 제안합니다. 첫 번째로 언어 간 한계 이익을 균등화하고, 두 번째로 결과 언어 할당 벡터의 크기를 최대화하여 본질적으로 복잡한 다국어 최적화 문제를 크게 단순화합니다. 광범위한 실험을 통해 Climb이 다양한 다국어 설정에서 언어 간 상호작용을 정확하게 측정할 수 있음을 확인했습니다. Climb에서 도출된 비율로 훈련된 LLM은 일관되게 최첨단 다국어 성능을 달성하며, 더 많은 토큰으로 훈련된 오픈 소스 LLM과도 경쟁력 있는 성능을 보여줍니다.

## 📝 요약

이 논문은 다국어 성능을 최적화하기 위한 새로운 프레임워크인 Climb을 소개합니다. Climb은 언어 간 상호작용을 고려한 언어 비율을 도입하여 각 언어의 효과적인 할당을 정량화합니다. 이를 통해 Climb은 언어 간 한계 이익을 균등화하고, 결과 언어 할당 벡터의 크기를 최대화하는 두 단계 최적화 절차를 제안합니다. 실험 결과, Climb을 통해 학습된 대형 언어 모델(LLM)은 다양한 다국어 환경에서 최첨단 성능을 달성하며, 더 많은 토큰으로 학습된 공개 LLM과도 경쟁력 있는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Climb는 다국어 데이터 할당을 최적화하기 위한 새로운 프레임워크로, 언어 간 상호작용을 고려한 언어 비율을 도입합니다.
- 2. Climb는 언어 간 의존성을 포착하여 각 언어의 효과적인 할당을 정량화합니다.
- 3. Climb의 최적화 절차는 언어 간 한계 이익을 균등화하고, 결과 언어 할당 벡터의 크기를 최대화하는 두 단계로 구성됩니다.
- 4. Climb를 통해 훈련된 대형 언어 모델은 다양한 다국어 환경에서 최첨단 성능을 일관되게 달성합니다.
- 5. Climb는 더 많은 토큰으로 훈련된 오픈소스 대형 언어 모델과 경쟁력 있는 성능을 발휘합니다.


---

*Generated on 2025-09-23 09:03:26*