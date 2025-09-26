---
keywords:
  - Vision-Language Model
  - Backdoor Attacks
  - Self-supervised Learning
  - Prompt Tuning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2502.19269
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:17:24.531844",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Backdoor Attacks",
    "Self-supervised Learning",
    "Prompt Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.8,
    "Backdoor Attacks": 0.78,
    "Self-supervised Learning": 0.77,
    "Prompt Tuning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on CLIP and backdoor defenses, linking to recent trends in multimodal learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Backdoor Attacks",
        "canonical": "Backdoor Attacks",
        "aliases": [
          "Backdoor Threats",
          "Poisoning Attacks"
        ],
        "category": "unique_technical",
        "rationale": "Backdoor Attacks are a specific threat addressed by the proposed method, crucial for understanding the paper's contribution.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive Learning is used in the paper to invert backdoor triggers, connecting to broader self-supervised learning techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Prompt Tuning",
        "canonical": "Prompt Tuning",
        "aliases": [
          "Text Prompt Optimization"
        ],
        "category": "unique_technical",
        "rationale": "Prompt Tuning is a novel method proposed in the paper, directly related to modifying model decision boundaries.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "fine-tuning",
      "model parameters",
      "clean accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Backdoor Attacks",
      "resolved_canonical": "Backdoor Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Prompt Tuning",
      "resolved_canonical": "Prompt Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Neural Antidote: Class-Wise Prompt Tuning for Purifying Backdoors in CLIP

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2502.19269.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2502.19269](https://arxiv.org/abs/2502.19269)

## 🔗 유사한 논문
- [[2025-09-23/Test-Time Multimodal Backdoor Detection by Contrastive Prompting_20250923|Test-Time Multimodal Backdoor Detection by Contrastive Prompting]] (92.1% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (85.3% similar)
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (85.2% similar)
- [[2025-09-23/Rethinking Backdoor Detection Evaluation for Language Models_20250923|Rethinking Backdoor Detection Evaluation for Language Models]] (84.7% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Backdoor Attacks|Backdoor Attacks]], [[keywords/Prompt Tuning|Prompt Tuning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.19269v2 Announce Type: replace 
Abstract: While pre-trained Vision-Language Models (VLMs) such as CLIP exhibit impressive representational capabilities for multimodal data, recent studies have revealed their vulnerability to backdoor attacks. To alleviate the threat, existing defense strategies primarily focus on fine-tuning the entire suspicious model. However, the substantial model parameters increase the difficulty of reaching a stable and consistent optimization direction, limiting their resistance against state-of-the-art attacks and often resulting in a degradation of clean accuracy. To address this challenge, we propose Class-wise Backdoor Prompt Tuning (CBPT), an efficient and effective defense mechanism that operates on text prompts to indirectly purify poisoned CLIP. Specifically, we first employ the advanced contrastive learning via carefully crafted positive and negative samples, to effectively invert the backdoor triggers that are potentially adopted by the attacker. Once the dummy trigger is established, we leverage three well-designed loss functions to optimize these class-wise text prompts, modifying the model's decision boundary and further reclassifying the feature regions affected by backdoor triggers. Extensive experiments demonstrate that CBPT significantly mitigates backdoor threats while preserving model utility, e.g. an average Clean Accuracy (CA) of 58.83% and an Attack Success Rate (ASR) of 0.39% across seven mainstream backdoor attacks. These results underscore the superiority of our prompt purifying design to strengthen CLIP's robustness against backdoor attacks.

## 📝 요약

이 논문은 CLIP과 같은 사전 학습된 비전-언어 모델(VLM)의 백도어 공격 취약성을 해결하기 위해 제안된 Class-wise Backdoor Prompt Tuning (CBPT) 방법론을 소개합니다. 기존 방어 전략은 전체 모델의 미세 조정에 집중하지만, 이는 모델의 안정적 최적화를 어렵게 하고 정확도를 저하시킬 수 있습니다. CBPT는 텍스트 프롬프트를 사용하여 간접적으로 오염된 CLIP을 정화하는 효율적인 방어 메커니즘으로, 대조 학습을 통해 공격자가 사용하는 백도어 트리거를 반전시킵니다. 세 가지 손실 함수를 활용하여 클래스별 텍스트 프롬프트를 최적화하고, 모델의 결정 경계를 수정하여 백도어 트리거에 영향을 받은 특징 영역을 재분류합니다. 실험 결과, CBPT는 백도어 위협을 효과적으로 완화하면서도 모델의 유용성을 유지하며, 평균 58.83%의 깨끗한 정확도(CA)와 0.39%의 공격 성공률(ASR)을 달성했습니다. 이 결과는 백도어 공격에 대한 CLIP의 강건성을 강화하는 CBPT의 우수성을 입증합니다.

## 🎯 주요 포인트

- 1. 기존의 비전-언어 모델(VLMs)은 백도어 공격에 취약하며, 이를 방어하기 위한 기존 전략은 주로 전체 모델의 미세 조정에 초점을 맞추고 있다.
- 2. Class-wise Backdoor Prompt Tuning (CBPT)은 텍스트 프롬프트를 활용하여 CLIP 모델의 백도어 공격을 간접적으로 정화하는 효율적이고 효과적인 방어 메커니즘을 제안한다.
- 3. CBPT는 고급 대조 학습을 통해 공격자가 사용하는 백도어 트리거를 효과적으로 역전시키고, 세 가지 손실 함수를 활용하여 클래스별 텍스트 프롬프트를 최적화한다.
- 4. 실험 결과, CBPT는 백도어 위협을 크게 완화하면서 모델의 유용성을 유지하며, 평균 58.83%의 깨끗한 정확도(CA)와 0.39%의 공격 성공률(ASR)을 기록했다.
- 5. CBPT의 프롬프트 정화 설계는 CLIP의 백도어 공격에 대한 강건성을 강화하는 데 있어 우수성을 입증한다.


---

*Generated on 2025-09-24 05:17:24*