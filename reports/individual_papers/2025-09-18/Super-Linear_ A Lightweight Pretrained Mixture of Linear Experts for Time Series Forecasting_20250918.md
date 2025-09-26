---
keywords:
  - Mixture of Experts
  - Time Series Forecasting
  - Zero-Shot Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:08:31.243786",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture of Experts",
    "Time Series Forecasting",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [
    "Spectral Gating Mechanism"
  ],
  "similarity_scores": {
    "Mixture of Experts": 0.82,
    "Time Series Forecasting": 0.8,
    "Zero-Shot Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Super-Linear: A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting

**Korean Title:** 초선형: 시계열 예측을 위한 경량 사전 학습 선형 전문가 혼합 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Time Series Forecasting|Time Series Forecasting]]
**🔗 Specific Connectable**: [[keywords/Mixture of Experts|Mixture of Experts]], [[keywords/Zero-Shot Learning|Zero-Shot Performance]]

## 🔗 유사한 논문
- [[CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (79.4% similar)
- [[Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (78.8% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (77.5% similar)
- [[Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (77.3% similar)
- [[DAG_ A Dual Causal Network for Time Series Forecasting with Exogenous Variables_20250919|DAG A Dual Causal Network for Time Series Forecasting with Exogenous Variables]] (77.1% similar)

## 📋 저자 정보

**Authors:** Liran Nochumsohn, Raz Marshanski, Hedi Zisling, Omri Azencot

## 📄 Abstract (원문)

Time series forecasting (TSF) is critical in domains like energy, finance,
healthcare, and logistics, requiring models that generalize across diverse
datasets. Large pre-trained models such as Chronos and Time-MoE show strong
zero-shot (ZS) performance but suffer from high computational costs. In this
work, We introduce Super-Linear, a lightweight and scalable mixture-of-experts
(MoE) model for general forecasting. It replaces deep architectures with simple
frequency-specialized linear experts, trained on resampled data across multiple
frequency regimes. A lightweight spectral gating mechanism dynamically selects
relevant experts, enabling efficient, accurate forecasting. Despite its
simplicity, Super-Linear matches state-of-the-art performance while offering
superior efficiency, robustness to various sampling rates, and enhanced
interpretability. The implementation of Super-Linear is available at
\href{https://github.com/azencot-group/SuperLinear}{https://github.com/azencot-group/SuperLinear}

## 🔍 Abstract (한글 번역)

시계열 예측(TSF)은 에너지, 금융, 의료, 물류와 같은 분야에서 매우 중요하며, 다양한 데이터셋에 일반화할 수 있는 모델이 필요합니다. Chronos와 Time-MoE와 같은 대형 사전 학습 모델은 강력한 제로샷(ZS) 성능을 보이지만 높은 계산 비용이 문제입니다. 본 연구에서는 일반 예측을 위한 경량화되고 확장 가능한 전문가 혼합(MoE) 모델인 Super-Linear를 소개합니다. 이는 심층 아키텍처를 간단한 주파수 특화 선형 전문가로 대체하며, 여러 주파수 체계에 걸쳐 재샘플링된 데이터로 학습됩니다. 경량 스펙트럼 게이팅 메커니즘이 관련 전문가를 동적으로 선택하여 효율적이고 정확한 예측을 가능하게 합니다. Super-Linear는 그 단순함에도 불구하고 최첨단 성능에 맞먹는 성과를 내며, 다양한 샘플링 속도에 대한 강력한 내구성과 향상된 해석 가능성을 제공합니다. Super-Linear의 구현은 [https://github.com/azencot-group/SuperLinear](https://github.com/azencot-group/SuperLinear)에서 확인할 수 있습니다.

## 📝 요약

이 논문에서는 시간 시계열 예측(TSF)을 위한 경량화되고 확장 가능한 전문가 혼합(MoE) 모델인 Super-Linear를 소개합니다. 기존의 대형 사전 학습 모델인 Chronos와 Time-MoE는 높은 성능을 보이지만, 계산 비용이 크다는 단점이 있습니다. Super-Linear는 복잡한 심층 구조 대신 주파수에 특화된 간단한 선형 전문가를 사용하여 다양한 주파수 범위의 재샘플링된 데이터로 학습합니다. 경량화된 스펙트럼 게이팅 메커니즘을 통해 관련 전문가를 동적으로 선택하여 효율적이고 정확한 예측을 가능하게 합니다. Super-Linear는 단순함에도 불구하고 최신 성능과 비슷한 수준을 유지하면서도 효율성, 다양한 샘플링 속도에 대한 강건성, 해석 가능성을 제공합니다.

## 🎯 주요 포인트

- 1. Super-Linear은 가벼운 혼합 전문가(MoE) 모델로, 다양한 주파수에 특화된 선형 전문가를 사용하여 일반적인 시계열 예측을 수행합니다.

- 2. 이 모델은 심플한 주파수 특화 선형 전문가를 사용하여 복잡한 심층 구조를 대체하며, 여러 주파수 체계에서 다시 샘플링된 데이터를 기반으로 학습됩니다.

- 3. 가벼운 스펙트럼 게이팅 메커니즘을 통해 관련 전문가를 동적으로 선택하여 효율적이고 정확한 예측을 가능하게 합니다.

- 4. Super-Linear는 단순함에도 불구하고 최첨단 성능을 유지하며, 다양한 샘플링 비율에 대한 강인성과 해석 가능성을 제공합니다.

- 5. Super-Linear의 구현은 GitHub에서 확인할 수 있습니다: https://github.com/azencot-group/SuperLinear.

---

*Generated on 2025-09-20 01:02:23*