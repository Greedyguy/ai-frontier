---
keywords:
  - Large Language Model
  - StableUN
  - Relearning Attacks
  - Feedback-Guided Optimization
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20230
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:03:36.126229",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "StableUN",
    "Relearning Attacks",
    "Feedback-Guided Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "StableUN": 0.8,
    "Relearning Attacks": 0.78,
    "Feedback-Guided Optimization": 0.77
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
        "rationale": "Central to the paper's focus on unlearning methods, connecting with a wide range of related research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "StableUN",
        "canonical": "StableUN",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents the novel framework introduced in the paper, essential for understanding the proposed solution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Relearning Attacks",
        "canonical": "Relearning Attacks",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights a specific threat addressed by the paper, crucial for discussions on model security.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Feedback-Guided Optimization",
        "canonical": "Feedback-Guided Optimization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Describes the optimization approach used, linking to broader optimization and learning strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "StableUN",
      "resolved_canonical": "StableUN",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Relearning Attacks",
      "resolved_canonical": "Relearning Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Feedback-Guided Optimization",
      "resolved_canonical": "Feedback-Guided Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Beyond Sharp Minima: Robust LLM Unlearning via Feedback-Guided Multi-Point Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20230.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20230](https://arxiv.org/abs/2509.20230)

## 🔗 유사한 논문
- [[2025-09-23/SUA_ Stealthy Multimodal Large Language Model Unlearning Attack_20250923|SUA: Stealthy Multimodal Large Language Model Unlearning Attack]] (88.4% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (87.0% similar)
- [[2025-09-23/SafeEraser_ Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning_20250923|SafeEraser: Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning]] (87.0% similar)
- [[2025-09-22/Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models_20250922|Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models]] (87.0% similar)
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG: Curriculum Unlearning Guided by the Forgetting Gradient]] (86.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Feedback-Guided Optimization|Feedback-Guided Optimization]]
**⚡ Unique Technical**: [[keywords/StableUN|StableUN]], [[keywords/Relearning Attacks|Relearning Attacks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20230v1 Announce Type: cross 
Abstract: Current LLM unlearning methods face a critical security vulnerability that undermines their fundamental purpose: while they appear to successfully remove sensitive or harmful knowledge, this ``forgotten" information remains precariously recoverable through relearning attacks. We identify that the root cause is that conventional methods optimizing the forgetting loss at individual data points will drive model parameters toward sharp minima in the loss landscape. In these unstable regions, even minimal parameter perturbations can drastically alter the model's behaviors. Consequently, relearning attacks exploit this vulnerability by using just a few fine-tuning samples to navigate the steep gradients surrounding these unstable regions, thereby rapidly recovering knowledge that was supposedly erased. This exposes a critical robustness gap between apparent unlearning and actual knowledge removal. To address this issue, we propose StableUN, a bi-level feedback-guided optimization framework that explicitly seeks more stable parameter regions via neighborhood-aware optimization. It integrates forgetting feedback, which uses adversarial perturbations to probe parameter neighborhoods, with remembering feedback to preserve model utility, aligning the two objectives through gradient projection. Experiments on WMDP and MUSE benchmarks demonstrate that our method is significantly more robust against both relearning and jailbreaking attacks while maintaining competitive utility performance.

## 📝 요약

현재의 대규모 언어 모델(LLM) 잊기 방법은 민감하거나 유해한 정보를 제거하는 데 성공한 것처럼 보이지만, 재학습 공격을 통해 해당 정보를 쉽게 복구할 수 있는 보안 취약점을 가지고 있습니다. 이는 개별 데이터 포인트에서 잊기 손실을 최적화하는 기존 방법이 모델 매개변수를 불안정한 손실 최소값으로 유도하기 때문입니다. 이러한 불안정한 영역에서는 작은 매개변수 변화만으로도 모델의 행동이 크게 변할 수 있습니다. 이를 해결하기 위해, 우리는 안정적인 매개변수 영역을 탐색하는 StableUN이라는 이중 피드백 기반 최적화 프레임워크를 제안합니다. 이 방법은 적대적 교란을 사용하여 매개변수 주변을 탐색하는 잊기 피드백과 모델 유용성을 유지하는 기억 피드백을 통합하여 두 목표를 정렬합니다. WMDP와 MUSE 벤치마크 실험에서 우리의 방법은 재학습 및 탈옥 공격에 대해 더 높은 견고성을 보이면서도 경쟁력 있는 유용성을 유지함을 입증했습니다.

## 🎯 주요 포인트

- 1. 기존 LLM 잊기 방법은 민감하거나 유해한 정보를 제거하는 데 실패하여 재학습 공격에 취약합니다.
- 2. 잊기 손실을 개별 데이터 포인트에서 최적화하는 기존 방법은 모델 매개변수를 불안정한 손실 지형의 급격한 최소값으로 유도합니다.
- 3. 재학습 공격은 이러한 불안정한 지역의 급격한 기울기를 이용하여 소수의 미세 조정 샘플로 잊혀진 지식을 빠르게 회복합니다.
- 4. StableUN은 이 문제를 해결하기 위해 이웃 인식 최적화를 통해 더 안정적인 매개변수 지역을 찾는 이중 피드백 기반 최적화 프레임워크를 제안합니다.
- 5. 실험 결과, StableUN은 재학습 및 탈옥 공격에 대해 더 강력하며 경쟁력 있는 유틸리티 성능을 유지합니다.


---

*Generated on 2025-09-25 16:03:36*