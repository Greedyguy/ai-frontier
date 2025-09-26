---
keywords:
  - Background-Oriented Schlieren Tomography
  - Neural Networks
  - Volumetric Indoor Airflow Estimation
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:53:03.316291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Background-Oriented Schlieren Tomography",
    "Neural Networks",
    "Volumetric Indoor Airflow Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Background-Oriented Schlieren Tomography": 0.8,
    "Neural Networks": 0.78,
    "Volumetric Indoor Airflow Estimation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Indoor Airflow Imaging Using Physics-Informed Background-Oriented Schlieren Tomography

**Korean Title:** 물리학에 기반한 배경 지향 슐리렌 단층촬영을 이용한 실내 공기 흐름 영상화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|Physics-Informed Neural Network]]
**⚡ Unique Technical**: [[keywords/Background-Oriented Schlieren Tomography|Background-Oriented Schlieren Tomography]], [[keywords/Volumetric Indoor Airflow Estimation|Volumetric Indoor Airflow Estimation]]

## 🔗 유사한 논문
- [[Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (77.3% similar)
- [[Physically-based Lighting Generation for Robotic Manipulation_20250919|Physically-based Lighting Generation for Robotic Manipulation]] (77.0% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (76.9% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (76.4% similar)
- [[Barometer-Aided Attitude Estimation_20250918|Barometer-Aided Attitude Estimation]] (76.2% similar)

## 📋 저자 정보

**Authors:** Arjun Teh, Wael H. Ali, Joshua Rapp, Hassan Mansour

## 📄 Abstract (원문)

We develop a framework for non-invasive volumetric indoor airflow estimation
from a single viewpoint using background-oriented schlieren (BOS) measurements
and physics-informed reconstruction. Our framework utilizes a light projector
that projects a pattern onto a target back-wall and a camera that observes
small distortions in the light pattern. While the single-view BOS tomography
problem is severely ill-posed, our proposed framework addresses this using: (1)
improved ray tracing, (2) a physics-based light rendering approach and loss
formulation, and (3) a physics-based regularization using a physics-informed
neural network (PINN) to ensure that the reconstructed airflow is consistent
with the governing equations for buoyancy-driven flows.

## 🔍 Abstract (한글 번역)

우리는 배경 지향 슐리렌(BOS) 측정과 물리 기반 재구성을 사용하여 단일 관점에서 비침습적인 실내 공기 흐름의 체적 추정을 위한 프레임워크를 개발합니다. 우리의 프레임워크는 목표 배경 벽에 패턴을 투사하는 광 프로젝터와 빛 패턴의 작은 왜곡을 관찰하는 카메라를 활용합니다. 단일 관점 BOS 단층촬영 문제는 심각하게 잘못 설정되어 있지만, 우리의 제안된 프레임워크는 다음을 통해 이를 해결합니다: (1) 개선된 광선 추적, (2) 물리 기반의 빛 렌더링 접근법과 손실 공식화, (3) 물리 기반의 정규화를 통한 물리 정보 신경망(PINN)을 사용하여 재구성된 공기 흐름이 부력에 의해 유도된 흐름의 지배 방정식과 일치하도록 보장합니다.

## 📝 요약

이 연구는 배경 지향 슐리렌(BOS) 측정과 물리학 기반 재구성을 통해 단일 관점에서 비침습적으로 실내 공기 흐름을 추정하는 프레임워크를 개발했습니다. 이 프레임워크는 패턴을 벽에 투사하는 프로젝터와 이를 관찰하는 카메라를 사용하여 빛 패턴의 작은 왜곡을 감지합니다. 단일 관점 BOS 단층 촬영 문제의 심각한 불완전성을 해결하기 위해, (1) 개선된 광선 추적, (2) 물리 기반의 빛 렌더링 접근법과 손실 공식화, (3) 물리학을 반영한 신경망(PINN)을 통한 물리 기반 정규화를 사용하여 부력에 의해 유도된 흐름의 지배 방정식과 일치하는 공기 흐름을 재구성합니다. 주요 기여는 이러한 방법론을 통해 정확한 실내 공기 흐름 추정을 가능하게 한 점입니다.

## 🎯 주요 포인트

- 1. 비침습적인 실내 공기 흐름 추정을 위한 단일 관점의 BOS 측정 및 물리 기반 재구성 프레임워크를 개발했습니다.

- 2. 프레임워크는 패턴을 투사하는 조명 프로젝터와 패턴의 작은 왜곡을 관찰하는 카메라를 활용합니다.

- 3. 단일 관점 BOS 단층 촬영 문제의 심각한 불완전성을 개선된 광선 추적과 물리 기반 조명 렌더링 접근법 및 손실 공식으로 해결합니다.

- 4. 물리 기반 신경망(PINN)을 사용한 물리 기반 정규화를 통해 재구성된 공기 흐름이 부력에 의해 유도되는 흐름의 지배 방정식과 일치하도록 보장합니다.

---

*Generated on 2025-09-20 05:56:44*