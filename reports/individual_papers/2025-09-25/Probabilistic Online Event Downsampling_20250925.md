---
keywords:
  - Event Cameras
  - Probabilistic Framework
  - Zero-Shot Learning
  - Contour-Preserving Probability Density Function
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2506.02547
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:25:52.759550",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Event Cameras",
    "Probabilistic Framework",
    "Zero-Shot Learning",
    "Contour-Preserving Probability Density Function"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Event Cameras": 0.78,
    "Probabilistic Framework": 0.65,
    "Zero-Shot Learning": 0.82,
    "Contour-Preserving Probability Density Function": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Event Cameras",
        "canonical": "Event Cameras",
        "aliases": [
          "Dynamic Vision Sensors"
        ],
        "category": "unique_technical",
        "rationale": "Event cameras are a specialized technology crucial for high temporal resolution applications, offering unique insights into asynchronous data capture.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Probabilistic Framework",
        "canonical": "Probabilistic Framework",
        "aliases": [
          "Probabilistic Model"
        ],
        "category": "broad_technical",
        "rationale": "Probabilistic frameworks are fundamental in modeling uncertainties and are widely applicable across various machine learning tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      },
      {
        "surface": "Zero-Shot Event Downsampling",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is a trending concept that enhances the adaptability of models to new tasks without task-specific training.",
        "novelty_score": 0.68,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Contour-Preserving ePDF",
        "canonical": "Contour-Preserving Probability Density Function",
        "aliases": [
          "Contour-Preserving ePDF"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach that prioritizes structurally important events, crucial for maintaining data integrity in downsampling.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Event Cameras",
      "resolved_canonical": "Event Cameras",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Probabilistic Framework",
      "resolved_canonical": "Probabilistic Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Zero-Shot Event Downsampling",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Contour-Preserving ePDF",
      "resolved_canonical": "Contour-Preserving Probability Density Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Probabilistic Online Event Downsampling

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.02547.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2506.02547](https://arxiv.org/abs/2506.02547)

## 🔗 유사한 논문
- [[2025-09-23/PASS_ Path-selective State Space Model for Event-based Recognition_20250923|PASS: Path-selective State Space Model for Event-based Recognition]] (83.0% similar)
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (81.6% similar)
- [[2025-09-24/Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction_20250924|Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction]] (81.2% similar)
- [[2025-09-24/HyperEvent_ A Strong Baseline for Dynamic Link Prediction via Relative Structural Encoding_20250924|HyperEvent: A Strong Baseline for Dynamic Link Prediction via Relative Structural Encoding]] (80.6% similar)
- [[2025-09-23/Event-Based Visual Teach-and-Repeat via Fast Fourier-Domain Cross-Correlation_20250923|Event-Based Visual Teach-and-Repeat via Fast Fourier-Domain Cross-Correlation]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Probabilistic Framework|Probabilistic Framework]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Event Cameras|Event Cameras]], [[keywords/Contour-Preserving Probability Density Function|Contour-Preserving Probability Density Function]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02547v2 Announce Type: replace 
Abstract: Event cameras capture scene changes asynchronously on a per-pixel basis, enabling extremely high temporal resolution. However, this advantage comes at the cost of high bandwidth, memory, and computational demands. To address this, prior work has explored event downsampling, but most approaches rely on fixed heuristics or threshold-based strategies, limiting their adaptability. Instead, we propose a probabilistic framework, POLED, that models event importance through an event-importance probability density function (ePDF), which can be arbitrarily defined and adapted to different applications. Our approach operates in a purely online setting, estimating event importance on-the-fly from raw event streams, enabling scene-specific adaptation. Additionally, we introduce zero-shot event downsampling, where downsampled events must remain usable for models trained on the original event stream, without task-specific adaptation. We design a contour-preserving ePDF that prioritizes structurally important events and evaluate our method across four datasets and tasks--object classification, image interpolation, surface normal estimation, and object detection--demonstrating that intelligent sampling is crucial for maintaining performance under event-budget constraints. Code available.

## 📝 요약

이 논문은 이벤트 카메라의 높은 대역폭과 메모리 요구를 해결하기 위해 POLED라는 확률적 프레임워크를 제안합니다. POLED는 이벤트의 중요성을 이벤트 중요도 확률 밀도 함수(ePDF)로 모델링하여 다양한 응용에 적응할 수 있습니다. 이 방법은 온라인 설정에서 작동하며, 장면에 맞춰 실시간으로 이벤트 중요도를 추정합니다. 또한, 원본 이벤트 스트림에 맞춰 훈련된 모델에서 사용할 수 있는 제로샷 이벤트 다운샘플링을 도입합니다. 구조적으로 중요한 이벤트를 우선시하는 ePDF를 설계하고, 네 가지 데이터셋과 작업에서 평가하여 이벤트 예산 제약 하에서도 성능을 유지할 수 있음을 입증했습니다. 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 이벤트 카메라는 픽셀 단위로 비동기적으로 장면 변화를 포착하여 매우 높은 시간 해상도를 제공하지만, 높은 대역폭, 메모리 및 계산 요구 사항이 필요합니다.
- 2. 기존의 이벤트 다운샘플링 방법은 고정된 휴리스틱이나 임계값 기반 전략에 의존하여 적응성이 제한적입니다.
- 3. POLED라는 확률론적 프레임워크를 제안하여 이벤트 중요도를 이벤트 중요도 확률 밀도 함수(ePDF)로 모델링하며, 이는 다양한 응용 프로그램에 맞게 임의로 정의 및 적응될 수 있습니다.
- 4. 제로샷 이벤트 다운샘플링을 도입하여 다운샘플링된 이벤트가 원래 이벤트 스트림에 대해 훈련된 모델에서 유용하게 사용될 수 있도록 합니다.
- 5. 네 가지 데이터셋과 작업(객체 분류, 이미지 보간, 표면 법선 추정, 객체 탐지)에서 방법을 평가하여 이벤트 예산 제약 하에서 성능을 유지하는 데 지능형 샘플링이 중요함을 입증했습니다.


---

*Generated on 2025-09-26 09:25:52*