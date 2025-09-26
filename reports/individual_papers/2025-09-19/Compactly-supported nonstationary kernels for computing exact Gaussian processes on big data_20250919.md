---
keywords:
  - Gaussian Processes
  - Uncertainty Quantification
  - Scalable Gaussian Processes
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2411.05869
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:52:03.136659",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Processes",
    "Uncertainty Quantification",
    "Scalable Gaussian Processes"
  ],
  "rejected_keywords": [
    "Nonstationary Kernels"
  ],
  "similarity_scores": {
    "Gaussian Processes": 0.78,
    "Uncertainty Quantification": 0.77,
    "Scalable Gaussian Processes": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data

**Korean Title:** 대규모 데이터에서 정확한 가우시안 프로세스를 계산하기 위한 컴팩트 지지 비정상 커널

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Gaussian Processes|Gaussian Processes]]
**🔗 Specific Connectable**: [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**🚀 Evolved Concepts**: [[keywords/Scalable Gaussian Processes|Scalable Gaussian Processes]]

## 🔗 유사한 논문
- [[Learning quantum many-body data locally A provably scalable framework]] (78.0% similar)
- [[Lightweight_Gradient-Aware_Upscaling_of_3D_Gaussian_Splatting_Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (77.9% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.2% similar)
- [[Tabular Data Generation Models An In-Depth Survey and Performance Benchmarks with Extensive Tuning]] (77.1% similar)
- [[Online_reinforcement_learning_via_sparse_Gaussian_mixture_model_Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.05869v3 Announce Type: replace-cross 
Abstract: The Gaussian process (GP) is a widely used probabilistic machine learning method with implicit uncertainty characterization for stochastic function approximation, stochastic modeling, and analyzing real-world measurements of nonlinear processes. Traditional implementations of GPs involve stationary kernels (also termed covariance functions) that limit their flexibility, and exact methods for inference that prevent application to data sets with more than about ten thousand points. Modern approaches to address stationarity assumptions generally fail to accommodate large data sets, while all attempts to address scalability focus on approximating the Gaussian likelihood, which can involve subjectivity and lead to inaccuracies. In this work, we explicitly derive an alternative kernel that can discover and encode both sparsity and nonstationarity. We embed the kernel within a fully Bayesian GP model and leverage high-performance computing resources to enable the analysis of massive data sets. We demonstrate the favorable performance of our novel kernel relative to existing exact and approximate GP methods across a variety of synthetic data examples. Furthermore, we conduct space-time prediction based on more than one million measurements of daily maximum temperature and verify that our results outperform state-of-the-art methods in the Earth sciences. More broadly, having access to exact GPs that use ultra-scalable, sparsity-discovering, nonstationary kernels allows GP methods to truly compete with a wide variety of machine learning methods.

## 🔍 Abstract (한글 번역)

arXiv:2411.05869v3 발표 유형: 교차 교체  
초록: 가우시안 프로세스(GP)는 확률적 함수 근사, 확률적 모델링, 비선형 프로세스의 실제 측정 분석을 위한 암묵적인 불확실성 특성을 가진 널리 사용되는 확률적 기계 학습 방법입니다. 전통적인 GP 구현은 유연성을 제한하는 정적 커널(공분산 함수라고도 함)과 약 만 개 이상의 데이터 포인트에 대한 적용을 방해하는 정확한 추론 방법을 포함합니다. 정적 가정에 대한 현대적 접근 방식은 일반적으로 대규모 데이터 세트를 수용하지 못하며, 확장성 문제를 해결하려는 모든 시도는 주관성을 수반할 수 있고 부정확성을 초래할 수 있는 가우시안 가능성을 근사하는 데 초점을 맞추고 있습니다. 이 연구에서는 희소성과 비정적성을 발견하고 인코딩할 수 있는 대체 커널을 명시적으로 도출합니다. 우리는 이 커널을 완전한 베이지안 GP 모델에 내장하고 고성능 컴퓨팅 자원을 활용하여 대규모 데이터 세트를 분석할 수 있게 합니다. 우리는 다양한 합성 데이터 예제에서 기존의 정확하고 근사적인 GP 방법과 비교하여 우리의 새로운 커널의 우수한 성능을 입증합니다. 또한, 일일 최고 기온의 백만 개 이상의 측정을 기반으로 시공간 예측을 수행하고, 지구 과학 분야에서 최첨단 방법보다 우리의 결과가 더 우수하다는 것을 검증합니다. 더 넓게는, 초확장 가능하고 희소성을 발견하는 비정적 커널을 사용하는 정확한 GP에 접근할 수 있게 됨으로써, GP 방법이 다양한 기계 학습 방법과 진정으로 경쟁할 수 있게 됩니다.

## 📝 요약

이 논문에서는 비정상성과 희소성을 발견하고 인코딩할 수 있는 새로운 커널을 제안하여 전통적인 가우시안 프로세스(GP)의 한계를 극복합니다. 이 커널은 대규모 데이터 세트를 분석할 수 있도록 고성능 컴퓨팅 자원과 결합된 완전한 베이지안 GP 모델에 내장됩니다. 제안된 방법은 기존의 정확한 및 근사 GP 방법보다 다양한 합성 데이터 예제에서 우수한 성능을 보였으며, 일일 최고 기온의 백만 개 이상의 측정치를 기반으로 한 시공간 예측에서 지구 과학 분야의 최신 방법보다 뛰어난 결과를 제공합니다. 이 연구는 초대형 데이터 세트에 적용 가능한 비정상 커널을 통해 GP 방법이 다양한 머신러닝 방법과 경쟁할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구에서는 희소성과 비정상성을 발견하고 인코딩할 수 있는 대체 커널을 명시적으로 도출하였습니다.

- 2. 제안된 커널을 완전한 베이지안 GP 모델에 내장하여 대규모 데이터 세트 분석을 가능하게 하였습니다.

- 3. 제안된 커널은 기존의 정확한 및 근사 GP 방법들보다 다양한 합성 데이터 예제에서 우수한 성능을 보였습니다.

- 4. 일일 최고 기온의 백만 개 이상의 측정을 기반으로 시공간 예측을 수행하여 지구 과학 분야의 최신 방법보다 우수한 결과를 입증하였습니다.

- 5. 초대규모, 희소성 발견, 비정상 커널을 사용하는 정확한 GP 접근 방식은 다양한 머신러닝 방법들과 진정으로 경쟁할 수 있게 합니다.

---

*Generated on 2025-09-19 15:43:18*