---
keywords:
  - Multimodal Learning
  - Few-Shot Learning
  - Transformer
  - Adaptive Global Class-Aware Contrastive Loss
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19315
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:22:41.771903",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Few-Shot Learning",
    "Transformer",
    "Adaptive Global Class-Aware Contrastive Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Few-Shot Learning": 0.82,
    "Transformer": 0.8,
    "Adaptive Global Class-Aware Contrastive Loss": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal",
          "Multimodal Framework"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key aspect of the proposed framework, enhancing connectivity with other multimodal research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Few-Shot Pediatric Arrhythmia Classification",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot Classification",
          "Few-Shot Arrhythmia"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is crucial for handling class imbalance in pediatric arrhythmia, linking to broader few-shot methodologies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transformer Encoder",
        "canonical": "Transformer",
        "aliases": [
          "Transformer Model",
          "Transformer Architecture"
        ],
        "category": "broad_technical",
        "rationale": "The use of a Transformer encoder for global dependency modeling connects to a wide range of Transformer-based research.",
        "novelty_score": 0.47,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Global Class-Aware Contrastive Loss",
        "canonical": "Adaptive Global Class-Aware Contrastive Loss",
        "aliases": [
          "AGCACL"
        ],
        "category": "unique_technical",
        "rationale": "This novel loss function is specific to the study and enhances intra-class compactness, offering unique insights.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
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
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Few-Shot Pediatric Arrhythmia Classification",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transformer Encoder",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.47,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Global Class-Aware Contrastive Loss",
      "resolved_canonical": "Adaptive Global Class-Aware Contrastive Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19315.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19315](https://arxiv.org/abs/2509.19315)

## 🔗 유사한 논문
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (84.2% similar)
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (83.9% similar)
- [[2025-09-22/SuPreME_ A Supervised Pre-training Framework for Multimodal ECG Representation Learning_20250922|SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning]] (83.8% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (83.7% similar)
- [[2025-09-23/Multimodal Medical Image Classification via Synergistic Learning Pre-training_20250923|Multimodal Medical Image Classification via Synergistic Learning Pre-training]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Adaptive Global Class-Aware Contrastive Loss|Adaptive Global Class-Aware Contrastive Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19315v1 Announce Type: cross 
Abstract: Pediatric arrhythmias are a major risk factor for disability and sudden cardiac death, yet their automated classification remains challenging due to class imbalance, few-shot categories, and complex signal characteristics, which severely limit the efficiency and reliability of early screening and clinical intervention. To address this problem, we propose a multimodal end-to-end deep learning framework that combines dual-branch convolutional encoders for ECG and IEGM, semantic attention for cross-modal feature alignment, and a lightweight Transformer encoder for global dependency modeling. In addition, we introduce a new contrastive loss fucntion named Adaptive Global Class-Aware Contrastive Loss (AGCACL) to enhance intra-class compactness and inter-class separability through class prototypes and a global similarity matrix. To the best of our knowledge, this is the first systematic study based on the Leipzig Heart Center pediatric/congenital ECG+IEGM dataset, for which we also provide a complete and reproducible preprocessing pipeline. Experimental results demonstrate that the proposed method achieves the overall best performance on this dataset, including 97.76\% Top-1 Accuracy, 94.08\% Macro Precision, 91.97\% Macro Recall, 92.97\% Macro F1, and 92.36\% Macro F2, with improvements of +13.64, +15.96, +19.82, and +19.44 percentage points over the strongest baseline in Macro Precision/Recall/F1/F2, respectively. These findings indicate that the framework significantly improves the detectability and robustness for minority arrhythmia classes, offering potential clinical value for rhythm screening, pre-procedural assessment, and postoperative follow-up in pediatric and congenital heart disease populations.

## 📝 요약

이 논문은 소아 부정맥의 자동 분류 문제를 해결하기 위해 다중 모달 종단 간 심층 학습 프레임워크를 제안합니다. ECG와 IEGM 데이터를 위한 이중 분기 컨볼루션 인코더, 교차 모달 특징 정렬을 위한 의미적 주의 메커니즘, 전역 의존성 모델링을 위한 경량 트랜스포머 인코더를 결합합니다. 또한, 클래스 프로토타입과 전역 유사성 행렬을 활용한 적응형 글로벌 클래스 인식 대조 손실(AGCACL)을 도입하여 클래스 내 밀집성과 클래스 간 분리를 강화합니다. 이 연구는 Leipzig Heart Center의 소아/선천성 ECG+IEGM 데이터셋을 기반으로 한 최초의 체계적 연구로, 완전하고 재현 가능한 전처리 파이프라인도 제공합니다. 실험 결과, 제안된 방법이 데이터셋에서 97.76%의 Top-1 정확도와 높은 매크로 정밀도, 재현율, F1, F2 점수를 기록하며 기존 방법보다 성능을 크게 향상시켰음을 보여줍니다. 이는 소수 부정맥 클래스의 검출 가능성과 강건성을 크게 개선하여 임상적 가치를 제공합니다.

## 🎯 주요 포인트

- 1. 소아 부정맥의 자동 분류는 클래스 불균형과 복잡한 신호 특성 때문에 어려움을 겪고 있습니다.
- 2. ECG와 IEGM의 듀얼 브랜치 컨볼루션 인코더를 결합한 멀티모달 딥러닝 프레임워크를 제안합니다.
- 3. 제안된 방법은 Leipzig Heart Center의 소아/선천성 ECG+IEGM 데이터셋에서 최고 성능을 달성했습니다.
- 4. 새로운 대조 손실 함수인 Adaptive Global Class-Aware Contrastive Loss (AGCACL)를 도입하여 클래스 간 분리성을 향상시켰습니다.
- 5. 이 프레임워크는 소수 부정맥 클래스의 탐지 가능성과 강건성을 크게 개선하여 임상적 가치를 제공합니다.


---

*Generated on 2025-09-25 15:22:41*