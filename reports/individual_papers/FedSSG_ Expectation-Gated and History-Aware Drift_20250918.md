
# FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning

**Korean Title:** FedSSG: 기대치 게이팅 및 역사 인식 드리프트 정렬을 위한 연합 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/broad/Federated Learning|Federated Learning]] [[keywords/broad/Drift Alignment|Drift Alignment]] [[keywords/specific/Stochastic Sampling|Stochastic Sampling]] [[keywords/specific/Local-Global Gap|Local-Global Gap]] [[keywords/unique/FedSSG|FedSSG]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: History-Aware Phase Control
**🔬 Broad Technical**: Federated Learning, Drift Alignment
**🔗 Specific Connectable**: Local Model Differences
**⭐ Unique Technical**: FedSSG

**ArXiv ID**: [2509.13895](https://arxiv.org/abs/2509.13895)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13895.pdf)


## 🏷️ 추출된 키워드



`Federated Learning` • 

`Drift Alignment` • 

`CIFAR-10/100` • 

`FedSSG` • 

`Client Drift`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13895v1 Announce Type: cross 
Abstract: Non-IID data and partial participation induce client drift and inconsistent local optima in federated learning, causing unstable convergence and accuracy loss. We present FedSSG, a stochastic sampling-guided, history-aware drift alignment method. FedSSG maintains a per-client drift memory that accumulates local model differences as a lightweight sketch of historical gradients; crucially, it gates both the memory update and the local alignment term by a smooth function of the observed/expected participation ratio (a phase-by-expectation signal derived from the server sampler). This statistically grounded gate stays weak and smooth when sampling noise dominates early, then strengthens once participation statistics stabilize, contracting the local-global gap without extra communication. Across CIFAR-10/100 with 100/500 clients and 2-15 percent participation, FedSSG consistently outperforms strong drift-aware baselines and accelerates convergence; on our benchmarks it improves test accuracy by up to a few points (e.g., about +0.9 on CIFAR-10 and about +2.7 on CIFAR-100 on average over the top-2 baseline) and yields about 4.5x faster target-accuracy convergence on average. The method adds only O(d) client memory and a constant-time gate, and degrades gracefully to a mild regularizer under near-IID or uniform sampling. FedSSG shows that sampling statistics can be turned into a principled, history-aware phase control to stabilize and speed up federated training.

## 🔍 Abstract (한글 번역)

arXiv:2509.13895v1 발표 유형: 교차
요약: 비-IID 데이터와 부분 참여는 연합 학습에서 클라이언트 드리프트와 일관되지 않은 로컬 최적값을 유발하여 불안정한 수렴과 정확도 손실을 초래합니다. 우리는 FedSSG를 제시합니다. 이는 확률적 샘플링 가이드, 역사를 고려한 드리프트 정렬 방법입니다. FedSSG는 가벼운 역사적 그래디언트의 스케치로서 로컬 모델의 차이를 축적하는 각 클라이언트 드리프트 메모리를 유지합니다. 중요한 점은 서버 샘플러에서 파생된 기대 참여 비율에 대한 부드러운 함수에 의해 메모리 업데이트와 로컬 정렬 용어를 모두 제어합니다. 이 통계적으로 근거 있는 게이트는 샘플링 노이즈가 초기에 우세할 때 약하고 부드럽게 유지되며, 참여 통계가 안정화되면 강화되어 로컬-글로벌 간격을 줄이고 추가 통신 없이 수렴합니다. 100/500 클라이언트 및 2-15% 참여도를 갖는 CIFAR-10/100에서 FedSSG는 강력한 드리프트 인식 베이스라인을 일관되게 능가하고 수렴을 가속화합니다. 우리의 벤치마크에서 CIFAR-10에서 약 +0.9, CIFAR-100에서 약 +2.7 정도의 테스트 정확도 향상을 보여주며 평균적으로 약 4.5배 빠른 목표 정확도 수렴을 제공합니다. 이 방법은 O(d) 클라이언트 메모리와 상수 시간 게이트만 추가하며, 거의 IID 또는 균일 샘플링에서는 약한 정규화기로 우아하게 저하됩니다. FedSSG는 샘플링 통계를 원칙적이고 역사를 고려한 단계 제어로 변환하여 연합 학습을 안정화하고 가속화할 수 있다는 것을 보여줍니다.

## 📝 요약

본 연구는 연합 학습에서 발생하는 클라이언트 이동과 불일치로 인한 불안정한 수렴과 정확도 손실 문제를 해결하기 위해 FedSSG라는 새로운 방법을 제안한다. 이 방법은 클라이언트 이동 메모리를 유지하고 이를 통해 역사적 그래디언트의 가벼운 스케치를 누적함으로써 로컬 모델의 차이를 추적한다. 이에 따라 참여 비율에 따라 메모리 업데이트 및 로컬 정렬을 제어하는 통계적으로 근거 있는 게이트를 제안하였다. CIFAR-10/100 데이터셋을 사용하여 실험한 결과, FedSSG는 강력한 기준선을 능가하고 수렴을 가속화시키며 테스트 정확도를 향상시킨다. 이 방법은 클라이언트 메모리와 게이트를 추가하며 근사적 또는 균일한 샘플링에서도 원활하게 작동한다. FedSSG는 샘플링 통계를 원칙적이고 역사적인 위상 제어로 변환하여 연합 학습을 안정화하고 가속화할 수 있음을 보여준다.

## 🎯 주요 포인트


- 1. 비균질 데이터와 부분 참여로 인한 클라이언트 이동과 불일치한 로컬 최적점을 해결하는 FedSSG 소개

- 2. FedSSG는 클라이언트 이동 메모리를 유지하고 통계적으로 기반한 게이트를 통해 로컬-글로벌 간격을 축소

- 3. CIFAR-10/100에서 FedSSG는 강력한 드리프트-인식 기준선을 consistently 능가하고 수렴을 가속화

- 4. FedSSG는 샘플링 통계를 원칙적이고 역사적인 위상 제어로 전환하여 연합 학습을 안정화하고 가속화함.


---

*Generated on 2025-09-18 16:23:17*