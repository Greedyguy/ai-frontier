---
keywords:
  - Self-supervised Learning
  - Transformer
  - Single-channel EEG
  - Motor Imagery
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17920
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:00:00.779152",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Transformer",
    "Single-channel EEG",
    "Motor Imagery"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.8,
    "Transformer": 0.85,
    "Single-channel EEG": 0.78,
    "Motor Imagery": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised foundation model",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervised model"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of self-supervised learning, which is crucial for understanding the model's training approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Hierarchical transformer",
        "canonical": "Transformer",
        "aliases": [
          "Hierarchical transformer model"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader technical category of transformers, highlighting the model's architecture.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Single-channel EEG",
        "canonical": "Single-channel EEG",
        "aliases": [
          "Single-channel electroencephalography"
        ],
        "category": "unique_technical",
        "rationale": "Represents a unique approach in EEG analysis, enabling hardware agnostic applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Motor imagery tasks",
        "canonical": "Motor Imagery",
        "aliases": [
          "Motor imagery experiments"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for linking to cognitive neuroscience and EEG task analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "foundation model",
      "large labeled datasets",
      "fixed feature extractor"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised foundation model",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Hierarchical transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Single-channel EEG",
      "resolved_canonical": "Single-channel EEG",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Motor imagery tasks",
      "resolved_canonical": "Motor Imagery",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SingLEM: Single-Channel Large EEG Model

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17920.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17920](https://arxiv.org/abs/2509.17920)

## 🔗 유사한 논문
- [[2025-09-23/A Simple Review of EEG Foundation Models_ Datasets, Advancements and Future Perspectives_20250923|A Simple Review of EEG Foundation Models: Datasets, Advancements and Future Perspectives]] (81.1% similar)
- [[2025-09-22/SuPreME_ A Supervised Pre-training Framework for Multimodal ECG Representation Learning_20250922|SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning]] (80.4% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (80.3% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (80.2% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding_20250919|UMind: A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Motor Imagery|Motor Imagery]]
**⚡ Unique Technical**: [[keywords/Single-channel EEG|Single-channel EEG]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17920v1 Announce Type: new 
Abstract: Current deep learning models for electroencephalography (EEG) are often task-specific and depend on large labeled datasets, limiting their adaptability. Although emerging foundation models aim for broader applicability, their rigid dependence on fixed, high-density multi-channel montages restricts their use across heterogeneous datasets and in missing-channel or practical low-channel settings. To address these limitations, we introduce SingLEM, a self-supervised foundation model that learns robust, general-purpose representations from single-channel EEG, making it inherently hardware agnostic. The model employs a hybrid encoder architecture that combines convolutional layers to extract local features with a hierarchical transformer to model both short- and long-range temporal dependencies. SingLEM is pretrained on 71 public datasets comprising over 9,200 subjects and 357,000 single-channel hours of EEG. When evaluated as a fixed feature extractor across six motor imagery and cognitive tasks, aggregated single-channel representations consistently outperformed leading multi-channel foundation models and handcrafted baselines. These results demonstrate that a single-channel approach can achieve state-of-the-art generalization while enabling fine-grained neurophysiological analysis and enhancing interpretability. The source code and pretrained models are available at https://github.com/ttlabtuat/SingLEM.

## 📝 요약

현재의 뇌전도(EEG) 딥러닝 모델은 특정 작업에 맞춰져 있으며, 대규모 라벨링 데이터셋에 의존하여 적응성이 제한됩니다. SingLEM은 이러한 한계를 극복하기 위해 제안된 자가 지도 학습 기반의 기초 모델로, 단일 채널 EEG로부터 견고하고 범용적인 표현을 학습하여 하드웨어에 구애받지 않습니다. 이 모델은 지역적 특징을 추출하는 합성곱 층과 단기 및 장기 시간 의존성을 모델링하는 계층적 트랜스포머를 결합한 하이브리드 인코더 아키텍처를 사용합니다. 71개의 공개 데이터셋에서 9,200명 이상의 피험자와 357,000시간 이상의 단일 채널 EEG 데이터를 사전 학습하였으며, 6개의 운동 이미지 및 인지 과제에서 고정된 특징 추출기로 평가된 결과, 단일 채널 표현이 다채널 모델과 수작업 기반을 능가했습니다. 이 연구는 단일 채널 접근법이 최첨단 일반화를 달성하면서 신경생리학적 분석과 해석 가능성을 향상시킬 수 있음을 보여줍니다. 소스 코드와 사전 학습된 모델은 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. SingLEM은 단일 채널 EEG에서 강력하고 범용적인 표현을 학습하는 자기 지도형 기초 모델로, 하드웨어에 구애받지 않습니다.
- 2. 이 모델은 지역적 특징을 추출하는 합성곱 층과 단기 및 장기 시간 의존성을 모델링하는 계층적 트랜스포머를 결합한 하이브리드 인코더 아키텍처를 사용합니다.
- 3. SingLEM은 71개의 공개 데이터셋에서 9,200명 이상의 피험자와 357,000시간 이상의 단일 채널 EEG 데이터를 사전 학습했습니다.
- 4. 단일 채널 표현은 여섯 가지 운동 심상 및 인지 과제에서 고정된 특징 추출기로 평가될 때, 다중 채널 기초 모델과 수작업 기준선을 일관되게 능가했습니다.
- 5. 이 연구는 단일 채널 접근 방식이 최첨단 일반화를 달성하면서 세밀한 신경생리학적 분석을 가능하게 하고 해석 가능성을 높일 수 있음을 보여줍니다.


---

*Generated on 2025-09-24 02:00:00*