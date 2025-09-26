---
keywords:
  - Few-Shot Learning
  - State-Space Models
  - Longhorn
  - Transformer
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19658
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:42:47.414034",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "State-Space Models",
    "Longhorn",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.82,
    "State-Space Models": 0.79,
    "Longhorn": 0.77,
    "Transformer": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "In-context Imitation Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "ICIL"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of learning from few examples, which is central to the paper's approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "State-Space Models",
        "canonical": "State-Space Models",
        "aliases": [
          "SSM"
        ],
        "category": "unique_technical",
        "rationale": "Key technical component of the proposed method, distinguishing it from Transformer-based approaches.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Longhorn",
        "canonical": "Longhorn",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific implementation of SSM that enhances scalability and efficiency, central to the paper's contribution.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Serves as a comparative baseline in the paper, highlighting the advantages of the proposed method.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "LIBERO benchmark",
      "deployment time",
      "parameter updates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "In-context Imitation Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "State-Space Models",
      "resolved_canonical": "State-Space Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Longhorn",
      "resolved_canonical": "Longhorn",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# RoboSSM: Scalable In-context Imitation Learning via State-Space Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19658.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19658](https://arxiv.org/abs/2509.19658)

## 🔗 유사한 논문
- [[2025-09-23/CodeSSM_ Towards State Space Models for Code Understanding_20250923|CodeSSM: Towards State Space Models for Code Understanding]] (84.7% similar)
- [[2025-09-25/Self-evolved Imitation Learning in Simulated World_20250925|Self-evolved Imitation Learning in Simulated World]] (83.1% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (81.8% similar)
- [[2025-09-23/TACO_ Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration_20250923|TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration]] (81.8% similar)
- [[2025-09-22/Disentangling Latent Shifts of In-Context Learning with Weak Supervision_20250922|Disentangling Latent Shifts of In-Context Learning with Weak Supervision]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/State-Space Models|State-Space Models]], [[keywords/Longhorn|Longhorn]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19658v1 Announce Type: cross 
Abstract: In-context imitation learning (ICIL) enables robots to learn tasks from prompts consisting of just a handful of demonstrations. By eliminating the need for parameter updates at deployment time, this paradigm supports few-shot adaptation to novel tasks. However, recent ICIL methods rely on Transformers, which have computational limitations and tend to underperform when handling longer prompts than those seen during training. In this work, we introduce RoboSSM, a scalable recipe for in-context imitation learning based on state-space models (SSM). Specifically, RoboSSM replaces Transformers with Longhorn -- a state-of-the-art SSM that provides linear-time inference and strong extrapolation capabilities, making it well-suited for long-context prompts. We evaluate our approach on the LIBERO benchmark and compare it against strong Transformer-based ICIL baselines. Experiments show that RoboSSM extrapolates effectively to varying numbers of in-context demonstrations, yields high performance on unseen tasks, and remains robust in long-horizon scenarios. These results highlight the potential of SSMs as an efficient and scalable backbone for ICIL. Our code is available at https://github.com/youngjuY/RoboSSM.

## 📝 요약

이 논문에서는 새로운 인컨텍스트 모방 학습(ICIL) 방법인 RoboSSM을 제안합니다. 기존의 ICIL 방법은 Transformer를 사용하여 긴 프롬프트 처리 시 성능이 저하되는 문제가 있었습니다. RoboSSM은 이 문제를 해결하기 위해 Longhorn이라는 최신 상태 공간 모델(SSM)을 도입하여 선형 시간 추론과 강력한 외삽 능력을 제공합니다. LIBERO 벤치마크에서 실험한 결과, RoboSSM은 다양한 인컨텍스트 데모에 효과적으로 대응하며, 새로운 작업에서도 높은 성능을 보이고 긴 시나리오에서도 강건함을 유지합니다. 이는 SSM이 ICIL의 효율적이고 확장 가능한 기반이 될 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. In-context imitation learning(ICIL)은 소수의 시연으로 로봇이 작업을 학습할 수 있게 하며, 새로운 작업에 대한 few-shot 적응을 지원합니다.
- 2. 기존 ICIL 방법은 Transformer에 의존하지만, 이는 긴 프롬프트 처리 시 성능이 저하되는 문제를 가지고 있습니다.
- 3. RoboSSM은 Transformer 대신 Longhorn이라는 최신 상태 공간 모델(SSM)을 사용하여 긴 프롬프트에 적합한 선형 시간 추론과 강력한 외삽 능력을 제공합니다.
- 4. LIBERO 벤치마크에서의 실험 결과, RoboSSM은 다양한 수의 시연에 효과적으로 외삽하고, 보지 못한 작업에서도 높은 성능을 보이며, 긴 수평선 시나리오에서도 강건함을 유지합니다.
- 5. SSM이 ICIL의 효율적이고 확장 가능한 백본으로서의 잠재력을 가지고 있음을 강조합니다.


---

*Generated on 2025-09-25 15:42:47*