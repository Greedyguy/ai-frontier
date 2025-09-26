---
keywords:
  - Vision-Language Model
  - Differentiable Token Pruning
  - Attention Mechanism
  - Gumbel Softmax
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.12594
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:18:20.256022",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Differentiable Token Pruning",
    "Attention Mechanism",
    "Gumbel Softmax"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Differentiable Token Pruning": 0.8,
    "Attention Mechanism": 0.82,
    "Gumbel Softmax": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-language-action models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLA models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language-action models represent an evolution of multimodal learning, crucial for linking to broader vision-language research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Differentiable token pruning",
        "canonical": "Differentiable Token Pruning",
        "aliases": [
          "token pruning"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique specific to the paper, enhancing connectivity in token management research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Attention-based computation",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention computation"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are central to the discussed models, facilitating connections to related neural network research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Gumbel softmax",
        "canonical": "Gumbel Softmax",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Gumbel softmax is a specific technique used in differentiable selection, linking to probabilistic model research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "LightVLA",
      "LIBERO benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-language-action models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Differentiable token pruning",
      "resolved_canonical": "Differentiable Token Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Attention-based computation",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Gumbel softmax",
      "resolved_canonical": "Gumbel Softmax",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12594.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.12594](https://arxiv.org/abs/2509.12594)

## 🔗 유사한 논문
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (86.7% similar)
- [[2025-09-22/Walk and Read Less_ Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning_20250922|Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning]] (85.9% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (85.7% similar)
- [[2025-09-19/ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (85.0% similar)
- [[2025-09-19/CollabVLA_ Self-Reflective Vision-Language-Action Model Dreaming Together with Human_20250919|CollabVLA: Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Gumbel Softmax|Gumbel Softmax]]
**⚡ Unique Technical**: [[keywords/Differentiable Token Pruning|Differentiable Token Pruning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12594v2 Announce Type: replace-cross 
Abstract: We present LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens. LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously. Notably, LightVLA requires no heuristic magic numbers and introduces no additional trainable parameters, making it compatible with modern inference frameworks. Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark, achieving higher success rates with substantially reduced computational overhead. Specifically, LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate. Meanwhile, we also investigate the learnable query-based token pruning method LightVLA* with additional trainable parameters, which also achieves satisfactory performance. Our work reveals that as VLA pursues optimal performance, LightVLA spontaneously learns to prune tokens from a performance-driven perspective. To the best of our knowledge, LightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance, marking a significant step toward more efficient, powerful and practical real-time robotic systems.

## 📝 요약

LightVLA는 비전-언어-행동(VLA) 모델을 위한 차별화된 토큰 가지치기 프레임워크로, 리소스가 제한된 플랫폼에서 VLA 모델의 효율성을 높입니다. 이 모델은 시각 토큰의 중요성을 동적으로 평가하고, Gumbel softmax를 사용해 차별화된 토큰 선택을 가능하게 합니다. 이를 통해 불필요한 토큰을 가지치기하면서도 중요한 정보는 보존하여 성능과 효율성을 동시에 개선합니다. LightVLA는 추가적인 학습 매개변수 없이 현대적 추론 프레임워크와 호환되며, LIBERO 벤치마크에서 기존 모델보다 높은 성공률과 낮은 계산 비용을 보였습니다. FLOPs와 지연 시간을 각각 59.1%와 38.2% 줄이면서도 작업 성공률을 2.6% 향상시켰습니다. 이 연구는 VLA 작업에 적응형 시각 토큰 가지치기를 적용한 최초의 사례로, 실시간 로봇 시스템의 효율성과 성능을 크게 향상시키는 데 기여합니다.

## 🎯 주요 포인트

- 1. LightVLA는 VLA 모델의 시각적 토큰을 성능 기반으로 적응적으로 가지치기하여 효율성과 성능을 동시에 향상시킵니다.
- 2. 이 프레임워크는 Gumbel softmax를 사용하여 차별 가능한 토큰 선택을 가능하게 하며, 추가적인 학습 가능한 매개변수를 도입하지 않습니다.
- 3. 실험 결과, LightVLA는 LIBERO 벤치마크에서 다양한 작업에 대해 기존 VLA 모델과 토큰 가지치기 방법을 능가하며, 계산 오버헤드를 크게 줄이면서 성공률을 높입니다.
- 4. LightVLA는 FLOPs와 지연 시간을 각각 59.1%와 38.2% 줄이면서 작업 성공률을 2.6% 향상시킵니다.
- 5. LightVLA는 VLA 작업에 적응형 시각적 토큰 가지치기를 적용한 최초의 연구로, 실시간 로봇 시스템의 효율성과 성능을 향상시키는 중요한 진전을 나타냅니다.


---

*Generated on 2025-09-24 04:18:20*