---
keywords:
  - Self-Supervised Learning
  - Dependency Controlled Pre-training
  - Instance-wise Patch Normalization
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:33:24.537285",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-Supervised Learning",
    "Dependency Controlled Pre-training",
    "Instance-wise Patch Normalization"
  ],
  "rejected_keywords": [
    "Hierarchical Dependency Controlled Learning",
    "Instance-level Contrastive Module"
  ],
  "similarity_scores": {
    "Self-Supervised Learning": 0.82,
    "Dependency Controlled Pre-training": 0.78,
    "Instance-wise Patch Normalization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# DeCoP: Enhancing Self-Supervised Time Series Representation with Dependency Controlled Pre-training

**Korean Title:** DeCoP: 종속성 제어 사전 훈련을 통한 자기 지도형 시계열 표현 향상

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-Supervised Learning|Self-Supervised Time Series Representation]]
**⚡ Unique Technical**: [[keywords/Dependency Controlled Pre-training|Dependency Controlled Pre-training]], [[keywords/Instance-wise Patch Normalization|Instance-wise Patch Normalization]]

## 🔗 유사한 논문
- [[Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (78.7% similar)
- [[Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (78.3% similar)
- [[DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250918|DPANet Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (77.8% similar)
- [[Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (77.7% similar)
- [[ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (77.0% similar)

## 📋 저자 정보

**Authors:** Yuemin Wu, Zhongze Wu, Xiu Su, Feng Yang, Hongyan Xu, Xi Lin, Wenti Huang, Shan You, Chang Xu

## 📄 Abstract (원문)

Modeling dynamic temporal dependencies is a critical challenge in time series
pre-training, which evolve due to distribution shifts and multi-scale patterns.
This temporal variability severely impairs the generalization of pre-trained
models to downstream tasks. Existing frameworks fail to capture the complex
interactions of short- and long-term dependencies, making them susceptible to
spurious correlations that degrade generalization. To address these
limitations, we propose DeCoP, a Dependency Controlled Pre-training framework
that explicitly models dynamic, multi-scale dependencies by simulating evolving
inter-patch dependencies. At the input level, DeCoP introduces Instance-wise
Patch Normalization (IPN) to mitigate distributional shifts while preserving
the unique characteristics of each patch, creating a robust foundation for
representation learning. At the latent level, a hierarchical Dependency
Controlled Learning (DCL) strategy explicitly models inter-patch dependencies
across multiple temporal scales, with an Instance-level Contrastive Module
(ICM) enhances global generalization by learning instance-discriminative
representations from time-invariant positive pairs. DeCoP achieves
state-of-the-art results on ten datasets with lower computing resources,
improving MSE by 3% on ETTh1 over PatchTST using only 37% of the FLOPs.

## 🔍 Abstract (한글 번역)

동적 시간 의존성을 모델링하는 것은 시계열 사전 학습에서 중요한 과제입니다. 이는 분포 변화와 다중 스케일 패턴으로 인해 진화합니다. 이러한 시간적 변동성은 사전 학습된 모델의 다운스트림 작업에 대한 일반화를 심각하게 저해합니다. 기존의 프레임워크는 단기 및 장기 의존성의 복잡한 상호작용을 포착하지 못하여, 일반화를 저해하는 잘못된 상관관계에 취약합니다. 이러한 한계를 해결하기 위해, 우리는 DeCoP(Dependency Controlled Pre-training)라는 프레임워크를 제안합니다. 이는 진화하는 패치 간 의존성을 시뮬레이션하여 동적이고 다중 스케일의 의존성을 명시적으로 모델링합니다. 입력 수준에서 DeCoP는 인스턴스별 패치 정규화(IPN)를 도입하여 각 패치의 고유한 특성을 유지하면서 분포 변화를 완화하여 표현 학습을 위한 견고한 기반을 만듭니다. 잠재 수준에서는 계층적 의존성 제어 학습(DCL) 전략이 여러 시간적 스케일에 걸쳐 패치 간 의존성을 명시적으로 모델링하며, 인스턴스 수준의 대조 모듈(ICM)은 시간 불변의 긍정 쌍에서 인스턴스 구별 표현을 학습하여 전반적인 일반화를 향상시킵니다. DeCoP는 10개의 데이터셋에서 최첨단 결과를 달성하며, PatchTST 대비 ETTh1에서 MSE를 3% 개선하면서도 연산 자원을 37%만 사용하여 성능을 향상시킵니다.

## 📝 요약

DeCoP는 시계열 데이터의 동적 시간 의존성을 효과적으로 모델링하기 위한 프레임워크로, 기존 모델들이 단기 및 장기 의존성의 복잡한 상호작용을 포착하지 못하는 문제를 해결합니다. DeCoP는 인스턴스별 패치 정규화(IPN)를 통해 분포 변화에 대응하고, 계층적 의존성 제어 학습(DCL) 전략으로 여러 시간 규모에 걸친 패치 간 의존성을 명시적으로 모델링합니다. 또한, 인스턴스 수준 대조 모듈(ICM)을 통해 전역 일반화를 강화합니다. DeCoP는 10개의 데이터셋에서 최첨단 성능을 보이며, PatchTST 대비 37%의 연산 자원으로 ETTh1에서 MSE를 3% 개선했습니다.

## 🎯 주요 포인트

- 1. 시간적 의존성 모델링은 시계열 사전 학습에서 중요한 도전 과제로, 분포 변화와 다중 스케일 패턴으로 인해 발전합니다.

- 2. 기존 프레임워크는 단기 및 장기 의존성의 복잡한 상호작용을 포착하지 못하여 일반화 성능이 저하됩니다.

- 3. DeCoP는 동적, 다중 스케일 의존성을 명시적으로 모델링하여 이러한 제한을 극복합니다.

- 4. 입력 수준에서 DeCoP는 인스턴스별 패치 정규화를 도입하여 분포 변화 완화와 패치의 고유 특성을 보존합니다.

- 5. DeCoP는 10개 데이터셋에서 최첨단 결과를 달성하며, PatchTST 대비 37%의 FLOPs만으로 MSE를 3% 개선합니다.

---

*Generated on 2025-09-20 05:47:31*