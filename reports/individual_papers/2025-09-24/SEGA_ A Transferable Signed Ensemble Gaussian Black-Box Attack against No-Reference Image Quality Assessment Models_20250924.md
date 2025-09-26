<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:01:48.942471",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "No-Reference Image Quality Assessment",
    "Adversarial Attacks",
    "Black-Box Attacks",
    "Gaussian Smoothing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "No-Reference Image Quality Assessment": 0.78,
    "Adversarial Attacks": 0.82,
    "Black-Box Attacks": 0.79,
    "Gaussian Smoothing": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "No-Reference Image Quality Assessment",
        "canonical": "No-Reference Image Quality Assessment",
        "aliases": [
          "NR-IQA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific domain within image quality assessment, crucial for linking to related research in image processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "adversarial attacks",
        "canonical": "Adversarial Attacks",
        "aliases": [
          "attack strategies"
        ],
        "category": "broad_technical",
        "rationale": "Adversarial attacks are a fundamental concept in security and robustness research, linking to broader discussions in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "black-box scenarios",
        "canonical": "Black-Box Attacks",
        "aliases": [
          "black-box methods"
        ],
        "category": "specific_connectable",
        "rationale": "Black-box attacks are a key concept in evaluating model robustness without internal access, linking to security and privacy research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Gaussian smoothing",
        "canonical": "Gaussian Smoothing",
        "aliases": [
          "smoothing techniques"
        ],
        "category": "specific_connectable",
        "rationale": "Gaussian smoothing is a technique used in image processing and can connect to discussions on noise reduction and image filtering.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "transferability",
      "imperceptibility"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "No-Reference Image Quality Assessment",
      "resolved_canonical": "No-Reference Image Quality Assessment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "adversarial attacks",
      "resolved_canonical": "Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "black-box scenarios",
      "resolved_canonical": "Black-Box Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Gaussian smoothing",
      "resolved_canonical": "Gaussian Smoothing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SEGA: A Transferable Signed Ensemble Gaussian Black-Box Attack against No-Reference Image Quality Assessment Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18546.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18546](https://arxiv.org/abs/2509.18546)

## 🔗 유사한 논문
- [[2025-09-23/Revisiting Vision Language Foundations for No-Reference Image Quality Assessment_20250923|Revisiting Vision Language Foundations for No-Reference Image Quality Assessment]] (80.9% similar)
- [[2025-09-24/Latent Danger Zone_ Distilling Unified Attention for Cross-Architecture Black-box Attacks_20250924|Latent Danger Zone: Distilling Unified Attention for Cross-Architecture Black-box Attacks]] (79.3% similar)
- [[2025-09-23/Budgeted Adversarial Attack against Graph-Based Anomaly Detection in Sensor Networks_20250923|Budgeted Adversarial Attack against Graph-Based Anomaly Detection in Sensor Networks]] (79.3% similar)
- [[2025-09-22/PolyJuice Makes It Real_ Black-Box, Universal Red Teaming for Synthetic Image Detectors_20250922|PolyJuice Makes It Real: Black-Box, Universal Red Teaming for Synthetic Image Detectors]] (78.6% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Adversarial Attacks|Adversarial Attacks]]
**🔗 Specific Connectable**: [[keywords/Black-Box Attacks|Black-Box Attacks]], [[keywords/Gaussian Smoothing|Gaussian Smoothing]]
**⚡ Unique Technical**: [[keywords/No-Reference Image Quality Assessment|No-Reference Image Quality Assessment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18546v1 Announce Type: new 
Abstract: No-Reference Image Quality Assessment (NR-IQA) models play an important role in various real-world applications. Recently, adversarial attacks against NR-IQA models have attracted increasing attention, as they provide valuable insights for revealing model vulnerabilities and guiding robust system design. Some effective attacks have been proposed against NR-IQA models in white-box settings, where the attacker has full access to the target model. However, these attacks often suffer from poor transferability to unknown target models in more realistic black-box scenarios, where the target model is inaccessible. This work makes the first attempt to address the challenge of low transferability in attacking NR-IQA models by proposing a transferable Signed Ensemble Gaussian black-box Attack (SEGA). The main idea is to approximate the gradient of the target model by applying Gaussian smoothing to source models and ensembling their smoothed gradients. To ensure the imperceptibility of adversarial perturbations, SEGA further removes inappropriate perturbations using a specially designed perturbation filter mask. Experimental results on the CLIVE dataset demonstrate the superior transferability of SEGA, validating its effectiveness in enabling successful transfer-based black-box attacks against NR-IQA models.

## 📝 요약

이 논문은 No-Reference Image Quality Assessment (NR-IQA) 모델에 대한 공격의 전이성을 개선하기 위해 새로운 방법론을 제안합니다. 기존의 화이트박스 공격은 목표 모델에 대한 완전한 접근이 가능한 상황에서 효과적이지만, 블랙박스 시나리오에서는 전이성이 낮아지는 문제가 있습니다. 이를 해결하기 위해, 저자들은 전이 가능한 서명된 앙상블 가우시안 블랙박스 공격(SEGA)을 제안합니다. SEGA는 소스 모델에 가우시안 스무딩을 적용하고, 스무딩된 그래디언트를 앙상블하여 목표 모델의 그래디언트를 근사화합니다. 또한, 특수 설계된 필터 마스크를 사용하여 부적절한 변형을 제거함으로써, 공격의 감지 불가능성을 보장합니다. 실험 결과, CLIVE 데이터셋에서 SEGA의 우수한 전이성을 입증하여, NR-IQA 모델에 대한 성공적인 블랙박스 공격이 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. NR-IQA 모델에 대한 적대적 공격은 모델의 취약성을 드러내고 견고한 시스템 설계를 유도하는 데 중요한 역할을 합니다.
- 2. 기존의 NR-IQA 모델 공격은 화이트박스 환경에서는 효과적이지만, 블랙박스 시나리오에서는 전이성이 낮다는 한계가 있습니다.
- 3. 본 연구는 전이 가능한 SEGA 공격을 제안하여 NR-IQA 모델에 대한 블랙박스 공격의 전이성 문제를 처음으로 해결하고자 합니다.
- 4. SEGA는 소스 모델에 가우시안 스무딩을 적용하고, 스무딩된 그래디언트를 앙상블하여 타겟 모델의 그래디언트를 근사화합니다.
- 5. 실험 결과, SEGA는 CLIVE 데이터셋에서 우수한 전이성을 보여 NR-IQA 모델에 대한 성공적인 블랙박스 공격을 가능하게 함을 검증했습니다.


---

*Generated on 2025-09-24 16:01:48*