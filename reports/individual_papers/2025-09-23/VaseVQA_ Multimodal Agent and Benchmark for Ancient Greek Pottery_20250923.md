---
keywords:
  - Multimodal Learning
  - VaseVQA
  - Supervised Fine-Tuning and Reinforcement Learning System
  - Historical Attribution
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17191
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:40:53.866091",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "VaseVQA",
    "Supervised Fine-Tuning and Reinforcement Learning System",
    "Historical Attribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "VaseVQA": 0.78,
    "Supervised Fine-Tuning and Reinforcement Learning System": 0.7,
    "Historical Attribution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Agent",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal System"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the trending concept of integrating multiple data types for enhanced learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "VaseVQA",
        "canonical": "VaseVQA",
        "aliases": [
          "Vase Visual Question Answering"
        ],
        "category": "unique_technical",
        "rationale": "Represents a unique benchmark specifically designed for ancient Greek pottery analysis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "SFT-then-RL system",
        "canonical": "Supervised Fine-Tuning and Reinforcement Learning System",
        "aliases": [
          "SFT-RL"
        ],
        "category": "unique_technical",
        "rationale": "Describes a novel approach combining supervised and reinforcement learning for model optimization.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Historical Attribution",
        "canonical": "Historical Attribution",
        "aliases": [
          "Artifact Attribution"
        ],
        "category": "specific_connectable",
        "rationale": "Focuses on the task of determining the origin and period of cultural artifacts.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "supervision",
      "performance gaps"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Agent",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "VaseVQA",
      "resolved_canonical": "VaseVQA",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SFT-then-RL system",
      "resolved_canonical": "Supervised Fine-Tuning and Reinforcement Learning System",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Historical Attribution",
      "resolved_canonical": "Historical Attribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# VaseVQA: Multimodal Agent and Benchmark for Ancient Greek Pottery

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17191.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17191](https://arxiv.org/abs/2509.17191)

## 🔗 유사한 논문
- [[2025-09-23/Seeing Culture_ A Benchmark for Visual Reasoning and Grounding_20250923|Seeing Culture: A Benchmark for Visual Reasoning and Grounding]] (82.2% similar)
- [[2025-09-23/When Big Models Train Small Ones_ Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs_20250923|When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs]] (81.7% similar)
- [[2025-09-23/SD-VLM_ Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models_20250923|SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models]] (81.7% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (81.2% similar)
- [[2025-09-23/VStyle_ A Benchmark for Voice Style Adaptation with Spoken Instructions_20250923|VStyle: A Benchmark for Voice Style Adaptation with Spoken Instructions]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Historical Attribution|Historical Attribution]]
**⚡ Unique Technical**: [[keywords/VaseVQA|VaseVQA]], [[keywords/Supervised Fine-Tuning and Reinforcement Learning System|Supervised Fine-Tuning and Reinforcement Learning System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17191v1 Announce Type: cross 
Abstract: Analyzing cultural-heritage artifacts remains challenging for MLLMs: general models lack domain expertise, and SFT often overfits superficial patterns, yielding brittle reasoning for authentication and historical attribution. This raises the question of how to equip MLLMs with robust, expert-level reasoning for ancient Greek pottery. We present VaseVL, an SFT-then-RL system that turns evaluation into supervision: we construct a taxonomy of question types, probe the SFT model to localize type-specific performance gaps, and optimize with type-conditioned, compositionality-oriented rewards targeting those gaps. We also release VaseVQA, a comprehensive benchmark of 31,773 images designed to probe deep understanding. Experiments show state-of-the-art results on style classification and historical attribution with marked gains in compositional robustness over SFT-only baselines, validating diagnosis-guided, taxonomy-conditioned reward engineering and providing a reusable resource for future research. Code and dataset will be available at https://github.com/AIGeeksGroup/VaseVQA.

## 📝 요약

이 논문은 고대 그리스 도자기의 분석을 위한 MLLM의 전문적 추론 능력을 강화하는 방법을 제안합니다. VaseVL 시스템은 SFT-then-RL 접근법을 사용하여 질문 유형의 분류 체계를 구축하고, 성능 격차를 식별하여 이를 보완하는 보상 체계를 최적화합니다. 또한, 31,773개의 이미지로 구성된 VaseVQA 벤치마크를 공개하여 심층 이해를 평가합니다. 실험 결과, 스타일 분류와 역사적 귀속에서 최첨단 성과를 보이며, SFT만을 사용한 모델에 비해 조합적 견고성이 향상되었습니다. 이 연구는 향후 연구를 위한 재사용 가능한 자원을 제공합니다.

## 🎯 주요 포인트

- 1. MLLMs는 일반적인 모델로는 문화유산 유물 분석에 어려움을 겪으며, SFT는 피상적인 패턴에 과적합되어 신뢰성 있는 추론을 제공하지 못한다.
- 2. VaseVL 시스템은 SFT-then-RL 접근법을 통해 평가를 감독으로 전환하여 고대 그리스 도자기에 대한 전문적인 수준의 추론을 가능하게 한다.
- 3. VaseVQA는 31,773개의 이미지를 포함한 포괄적인 벤치마크로, 깊이 있는 이해를 평가하기 위해 설계되었다.
- 4. 실험 결과, VaseVL은 스타일 분류 및 역사적 귀속에서 최첨단 성과를 보였으며, SFT만 사용한 기준선에 비해 조합적 견고성이 크게 향상되었다.
- 5. 연구의 코드와 데이터셋은 https://github.com/AIGeeksGroup/VaseVQA에서 제공될 예정이다.


---

*Generated on 2025-09-24 03:40:53*