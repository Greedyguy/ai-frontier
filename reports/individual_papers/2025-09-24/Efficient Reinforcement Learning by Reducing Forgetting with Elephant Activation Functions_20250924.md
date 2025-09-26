<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:01:05.966071",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Catastrophic Forgetting",
    "Elephant Activation Functions",
    "Sparse Representations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Catastrophic Forgetting": 0.88,
    "Elephant Activation Functions": 0.92,
    "Sparse Representations": 0.8
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
        "rationale": "A fundamental concept in the paper, linking to a broad range of related topics in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Catastrophic Forgetting",
        "canonical": "Catastrophic Forgetting",
        "aliases": [
          "Forgetting"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus, connecting to studies on neural network memory and learning efficiency.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Elephant Activation Functions",
        "canonical": "Elephant Activation Functions",
        "aliases": [
          "Elephant Functions"
        ],
        "category": "unique_technical",
        "rationale": "A novel concept introduced in the paper, offering new insights into activation function design.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.92
      },
      {
        "surface": "Sparse Representations",
        "canonical": "Sparse Representations",
        "aliases": [
          "Sparse Outputs"
        ],
        "category": "specific_connectable",
        "rationale": "Important for understanding the impact of activation functions on neural network efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "algorithmic side",
      "training dynamics",
      "value-based algorithms"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Catastrophic Forgetting",
      "resolved_canonical": "Catastrophic Forgetting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Elephant Activation Functions",
      "resolved_canonical": "Elephant Activation Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Sparse Representations",
      "resolved_canonical": "Sparse Representations",
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

# Efficient Reinforcement Learning by Reducing Forgetting with Elephant Activation Functions

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19159.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19159](https://arxiv.org/abs/2509.19159)

## 🔗 유사한 논문
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG: Curriculum Unlearning Guided by the Forgetting Gradient]] (83.0% similar)
- [[2025-09-19/Don't Forget the Nonlinearity_ Unlocking Activation Functions in Efficient Fine-Tuning_20250919|Don't Forget the Nonlinearity: Unlocking Activation Functions in Efficient Fine-Tuning]] (82.1% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (81.3% similar)
- [[2025-09-19/Sample Efficient Experience Replay in Non-stationary Environments_20250919|Sample Efficient Experience Replay in Non-stationary Environments]] (81.2% similar)
- [[2025-09-22/Latent learning_ episodic memory complements parametric learning by enabling flexible reuse of experiences_20250922|Latent learning: episodic memory complements parametric learning by enabling flexible reuse of experiences]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Catastrophic Forgetting|Catastrophic Forgetting]], [[keywords/Sparse Representations|Sparse Representations]]
**⚡ Unique Technical**: [[keywords/Elephant Activation Functions|Elephant Activation Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19159v1 Announce Type: new 
Abstract: Catastrophic forgetting has remained a significant challenge for efficient reinforcement learning for decades (Ring 1994, Rivest and Precup 2003). While recent works have proposed effective methods to mitigate this issue, they mainly focus on the algorithmic side. Meanwhile, we do not fully understand what architectural properties of neural networks lead to catastrophic forgetting. This study aims to fill this gap by studying the role of activation functions in the training dynamics of neural networks and their impact on catastrophic forgetting in reinforcement learning setup. Our study reveals that, besides sparse representations, the gradient sparsity of activation functions also plays an important role in reducing forgetting. Based on this insight, we propose a new class of activation functions, elephant activation functions, that can generate both sparse outputs and sparse gradients. We show that by simply replacing classical activation functions with elephant activation functions in the neural networks of value-based algorithms, we can significantly improve the resilience of neural networks to catastrophic forgetting, thus making reinforcement learning more sample-efficient and memory-efficient.

## 📝 요약

이 연구는 강화 학습에서 발생하는 망각 문제를 해결하기 위해 신경망의 활성화 함수가 어떤 역할을 하는지 분석합니다. 기존 연구들이 주로 알고리즘 측면에 집중한 반면, 본 연구는 활성화 함수의 출력 및 기울기 희소성이 망각 감소에 중요한 역할을 한다는 점을 발견했습니다. 이를 바탕으로, 희소한 출력과 기울기를 생성할 수 있는 새로운 클래스의 활성화 함수인 'elephant 활성화 함수'를 제안합니다. 이 함수를 기존의 활성화 함수 대신 사용하면, 신경망의 망각 저항성을 크게 향상시켜 강화 학습의 샘플 및 메모리 효율성을 높일 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 재난적 망각은 효율적인 강화 학습에서 여전히 큰 도전 과제로 남아 있다.
- 2. 활성화 함수의 그래디언트 희소성이 망각 감소에 중요한 역할을 한다.
- 3. 새로운 클래스의 활성화 함수인 'elephant 활성화 함수'를 제안하여 망각 저항성을 향상시킨다.
- 4. elephant 활성화 함수를 사용하면 강화 학습의 샘플 효율성과 메모리 효율성을 크게 개선할 수 있다.
- 5. 기존 활성화 함수를 elephant 활성화 함수로 대체함으로써 신경망의 망각 저항성을 크게 향상시킬 수 있다.


---

*Generated on 2025-09-24 15:01:05*