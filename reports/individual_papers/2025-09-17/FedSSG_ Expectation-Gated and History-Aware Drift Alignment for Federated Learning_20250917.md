# FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning

**Korean Title:** 연합 학습을 위한 기대 게이트 및 이력 인식 드리프트 정렬: FedSSG

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Zhanting Zhou|Zhanting Zhou]] [[authors/Jinshan Lai|Jinshan Lai]] [[authors/Fengchun Zhang|Fengchun Zhang]] [[authors/Zeqin Wu|Zeqin Wu]] [[authors/Fengli Zhang|Fengli Zhang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: History-Aware Drift Alignment

## 🔗 유사한 논문
- [[FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (81.3% similar)
- [[Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (78.9% similar)
- [[Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy Toward Privacy-Aware Hypergraph Structure Completion]] (78.5% similar)
- [[Class-invariant Test-Time Augmentation for Domain Generalization_20250917|Class-invariant Test-Time Augmentation for Domain Generalization]] (78.2% similar)
- [[Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking_20250918|Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking]] (78.0% similar)

## 📋 저자 정보

**Authors:** Zhanting Zhou, Jinshan Lai, Fengchun Zhang, Zeqin Wu, Fengli Zhang

## 📄 Abstract (원문)

Non-IID data and partial participation induce client drift and inconsistent
local optima in federated learning, causing unstable convergence and accuracy
loss. We present FedSSG, a stochastic sampling-guided, history-aware drift
alignment method. FedSSG maintains a per-client drift memory that accumulates
local model differences as a lightweight sketch of historical gradients;
crucially, it gates both the memory update and the local alignment term by a
smooth function of the observed/expected participation ratio (a
phase-by-expectation signal derived from the server sampler). This
statistically grounded gate stays weak and smooth when sampling noise dominates
early, then strengthens once participation statistics stabilize, contracting
the local-global gap without extra communication. Across CIFAR-10/100 with
100/500 clients and 2-15 percent participation, FedSSG consistently outperforms
strong drift-aware baselines and accelerates convergence; on our benchmarks it
improves test accuracy by up to a few points (e.g., about +0.9 on CIFAR-10 and
about +2.7 on CIFAR-100 on average over the top-2 baseline) and yields about
4.5x faster target-accuracy convergence on average. The method adds only O(d)
client memory and a constant-time gate, and degrades gracefully to a mild
regularizer under near-IID or uniform sampling. FedSSG shows that sampling
statistics can be turned into a principled, history-aware phase control to
stabilize and speed up federated training.

## 🔍 Abstract (한글 번역)

비독립적이고 동일하게 분포되지 않은(Non-IID) 데이터와 부분 참여는 연합 학습에서 클라이언트 드리프트와 불일치한 지역 최적점을 유발하여 불안정한 수렴과 정확도 손실을 초래합니다. 우리는 FedSSG라는 확률적 샘플링 유도, 이력 인식 드리프트 정렬 방법을 제시합니다. FedSSG는 각 클라이언트별 드리프트 메모리를 유지하여 로컬 모델 차이를 역사적 기울기의 경량 스케치로 축적합니다. 특히, 이는 관찰된/예상된 참여 비율(서버 샘플러에서 유도된 기대에 따른 단계 신호)의 매끄러운 함수에 의해 메모리 업데이트와 로컬 정렬 항을 모두 조절합니다. 이 통계적으로 근거 있는 게이트는 초기 샘플링 노이즈가 지배적일 때는 약하고 부드럽게 유지되다가, 참여 통계가 안정화되면 강해져 추가 통신 없이 로컬-글로벌 간극을 축소합니다. CIFAR-10/100에서 100/500명의 클라이언트와 2-15%의 참여율로 FedSSG는 강력한 드리프트 인식 기준선을 일관되게 능가하며 수렴을 가속화합니다. 우리의 벤치마크에서 테스트 정확도를 몇 포인트 향상시키며(예: CIFAR-10에서 약 +0.9, CIFAR-100에서 약 +2.7의 평균 향상) 평균적으로 목표 정확도 수렴을 약 4.5배 빠르게 달성합니다. 이 방법은 O(d) 클라이언트 메모리와 상수 시간 게이트만 추가하며, 거의 IID 또는 균일 샘플링 하에서는 온화한 정규화자로 우아하게 저하됩니다. FedSSG는 샘플링 통계를 원칙적이고 이력 인식적인 단계 제어로 전환하여 연합 학습을 안정화하고 가속화할 수 있음을 보여줍니다.

## 📝 요약

FedSSG는 비독립적이고 동일하지 않은(non-IID) 데이터와 부분 참여로 인한 클라이언트 드리프트 문제를 해결하기 위한 방법론으로, 역사 기반의 드리프트 정렬을 통해 연합 학습의 수렴 불안정성과 정확도 손실을 개선합니다. FedSSG는 클라이언트별 드리프트 메모리를 유지하여 로컬 모델 차이를 기록하고, 서버 샘플러에서 파생된 참여 비율에 기반한 부드러운 함수로 메모리 업데이트와 로컬 정렬을 조절합니다. 이는 참여 통계가 안정화되면 로컬과 글로벌 간의 격차를 줄여줍니다. CIFAR-10/100 데이터셋 실험에서 FedSSG는 강력한 드리프트 인식 기준선보다 우수한 성능을 보이며, 테스트 정확도를 평균적으로 CIFAR-10에서 약 0.9, CIFAR-100에서 약 2.7 향상시켰습니다. 또한, 목표 정확도 도달 시간을 약 4.5배 가속화했습니다. FedSSG는 클라이언트 메모리와 상수 시간 게이트를 추가하여, 거의 독립적이거나 균일한 샘플링에서도 성능 저하 없이 안정적인 학습을 지원합니다.

## 🎯 주요 포인트

- 1. FedSSG는 비독립적 데이터와 부분 참여로 인한 클라이언트 드리프트 문제를 해결하기 위한 역사 인식 드리프트 정렬 방법입니다.

- 2. FedSSG는 클라이언트별 드리프트 메모리를 유지하여 로컬 모델 차이를 누적하고, 참여 비율에 따른 부드러운 함수로 메모리 업데이트와 로컬 정렬 항을 조절합니다.

- 3. CIFAR-10/100 데이터셋에서 FedSSG는 강력한 드리프트 인식 기준선을 능가하며, 테스트 정확도를 최대 몇 포인트 향상시키고 목표 정확도 수렴 속도를 약 4.5배 가속화합니다.

- 4. FedSSG는 O(d) 클라이언트 메모리와 상수 시간 게이트만 추가하며, 거의 독립적이거나 균일한 샘플링에서도 성능 저하 없이 작동합니다.

- 5. FedSSG는 샘플링 통계를 원칙적이고 역사 인식적인 단계 제어로 전환하여 연합 학습을 안정화하고 가속화할 수 있음을 보여줍니다.

---

*Generated on 2025-09-20 09:25:38*