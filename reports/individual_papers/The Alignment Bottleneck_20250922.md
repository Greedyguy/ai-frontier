# The Alignment Bottleneck

**Korean Title:** 정렬 병목현상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Capacity Coupled Alignment

## 🔗 유사한 논문
- [[2025-09-19/Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (82.5% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (81.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (81.1% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (80.4% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15932v1 Announce Type: cross 
Abstract: Large language models improve with scale, yet feedback-based alignment still exhibits systematic deviations from intended behavior. Motivated by bounded rationality in economics and cognitive science, we view judgment as resource-limited and feedback as a constrained channel. On this basis, we model the loop as a two-stage cascade $U \to H \to Y$ given $S$, with cognitive capacity $C_{\text{cog}|S}$ and average total capacity $\bar{C}_{\text{tot}|S}$. Our main result is a capacity-coupled Alignment Performance Interval. It pairs a data size-independent Fano lower bound proved on a separable codebook mixture with a PAC-Bayes upper bound whose KL term is controlled by the same channel via $m \, \bar{C}_{\text{tot}|S}$. The PAC-Bayes bound becomes an upper bound on the same true risk when the canonical observable loss is used and the dataset is drawn from the same mixture. Under these matched conditions, both limits are governed by a single capacity. Consequences include that, with value complexity and capacity fixed, adding labels alone cannot cross the bound; attaining lower risk on more complex targets requires capacity that grows with $\log M$; and once useful signal saturates capacity, further optimization tends to fit channel regularities, consistent with reports of sycophancy and reward hacking. The analysis views alignment as interface engineering: measure and allocate limited capacity, manage task complexity, and decide where information is spent.

## 🔍 Abstract (한글 번역)

arXiv:2509.15932v1 발표 유형: 교차  
초록: 대형 언어 모델은 규모가 커질수록 성능이 향상되지만, 피드백 기반의 정렬은 여전히 의도된 행동에서 체계적인 편차를 보입니다. 경제학과 인지과학에서의 제한된 합리성에 영감을 받아, 우리는 판단을 자원 제한적이고 피드백을 제한된 채널로 간주합니다. 이를 바탕으로, 우리는 $S$가 주어졌을 때 인지 용량 $C_{\text{cog}|S}$와 평균 총 용량 $\bar{C}_{\text{tot}|S}$를 가진 $U \to H \to Y$의 두 단계 캐스케이드로 이 루프를 모델링합니다. 우리의 주요 결과는 용량이 결합된 정렬 성능 간격입니다. 이는 분리 가능한 코드북 혼합물에서 증명된 데이터 크기와 무관한 파노 하한과, 동일한 채널이 $m \, \bar{C}_{\text{tot}|S}$를 통해 제어하는 KL 항을 가진 PAC-Bayes 상한을 짝지어 줍니다. PAC-Bayes 경계는 표준 관측 손실이 사용되고 데이터셋이 동일한 혼합물에서 추출될 때 동일한 실제 위험에 대한 상한이 됩니다. 이러한 일치된 조건하에서, 두 한계는 단일 용량에 의해 지배됩니다. 그 결과, 가치 복잡성과 용량이 고정된 상태에서 라벨을 추가하는 것만으로는 경계를 넘을 수 없으며, 더 복잡한 목표에서 낮은 위험을 달성하려면 $\log M$과 함께 증가하는 용량이 필요합니다. 그리고 유용한 신호가 용량을 포화시키면, 추가 최적화는 채널 규칙성을 맞추는 경향이 있으며, 이는 아첨과 보상 해킹에 대한 보고와 일치합니다. 이 분석은 정렬을 인터페이스 엔지니어링으로 간주합니다: 제한된 용량을 측정하고 할당하며, 작업 복잡성을 관리하고, 정보를 어디에 사용할지 결정합니다.

## 📝 요약

이 논문은 대형 언어 모델의 피드백 기반 정렬이 의도된 행동과 체계적으로 어긋나는 문제를 다룹니다. 경제학과 인지과학의 제한된 합리성 개념을 바탕으로, 판단을 자원 제한적이고 피드백을 제약된 채널로 간주합니다. 이를 통해 두 단계의 연쇄 모델을 제안하며, 주요 결과로는 용량 결합 정렬 성능 간격을 제시합니다. 이 간격은 데이터 크기와 무관한 Fano 하한과 PAC-Bayes 상한으로 구성되며, 동일한 채널에 의해 제어됩니다. 이 분석은 정렬을 인터페이스 엔지니어링으로 보고, 제한된 용량을 측정하고 할당하며, 과제 복잡성을 관리하고 정보 사용처를 결정하는 데 중점을 둡니다. 주요 발견 사항으로는 레이블 추가만으로는 한계를 넘을 수 없고, 복잡한 목표에 대한 낮은 위험을 달성하려면 용량이 증가해야 한다는 점이 있습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델은 규모가 커질수록 성능이 향상되지만, 피드백 기반의 정렬은 여전히 의도된 행동에서 체계적인 편차를 보입니다.

- 2. 본 연구는 판단을 자원 제한적이고 피드백을 제한된 채널로 간주하여, 정렬 성능을 용량과 결합된 인터벌로 모델링합니다.

- 3. 데이터 크기와 무관한 Fano 하한과 PAC-Bayes 상한을 결합하여, 동일한 채널에 의해 제어되는 KL 항을 통해 정렬 성능을 분석합니다.

- 4. 용량이 고정된 상태에서 레이블을 추가하는 것만으로는 하한을 넘을 수 없으며, 더 복잡한 목표에서 낮은 위험을 달성하려면 용량이 증가해야 합니다.

- 5. 유용한 신호가 용량을 포화시키면, 추가 최적화는 채널의 규칙성을 맞추는 경향이 있으며, 이는 아첨과 보상 해킹 보고와 일치합니다.

---

*Generated on 2025-09-22 14:17:46*