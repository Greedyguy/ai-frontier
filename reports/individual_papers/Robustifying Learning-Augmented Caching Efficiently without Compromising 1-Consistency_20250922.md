# Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency

**Korean Title:** 학습 보강 캐싱을 1-일관성을 손상시키지 않고 효율적으로 견고화하기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Robustification of Caching Algorithms|Robustification of Caching Algorithms]] [[keywords/specific/Learning-Augmented Caching|Learning-Augmented Caching]] [[keywords/broad/Online Caching|Online Caching]] [[keywords/unique/Guard Framework|Guard Framework]] [[categories/cs.LG|cs.LG]] [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (81.4% similar) [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.9% similar) [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robustification of Caching Algorithms
**🔗 Specific Connectable**: Learning-Augmented Caching
**🔬 Broad Technical**: Online Caching
**⭐ Unique Technical**: Guard Framework
## 🔗 유사한 논문
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (81.4% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.9% similar)
- [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (78.8% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose Efficient Structured KV Cache Compression with Composite Tokens]] (78.8% similar)
- [[2025-09-22/Online Robust Planning under Model Uncertainty_ A Sample-Based Approach_20250922|Online Robust Planning under Model Uncertainty A Sample-Based Approach]] (78.8% similar)


**ArXiv ID**: [2507.16242](https://arxiv.org/abs/2507.16242)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2507.16242.pdf)


**ArXiv ID**: [2507.16242](https://arxiv.org/abs/2507.16242)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2507.16242.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robustification Framework
**🔗 Specific Connectable**: Learning-Augmented Caching
**⭐ Unique Technical**: Guard Framework
**🔬 Broad Technical**: Online Caching

## 🏷️ 추출된 키워드



`Online Caching` • 

`Learning-Augmented Caching` • 

`Guard Framework` • 

`Robustification Methods`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.16242v3 Announce Type: replace-cross 
Abstract: The online caching problem aims to minimize cache misses when serving a sequence of requests under a limited cache size. While naive learning-augmented caching algorithms achieve ideal $1$-consistency, they lack robustness guarantees. Existing robustification methods either sacrifice $1$-consistency or introduce significant computational overhead. In this paper, we introduce Guard, a lightweight robustification framework that enhances the robustness of a broad class of learning-augmented caching algorithms to $2H_k + 2$, while preserving their $1$-consistency. Guard achieves the current best-known trade-off between consistency and robustness, with only $O(1)$ additional per-request overhead, thereby maintaining the original time complexity of the base algorithm. Extensive experiments across multiple real-world datasets and prediction models validate the effectiveness of Guard in practice.

## 🔍 Abstract (한글 번역)

arXiv:2507.16242v3 발표 유형: 교체-교차  
초록: 온라인 캐싱 문제는 제한된 캐시 크기 하에서 일련의 요청을 처리할 때 캐시 미스를 최소화하는 것을 목표로 합니다. 단순한 학습 보강 캐싱 알고리즘은 이상적인 $1$-일관성을 달성하지만, 견고성 보장은 부족합니다. 기존의 견고화 방법은 $1$-일관성을 희생하거나 상당한 계산 오버헤드를 도입합니다. 본 논문에서는 Guard라는 경량의 견고화 프레임워크를 소개하여, 학습 보강 캐싱 알고리즘의 광범위한 클래스의 견고성을 $2H_k + 2$로 향상시키면서도 $1$-일관성을 유지합니다. Guard는 일관성과 견고성 사이의 현재 알려진 최상의 절충안을 달성하며, 요청당 추가 오버헤드가 $O(1)$에 불과하여 기본 알고리즘의 원래 시간 복잡성을 유지합니다. 여러 실제 데이터셋과 예측 모델을 통한 광범위한 실험은 실무에서 Guard의 효과성을 입증합니다.

## 📝 요약

이 논문은 온라인 캐싱 문제에서 캐시 미스를 최소화하기 위한 새로운 방법론인 Guard를 제안합니다. 기존의 학습 보강 캐싱 알고리즘은 $1$-일관성을 달성하지만, 견고성 보장이 부족합니다. Guard는 이러한 알고리즘의 견고성을 $2H_k + 2$로 향상시키면서도 $1$-일관성을 유지합니다. 이 방법은 일관성과 견고성 간의 최적의 균형을 제공하며, 요청당 $O(1)$의 추가적인 오버헤드만 발생시켜 기본 알고리즘의 시간 복잡성을 유지합니다. 다양한 실제 데이터셋과 예측 모델을 통한 실험을 통해 Guard의 실용성을 입증했습니다.

## 🎯 주요 포인트


- 1. 온라인 캐싱 문제는 제한된 캐시 크기에서 요청 시퀀스를 처리할 때 캐시 미스를 최소화하는 것을 목표로 한다.

- 2. 기존의 학습 보강 캐싱 알고리즘은 이상적인 $1$-일관성을 달성하지만, 견고성 보장이 부족하다.

- 3. Guard는 다양한 학습 보강 캐싱 알고리즘의 견고성을 $2H_k + 2$로 향상시키면서 $1$-일관성을 유지하는 경량화된 견고화 프레임워크이다.

- 4. Guard는 일관성과 견고성 간의 최상의 균형을 이루며, 요청당 $O(1)$의 추가 오버헤드만으로 기본 알고리즘의 시간 복잡성을 유지한다.

- 5. 다양한 실제 데이터셋과 예측 모델을 통한 광범위한 실험에서 Guard의 실효성이 검증되었다.


---

*Generated on 2025-09-22 16:13:07*