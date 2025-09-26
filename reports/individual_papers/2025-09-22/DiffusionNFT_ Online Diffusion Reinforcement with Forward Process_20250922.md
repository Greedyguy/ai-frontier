---
keywords:
  - Diffusion Negative-aware FineTuning
  - Online Reinforcement Learning
  - Flow Matching
  - Classifier-Free Guidance
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16117
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:29:04.713653",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Negative-aware FineTuning",
    "Online Reinforcement Learning",
    "Flow Matching",
    "Classifier-Free Guidance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Negative-aware FineTuning": 0.85,
    "Online Reinforcement Learning": 0.78,
    "Flow Matching": 0.82,
    "Classifier-Free Guidance": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DiffusionNFT",
        "canonical": "Diffusion Negative-aware FineTuning",
        "aliases": [
          "DiffusionNFT"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, specifically for optimizing diffusion models, and is central to the paper's contributions.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Online Reinforcement Learning",
        "canonical": "Online Reinforcement Learning",
        "aliases": [
          "Online RL"
        ],
        "category": "broad_technical",
        "rationale": "Online reinforcement learning is a fundamental concept in the paper, linking it to broader machine learning contexts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Flow Matching",
        "canonical": "Flow Matching",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Flow matching is a key technique used in the paper to optimize the forward process of diffusion models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Classifier-Free Guidance",
        "canonical": "Classifier-Free Guidance",
        "aliases": [
          "CFG"
        ],
        "category": "specific_connectable",
        "rationale": "The paper discusses improvements over methods that require classifier-free guidance, making it a relevant concept for linking.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "likelihood estimation",
      "sampling trajectories"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DiffusionNFT",
      "resolved_canonical": "Diffusion Negative-aware FineTuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Online Reinforcement Learning",
      "resolved_canonical": "Online Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Flow Matching",
      "resolved_canonical": "Flow Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Classifier-Free Guidance",
      "resolved_canonical": "Classifier-Free Guidance",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# DiffusionNFT: Online Diffusion Reinforcement with Forward Process

**Korean Title:** DiffusionNFT: 순방향 프로세스를 통한 온라인 확산 강화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16117.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16117](https://arxiv.org/abs/2509.16117)

## 🔗 유사한 논문
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (84.1% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (83.9% similar)
- [[2025-09-18/FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (83.9% similar)
- [[2025-09-19/FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL: Matching Reward Distributions for LLM Reasoning]] (83.8% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Online Reinforcement Learning|Online Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Flow Matching|Flow Matching]], [[keywords/Classifier-Free Guidance|Classifier-Free Guidance]]
**⚡ Unique Technical**: [[keywords/Diffusion Negative-aware FineTuning|Diffusion Negative-aware FineTuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16117v1 Announce Type: cross 
Abstract: Online reinforcement learning (RL) has been central to post-training language models, but its extension to diffusion models remains challenging due to intractable likelihoods. Recent works discretize the reverse sampling process to enable GRPO-style training, yet they inherit fundamental drawbacks, including solver restrictions, forward-reverse inconsistency, and complicated integration with classifier-free guidance (CFG). We introduce Diffusion Negative-aware FineTuning (DiffusionNFT), a new online RL paradigm that optimizes diffusion models directly on the forward process via flow matching. DiffusionNFT contrasts positive and negative generations to define an implicit policy improvement direction, naturally incorporating reinforcement signals into the supervised learning objective. This formulation enables training with arbitrary black-box solvers, eliminates the need for likelihood estimation, and requires only clean images rather than sampling trajectories for policy optimization. DiffusionNFT is up to $25\times$ more efficient than FlowGRPO in head-to-head comparisons, while being CFG-free. For instance, DiffusionNFT improves the GenEval score from 0.24 to 0.98 within 1k steps, while FlowGRPO achieves 0.95 with over 5k steps and additional CFG employment. By leveraging multiple reward models, DiffusionNFT significantly boosts the performance of SD3.5-Medium in every benchmark tested.

## 🔍 Abstract (한글 번역)

arXiv:2509.16117v1 발표 유형: 교차  
초록: 온라인 강화 학습(RL)은 사후 훈련 언어 모델에 중심적이었지만, 확산 모델로의 확장은 난해한 가능성 때문에 여전히 도전적입니다. 최근 연구들은 GRPO 스타일의 훈련을 가능하게 하기 위해 역 샘플링 과정을 이산화하지만, 이들은 기본적인 단점들을 물려받습니다. 여기에는 해석기 제한, 순방향-역방향 불일치, 분류기 없는 안내(CFG)와의 복잡한 통합이 포함됩니다. 우리는 확산 부정 인식 미세 조정(DiffusionNFT)을 소개합니다. 이는 흐름 매칭을 통해 순방향 과정에서 확산 모델을 직접 최적화하는 새로운 온라인 RL 패러다임입니다. DiffusionNFT는 긍정적 및 부정적 생성을 대조하여 암묵적인 정책 개선 방향을 정의하며, 강화 신호를 지도 학습 목표에 자연스럽게 통합합니다. 이 공식화는 임의의 블랙박스 해석기를 사용한 훈련을 가능하게 하고, 가능성 추정을 필요로 하지 않으며, 정책 최적화를 위한 샘플링 경로 대신 깨끗한 이미지만을 필요로 합니다. DiffusionNFT는 FlowGRPO와의 직접 비교에서 최대 25배 더 효율적이며, CFG가 필요하지 않습니다. 예를 들어, DiffusionNFT는 GenEval 점수를 1,000 단계 내에 0.24에서 0.98로 향상시키는 반면, FlowGRPO는 5,000 단계 이상과 추가적인 CFG 사용으로 0.95를 달성합니다. 여러 보상 모델을 활용하여, DiffusionNFT는 테스트된 모든 벤치마크에서 SD3.5-Medium의 성능을 크게 향상시킵니다.

## 📝 요약

이 논문은 확산 모델에 온라인 강화 학습(RL)을 적용하는 새로운 패러다임인 Diffusion Negative-aware FineTuning(DiffusionNFT)을 제안합니다. 기존 방법들은 역방향 샘플링 과정의 불연속성과 복잡한 통합 문제를 겪지만, DiffusionNFT는 흐름 매칭을 통해 전방 과정에서 직접 최적화하여 이러한 문제를 해결합니다. 이 방법은 강화 신호를 지도 학습 목표에 자연스럽게 통합하며, 임의의 블랙박스 솔버와 함께 사용할 수 있어 효율적입니다. DiffusionNFT는 FlowGRPO보다 최대 25배 효율적이며, GenEval 점수를 1,000단계 내에 0.24에서 0.98로 향상시킵니다. 다양한 보상 모델을 활용하여 SD3.5-Medium의 성능을 모든 테스트에서 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. DiffusionNFT는 역 샘플링 과정의 제한을 극복하고, 흐름 매칭을 통해 전방 과정에서 확산 모델을 직접 최적화하는 새로운 온라인 강화 학습 패러다임을 제안합니다.
- 2. DiffusionNFT는 긍정 및 부정 생성물을 대조하여 암묵적인 정책 개선 방향을 정의하고, 강화 신호를 지도 학습 목표에 자연스럽게 통합합니다.
- 3. DiffusionNFT는 임의의 블랙박스 솔버와의 통합이 가능하며, 가능도 추정이 필요 없고 정책 최적화를 위한 샘플링 경로 대신 깨끗한 이미지만 필요합니다.
- 4. DiffusionNFT는 FlowGRPO에 비해 최대 25배 더 효율적이며, GenEval 점수를 1k 스텝 내에서 0.24에서 0.98로 향상시킵니다.
- 5. 여러 보상 모델을 활용하여 DiffusionNFT는 모든 테스트된 벤치마크에서 SD3.5-Medium의 성능을 크게 향상시킵니다.


---

*Generated on 2025-09-23 09:29:04*