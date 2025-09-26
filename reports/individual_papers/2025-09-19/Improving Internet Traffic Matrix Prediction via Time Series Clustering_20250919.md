---
keywords:
  - Deep Learning
  - Time Series Clustering
  - Traffic Matrix Prediction
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15072
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:39:59.293045",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Time Series Clustering",
    "Traffic Matrix Prediction"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Time Series Clustering": 0.78,
    "Traffic Matrix Prediction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Improving Internet Traffic Matrix Prediction via Time Series Clustering

**Korean Title:** 인터넷 트래픽 매트릭스 예측 향상을 위한 시계열 클러스터링 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Time Series Clustering|Time Series Clustering]], [[keywords/Traffic Matrix Prediction|Traffic Matrix Prediction]]

## 🔗 유사한 논문
- [[STEP Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (80.6% similar)
- [[RF-LSCM Pushing Radiance Fields to Multi-Domain Localized Statistical Channel Modeling for Cellular Network Optimization]] (80.4% similar)
- [[Causal Clustering for Conditional Average Treatment Effects Estimation and Subgroup Discovery]] (79.9% similar)
- [[TableDART Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (79.4% similar)
- [[BERTector An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15072v1 Announce Type: new 
Abstract: We present a novel framework that leverages time series clustering to improve internet traffic matrix (TM) prediction using deep learning (DL) models. Traffic flows within a TM often exhibit diverse temporal behaviors, which can hinder prediction accuracy when training a single model across all flows. To address this, we propose two clustering strategies, source clustering and histogram clustering, that group flows with similar temporal patterns prior to model training. Clustering creates more homogeneous data subsets, enabling models to capture underlying patterns more effectively and generalize better than global prediction approaches that fit a single model to the entire TM. Compared to existing TM prediction methods, our method reduces RMSE by up to 92\% for Abilene and 75\% for G\'EANT. In routing scenarios, our clustered predictions also reduce maximum link utilization (MLU) bias by 18\% and 21\%, respectively, demonstrating the practical benefits of clustering when TMs are used for network optimization.

## 🔍 Abstract (한글 번역)

arXiv:2509.15072v1 발표 유형: 신규  
초록: 우리는 시계열 군집화를 활용하여 심층 학습(DL) 모델을 사용한 인터넷 트래픽 매트릭스(TM) 예측을 개선하는 새로운 프레임워크를 제시합니다. TM 내의 트래픽 흐름은 종종 다양한 시간적 행동을 보이며, 이는 모든 흐름에 대해 단일 모델을 훈련할 때 예측 정확도를 저해할 수 있습니다. 이를 해결하기 위해, 우리는 모델 훈련 전에 유사한 시간적 패턴을 가진 흐름을 그룹화하는 소스 군집화와 히스토그램 군집화라는 두 가지 군집화 전략을 제안합니다. 군집화는 보다 동질적인 데이터 하위 집합을 생성하여 모델이 기본 패턴을 보다 효과적으로 포착하고 전체 TM에 단일 모델을 맞추는 글로벌 예측 접근 방식보다 일반화할 수 있게 합니다. 기존의 TM 예측 방법과 비교하여, 우리의 방법은 Abilene에서는 최대 92\%, G\'EANT에서는 75\% RMSE를 감소시킵니다. 라우팅 시나리오에서, 우리의 군집화된 예측은 최대 링크 활용도(MLU) 편향을 각각 18\%와 21\% 줄여, 네트워크 최적화를 위해 TM이 사용될 때 군집화의 실질적인 이점을 보여줍니다.

## 📝 요약

이 논문은 시계열 클러스터링을 활용하여 인터넷 트래픽 매트릭스(Traffic Matrix, TM) 예측의 정확성을 향상시키는 새로운 프레임워크를 제안합니다. 다양한 시간적 행동을 보이는 트래픽 흐름을 단일 모델로 예측할 때의 한계를 극복하기 위해, 저자들은 소스 클러스터링과 히스토그램 클러스터링이라는 두 가지 전략을 제안합니다. 이러한 클러스터링은 유사한 시간 패턴을 가진 흐름을 그룹화하여 보다 동질적인 데이터 하위 집합을 생성하고, 모델이 패턴을 효과적으로 포착하도록 합니다. 기존의 TM 예측 방법과 비교했을 때, 제안된 방법은 Abilene 네트워크에서 최대 92%, GÉANT 네트워크에서 75%까지 RMSE를 감소시켰습니다. 또한, 라우팅 시나리오에서 최대 링크 활용도 편향을 각각 18%와 21% 줄여 네트워크 최적화에 실질적인 이점을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 시계열 클러스터링을 활용하여 딥러닝 모델 기반 인터넷 트래픽 매트릭스(Traffic Matrix, TM) 예측을 개선하는 새로운 프레임워크를 제안합니다.

- 2. 트래픽 흐름의 다양한 시간적 특성을 고려하여, 모델 학습 전에 유사한 시간 패턴을 가진 흐름을 그룹화하는 소스 클러스터링과 히스토그램 클러스터링 두 가지 전략을 제안합니다.

- 3. 클러스터링을 통해 보다 동질적인 데이터 하위 집합을 생성하여, 모델이 기저 패턴을 더 효과적으로 포착하고 전체 TM에 단일 모델을 적용하는 글로벌 예측 접근 방식보다 일반화 성능을 향상시킵니다.

- 4. 제안된 방법은 기존 TM 예측 방법에 비해 Abilene 네트워크에서 최대 92%, G\'EANT 네트워크에서 75%까지 RMSE를 감소시킵니다.

- 5. 클러스터링된 예측은 라우팅 시나리오에서 최대 링크 활용도(MLU) 편향을 각각 18%와 21% 감소시켜, 네트워크 최적화에 있어 클러스터링의 실질적 이점을 입증합니다.

---

*Generated on 2025-09-19 15:29:51*