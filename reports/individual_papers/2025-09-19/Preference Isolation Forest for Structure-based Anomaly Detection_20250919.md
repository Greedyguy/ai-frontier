---
keywords:
  - Preference Isolation Forest
  - Local Sensitive Hashing
  - Anomaly Detection
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2505.10876
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:28:48.842039",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Preference Isolation Forest",
    "Local Sensitive Hashing",
    "Anomaly Detection"
  ],
  "rejected_keywords": [
    "Low-Dimensional Manifolds"
  ],
  "similarity_scores": {
    "Preference Isolation Forest": 0.8,
    "Local Sensitive Hashing": 0.82,
    "Anomaly Detection": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Preference Isolation Forest for Structure-based Anomaly Detection

**Korean Title:** 구조 기반 이상 탐지를 위한 선호 격리 숲

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Anomaly Detection|anomaly detection]]
**🔗 Specific Connectable**: [[keywords/Local Sensitive Hashing|Local Sensitive Hashing]]
**⚡ Unique Technical**: [[keywords/Preference Isolation Forest|Preference Isolation Forest]]

## 🔗 유사한 논문
- [[RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (79.2% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.9% similar)
- [[GROOD GRadient-Aware Out-of-Distribution Detection]] (76.9% similar)
- [[TFLAGTowards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph]] (76.9% similar)
- [[BERTector An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (76.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.10876v2 Announce Type: replace-cross 
Abstract: We address the problem of detecting anomalies as samples that do not conform to structured patterns represented by low-dimensional manifolds. To this end, we conceive a general anomaly detection framework called Preference Isolation Forest (PIF), that combines the benefits of adaptive isolation-based methods with the flexibility of preference embedding. The key intuition is to embed the data into a high-dimensional preference space by fitting low-dimensional manifolds, and to identify anomalies as isolated points. We propose three isolation approaches to identify anomalies: $i$) Voronoi-iForest, the most general solution, $ii$) RuzHash-iForest, that avoids explicit computation of distances via Local Sensitive Hashing, and $iii$) Sliding-PIF, that leverages a locality prior to improve efficiency and effectiveness.

## 🔍 Abstract (한글 번역)

arXiv:2505.10876v2 발표 유형: 교차 교체  
초록: 우리는 저차원 다양체로 표현된 구조화된 패턴에 부합하지 않는 샘플로서 이상을 탐지하는 문제를 다룹니다. 이를 위해, 적응형 격리 기반 방법의 이점과 선호도 임베딩의 유연성을 결합한 일반적인 이상 탐지 프레임워크인 Preference Isolation Forest (PIF)을 고안했습니다. 핵심 직관은 저차원 다양체에 맞춰 데이터를 고차원 선호도 공간에 임베딩하고, 고립된 점으로 이상을 식별하는 것입니다. 우리는 이상을 식별하기 위한 세 가지 격리 접근 방식을 제안합니다: $i$) 가장 일반적인 솔루션인 Voronoi-iForest, $ii$) 지역 민감 해싱을 통해 거리의 명시적 계산을 피하는 RuzHash-iForest, 그리고 $iii$) 효율성과 효과성을 향상시키기 위해 지역성을 활용하는 Sliding-PIF.

## 📝 요약

이 논문은 저차원 매니폴드로 표현되는 구조적 패턴에 부합하지 않는 샘플을 이상치로 감지하는 문제를 다룹니다. 이를 위해, 적응형 고립 기반 방법의 장점과 선호도 임베딩의 유연성을 결합한 일반적인 이상치 탐지 프레임워크인 Preference Isolation Forest (PIF)을 제안합니다. 핵심 아이디어는 데이터를 저차원 매니폴드에 맞춰 고차원 선호도 공간에 임베딩하고, 고립된 점으로 이상치를 식별하는 것입니다. 세 가지 고립 접근법을 제안합니다: i) 가장 일반적인 솔루션인 Voronoi-iForest, ii) 지역 민감 해싱을 통해 거리 계산을 피하는 RuzHash-iForest, iii) 효율성과 효과성을 높이기 위해 지역성을 활용하는 Sliding-PIF입니다.

## 🎯 주요 포인트

- 1. 본 연구는 저차원 매니폴드로 표현되는 구조적 패턴에 부합하지 않는 샘플을 이상치로 탐지하는 문제를 다룹니다.

- 2. Preference Isolation Forest (PIF)라는 일반적인 이상 탐지 프레임워크를 제안하며, 이는 적응형 고립 기반 방법의 이점과 선호도 임베딩의 유연성을 결합합니다.

- 3. 데이터는 저차원 매니폴드를 맞춤으로써 고차원 선호도 공간에 임베딩되고, 이상치는 고립된 점으로 식별됩니다.

- 4. 이상치를 식별하기 위해 Voronoi-iForest, RuzHash-iForest, Sliding-PIF의 세 가지 고립 접근법을 제안합니다.

- 5. RuzHash-iForest는 Local Sensitive Hashing을 통해 거리의 명시적 계산을 피하고, Sliding-PIF는 지역성을 활용하여 효율성과 효과성을 향상시킵니다.

---

*Generated on 2025-09-19 15:15:14*