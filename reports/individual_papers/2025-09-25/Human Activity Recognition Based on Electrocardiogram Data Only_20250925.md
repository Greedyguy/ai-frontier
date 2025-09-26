---
keywords:
  - ECG-only Activity Recognition
  - CNN-Transformer Hybrid
  - Attention Mechanism
  - Deep Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19328
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:24:34.979670",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ECG-only Activity Recognition",
    "CNN-Transformer Hybrid",
    "Attention Mechanism",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ECG-only Activity Recognition": 0.8,
    "CNN-Transformer Hybrid": 0.75,
    "Attention Mechanism": 0.85,
    "Deep Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ECG-only activity classification",
        "canonical": "ECG-only Activity Recognition",
        "aliases": [
          "Electrocardiogram-based Activity Recognition"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel approach to activity recognition using only ECG data, which is a significant advancement in the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "CNNTransformer hybrid",
        "canonical": "CNN-Transformer Hybrid",
        "aliases": [
          "Convolutional Transformer Hybrid"
        ],
        "category": "unique_technical",
        "rationale": "This model combines convolutional and transformer architectures, offering a unique approach to feature extraction and temporal relationship modeling.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for modeling long-range dependencies, making them a key component in advanced neural networks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Deep learning models",
        "canonical": "Deep Learning",
        "aliases": [
          "DL Models"
        ],
        "category": "broad_technical",
        "rationale": "Deep learning is the foundational technology for the models discussed, providing a broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.6,
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
      "candidate_surface": "ECG-only activity classification",
      "resolved_canonical": "ECG-only Activity Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "CNNTransformer hybrid",
      "resolved_canonical": "CNN-Transformer Hybrid",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Deep learning models",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Human Activity Recognition Based on Electrocardiogram Data Only

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19328.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19328](https://arxiv.org/abs/2509.19328)

## 🔗 유사한 논문
- [[2025-09-25/Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning_20250925|Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning]] (82.4% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.3% similar)
- [[2025-09-24/UniECG_ Understanding and Generating ECG in One Unified Model_20250924|UniECG: Understanding and Generating ECG in One Unified Model]] (82.2% similar)
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (80.8% similar)
- [[2025-09-22/SuPreME_ A Supervised Pre-training Framework for Multimodal ECG Representation Learning_20250922|SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/ECG-only Activity Recognition|ECG-only Activity Recognition]], [[keywords/CNN-Transformer Hybrid|CNN-Transformer Hybrid]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19328v1 Announce Type: cross 
Abstract: Human activity recognition is critical for applications such as early intervention and health analytics. Traditional activity recognition relies on inertial measurement units (IMUs), which are resource intensive and require calibration. Although electrocardiogram (ECG)-based methods have been explored, these have typically served as supplements to IMUs or have been limited to broad categorical classification such as fall detection or active vs. inactive in daily activities. In this paper, we advance the field by demonstrating, for the first time, robust recognition of activity only with ECG in six distinct activities, which is beyond the scope of previous work. We design and evaluate three new deep learning models, including a CNN classifier with Squeeze-and-Excitation blocks for channel-wise feature recalibration, a ResNet classifier with dilated convolutions for multiscale temporal dependency capture, and a novel CNNTransformer hybrid combining convolutional feature extraction with attention mechanisms for long-range temporal relationship modeling. Tested on data from 54 subjects for six activities, all three models achieve over 94% accuracy for seen subjects, while CNNTransformer hybrid reaching the best accuracy of 72% for unseen subjects, a result that can be further improved by increasing the training population. This study demonstrates the first successful ECG-only activity classification in multiple physical activities, offering significant potential for developing next-generation wearables capable of simultaneous cardiac monitoring and activity recognition without additional motion sensors.

## 📝 요약

이 논문은 ECG(심전도)만을 사용하여 여섯 가지 활동을 인식하는 새로운 방법론을 제시합니다. 기존의 활동 인식은 주로 IMU(관성 측정 장치)에 의존했으나, 이 연구는 ECG만으로도 높은 정확도의 활동 인식이 가능함을 보여줍니다. 세 가지 딥러닝 모델을 설계하고 평가했으며, 특히 CNN-Transformer 하이브리드 모델은 보지 못한 피험자에 대해 72%의 정확도를 기록했습니다. 이는 ECG만으로 다중 신체 활동을 성공적으로 분류한 최초의 연구로, 추가적인 움직임 센서 없이도 심박수 모니터링과 활동 인식이 가능한 차세대 웨어러블 기기의 개발 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 ECG만으로 6개의 서로 다른 활동을 인식하는 데 성공하여 기존 연구의 범위를 넘어섰습니다.
- 2. 세 가지 새로운 딥러닝 모델을 설계 및 평가하였으며, 각각 CNN, ResNet, CNN-Transformer 하이브리드를 포함합니다.
- 3. 54명의 데이터를 대상으로 테스트한 결과, 모든 모델이 94% 이상의 정확도를 기록했으며, 특히 CNN-Transformer 하이브리드는 보지 못한 피험자에 대해 72%의 정확도를 달성했습니다.
- 4. 본 연구는 ECG만으로 다중 신체 활동을 분류하는 첫 번째 성공 사례로, 추가적인 모션 센서 없이 심박 모니터링과 활동 인식이 가능한 차세대 웨어러블 기기의 개발 가능성을 제시합니다.


---

*Generated on 2025-09-25 15:24:34*