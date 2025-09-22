# FLARE: Faithful Logic-Aided Reasoning and Exploration

**Korean Title:** FLARE: 신뢰할 수 있는 논리 보조 추론 및 탐색

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Chain of Thought, Multi-hop Search

## 🔗 유사한 논문
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (85.1% similar)
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (84.7% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (84.6% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (83.5% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression A Self-Optimizing Framework]] (83.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.11900v5 Announce Type: replace 
Abstract: Modern Question Answering (QA) and Reasoning approaches based on Large Language Models (LLMs) commonly use prompting techniques, such as Chain-of-Thought (CoT), assuming the resulting generation will have a more granular exploration and reasoning over the question space and scope. However, such methods struggle with generating outputs that are faithful to the intermediate chain of reasoning produced by the model. On the other end of the spectrum, neuro-symbolic methods such as Faithful CoT (F-CoT) propose to combine LLMs with external symbolic solvers. While such approaches boast a high degree of faithfulness, they usually require a model trained for code generation and struggle with tasks that are ambiguous or hard to formalise strictly. We introduce $\textbf{F}$aithful $\textbf{L}$ogic-$\textbf{A}$ided $\textbf{R}$easoning and $\textbf{E}$xploration ($\textbf{FLARE}$), a novel interpretable approach for traversing the problem space using task decompositions. We use the LLM to plan a solution, soft-formalise the query into facts and predicates using a logic programming code and simulate that code execution using an exhaustive multi-hop search over the defined space. Our method allows us to compute the faithfulness of the reasoning process w.r.t. the generated code and analyse the steps of the multi-hop search without relying on external solvers. Our methods achieve SOTA results on $\mathbf{7}$ out of $\mathbf{9}$ diverse reasoning benchmarks. We also show that model faithfulness positively correlates with overall performance and further demonstrate that $\textbf{FLARE}$ allows pinpointing the decisive factors sufficient for and leading to the correct answer with optimal reasoning during the multi-hop search.

## 🔍 Abstract (한글 번역)

arXiv:2410.11900v5 발표 유형: 교체  
초록: 대형 언어 모델(LLMs)을 기반으로 한 현대의 질문 응답(QA) 및 추론 접근 방식은 일반적으로 Chain-of-Thought (CoT)와 같은 프롬프트 기법을 사용하여 질문 공간과 범위에 대한 더 세분화된 탐색과 추론을 유도한다고 가정합니다. 그러나 이러한 방법은 모델이 생성한 중간 추론 체인에 충실한 출력을 생성하는 데 어려움을 겪습니다. 반면에, Faithful CoT (F-CoT)와 같은 신경-기호적 방법은 LLMs를 외부 기호 솔버와 결합할 것을 제안합니다. 이러한 접근 방식은 높은 충실도를 자랑하지만, 일반적으로 코드 생성에 훈련된 모델이 필요하며 모호하거나 엄격하게 형식화하기 어려운 작업에서는 어려움을 겪습니다. 우리는 문제 공간을 탐색하기 위한 새로운 해석 가능한 접근 방식인 $\textbf{F}$aithful $\textbf{L}$ogic-$\textbf{A}$ided $\textbf{R}$easoning and $\textbf{E}$xploration ($\textbf{FLARE}$)을 소개합니다. 우리는 LLM을 사용하여 솔루션을 계획하고, 논리 프로그래밍 코드를 사용하여 쿼리를 사실과 술어로 부드럽게 형식화하며, 정의된 공간에 대한 철저한 다중 홉 검색을 통해 그 코드 실행을 시뮬레이션합니다. 우리의 방법은 외부 솔버에 의존하지 않고 생성된 코드에 대한 추론 과정의 충실도를 계산하고 다중 홉 검색의 단계를 분석할 수 있게 합니다. 우리의 방법은 $\mathbf{9}$개의 다양한 추론 벤치마크 중 $\mathbf{7}$개에서 SOTA 결과를 달성합니다. 우리는 또한 모델의 충실도가 전체 성능과 긍정적으로 상관관계가 있음을 보여주며, $\textbf{FLARE}$가 다중 홉 검색 중 최적의 추론을 통해 올바른 답변으로 이어지는 충분한 결정적 요소를 정확히 찾아낼 수 있음을 추가로 입증합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용한 현대의 질문 답변(QA) 및 추론 방법론의 문제점을 해결하기 위해 새로운 접근법인 FLARE를 제안합니다. 기존의 방법들은 중간 추론 과정의 충실성을 보장하기 어려운 반면, FLARE는 LLM과 논리 프로그래밍을 결합하여 문제 공간을 탐색합니다. FLARE는 문제를 세분화하고 논리적 사실과 술어로 변환한 후, 다단계 검색을 통해 추론 과정을 시뮬레이션하여 충실성을 평가합니다. 이 방법은 외부 솔버에 의존하지 않고도 추론 과정을 분석할 수 있으며, 9개의 다양한 추론 벤치마크 중 7개에서 최첨단(SOTA) 성능을 달성했습니다. 또한, 모델의 충실성이 전체 성능과 긍정적인 상관관계를 가지며, FLARE는 최적의 추론을 통해 정답을 도출하는 결정적 요인을 식별할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)을 기반으로 한 현대의 질문 응답(QA) 및 추론 접근법은 주로 Chain-of-Thought(CoT)와 같은 프롬프트 기법을 사용하지만, 중간 추론 체인에 충실한 출력을 생성하는 데 어려움을 겪습니다.

- 2. Faithful CoT(F-CoT)와 같은 신경-기호적 방법은 LLM과 외부 기호 해석기를 결합하여 높은 충실도를 자랑하지만, 코드 생성에 훈련된 모델이 필요하고 모호하거나 엄격히 형식화하기 어려운 작업에 어려움을 겪습니다.

- 3. FLARE는 문제 공간을 탐색하기 위한 새로운 해석 가능한 접근법으로, LLM을 사용하여 해결책을 계획하고 논리 프로그래밍 코드를 통해 쿼리를 사실과 술어로 소프트 형식화하여 정의된 공간에서 철저한 멀티홉 검색을 통해 코드 실행을 시뮬레이션합니다.

- 4. FLARE는 외부 해석기에 의존하지 않고 생성된 코드에 대한 추론 과정의 충실도를 계산하고 멀티홉 검색의 단계를 분석할 수 있게 해줍니다.

- 5. FLARE는 9개의 다양한 추론 벤치마크 중 7개에서 SOTA 결과를 달성했으며, 모델의 충실도가 전체 성능과 긍정적으로 상관관계가 있음을 보여주고, 멀티홉 검색 중 최적의 추론으로 올바른 답변을 이끌어내는 결정적 요인을 정확히 지적할 수 있음을 입증했습니다.

---

*Generated on 2025-09-22 14:28:52*