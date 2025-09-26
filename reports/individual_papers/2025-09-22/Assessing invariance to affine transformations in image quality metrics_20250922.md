---
keywords:
  - Image Quality Metrics
  - Affine Transformations
  - Invisibility Threshold
  - Psychophysics
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2407.17927
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:44:41.467783",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Image Quality Metrics",
    "Affine Transformations",
    "Invisibility Threshold",
    "Psychophysics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Image Quality Metrics": 0.78,
    "Affine Transformations": 0.81,
    "Invisibility Threshold": 0.77,
    "Psychophysics": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "image quality metrics",
        "canonical": "Image Quality Metrics",
        "aliases": [
          "IQM",
          "image quality assessment"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's methodology and evaluation, offering a unique perspective on invariance.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "affine transformations",
        "canonical": "Affine Transformations",
        "aliases": [
          "affine changes",
          "geometric transformations"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for understanding the proposed evaluation methodology.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "invisibility threshold",
        "canonical": "Invisibility Threshold",
        "aliases": [
          "visibility threshold",
          "perceptual threshold"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for assessing image quality metrics.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "psychophysics",
        "canonical": "Psychophysics",
        "aliases": [
          "perceptual psychology",
          "sensory psychology"
        ],
        "category": "broad_technical",
        "rationale": "Provides the scientific basis for determining perceptual thresholds.",
        "novelty_score": 0.45,
        "connectivity_score": 0.83,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "methodology",
      "human opinion",
      "digital media"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "image quality metrics",
      "resolved_canonical": "Image Quality Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "affine transformations",
      "resolved_canonical": "Affine Transformations",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "invisibility threshold",
      "resolved_canonical": "Invisibility Threshold",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "psychophysics",
      "resolved_canonical": "Psychophysics",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.83,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Assessing invariance to affine transformations in image quality metrics

**Korean Title:** 이미지 품질 지표에서 아핀 변환에 대한 불변성 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2407.17927.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2407.17927](https://arxiv.org/abs/2407.17927)

## 🔗 유사한 논문
- [[2025-09-19/On the Role of Individual Differences in Current Approaches to Computational Image Aesthetics_20250919|On the Role of Individual Differences in Current Approaches to Computational Image Aesthetics]] (79.0% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence: Label Quality, Domain Shift, Bias and Evaluation Challenges]] (78.8% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (78.8% similar)
- [[2025-09-22/Where Fact Ends and Fairness Begins_ Redefining AI Bias Evaluation through Cognitive Biases_20250922|Where Fact Ends and Fairness Begins: Redefining AI Bias Evaluation through Cognitive Biases]] (78.8% similar)
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (78.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Psychophysics|Psychophysics]]
**🔗 Specific Connectable**: [[keywords/Affine Transformations|Affine Transformations]]
**⚡ Unique Technical**: [[keywords/Image Quality Metrics|Image Quality Metrics]], [[keywords/Invisibility Threshold|Invisibility Threshold]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.17927v3 Announce Type: replace-cross 
Abstract: Subjective image quality metrics are usually evaluated according to the correlation with human opinion in databases with distortions that may appear in digital media. However, these oversee affine transformations which may represent better the changes in the images actually happening in natural conditions. Humans can be particularly invariant to these natural transformations, as opposed to the digital ones.
  In this work, we propose a methodology to evaluate any image quality metric by assessing their invariance to affine transformations, specifically: rotation, translation, scaling, and changes in spectral illumination. Here, invariance refers to the fact that certain distances should be neglected if their values are below a threshold. This is what we call invisibility threshold of a metric. Our methodology consists of two elements: (1) the determination of a visibility threshold in a subjective representation common to every metric, and (2) a transduction from the distance values of the metric and this common representation. This common representation is based on subjective ratings of readily available image quality databases. We determine the threshold in such common representation (the first element) using accurate psychophysics. Then, the transduction (the second element) can be trivially fitted for any metric: with the provided threshold extension of the method to any metric is straightforward. We test our methodology with some well-established metrics and find that none of them show human-like invisibility thresholds.
  This means that tuning the models exclusively to predict the visibility of generic distortions may disregard other properties of human vision as for instance invariances or invisibility thresholds. The data and code are publicly available to test other metrics.

## 🔍 Abstract (한글 번역)

arXiv:2407.17927v3 발표 유형: 교차 대체  
초록: 주관적인 이미지 품질 지표는 일반적으로 디지털 미디어에서 나타날 수 있는 왜곡이 있는 데이터베이스에서 인간의 의견과의 상관관계에 따라 평가됩니다. 그러나 이러한 평가는 자연 조건에서 실제로 발생하는 이미지의 변화를 더 잘 나타낼 수 있는 아핀 변환을 간과합니다. 인간은 디지털 변환과 달리 이러한 자연 변환에 특히 불변일 수 있습니다. 

이 연구에서는 아핀 변환, 특히 회전, 평행 이동, 스케일링 및 스펙트럼 조명 변화에 대한 불변성을 평가하여 이미지 품질 지표를 평가하는 방법론을 제안합니다. 여기서 불변성은 특정 거리가 임계값 이하일 경우 무시되어야 한다는 사실을 의미합니다. 이를 우리는 지표의 비가시성 임계값이라고 부릅니다. 우리의 방법론은 두 가지 요소로 구성됩니다: (1) 모든 지표에 공통적인 주관적 표현에서 가시성 임계값의 결정, (2) 지표의 거리 값과 이 공통 표현 간의 변환. 이 공통 표현은 쉽게 접근할 수 있는 이미지 품질 데이터베이스의 주관적 평가에 기반합니다. 우리는 정확한 심리물리학을 사용하여 이러한 공통 표현(첫 번째 요소)에서 임계값을 결정합니다. 그런 다음, 변환(두 번째 요소)은 어떤 지표에도 쉽게 맞출 수 있습니다: 제공된 임계값 확장을 통해 어떤 지표에도 방법을 쉽게 적용할 수 있습니다. 우리는 몇 가지 잘 확립된 지표로 우리의 방법론을 테스트했으며, 그들 중 어느 것도 인간과 유사한 비가시성 임계값을 보여주지 않는다는 것을 발견했습니다.

이는 일반적인 왜곡의 가시성을 예측하기 위해 모델을 조정하는 것만으로는 예를 들어 불변성이나 비가시성 임계값과 같은 인간 시각의 다른 특성을 무시할 수 있음을 의미합니다. 데이터와 코드는 다른 지표를 테스트하기 위해 공개적으로 제공됩니다.

## 📝 요약

이 논문은 이미지 품질 평가 지표의 인간 의견과의 상관성을 평가할 때 디지털 미디어의 왜곡뿐만 아니라 자연 조건에서 발생하는 아핀 변환에 대한 불변성을 고려해야 한다고 주장합니다. 저자들은 회전, 이동, 크기 조정, 스펙트럼 조명 변화와 같은 아핀 변환에 대한 불변성을 평가하는 방법론을 제안합니다. 이 방법론은 두 가지 요소로 구성됩니다: (1) 모든 지표에 공통된 주관적 표현에서의 가시성 임계값 결정, (2) 지표의 거리 값과 이 공통 표현 간의 변환. 실험 결과, 기존의 이미지 품질 평가 지표는 인간과 유사한 불가시성 임계값을 보이지 않는 것으로 나타났습니다. 이는 일반적인 왜곡의 가시성 예측에만 초점을 맞추는 것이 인간 시각의 다른 특성을 간과할 수 있음을 시사합니다. 데이터와 코드는 공개되어 있어 다른 지표의 테스트가 가능합니다.

## 🎯 주요 포인트

- 1. 주관적 이미지 품질 지표는 디지털 미디어에서 나타날 수 있는 왜곡과의 상관관계를 통해 평가되지만, 자연 조건에서 실제로 발생하는 이미지 변화를 더 잘 나타낼 수 있는 아핀 변환을 간과하고 있다.
- 2. 본 연구에서는 회전, 평행 이동, 스케일링, 스펙트럼 조명 변화와 같은 아핀 변환에 대한 불변성을 평가하여 이미지 품질 지표를 평가하는 방법론을 제안한다.
- 3. 제안된 방법론은 모든 지표에 공통된 주관적 표현에서 가시성 임계값을 결정하고, 지표의 거리 값과 이 공통 표현 간의 변환을 포함한다.
- 4. 실험 결과, 기존의 이미지 품질 지표들은 인간과 유사한 불가시성 임계값을 보여주지 못한다는 것을 발견하였다.
- 5. 데이터와 코드는 다른 지표를 테스트할 수 있도록 공개되어 있다.


---

*Generated on 2025-09-23 09:44:41*