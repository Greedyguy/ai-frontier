<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:00:49.945979",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Large Language Model",
    "PipelineRL",
    "On-policy Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Large Language Model": 0.83,
    "PipelineRL": 0.78,
    "On-policy Training": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational concept that connects with various advanced AI techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus and link to numerous NLP advancements.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.83
      },
      {
        "surface": "PipelineRL",
        "canonical": "PipelineRL",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "PipelineRL is a novel approach introduced in the paper, offering unique insights into RL efficiency.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "On-policy Training",
        "canonical": "On-policy Training",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "On-policy Training is crucial for understanding the data generation strategy in RL.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "PipelineRL",
      "resolved_canonical": "PipelineRL",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "On-policy Training",
      "resolved_canonical": "On-policy Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# PipelineRL: Faster On-policy Reinforcement Learning for Long Sequence Generatio

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19128.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19128](https://arxiv.org/abs/2509.19128)

## 🔗 유사한 논문
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (89.3% similar)
- [[2025-09-24/APRIL_ Active Partial Rollouts in Reinforcement Learning to tame long-tail generation_20250924|APRIL: Active Partial Rollouts in Reinforcement Learning to tame long-tail generation]] (88.2% similar)
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (86.9% similar)
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (86.4% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/On-policy Training|On-policy Training]]
**⚡ Unique Technical**: [[keywords/PipelineRL|PipelineRL]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19128v1 Announce Type: new 
Abstract: Reinforcement Learning (RL) is increasingly utilized to enhance the reasoning capabilities of Large Language Models (LLMs). However, effectively scaling these RL methods presents significant challenges, primarily due to the difficulty in maintaining high AI accelerator utilization without generating stale, off-policy data that harms common RL algorithms. This paper introduces PipelineRL, an approach designed to achieve a superior trade-off between hardware efficiency and data on-policyness for LLM training. PipelineRL employs concurrent asynchronous data generation and model training, distinguished by the novel in-flight weight updates. This mechanism allows the LLM generation engine to receive updated model weights with minimal interruption during the generation of token sequences, thereby maximizing both the accelerator utilization and the freshness of training data. Experiments conducted on long-form reasoning tasks using 128 H100 GPUs demonstrate that PipelineRL achieves approximately $\sim 2x$ faster learning compared to conventional RL baselines while maintaining highly on-policy training data. A scalable and modular open-source implementation of PipelineRL is also released as a key contribution.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 추론 능력을 강화하기 위해 강화 학습(RL)을 활용하는 방법을 다룹니다. 기존 RL 방법의 확장에는 AI 가속기의 효율적 활용과 오래된 데이터 생성 문제로 인한 어려움이 있습니다. 이를 해결하기 위해, 논문은 PipelineRL을 제안합니다. 이 방법은 동시 비동기 데이터 생성과 모델 훈련을 통해 하드웨어 효율성과 데이터의 최신성을 동시에 높입니다. 특히, 새로운 'in-flight' 가중치 업데이트 메커니즘을 도입하여, 토큰 시퀀스 생성 중에도 모델 가중치를 최신 상태로 유지합니다. 실험 결과, 128개의 H100 GPU를 사용한 장기 추론 작업에서 PipelineRL은 기존 RL 기준보다 약 2배 빠른 학습 속도를 보이며, 데이터의 최신성을 유지합니다. 또한, 확장 가능하고 모듈화된 오픈 소스 구현도 제공됩니다.

## 🎯 주요 포인트

- 1. PipelineRL은 대규모 언어 모델(LLM) 훈련을 위한 하드웨어 효율성과 데이터의 정책 준수성을 균형 있게 향상시키는 접근법을 제안합니다.
- 2. 이 방법은 동시 비동기 데이터 생성과 모델 훈련을 통해, 새로운 비행 중 가중치 업데이트 메커니즘을 도입하여 훈련 데이터의 신선도를 극대화합니다.
- 3. 128개의 H100 GPU를 사용한 실험에서 PipelineRL은 기존 강화 학습(RL) 기준보다 약 2배 빠른 학습 속도를 달성했습니다.
- 4. PipelineRL의 확장 가능하고 모듈화된 오픈 소스 구현이 주요 기여로 공개되었습니다.


---

*Generated on 2025-09-24 15:00:49*