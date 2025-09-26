---
keywords:
  - Transit Light Curve Analysis
  - Deep Learning
  - Fourier Analysis
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:37:13.822405",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transit Light Curve Analysis",
    "Deep Learning",
    "Fourier Analysis"
  ],
  "rejected_keywords": [
    "Shape Reconstruction"
  ],
  "similarity_scores": {
    "Transit Light Curve Analysis": 0.8,
    "Deep Learning": 0.85,
    "Fourier Analysis": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Beyond Spherical geometry: Unraveling complex features of objects orbiting around stars from its transit light curve using deep learning

**Korean Title:** 구면 기하학을 넘어서: 심층 학습을 활용한 항성 주위를 공전하는 물체의 복잡한 특징을 통과 광곡선으로부터 해명하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|deep neural networks]]
**🔗 Specific Connectable**: [[keywords/Fourier Analysis|Fourier coefficients]]
**⚡ Unique Technical**: [[keywords/Transit Light Curve Analysis|transit light curve]]

## 🔗 유사한 논문
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.1% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (77.2% similar)
- [[Sensing the Shape of Data_ Non-Visual Exploration of Statistical Concepts in Histograms with Blind and Low-Vision Learners_20250919|Sensing the Shape of Data Non-Visual Exploration of Statistical Concepts in Histograms with Blind and Low-Vision Learners]] (76.6% similar)
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (76.5% similar)
- [[Generalizable Geometric Image Caption Synthesis_20250919|Generalizable Geometric Image Caption Synthesis]] (76.4% similar)

## 📋 저자 정보

**Authors:** Ushasi Bhowmick, Shivam Kumaran

## 📄 Abstract (원문)

Characterizing the geometry of an object orbiting around a star from its
transit light curve is a powerful tool to uncover various complex phenomena.
This problem is inherently ill-posed, since similar or identical light curves
can be produced by multiple different shapes. In this study, we investigate the
extent to which the features of a shape can be embedded in a transit light
curve. We generate a library of two-dimensional random shapes and simulate
their transit light curves with light curve simulator, Yuti. Each shape is
decomposed into a series of elliptical components expressed in the form of
Fourier coefficients that adds increasingly diminishing perturbations to an
ideal ellipse. We train deep neural networks to predict these Fourier
coefficients directly from simulated light curves. Our results demonstrate that
the neural network can successfully reconstruct the low-order ellipses, which
describe overall shape, orientation and large-scale perturbations. For higher
order ellipses the scale is successfully determined but the inference of
eccentricity and orientation is limited, demonstrating the extent of shape
information in the light curve. We explore the impact of non-convex shape
features in reconstruction, and show its dependence on shape orientation. The
level of reconstruction achieved by the neural network underscores the utility
of using light curves as a means to extract geometric information from
transiting systems.

## 🔍 Abstract (한글 번역)

별 주위를 공전하는 물체의 기하학적 특성을 통과 광곡선으로부터 특성화하는 것은 다양한 복잡한 현상을 밝혀내는 강력한 도구입니다. 이 문제는 본질적으로 잘못 설정된 문제인데, 이는 유사하거나 동일한 광곡선이 여러 다른 형태에 의해 생성될 수 있기 때문입니다. 본 연구에서는 형태의 특징이 통과 광곡선에 어느 정도까지 내재될 수 있는지를 조사합니다. 우리는 이차원 임의 형태의 라이브러리를 생성하고, 광곡선 시뮬레이터인 Yuti를 사용하여 그들의 통과 광곡선을 시뮬레이션합니다. 각 형태는 점점 줄어드는 변형을 이상적인 타원에 추가하는 푸리에 계수 형태로 표현된 일련의 타원 성분으로 분해됩니다. 우리는 심층 신경망을 훈련시켜 시뮬레이션된 광곡선으로부터 이러한 푸리에 계수를 직접 예측합니다. 우리의 결과는 신경망이 전체적인 형태, 방향 및 대규모 변형을 설명하는 저차 타원을 성공적으로 재구성할 수 있음을 보여줍니다. 고차 타원의 경우, 규모는 성공적으로 결정되지만 이심률과 방향의 추론은 제한적이며, 이는 광곡선에 포함된 형태 정보의 범위를 보여줍니다. 우리는 재구성에서 비볼록 형태의 특징이 미치는 영향을 탐구하고, 형태 방향에 대한 의존성을 보여줍니다. 신경망에 의해 달성된 재구성 수준은 통과 시스템으로부터 기하학적 정보를 추출하는 수단으로서 광곡선을 사용하는 유용성을 강조합니다.

## 📝 요약

이 연구는 항성을 도는 물체의 통과 광곡선에서 형상의 기하학적 정보를 추출하는 방법을 제시합니다. 다양한 2차원 무작위 형태의 광곡선을 시뮬레이션하고, 이를 통해 얻은 데이터를 사용하여 심층 신경망을 훈련시켰습니다. 연구 결과, 신경망은 저차 타원 요소를 성공적으로 재구성하여 전체적인 형태와 방향, 대규모 변형을 설명할 수 있었습니다. 고차 타원에서는 크기는 잘 예측되었으나 이심률과 방향 추론에는 한계가 있었습니다. 비볼록 형태의 재구성은 형태의 방향에 따라 달라졌으며, 이는 광곡선을 통해 기하학적 정보를 추출하는 데 유용함을 보여줍니다.

## 🎯 주요 포인트

- 1. 천체의 통과 광곡선을 통해 물체의 기하학적 특성을 분석하는 것은 복잡한 현상을 밝히는 강력한 도구입니다.

- 2. 유사하거나 동일한 광곡선이 여러 다른 형태에 의해 생성될 수 있어 이 문제는 본질적으로 잘못 설정된 문제입니다.

- 3. 연구에서는 2차원 랜덤 형태의 도서관을 생성하고, 이를 통해 생성된 광곡선을 심층 신경망으로 분석하여 푸리에 계수를 예측합니다.

- 4. 신경망은 저차원 타원을 성공적으로 재구성하여 전체적인 형태, 방향 및 대규모 변형을 설명할 수 있습니다.

- 5. 비볼록 형태의 특징이 재구성에 미치는 영향을 탐구하며, 형태의 방향에 따라 그 의존성을 보여줍니다.

---

*Generated on 2025-09-20 02:45:48*