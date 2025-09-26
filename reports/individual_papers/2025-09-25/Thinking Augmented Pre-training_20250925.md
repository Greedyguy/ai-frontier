---
keywords:
  - Large Language Model
  - Thinking Augmented Pre-Training
  - Reasoning Benchmarks
  - Data Efficiency
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20186
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:02:01.043586",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Thinking Augmented Pre-Training",
    "Reasoning Benchmarks",
    "Data Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Thinking Augmented Pre-Training": 0.92,
    "Reasoning Benchmarks": 0.78,
    "Data Efficiency": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology and improvements, making them crucial for linking related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Thinking Augmented Pre-Training",
        "canonical": "Thinking Augmented Pre-Training",
        "aliases": [
          "TPT"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel methodology introduced by the paper, essential for understanding the specific contributions of the research.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "Reasoning Benchmarks",
        "canonical": "Reasoning Benchmarks",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Reasoning benchmarks are used to evaluate the effectiveness of the proposed method, linking it to performance metrics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data Efficiency",
        "canonical": "Data Efficiency",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Improving data efficiency is a key outcome of the research, relevant for linking to optimization studies in LLM training.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "methodology",
      "performance",
      "training data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Thinking Augmented Pre-Training",
      "resolved_canonical": "Thinking Augmented Pre-Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Reasoning Benchmarks",
      "resolved_canonical": "Reasoning Benchmarks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data Efficiency",
      "resolved_canonical": "Data Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Thinking Augmented Pre-training

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20186.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20186](https://arxiv.org/abs/2509.20186)

## 🔗 유사한 논문
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (88.5% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (86.5% similar)
- [[2025-09-23/Language Modeling with Learned Meta-Tokens_20250923|Language Modeling with Learned Meta-Tokens]] (85.8% similar)
- [[2025-09-23/L-MTP_ Leap Multi-Token Prediction Beyond Adjacent Context for Large Language Models_20250923|L-MTP: Leap Multi-Token Prediction Beyond Adjacent Context for Large Language Models]] (84.9% similar)
- [[2025-09-22/Tag&Tab_ Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack_20250922|Tag&Tab: Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reasoning Benchmarks|Reasoning Benchmarks]], [[keywords/Data Efficiency|Data Efficiency]]
**⚡ Unique Technical**: [[keywords/Thinking Augmented Pre-Training|Thinking Augmented Pre-Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20186v1 Announce Type: cross 
Abstract: This paper introduces a simple and scalable approach to improve the data efficiency of large language model (LLM) training by augmenting existing text data with thinking trajectories. The compute for pre-training LLMs has been growing at an unprecedented rate, while the availability of high-quality data remains limited. Consequently, maximizing the utility of available data constitutes a significant research challenge. A primary impediment is that certain high-quality tokens are difficult to learn given a fixed model capacity, as the underlying rationale for a single token can be exceptionally complex and deep. To address this issue, we propose Thinking augmented Pre-Training (TPT), a universal methodology that augments text with automatically generated thinking trajectories. Such augmentation effectively increases the volume of the training data and makes high-quality tokens more learnable through step-by-step reasoning and decomposition. We apply TPT across diverse training configurations up to $100$B tokens, encompassing pre-training with both constrained and abundant data, as well as mid-training from strong open-source checkpoints. Experimental results indicate that our method substantially improves the performance of LLMs across various model sizes and families. Notably, TPT enhances the data efficiency of LLM pre-training by a factor of $3$. For a $3$B parameter model, it improves the post-training performance by over $10\%$ on several challenging reasoning benchmarks.

## 📝 요약

이 논문은 대형 언어 모델(LLM) 훈련의 데이터 효율성을 개선하기 위해 기존 텍스트 데이터에 사고 경로를 추가하는 간단하고 확장 가능한 방법을 제안합니다. 고품질 데이터의 제한된 가용성 문제를 해결하기 위해 'Thinking augmented Pre-Training (TPT)' 방법론을 도입하여 자동 생성된 사고 경로로 텍스트를 보강합니다. 이를 통해 훈련 데이터의 양을 효과적으로 증가시키고, 복잡한 고품질 토큰을 단계별 추론과 분해를 통해 학습 가능하게 만듭니다. 다양한 훈련 설정에서 TPT를 적용한 결과, LLM의 성능이 크게 향상되었으며, 데이터 효율성이 3배 증가했습니다. 특히, 3B 파라미터 모델에서는 여러 어려운 추론 벤치마크에서 훈련 후 성능이 10% 이상 개선되었습니다.

## 🎯 주요 포인트

- 1. 본 논문은 기존 텍스트 데이터에 사고 경로를 추가하여 대형 언어 모델(LLM) 훈련의 데이터 효율성을 개선하는 방법을 제안합니다.
- 2. Thinking augmented Pre-Training (TPT)은 자동 생성된 사고 경로를 통해 텍스트를 보강하여 훈련 데이터의 양을 효과적으로 증가시키고, 고품질 토큰을 단계별 추론과 분해를 통해 더 쉽게 학습할 수 있도록 합니다.
- 3. TPT는 다양한 훈련 구성에서 적용되며, 실험 결과 LLM의 성능을 모델 크기와 계열에 걸쳐 크게 향상시킵니다.
- 4. TPT는 LLM 사전 훈련의 데이터 효율성을 3배 향상시키며, 3B 파라미터 모델의 경우 여러 어려운 추론 벤치마크에서 훈련 후 성능을 10% 이상 개선합니다.


---

*Generated on 2025-09-25 17:02:01*