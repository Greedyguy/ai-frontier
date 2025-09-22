# Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs

**Korean Title:** 대규모 언어 모델과 진화하는 지식 그래프에 의해 보강된 시간적 추론

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Knowledge Graph Evolution

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.8% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (85.2% similar)
- [[2025-09-17/THOR_ Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning_20250917|THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (85.1% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak Bridging Complex Thoughts and Comprehensible Speech]] (84.8% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text]] (84.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15464v1 Announce Type: new 
Abstract: Large language models (LLMs) excel at many language understanding tasks but struggle to reason over knowledge that evolves. To address this, recent work has explored augmenting LLMs with knowledge graphs (KGs) to provide structured, up-to-date information. However, many existing approaches assume a static snapshot of the KG and overlook the temporal dynamics and factual inconsistencies inherent in real-world data. To address the challenge of reasoning over temporally shifting knowledge, we propose EvoReasoner, a temporal-aware multi-hop reasoning algorithm that performs global-local entity grounding, multi-route decomposition, and temporally grounded scoring. To ensure that the underlying KG remains accurate and up-to-date, we introduce EvoKG, a noise-tolerant KG evolution module that incrementally updates the KG from unstructured documents through confidence-based contradiction resolution and temporal trend tracking. We evaluate our approach on temporal QA benchmarks and a novel end-to-end setting where the KG is dynamically updated from raw documents. Our method outperforms both prompting-based and KG-enhanced baselines, effectively narrowing the gap between small and large LLMs on dynamic question answering. Notably, an 8B-parameter model using our approach matches the performance of a 671B model prompted seven months later. These results highlight the importance of combining temporal reasoning with KG evolution for robust and up-to-date LLM performance. Our code is publicly available at github.com/junhongmit/TREK.

## 🔍 Abstract (한글 번역)

arXiv:2509.15464v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)은 많은 언어 이해 작업에서 뛰어난 성능을 보이지만, 변화하는 지식을 추론하는 데 어려움을 겪습니다. 이를 해결하기 위해 최근 연구에서는 LLMs에 지식 그래프(KGs)를 추가하여 구조화되고 최신 정보를 제공하는 방법을 탐구하고 있습니다. 그러나 많은 기존 접근법은 KG의 정적 스냅샷을 가정하고, 현실 세계 데이터에 내재된 시간적 역학과 사실적 불일치를 간과합니다. 시간적으로 변화하는 지식을 추론하는 문제를 해결하기 위해, 우리는 전역-지역 엔티티 기반, 다중 경로 분해, 시간적 기반 점수를 수행하는 시간 인식 다중 홉 추론 알고리즘인 EvoReasoner를 제안합니다. 기본 KG가 정확하고 최신 상태를 유지하도록 하기 위해, 우리는 신뢰 기반 모순 해결 및 시간적 추세 추적을 통해 비구조화된 문서에서 KG를 점진적으로 업데이트하는 노이즈 내성 KG 진화 모듈인 EvoKG를 도입합니다. 우리는 시간적 QA 벤치마크와 KG가 원시 문서에서 동적으로 업데이트되는 새로운 종단 간 설정에서 우리의 접근법을 평가합니다. 우리의 방법은 프롬프트 기반 및 KG 강화 기준선을 능가하며, 동적 질문 응답에서 소형 및 대형 LLM 간의 격차를 효과적으로 좁힙니다. 특히, 우리의 접근법을 사용하는 80억 매개변수 모델은 7개월 후에 프롬프트된 6710억 모델의 성능과 일치합니다. 이러한 결과는 견고하고 최신의 LLM 성능을 위해 시간적 추론과 KG 진화를 결합하는 것의 중요성을 강조합니다. 우리의 코드는 github.com/junhongmit/TREK에서 공개적으로 이용 가능합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 변화하는 지식을 다루는 데 어려움을 겪는 문제를 해결하기 위해, 지식 그래프(KG)를 활용하여 최신 정보를 제공하는 방법을 제안합니다. 기존 방법들은 정적인 KG를 가정하여 시간적 변화와 사실의 불일치를 간과했습니다. 이를 해결하기 위해, 저자들은 EvoReasoner라는 알고리즘을 제안하여 시간 인식 멀티홉 추론을 수행하고, EvoKG 모듈을 통해 KG를 지속적으로 업데이트합니다. 이 방법은 시간적 질문 응답 벤치마크와 새로운 설정에서 기존 방법들을 능가하며, 작은 LLM과 큰 LLM 간의 성능 격차를 줄입니다. 특히, 8B-파라미터 모델이 671B 모델과 유사한 성능을 보입니다. 이 연구는 시간적 추론과 KG 진화의 결합이 LLM의 성능 향상에 중요함을 강조합니다.

## 🎯 주요 포인트

- 1. EvoReasoner는 시간에 따라 변화하는 지식을 다루기 위해 설계된 다중 단계 추론 알고리즘으로, 글로벌-로컬 엔티티 연결, 다중 경로 분해, 시간 기반 점수를 수행합니다.

- 2. EvoKG는 비구조화된 문서에서 신뢰 기반 모순 해결과 시간적 경향 추적을 통해 KG를 점진적으로 업데이트하는 노이즈 내성 KG 진화 모듈입니다.

- 3. 제안된 방법은 시간적 QA 벤치마크와 KG가 원시 문서에서 동적으로 업데이트되는 새로운 종단 간 설정에서 평가되었으며, 기존의 프롬프트 기반 및 KG 강화 기법보다 우수한 성능을 보였습니다.

- 4. 8B-파라미터 모델이 제안된 방법을 사용하여 7개월 후에 프롬프트된 671B 모델의 성능을 맞추었으며, 이는 시간적 추론과 KG 진화의 결합이 최신 LLM 성능에 중요함을 강조합니다.

- 5. 연구의 코드는 github.com/junhongmit/TREK에서 공개적으로 제공됩니다.

---

*Generated on 2025-09-22 15:15:05*