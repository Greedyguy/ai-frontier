---
keywords:
  - Diffusion Models
  - Optimal Transport
  - Optimization
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:51:10.730463",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Optimal Transport",
    "Optimization"
  ],
  "rejected_keywords": [
    "Beta Distributions"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.9,
    "Optimal Transport": 0.8,
    "Optimization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Masked Diffusion Models as Energy Minimization

**Korean Title:** 마스크드 확산 모델의 에너지 최소화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|energy minimization]]
**🔗 Specific Connectable**: [[keywords/Diffusion Models|masked diffusion models]]
**⚡ Unique Technical**: [[keywords/Optimal Transport|discrete optimal transport]]

## 🔗 유사한 논문
- [[Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (80.9% similar)
- [[Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization_20250919|Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization]] (79.2% similar)
- [[TICA-Based Free Energy Matching for Machine-Learned Molecular Dynamics_20250918|TICA-Based Free Energy Matching for Machine-Learned Molecular Dynamics]] (79.1% similar)
- [[Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (78.8% similar)
- [[Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (78.3% similar)

## 📋 저자 정보

**Authors:** Sitong Chen, Shen Nie, Jiacheng Sun, Zijin Feng, Zhenguo Li, Ji-Rong Wen, Chongxuan Li

## 📄 Abstract (원문)

We present a systematic theoretical framework that interprets masked
diffusion models (MDMs) as solutions to energy minimization problems in
discrete optimal transport. Specifically, we prove that three distinct energy
formulations--kinetic, conditional kinetic, and geodesic energy--are
mathematically equivalent under the structure of MDMs, and that MDMs minimize
all three when the mask schedule satisfies a closed-form optimality condition.
This unification not only clarifies the theoretical foundations of MDMs, but
also motivates practical improvements in sampling. By parameterizing
interpolation schedules via Beta distributions, we reduce the schedule design
space to a tractable 2D search, enabling efficient post-training tuning without
model modification. Experiments on synthetic and real-world benchmarks
demonstrate that our energy-inspired schedules outperform hand-crafted
baselines, particularly in low-step sampling settings.

## 🔍 Abstract (한글 번역)

우리는 마스킹 확산 모델(MDMs)을 이산 최적 수송의 에너지 최소화 문제의 해로 해석하는 체계적인 이론적 틀을 제시합니다. 구체적으로, 우리는 세 가지 서로 다른 에너지 공식--운동 에너지, 조건부 운동 에너지, 그리고 측지 에너지--가 MDM의 구조 하에서 수학적으로 동등하며, 마스크 스케줄이 닫힌 형태의 최적 조건을 만족할 때 MDM이 세 가지 모두를 최소화한다는 것을 증명합니다. 이러한 통합은 MDM의 이론적 기초를 명확히 할 뿐만 아니라 샘플링의 실질적인 개선을 촉진합니다. 베타 분포를 통해 보간 스케줄을 매개변수화함으로써, 우리는 스케줄 설계 공간을 다루기 쉬운 2차원 탐색으로 줄여 모델 수정 없이 효율적인 사후 학습 조정을 가능하게 합니다. 합성 및 실제 벤치마크 실험에서 우리의 에너지 기반 스케줄이 수작업으로 제작된 기준선을 능가하며, 특히 저단계 샘플링 설정에서 뛰어난 성능을 보임을 입증합니다.

## 📝 요약

이 논문은 마스크 확산 모델(MDMs)을 이산 최적 수송의 에너지 최소화 문제로 해석하는 이론적 틀을 제시합니다. 세 가지 에너지 공식(운동 에너지, 조건부 운동 에너지, 측지 에너지)이 MDMs 구조에서 수학적으로 동등하며, 특정 조건을 만족하는 마스크 일정에서 MDMs가 이를 최소화함을 증명합니다. 이 통합은 MDMs의 이론적 기초를 명확히 하고, 샘플링의 실질적 개선을 촉진합니다. 베타 분포를 통한 보간 일정 매개변수화로 일정 설계 공간을 2D 검색으로 축소하여 모델 수정 없이 효율적인 사후 튜닝이 가능합니다. 실험 결과, 에너지 기반 일정이 특히 저단계 샘플링 환경에서 수작업 기준을 능가함을 보여줍니다.

## 🎯 주요 포인트

- 1. 마스크 확산 모델(MDMs)은 이산 최적 수송의 에너지 최소화 문제의 해로 해석됩니다.

- 2. 세 가지 에너지 공식(운동, 조건부 운동, 측지 에너지)이 MDMs 구조 하에서 수학적으로 동등함을 증명했습니다.

- 3. MDMs는 마스크 스케줄이 폐쇄형 최적 조건을 만족할 때 세 가지 에너지를 모두 최소화합니다.

- 4. 베타 분포를 통한 보간 스케줄 매개변수화로 스케줄 설계 공간을 2D 탐색으로 축소하여 효율적인 사후 튜닝을 가능하게 합니다.

- 5. 실험 결과, 에너지 기반 스케줄이 저단계 샘플링 설정에서 수작업 기반 기준보다 우수한 성능을 보였습니다.

---

*Generated on 2025-09-20 09:27:47*