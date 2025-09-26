---
keywords:
  - Object Hallucination
  - Vision-Language Model
  - GLSim
  - Multimodal Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.19972
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:23:07.528746",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Object Hallucination",
    "Vision-Language Model",
    "GLSim",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Object Hallucination": 0.8,
    "Vision-Language Model": 0.85,
    "GLSim": 0.78,
    "Multimodal Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Object Hallucination",
        "canonical": "Object Hallucination",
        "aliases": [
          "Object-level Hallucination"
        ],
        "category": "unique_technical",
        "rationale": "It is a specific challenge addressed by the paper, crucial for linking discussions on model reliability.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Central to the paper's focus, linking advancements in multimodal AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "GLSim",
        "canonical": "GLSim",
        "aliases": [
          "Global-Local Similarity"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework specific to the paper, enhancing discussions on detection methods.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Relevant for linking to broader discussions on integrating multiple data modalities.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Object Hallucination",
      "resolved_canonical": "Object Hallucination",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "GLSim",
      "resolved_canonical": "GLSim",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# GLSim: Detecting Object Hallucinations in LVLMs via Global-Local Similarity

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.19972.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.19972](https://arxiv.org/abs/2508.19972)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization_20250923|Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization]] (84.9% similar)
- [[2025-09-22/ORIC_ Benchmarking Object Recognition in Incongruous Context for Large Vision-Language Models_20250922|ORIC: Benchmarking Object Recognition in Incongruous Context for Large Vision-Language Models]] (84.4% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (83.9% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (82.7% similar)
- [[2025-09-23/ChartHal_ A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding_20250923|ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Object Hallucination|Object Hallucination]], [[keywords/GLSim|GLSim]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.19972v2 Announce Type: replace-cross 
Abstract: Object hallucination in large vision-language models presents a significant challenge to their safe deployment in real-world applications. Recent works have proposed object-level hallucination scores to estimate the likelihood of object hallucination; however, these methods typically adopt either a global or local perspective in isolation, which may limit detection reliability. In this paper, we introduce GLSim, a novel training-free object hallucination detection framework that leverages complementary global and local embedding similarity signals between image and text modalities, enabling more accurate and reliable hallucination detection in diverse scenarios. We comprehensively benchmark existing object hallucination detection methods and demonstrate that GLSim achieves superior detection performance, outperforming competitive baselines by a significant margin.

## 📝 요약

이 논문은 대규모 시각-언어 모델에서 발생하는 객체 환각 문제를 해결하기 위한 새로운 접근법인 GLSim을 제안합니다. 기존의 객체 환각 점수는 주로 전역적 또는 국소적 관점 중 하나만을 사용하여 환각을 감지하는 데 한계가 있었습니다. GLSim은 이미지와 텍스트 간의 전역 및 국소 임베딩 유사성을 활용하여 보다 정확하고 신뢰할 수 있는 환각 감지를 가능하게 합니다. 다양한 시나리오에서 GLSim의 우수한 성능을 입증하며, 기존 방법들보다 뛰어난 환각 감지 성능을 보여줍니다.

## 🎯 주요 포인트

- 1. 대규모 비전-언어 모델에서 객체 환각 문제는 실제 응용에서의 안전한 배포에 중요한 도전 과제입니다.
- 2. 기존 연구들은 객체 환각 가능성을 추정하기 위해 객체 수준의 환각 점수를 제안했으나, 주로 전역 또는 국부적 관점을 단독으로 채택하여 탐지 신뢰성을 제한할 수 있습니다.
- 3. 본 논문에서는 이미지와 텍스트 모달리티 간의 전역 및 국부 임베딩 유사성 신호를 활용하여 다양한 시나리오에서 더 정확하고 신뢰할 수 있는 환각 탐지를 가능하게 하는 GLSim이라는 새로운 훈련 불필요 객체 환각 탐지 프레임워크를 소개합니다.
- 4. 기존 객체 환각 탐지 방법을 종합적으로 벤치마킹한 결과, GLSim이 경쟁적인 기준선을 상당한 차이로 능가하는 우수한 탐지 성능을 달성함을 입증했습니다.


---

*Generated on 2025-09-24 01:23:07*