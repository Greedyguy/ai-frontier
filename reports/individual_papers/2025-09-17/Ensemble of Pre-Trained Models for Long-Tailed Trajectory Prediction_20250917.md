# Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction

**Korean Title:** 사전 학습된 모델 앙상블을 활용한 긴 꼬리 궤적 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Divya Thuremella|Divya Thuremella]] [[authors/Yi Yang|Yi Yang]] [[authors/Simon Wanna|Simon Wanna]] [[authors/Lars Kunze|Lars Kunze]] [[authors/Daniele De Martini|Daniele De Martini]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Confidence-weighted Average Method

## 🔗 유사한 논문
- [[STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (80.6% similar)
- [[NavMoE_ Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts_20250918|NavMoE Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (80.3% similar)
- [[Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.1% similar)
- [[Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (79.9% similar)
- [[Artificial neural networks ensemble methodology to predict significant wave height_20250917|Artificial neural networks ensemble methodology to predict significant wave height]] (79.8% similar)

## 📋 저자 정보

**Authors:** Divya Thuremella, Yi Yang, Simon Wanna, Lars Kunze, Daniele De Martini

## 📄 Abstract (원문)

This work explores the application of ensemble modeling to the
multidimensional regression problem of trajectory prediction for vehicles in
urban environments. As newer and bigger state-of-the-art prediction models for
autonomous driving continue to emerge, an important open challenge is the
problem of how to combine the strengths of these big models without the need
for costly re-training. We show how, perhaps surprisingly, combining
state-of-the-art deep learning models out-of-the-box (without retraining or
fine-tuning) with a simple confidence-weighted average method can enhance the
overall prediction. Indeed, while combining trajectory prediction models is not
straightforward, this simple approach enhances performance by 10% over the best
prediction model, especially in the long-tailed metrics. We show that this
performance improvement holds on both the NuScenes and Argoverse datasets, and
that these improvements are made across the dataset distribution. The code for
our work is open source.

## 🔍 Abstract (한글 번역)

이 연구는 도시 환경에서 차량의 궤적 예측을 위한 다차원 회귀 문제에 앙상블 모델링을 적용하는 것을 탐구합니다. 자율 주행을 위한 최신의 대규모 예측 모델들이 계속해서 등장함에 따라, 이러한 대형 모델들의 강점을 비용이 많이 드는 재훈련 없이 결합하는 문제가 중요한 미해결 과제로 남아 있습니다. 우리는, 아마도 놀랍게도, 최신의 심층 학습 모델들을 재훈련이나 미세 조정 없이 간단한 신뢰도 가중 평균 방법과 결합함으로써 전체적인 예측 성능을 향상시킬 수 있음을 보여줍니다. 실제로 궤적 예측 모델을 결합하는 것이 간단하지는 않지만, 이 간단한 접근법은 특히 긴 꼬리 메트릭에서 최고의 예측 모델보다 성능을 10% 향상시킵니다. 우리는 이 성능 향상이 NuScenes 및 Argoverse 데이터셋 모두에서 유효하며, 이러한 개선이 데이터셋 분포 전반에 걸쳐 이루어졌음을 보여줍니다. 우리의 연구 코드는 오픈 소스로 제공됩니다.

## 📝 요약

이 연구는 도시 환경에서 차량 경로 예측을 위한 다차원 회귀 문제에 앙상블 모델링을 적용한 것이다. 최신 예측 모델을 결합하여 재훈련 없이 성능을 향상시키는 방법론을 제안한다. 본 연구에서는 최첨단 딥러닝 모델들을 재훈련이나 미세 조정 없이 단순한 신뢰도 가중 평균 방법으로 결합하여 예측 성능을 개선할 수 있음을 보여준다. 이 방법은 특히 긴 꼬리 분포에서 성능을 10% 향상시켰으며, NuScenes와 Argoverse 데이터셋에서 유효성을 입증했다. 연구의 코드는 오픈 소스로 제공된다.

## 🎯 주요 포인트

- 1. 이 연구는 도시 환경에서 차량의 궤적 예측을 위한 다차원 회귀 문제에 앙상블 모델링을 적용합니다.

- 2. 최신 예측 모델들을 결합하여 재훈련 없이 성능을 향상시키는 방법을 제안합니다.

- 3. 간단한 신뢰도 가중 평균 방법을 사용하여 예측 성능을 10% 향상시켰습니다.

- 4. NuScenes와 Argoverse 데이터셋에서 성능 향상이 확인되었으며, 데이터셋 전반에 걸쳐 개선이 이루어졌습니다.

- 5. 연구의 코드는 오픈 소스로 제공됩니다.

---

*Generated on 2025-09-20 09:24:15*