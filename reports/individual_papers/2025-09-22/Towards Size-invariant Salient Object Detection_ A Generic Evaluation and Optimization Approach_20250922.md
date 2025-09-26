---
keywords:
  - Salient Object Detection
  - Size-Invariant Evaluation
  - Optimization Framework
  - Computer Vision
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15573
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:05:19.720930",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Salient Object Detection",
    "Size-Invariant Evaluation",
    "Optimization Framework",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Salient Object Detection": 0.8,
    "Size-Invariant Evaluation": 0.78,
    "Optimization Framework": 0.75,
    "Computer Vision": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Salient Object Detection",
        "canonical": "Salient Object Detection",
        "aliases": [
          "SOD"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, offering a unique perspective on size-invariance in object detection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Size-Invariant Evaluation",
        "canonical": "Size-Invariant Evaluation",
        "aliases": [
          "SIEva"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel evaluation framework addressing size imbalance in object detection.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Optimization Framework",
        "canonical": "Optimization Framework",
        "aliases": [
          "SIOpt"
        ],
        "category": "unique_technical",
        "rationale": "Proposes a new framework enhancing detection across various sizes, relevant for linking optimization techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.66,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Provides a broad technical context for the paper's focus on object detection.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "evaluation protocols",
      "performance assessments",
      "practical degradation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Salient Object Detection",
      "resolved_canonical": "Salient Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Size-Invariant Evaluation",
      "resolved_canonical": "Size-Invariant Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Optimization Framework",
      "resolved_canonical": "Optimization Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.66,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Towards Size-invariant Salient Object Detection: A Generic Evaluation and Optimization Approach

**Korean Title:** 크기 불변의 주목 객체 검출을 향하여: 일반적인 평가 및 최적화 접근법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15573.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15573](https://arxiv.org/abs/2509.15573)

## 🔗 유사한 논문
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (79.9% similar)
- [[2025-09-22/MIDOG 2025_ Mitotic Figure Detection with Attention-Guided False Positive Correction_20250922|MIDOG 2025: Mitotic Figure Detection with Attention-Guided False Positive Correction]] (78.8% similar)
- [[2025-09-22/OSPO_ Object-centric Self-improving Preference Optimization for Text-to-Image Generation_20250922|OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation]] (78.6% similar)
- [[2025-09-22/MCOD_ The First Challenging Benchmark for Multispectral Camouflaged Object Detection_20250922|MCOD: The First Challenging Benchmark for Multispectral Camouflaged Object Detection]] (78.5% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Salient Object Detection|Salient Object Detection]], [[keywords/Size-Invariant Evaluation|Size-Invariant Evaluation]], [[keywords/Optimization Framework|Optimization Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15573v1 Announce Type: cross 
Abstract: This paper investigates a fundamental yet underexplored issue in Salient Object Detection (SOD): the size-invariant property for evaluation protocols, particularly in scenarios when multiple salient objects of significantly different sizes appear within a single image. We first present a novel perspective to expose the inherent size sensitivity of existing widely used SOD metrics. Through careful theoretical derivations, we show that the evaluation outcome of an image under current SOD metrics can be essentially decomposed into a sum of several separable terms, with the contribution of each term being directly proportional to its corresponding region size. Consequently, the prediction errors would be dominated by the larger regions, while smaller yet potentially more semantically important objects are often overlooked, leading to biased performance assessments and practical degradation. To address this challenge, a generic Size-Invariant Evaluation (SIEva) framework is proposed. The core idea is to evaluate each separable component individually and then aggregate the results, thereby effectively mitigating the impact of size imbalance across objects. Building upon this, we further develop a dedicated optimization framework (SIOpt), which adheres to the size-invariant principle and significantly enhances the detection of salient objects across a broad range of sizes. Notably, SIOpt is model-agnostic and can be seamlessly integrated with a wide range of SOD backbones. Theoretically, we also present generalization analysis of SOD methods and provide evidence supporting the validity of our new evaluation protocols. Finally, comprehensive experiments speak to the efficacy of our proposed approach. The code is available at https://github.com/Ferry-Li/SI-SOD.

## 🔍 Abstract (한글 번역)

arXiv:2509.15573v1 발표 유형: 교차  
초록: 본 논문은 주목 객체 검출(Salient Object Detection, SOD)에서 근본적이지만 충분히 탐구되지 않은 문제, 즉 평가 프로토콜에서 크기 불변 속성을 조사합니다. 특히, 단일 이미지 내에 크기가 크게 다른 여러 주목 객체가 나타나는 시나리오에서 이 문제를 다룹니다. 우리는 먼저 기존에 널리 사용되는 SOD 지표의 내재된 크기 민감성을 드러내는 새로운 관점을 제시합니다. 신중한 이론적 유도를 통해, 현재 SOD 지표 하에서 이미지의 평가 결과가 본질적으로 여러 분리 가능한 항의 합으로 분해될 수 있음을 보여줍니다. 각 항의 기여도는 해당 영역 크기에 직접 비례합니다. 결과적으로, 예측 오류는 더 큰 영역에 의해 지배되며, 더 작지만 잠재적으로 더 의미 있는 객체는 종종 간과되어 편향된 성능 평가와 실질적인 저하를 초래합니다. 이 문제를 해결하기 위해 일반적인 크기 불변 평가(SIEva) 프레임워크를 제안합니다. 핵심 아이디어는 각 분리 가능한 구성 요소를 개별적으로 평가한 후 결과를 집계하여 객체 간의 크기 불균형 영향을 효과적으로 완화하는 것입니다. 이를 바탕으로, 우리는 크기 불변 원칙을 준수하고 다양한 크기의 주목 객체 검출을 크게 향상시키는 전용 최적화 프레임워크(SIOpt)를 개발합니다. 특히, SIOpt는 모델에 구애받지 않으며 다양한 SOD 백본과 원활하게 통합될 수 있습니다. 이론적으로, 우리는 또한 SOD 방법의 일반화 분석을 제시하고 새로운 평가 프로토콜의 타당성을 뒷받침하는 증거를 제공합니다. 마지막으로, 포괄적인 실험은 제안된 접근 방식의 효과를 입증합니다. 코드는 https://github.com/Ferry-Li/SI-SOD에서 제공됩니다.

## 📝 요약

이 논문은 주목 객체 검출(SOD)에서 평가 프로토콜의 크기 불변 속성 문제를 다룹니다. 기존 SOD 지표들이 크기 민감성을 가지고 있어, 큰 객체가 작은 객체보다 평가 결과에 더 큰 영향을 미치는 문제를 지적합니다. 이를 해결하기 위해, 각 객체의 크기를 개별적으로 평가하고 결과를 종합하는 크기 불변 평가(SIEva) 프레임워크를 제안합니다. 또한, 다양한 크기의 주목 객체를 효과적으로 검출할 수 있는 최적화 프레임워크(SIOpt)를 개발했습니다. SIOpt는 모델에 구애받지 않으며 다양한 SOD 백본과 통합될 수 있습니다. 이론적 분석과 실험 결과는 제안된 접근법의 효율성을 입증합니다. 코드는 [GitHub 링크](https://github.com/Ferry-Li/SI-SOD)에서 제공됩니다.

## 🎯 주요 포인트

- 1. 본 논문은 Salient Object Detection(SOD)에서 평가 프로토콜의 크기 불변 속성을 조사하며, 특히 크기가 크게 다른 여러 주목할 만한 객체가 하나의 이미지에 나타나는 시나리오를 다룹니다.
- 2. 기존 SOD 메트릭의 크기 민감성을 드러내기 위해 이론적 유도 과정을 통해 이미지 평가 결과가 여러 분리 가능한 항의 합으로 분해될 수 있음을 보여줍니다.
- 3. 크기 불균형 문제를 해결하기 위해 각 분리 가능한 구성 요소를 개별적으로 평가하고 결과를 집계하는 일반적인 크기 불변 평가(SIEva) 프레임워크를 제안합니다.
- 4. 크기 불변 원칙을 준수하고 다양한 크기의 주목할 만한 객체 탐지를 크게 향상시키는 전용 최적화 프레임워크(SIOpt)를 개발했습니다.
- 5. 제안된 접근 방식의 효능을 입증하는 포괄적인 실험 결과를 제시하며, 코드는 https://github.com/Ferry-Li/SI-SOD에서 제공됩니다.


---

*Generated on 2025-09-23 09:05:19*