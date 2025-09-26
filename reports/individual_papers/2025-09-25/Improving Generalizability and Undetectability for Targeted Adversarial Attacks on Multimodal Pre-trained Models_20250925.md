---
keywords:
  - Multimodal Learning
  - Adversarial Attacks
  - Proxy Targeted Attack
  - Anomaly Detection
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19994
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:11:09.400427",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Adversarial Attacks",
    "Proxy Targeted Attack",
    "Anomaly Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Adversarial Attacks": 0.78,
    "Proxy Targeted Attack": 0.7,
    "Anomaly Detection": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal pre-trained models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Models",
          "Multimodal Pre-trained"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key area connecting various data modalities, making it crucial for linking across related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Targeted Adversarial Attacks",
        "canonical": "Adversarial Attacks",
        "aliases": [
          "Targeted AEs",
          "Adversarial Examples"
        ],
        "category": "unique_technical",
        "rationale": "Adversarial Attacks are central to security concerns in AI, providing strong links to research on model robustness.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Proxy Targeted Attack",
        "canonical": "Proxy Targeted Attack",
        "aliases": [
          "PTA"
        ],
        "category": "unique_technical",
        "rationale": "The proposed method, Proxy Targeted Attack, is novel and specific to the paper, offering a unique link to this research.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Anomaly Detection Methods",
        "canonical": "Anomaly Detection",
        "aliases": [
          "Detection Methods"
        ],
        "category": "broad_technical",
        "rationale": "Anomaly Detection is a broad technique applicable across various domains, linking to research on security and model evaluation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.6,
        "link_intent_score": 0.68
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
      "candidate_surface": "Multimodal pre-trained models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Targeted Adversarial Attacks",
      "resolved_canonical": "Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Proxy Targeted Attack",
      "resolved_canonical": "Proxy Targeted Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Anomaly Detection Methods",
      "resolved_canonical": "Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.6,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Improving Generalizability and Undetectability for Targeted Adversarial Attacks on Multimodal Pre-trained Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19994.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19994](https://arxiv.org/abs/2509.19994)

## 🔗 유사한 논문
- [[2025-09-25/Universal Camouflage Attack on Vision-Language Models for Autonomous Driving_20250925|Universal Camouflage Attack on Vision-Language Models for Autonomous Driving]] (83.2% similar)
- [[2025-09-25/BiTAA_ A Bi-Task Adversarial Attack for Object Detection and Depth Estimation via 3D Gaussian Splatting_20250925|BiTAA: A Bi-Task Adversarial Attack for Object Detection and Depth Estimation via 3D Gaussian Splatting]] (83.1% similar)
- [[2025-09-24/Latent Danger Zone_ Distilling Unified Attention for Cross-Architecture Black-box Attacks_20250924|Latent Danger Zone: Distilling Unified Attention for Cross-Architecture Black-box Attacks]] (82.9% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (82.8% similar)
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Anomaly Detection|Anomaly Detection]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Adversarial Attacks|Adversarial Attacks]], [[keywords/Proxy Targeted Attack|Proxy Targeted Attack]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19994v1 Announce Type: new 
Abstract: Multimodal pre-trained models (e.g., ImageBind), which align distinct data modalities into a shared embedding space, have shown remarkable success across downstream tasks. However, their increasing adoption raises serious security concerns, especially regarding targeted adversarial attacks. In this paper, we show that existing targeted adversarial attacks on multimodal pre-trained models still have limitations in two aspects: generalizability and undetectability. Specifically, the crafted targeted adversarial examples (AEs) exhibit limited generalization to partially known or semantically similar targets in cross-modal alignment tasks (i.e., limited generalizability) and can be easily detected by simple anomaly detection methods (i.e., limited undetectability). To address these limitations, we propose a novel method called Proxy Targeted Attack (PTA), which leverages multiple source-modal and target-modal proxies to optimize targeted AEs, ensuring they remain evasive to defenses while aligning with multiple potential targets. We also provide theoretical analyses to highlight the relationship between generalizability and undetectability and to ensure optimal generalizability while meeting the specified requirements for undetectability. Furthermore, experimental results demonstrate that our PTA can achieve a high success rate across various related targets and remain undetectable against multiple anomaly detection methods.

## 📝 요약

이 논문은 멀티모달 사전 학습 모델에 대한 기존의 표적 적대적 공격이 일반화 가능성과 탐지 회피 측면에서 한계를 가지고 있음을 지적합니다. 이를 해결하기 위해, 저자들은 Proxy Targeted Attack (PTA)라는 새로운 방법을 제안합니다. PTA는 여러 소스 및 타겟 모달 프록시를 활용하여 표적 적대적 예제를 최적화하며, 다양한 잠재적 표적과의 정렬을 유지하면서 방어를 회피할 수 있도록 설계되었습니다. 이 방법은 이론적 분석을 통해 일반화 가능성과 탐지 회피 간의 관계를 설명하고, 실험 결과를 통해 높은 성공률과 탐지 회피 성능을 입증합니다.

## 🎯 주요 포인트

- 1. 다중모달 사전 학습 모델은 보안 문제, 특히 표적 적대적 공격에 취약하다.
- 2. 기존의 표적 적대적 공격은 일반화 가능성과 탐지 불가성에서 한계를 가지고 있다.
- 3. Proxy Targeted Attack (PTA) 방법은 다중 소스 및 타겟 모달 프록시를 활용하여 표적 적대적 예제를 최적화한다.
- 4. PTA는 다양한 관련 타겟에 대해 높은 성공률을 보이며, 여러 이상 탐지 방법에 대해 탐지되지 않는다.
- 5. 이론적 분석을 통해 일반화 가능성과 탐지 불가성 간의 관계를 강조하고 최적의 일반화 가능성을 보장한다.


---

*Generated on 2025-09-26 09:11:09*