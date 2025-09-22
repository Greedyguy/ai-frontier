# LLM Cache Bandit Revisited: Addressing Query Heterogeneity for Cost-Effective LLM Inference

**Korean Title:** LLM 캐시 밴딧 재검토: 비용 효율적인 LLM 추론을 위한 쿼리 이질성 해결

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Query Heterogeneity|Query Heterogeneity]] [[keywords/specific/Knapsack Problem|Knapsack Problem]] [[keywords/broad/LLM|LLM]] [[keywords/broad/Cache Management|Cache Management]] [[keywords/unique/LLM Cache Bandit|LLM Cache Bandit]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency_20250922|Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency]] (82.5% similar) [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (82.2% similar) [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query Heterogeneity
**🔗 Specific Connectable**: Knapsack Problem
**🔬 Broad Technical**: LLM, Cache Management
**⭐ Unique Technical**: LLM Cache Bandit
## 🔗 유사한 논문
- [[2025-09-22/Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency_20250922|Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency]] (82.5% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose Efficient Structured KV Cache Compression with Composite Tokens]] (82.2% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (81.4% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.6% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (79.5% similar)


**ArXiv ID**: [2509.15515](https://arxiv.org/abs/2509.15515)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15515.pdf)


**ArXiv ID**: [2509.15515](https://arxiv.org/abs/2509.15515)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15515.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query Heterogeneity
**🔗 Specific Connectable**: Knapsack Problem
**⭐ Unique Technical**: LLM Cache Bandit
**🔬 Broad Technical**: LLM, Cache Management

## 🏷️ 추출된 키워드



`LLM` • 

`Cache Management` • 

`Knapsack Problem` • 

`LLM Cache Bandit` • 

`Query Heterogeneity`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15515v1 Announce Type: new 
Abstract: This paper revisits the LLM cache bandit problem, with a special focus on addressing the query heterogeneity for cost-effective LLM inference. Previous works often assume uniform query sizes. Heterogeneous query sizes introduce a combinatorial structure for cache selection, making the cache replacement process more computationally and statistically challenging. We treat optimal cache selection as a knapsack problem and employ an accumulation-based strategy to effectively balance computational overhead and cache updates. In theoretical analysis, we prove that the regret of our algorithm achieves an $O(\sqrt{MNT})$ bound, improving the coefficient of $\sqrt{MN}$ compared to the $O(MN\sqrt{T})$ result in Berkeley, where $N$ is the total number of queries and $M$ is the cache size. Additionally, we also provide a problem-dependent bound, which was absent in previous works. The experiment rely on real-world data show that our algorithm reduces the total cost by approximately 12\%.

## 🔍 Abstract (한글 번역)

arXiv:2509.15515v1 발표 유형: 새로운 논문  
초록: 본 논문은 비용 효율적인 대형 언어 모델(LLM) 추론을 위해 쿼리 이질성을 해결하는 데 중점을 두고 LLM 캐시 밴딧 문제를 재검토합니다. 이전 연구들은 종종 균일한 쿼리 크기를 가정합니다. 이질적인 쿼리 크기는 캐시 선택에 조합적 구조를 도입하여 캐시 교체 과정을 더 복잡하고 통계적으로 도전적으로 만듭니다. 우리는 최적의 캐시 선택을 배낭 문제로 간주하고, 계산 오버헤드와 캐시 업데이트를 효과적으로 균형 잡기 위해 축적 기반 전략을 사용합니다. 이론적 분석에서, 우리는 우리의 알고리즘의 후회가 $O(\sqrt{MNT})$ 경계를 달성함을 증명하며, 이는 버클리의 $O(MN\sqrt{T})$ 결과에 비해 $\sqrt{MN}$ 계수를 개선합니다. 여기서 $N$은 총 쿼리 수이고 $M$은 캐시 크기입니다. 추가적으로, 이전 연구에서 결여되었던 문제 의존적 경계도 제공합니다. 실제 데이터에 기반한 실험은 우리의 알고리즘이 총 비용을 약 12% 감소시킴을 보여줍니다.

## 📝 요약

이 논문은 LLM 캐시 밴딧 문제를 재검토하며, 특히 비용 효율적인 LLM 추론을 위한 쿼리 이질성 문제를 다룹니다. 기존 연구는 주로 균일한 쿼리 크기를 가정했으나, 이질적인 쿼리 크기는 캐시 선택의 조합적 구조를 도입하여 캐시 교체 과정을 더 복잡하게 만듭니다. 본 연구는 최적의 캐시 선택을 배낭 문제로 간주하고, 누적 기반 전략을 사용하여 계산 오버헤드와 캐시 업데이트를 효과적으로 균형 잡습니다. 이론적 분석에서, 제안된 알고리즘의 후회가 $O(\sqrt{MNT})$ 경계를 달성함을 증명하며, 이는 Berkeley의 $O(MN\sqrt{T})$ 결과에 비해 $\sqrt{MN}$ 계수를 개선합니다. 또한, 이전 연구에 없던 문제 종속적인 경계도 제공합니다. 실험 결과, 제안된 알고리즘은 총 비용을 약 12% 절감함을 보여줍니다.

## 🎯 주요 포인트


- 1. 본 논문은 LLM 캐시 밴딧 문제를 재검토하며, 비용 효율적인 LLM 추론을 위한 쿼리 이질성 문제를 중점적으로 다룹니다.

- 2. 이질적인 쿼리 크기는 캐시 선택에 조합적 구조를 도입하여 캐시 교체 과정을 더 복잡하게 만듭니다.

- 3. 최적의 캐시 선택을 배낭 문제로 간주하고, 계산 오버헤드와 캐시 업데이트를 효과적으로 균형 잡기 위한 누적 기반 전략을 사용합니다.

- 4. 이론적 분석에서 우리의 알고리즘이 $O(\sqrt{MNT})$의 후회를 달성함을 증명하며, 이는 Berkeley의 $O(MN\sqrt{T})$ 결과와 비교하여 $\sqrt{MN}$의 계수를 개선합니다.

- 5. 실제 데이터에 기반한 실험 결과, 우리의 알고리즘은 총 비용을 약 12% 절감합니다.


---

*Generated on 2025-09-22 16:22:18*