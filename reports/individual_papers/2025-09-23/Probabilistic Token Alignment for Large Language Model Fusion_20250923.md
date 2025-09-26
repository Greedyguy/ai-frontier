---
keywords:
  - Large Language Model
  - Probabilistic Token Alignment
  - Optimal Transport
  - Distribution Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17276
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:49:55.108228",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Probabilistic Token Alignment",
    "Optimal Transport",
    "Distribution Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Probabilistic Token Alignment": 0.8,
    "Optimal Transport": 0.78,
    "Distribution Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Key concept in the paper, linking to existing work on language models.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Probabilistic Token Alignment",
        "canonical": "Probabilistic Token Alignment",
        "aliases": [
          "PTA",
          "PTA-LLM"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for token alignment in model fusion.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optimal Transport",
        "canonical": "Optimal Transport",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Connects to mathematical methods used in distribution learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Distribution Learning",
        "canonical": "Distribution Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the proposed method's theoretical foundation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "model fusion",
      "vocabulary alignment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Probabilistic Token Alignment",
      "resolved_canonical": "Probabilistic Token Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Optimal Transport",
      "resolved_canonical": "Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Distribution Learning",
      "resolved_canonical": "Distribution Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Probabilistic Token Alignment for Large Language Model Fusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17276.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17276](https://arxiv.org/abs/2509.17276)

## 🔗 유사한 논문
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (88.2% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (85.0% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (84.8% similar)
- [[2025-09-23/LifeAlign_ Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization_20250923|LifeAlign: Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization]] (84.3% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Optimal Transport|Optimal Transport]], [[keywords/Distribution Learning|Distribution Learning]]
**⚡ Unique Technical**: [[keywords/Probabilistic Token Alignment|Probabilistic Token Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17276v1 Announce Type: cross 
Abstract: Training large language models (LLMs) from scratch can yield models with unique functionalities and strengths, but it is costly and often leads to redundant capabilities. A more cost-effective alternative is to fuse existing pre-trained LLMs with different architectures into a more powerful model. However, a key challenge in existing model fusion is their dependence on manually predefined vocabulary alignment, which may not generalize well across diverse contexts, leading to performance degradation in several evaluation. To solve this, we draw inspiration from distribution learning and propose the probabilistic token alignment method as a general and soft mapping for alignment, named as PTA-LLM. Our approach innovatively reformulates token alignment into a classic mathematical problem: optimal transport, seamlessly leveraging distribution-aware learning to facilitate more coherent model fusion. Apart from its inherent generality, PTA-LLM exhibits interpretability from a distributional perspective, offering insights into the essence of the token alignment. Empirical results demonstrate that probabilistic token alignment enhances the target model's performance across multiple capabilities. Our code is avaliable at https://runjia.tech/neurips_pta-llm/.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 처음부터 훈련하는 대신, 기존의 사전 훈련된 LLM을 결합하여 더 강력한 모델을 만드는 방법을 제안합니다. 기존 모델 결합의 문제점인 수동적 어휘 정렬의 한계를 극복하기 위해, 저자들은 확률적 토큰 정렬(PTA-LLM) 방법을 제안합니다. 이는 최적 수송 문제를 활용하여 더 일관된 모델 결합을 가능하게 합니다. PTA-LLM은 다양한 기능에서 모델의 성능을 향상시키며, 분포 관점에서 해석 가능한 장점을 제공합니다. 실험 결과, 제안된 방법이 여러 평가에서 목표 모델의 성능을 향상시킴을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)을 처음부터 훈련하는 것은 독특한 기능과 강점을 가진 모델을 만들 수 있지만 비용이 많이 들고 중복된 기능을 초래할 수 있습니다.
- 2. 기존의 사전 훈련된 LLM을 결합하여 더 강력한 모델을 만드는 것이 비용 효율적인 대안입니다.
- 3. 기존 모델 결합의 주요 문제는 수동으로 정의된 어휘 정렬에 의존하여 다양한 맥락에서 일반화되지 못하고 성능 저하를 초래할 수 있다는 점입니다.
- 4. 우리는 확률적 토큰 정렬 방법(PTA-LLM)을 제안하여 최적 수송 문제로 토큰 정렬을 재구성하고, 분포 인식 학습을 활용하여 모델 결합을 개선합니다.
- 5. 실험 결과, 확률적 토큰 정렬은 여러 기능에서 대상 모델의 성능을 향상시킵니다.


---

*Generated on 2025-09-23 23:49:55*