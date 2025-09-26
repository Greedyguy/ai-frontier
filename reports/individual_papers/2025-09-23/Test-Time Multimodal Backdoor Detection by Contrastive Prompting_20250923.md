---
keywords:
  - Multimodal Learning
  - Backdoor Detection
  - Zero-Shot Learning
  - Vision-Language Model
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2405.15269
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:55:46.266793",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Backdoor Detection",
    "Zero-Shot Learning",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Backdoor Detection": 0.79,
    "Zero-Shot Learning": 0.84,
    "Vision-Language Model": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal contrastive learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal contrastive methods",
          "Multimodal contrastive"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the trending concept of integrating multiple modalities in learning systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Backdoor detection",
        "canonical": "Backdoor Detection",
        "aliases": [
          "Backdoor attack defense",
          "Backdoor defense"
        ],
        "category": "unique_technical",
        "rationale": "A unique technical concept focusing on identifying and mitigating backdoor attacks in models.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Zero-shot classification",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot inference",
          "Zero-shot methods"
        ],
        "category": "specific_connectable",
        "rationale": "A specific learning paradigm that enhances model adaptability and is widely discussed in recent research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.75,
        "link_intent_score": 0.84
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language integration",
          "Vision-Language systems"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents the integration of visual and textual data, a growing area in AI research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal contrastive learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Backdoor detection",
      "resolved_canonical": "Backdoor Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Zero-shot classification",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.75,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Test-Time Multimodal Backdoor Detection by Contrastive Prompting

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2405.15269.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2405.15269](https://arxiv.org/abs/2405.15269)

## 🔗 유사한 논문
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (85.2% similar)
- [[2025-09-22/Inverting Trojans in LLMs_20250922|Inverting Trojans in LLMs]] (84.8% similar)
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (83.7% similar)
- [[2025-09-22/CoDoL_ Conditional Domain Prompt Learning for Out-of-Distribution Generalization_20250922|CoDoL: Conditional Domain Prompt Learning for Out-of-Distribution Generalization]] (83.3% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Backdoor Detection|Backdoor Detection]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.15269v3 Announce Type: replace-cross 
Abstract: While multimodal contrastive learning methods (e.g., CLIP) can achieve impressive zero-shot classification performance, recent research has revealed that these methods are vulnerable to backdoor attacks. To defend against backdoor attacks on CLIP, existing defense methods focus on either the pre-training stage or the fine-tuning stage, which would unfortunately cause high computational costs due to numerous parameter updates and are not applicable in black-box settings. In this paper, we provide the first attempt at a computationally efficient backdoor detection method to defend against backdoored CLIP in the \emph{inference} stage. We empirically find that the visual representations of backdoored images are \emph{insensitive} to \emph{benign} and \emph{malignant} changes in class description texts. Motivated by this observation, we propose BDetCLIP, a novel test-time backdoor detection method based on contrastive prompting. Specifically, we first prompt a language model (e.g., GPT-4) to produce class-related description texts (benign) and class-perturbed random texts (malignant) by specially designed instructions. Then, the distribution difference in cosine similarity between images and the two types of class description texts can be used as the criterion to detect backdoor samples. Extensive experiments validate that our proposed BDetCLIP is superior to state-of-the-art backdoor detection methods, in terms of both effectiveness and efficiency. Our codes are publicly available at: https://github.com/Purshow/BDetCLIP.

## 📝 요약

이 논문은 CLIP과 같은 멀티모달 대조 학습 방법이 백도어 공격에 취약하다는 문제를 해결하기 위해, 추론 단계에서 효율적인 백도어 탐지 방법을 제안합니다. 기존 방어 방법은 사전 훈련이나 미세 조정 단계에 초점을 맞춰 높은 계산 비용이 들고 블랙박스 환경에서는 적용이 어렵습니다. 저자들은 백도어 이미지의 시각적 표현이 클래스 설명 텍스트의 변화에 둔감하다는 점을 발견하고, 이를 바탕으로 BDetCLIP이라는 새로운 테스트 단계 백도어 탐지 방법을 제안합니다. 이 방법은 언어 모델을 사용하여 클래스 관련 설명 텍스트와 클래스 변형 랜덤 텍스트를 생성하고, 이미지와 이 두 텍스트 간의 코사인 유사도 분포 차이를 통해 백도어 샘플을 탐지합니다. 실험 결과, BDetCLIP은 기존 최첨단 방법들보다 효과적이고 효율적임을 입증했습니다.

## 🎯 주요 포인트

- 1. 멀티모달 대조 학습 방법은 백도어 공격에 취약하다는 것이 최근 연구에서 밝혀졌습니다.
- 2. 기존 방어 방법은 사전 훈련 단계나 미세 조정 단계에 초점을 맞추어 높은 계산 비용을 초래합니다.
- 3. 본 논문에서는 추론 단계에서 백도어 공격을 방어하기 위한 효율적인 백도어 탐지 방법을 제안합니다.
- 4. 제안된 BDetCLIP 방법은 대조적 프롬프트를 기반으로 하여 테스트 시 백도어 샘플을 탐지합니다.
- 5. BDetCLIP은 효과성과 효율성 면에서 최신 백도어 탐지 방법보다 우수하다는 것이 실험을 통해 검증되었습니다.


---

*Generated on 2025-09-24 02:55:46*