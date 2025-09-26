---
keywords:
  - Large Language Model
  - Knowledge Infusion Scaling Law
  - Memory Collapse
  - Domain Knowledge
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19371
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:31:55.368538",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Knowledge Infusion Scaling Law",
    "Memory Collapse",
    "Domain Knowledge"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Knowledge Infusion Scaling Law": 0.8,
    "Memory Collapse": 0.78,
    "Domain Knowledge": 0.75
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
        "rationale": "This is a central concept in the paper, linking to many discussions on language model architectures and capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "knowledge infusion scaling law",
        "canonical": "Knowledge Infusion Scaling Law",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced by the paper, crucial for understanding the proposed methodology.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "memory collapse",
        "canonical": "Memory Collapse",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This term describes a specific failure mode in LLMs, which is key to the paper's analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "domain knowledge",
        "canonical": "Domain Knowledge",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding how domain-specific data impacts LLMs is crucial for linking to broader discussions on knowledge representation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "pretraining",
      "downstream performance",
      "catastrophic forgetting"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "knowledge infusion scaling law",
      "resolved_canonical": "Knowledge Infusion Scaling Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "memory collapse",
      "resolved_canonical": "Memory Collapse",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "domain knowledge",
      "resolved_canonical": "Domain Knowledge",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# How to inject knowledge efficiently? Knowledge Infusion Scaling Law for Pre-training Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19371.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19371](https://arxiv.org/abs/2509.19371)

## 🔗 유사한 논문
- [[2025-09-24/Experience Scaling_ Post-Deployment Evolution For Large Language Models_20250924|Experience Scaling: Post-Deployment Evolution For Large Language Models]] (85.3% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (85.2% similar)
- [[2025-09-25/Cognitive Load Limits in Large Language Models_ Benchmarking Multi-Hop Reasoning_20250925|Cognitive Load Limits in Large Language Models: Benchmarking Multi-Hop Reasoning]] (84.1% similar)
- [[2025-09-23/Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels_20250923|Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels]] (83.8% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Domain Knowledge|Domain Knowledge]]
**⚡ Unique Technical**: [[keywords/Knowledge Infusion Scaling Law|Knowledge Infusion Scaling Law]], [[keywords/Memory Collapse|Memory Collapse]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19371v1 Announce Type: cross 
Abstract: Large language models (LLMs) have attracted significant attention due to their impressive general capabilities across diverse downstream tasks. However, without domain-specific optimization, they often underperform on specialized knowledge benchmarks and even produce hallucination. Recent studies show that strategically infusing domain knowledge during pretraining can substantially improve downstream performance. A critical challenge lies in balancing this infusion trade-off: injecting too little domain-specific data yields insufficient specialization, whereas excessive infusion triggers catastrophic forgetting of previously acquired knowledge. In this work, we focus on the phenomenon of memory collapse induced by over-infusion. Through systematic experiments, we make two key observations, i.e. 1) Critical collapse point: each model exhibits a threshold beyond which its knowledge retention capabilities sharply degrade. 2) Scale correlation: these collapse points scale consistently with the model's size. Building on these insights, we propose a knowledge infusion scaling law that predicts the optimal amount of domain knowledge to inject into large LLMs by analyzing their smaller counterparts. Extensive experiments across different model sizes and pertaining token budgets validate both the effectiveness and generalizability of our scaling law.

## 📝 요약

대형 언어 모델(LLM)은 다양한 작업에서 뛰어난 성능을 보이지만, 특정 분야의 지식이 부족할 경우 전문 지식 벤치마크에서 성능이 저하되고 환각을 일으킬 수 있습니다. 본 연구는 사전 학습 단계에서 전략적으로 분야 지식을 주입하면 성능이 향상된다는 점을 확인했습니다. 그러나 과도한 지식 주입은 기존 지식의 망각을 초래할 수 있습니다. 우리는 과도한 주입으로 인한 기억 붕괴 현상에 주목하여, 1) 각 모델에는 지식 유지 능력이 급격히 저하되는 임계점이 존재하며, 2) 이러한 붕괴점은 모델 크기와 비례한다는 두 가지 주요 발견을 했습니다. 이를 바탕으로, 작은 모델을 분석하여 대형 LLM에 최적의 분야 지식 주입량을 예측하는 지식 주입 스케일링 법칙을 제안했습니다. 다양한 모델 크기와 토큰 예산에 대한 실험을 통해 이 법칙의 효과성과 일반성을 검증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 다양한 작업에서 뛰어난 성능을 보이지만, 특정 분야의 최적화가 없으면 전문 지식 벤치마크에서 성능이 저하될 수 있다.
- 2. 도메인 지식을 전략적으로 주입하면 다운스트림 성능을 크게 향상시킬 수 있지만, 과도한 주입은 기존 지식의 망각을 초래할 수 있다.
- 3. 메모리 붕괴 현상은 도메인 지식의 과도한 주입으로 인해 발생하며, 모델의 지식 유지 능력이 급격히 저하되는 임계 붕괴점이 존재한다.
- 4. 임계 붕괴점은 모델의 크기와 일관되게 비례하며, 이를 바탕으로 최적의 도메인 지식 주입량을 예측하는 지식 주입 스케일링 법칙을 제안한다.
- 5. 다양한 모델 크기와 토큰 예산에 대한 실험을 통해 제안된 스케일링 법칙의 효과성과 일반화 가능성을 입증하였다.


---

*Generated on 2025-09-25 15:31:55*