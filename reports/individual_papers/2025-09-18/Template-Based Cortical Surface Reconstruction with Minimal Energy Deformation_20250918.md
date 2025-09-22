# Template-Based Cortical Surface Reconstruction with Minimal Energy Deformation

**Korean Title:** 최소 에너지 변형을 통한 템플릿 기반 대뇌 피질 표면 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Patrick Madlindl|Patrick Madlindl]] [[authors/Fabian Bongratz|Fabian Bongratz]] [[authors/Christian Wachinger|Christian Wachinger]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Learning-Based Cortical Surface Reconstruction

## 🔗 유사한 논문
- [[Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (78.8% similar)
- [[Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (77.4% similar)
- [[Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (77.2% similar)
- [[Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease_20250918|Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease]] (77.1% similar)
- [[UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (76.9% similar)

## 📋 저자 정보

**Authors:** Patrick Madlindl, Fabian Bongratz, Christian Wachinger

## 📄 Abstract (원문)

Cortical surface reconstruction (CSR) from magnetic resonance imaging (MRI)
is fundamental to neuroimage analysis, enabling morphological studies of the
cerebral cortex and functional brain mapping. Recent advances in learning-based
CSR have dramatically accelerated processing, allowing for reconstructions
through the deformation of anatomical templates within seconds. However,
ensuring the learned deformations are optimal in terms of deformation energy
and consistent across training runs remains a particular challenge. In this
work, we design a Minimal Energy Deformation (MED) loss, acting as a
regularizer on the deformation trajectories and complementing the widely used
Chamfer distance in CSR. We incorporate it into the recent V2C-Flow model and
demonstrate considerable improvements in previously neglected training
consistency and reproducibility without harming reconstruction accuracy and
topological correctness.

## 🔍 Abstract (한글 번역)

자기공명영상(MRI)으로부터의 피질 표면 재구성(Cortical Surface Reconstruction, CSR)은 신경 영상 분석의 기초로, 대뇌 피질의 형태학적 연구와 기능적 뇌 매핑을 가능하게 합니다. 최근 학습 기반 CSR의 발전은 처리 속도를 획기적으로 가속화하여, 해부학적 템플릿의 변형을 통해 몇 초 안에 재구성을 가능하게 했습니다. 그러나 학습된 변형이 변형 에너지 측면에서 최적이며, 훈련 실행 간 일관성을 유지하는 것은 여전히 특별한 도전 과제로 남아 있습니다. 본 연구에서는 변형 경로에 대한 정규화자로 작용하며 CSR에서 널리 사용되는 샴퍼 거리(Chamfer distance)를 보완하는 최소 에너지 변형(Minimal Energy Deformation, MED) 손실을 설계하였습니다. 이를 최근의 V2C-Flow 모델에 통합하여, 재구성 정확도와 위상적 정확성을 해치지 않으면서 이전에 간과되었던 훈련의 일관성과 재현성에서 상당한 개선을 입증하였습니다.

## 📝 요약

이 논문은 자기공명영상(MRI)에서 대뇌 피질 표면을 재구성하는 과정에서 발생하는 변형 에너지를 최소화하는 새로운 손실 함수인 최소 에너지 변형(MED) 손실을 제안합니다. 이 방법은 기존의 Chamfer 거리와 함께 사용되어, V2C-Flow 모델에 통합되었습니다. 이를 통해 재구성 정확도와 위상적 정확성을 유지하면서도 훈련의 일관성과 재현성을 크게 개선하였습니다. 이 연구는 학습 기반의 피질 표면 재구성에서 변형 에너지를 최적화하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 자기공명영상(MRI) 기반의 피질 표면 재구성(CSR)은 대뇌 피질의 형태학적 연구와 기능적 뇌 매핑에 필수적이다.

- 2. 학습 기반 CSR의 최근 발전은 해부학적 템플릿의 변형을 통해 몇 초 만에 재구성을 가능하게 하여 처리 속도를 크게 향상시켰다.

- 3. 본 연구에서는 변형 경로에 대한 정규화 역할을 하는 최소 에너지 변형(MED) 손실을 설계하여 CSR에서 널리 사용되는 챔퍼 거리와 보완적으로 작용하도록 하였다.

- 4. MED 손실을 최신 V2C-Flow 모델에 통합하여 재구성 정확도와 위상적 정확성을 해치지 않으면서 훈련 일관성과 재현성을 크게 개선하였다.

---

*Generated on 2025-09-20 02:49:32*