# Can Large Language Models Infer Causal Relationships from Real-World Text?

**Korean Title:** 대형 언어 모델이 실제 텍스트에서 인과 관계를 추론할 수 있는가?

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Benchmark Development

## 🔗 유사한 논문
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (86.3% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (85.5% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (85.5% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.3% similar)
- [[2025-09-19/CLEAR_ A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models_20250919|CLEAR A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models]] (84.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18931v2 Announce Type: replace 
Abstract: Understanding and inferring causal relationships from texts is a core aspect of human cognition and is essential for advancing large language models (LLMs) towards artificial general intelligence. Existing work evaluating LLM causal reasoning primarily focuses on synthetically generated texts which involve straightforward causal relationships that are explicitly mentioned in the text. This fails to reflect the complexities of real-world tasks. In this paper, we investigate whether LLMs are capable of inferring causal relationships from real-world texts. We develop a benchmark drawn from real-world academic literature which includes diverse texts with respect to length, complexity of relationships (different levels of explicitness, number of nodes, and causal relationships), and domains and sub-domains. To the best of our knowledge, our benchmark is the first-ever real-world dataset for this task. Our experiments on this dataset show that LLMs face significant challenges in inferring causal relationships from real-world text, with the best-performing model achieving an average F1 score of only 0.477. Through systematic analysis across aspects of real-world text (degree of confounding, size of graph, length of text, domain), our benchmark offers targeted insights for further research into advancing LLM causal reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2505.18931v2 발표 유형: 교체  
초록: 텍스트에서 인과 관계를 이해하고 추론하는 것은 인간 인지의 핵심 측면이며, 대형 언어 모델(LLMs)을 인공지능 일반 지능으로 발전시키기 위해 필수적입니다. 기존의 LLM 인과 추론 평가 작업은 주로 텍스트에 명시적으로 언급된 간단한 인과 관계를 포함하는 합성적으로 생성된 텍스트에 중점을 둡니다. 이는 실제 과제의 복잡성을 반영하지 못합니다. 본 논문에서는 LLM이 실제 텍스트에서 인과 관계를 추론할 수 있는지를 조사합니다. 우리는 다양한 텍스트(길이, 관계의 복잡성, 명시성의 수준, 노드의 수, 인과 관계) 및 도메인과 하위 도메인에 대한 실제 학술 문헌에서 추출한 벤치마크를 개발했습니다. 우리가 아는 한, 이 벤치마크는 이 작업을 위한 최초의 실제 데이터셋입니다. 이 데이터셋에 대한 실험 결과, LLM은 실제 텍스트에서 인과 관계를 추론하는 데 상당한 어려움을 겪고 있으며, 가장 성능이 좋은 모델조차 평균 F1 점수 0.477에 그쳤습니다. 실제 텍스트의 다양한 측면(혼란의 정도, 그래프의 크기, 텍스트의 길이, 도메인)에 대한 체계적인 분석을 통해, 우리의 벤치마크는 LLM 인과 추론을 발전시키기 위한 추가 연구에 대한 목표 지향적인 통찰력을 제공합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 실제 텍스트에서 인과 관계를 추론할 수 있는지를 조사합니다. 기존 연구는 주로 명시적인 인과 관계가 포함된 합성 텍스트에 초점을 맞추고 있어 현실 세계의 복잡성을 반영하지 못합니다. 이를 해결하기 위해, 다양한 길이와 관계 복잡성, 도메인을 포함한 실제 학술 문헌에서 추출한 벤치마크를 개발했습니다. 실험 결과, LLM이 실제 텍스트에서 인과 관계를 추론하는 데 어려움을 겪으며, 최고 성능 모델의 평균 F1 점수는 0.477에 불과했습니다. 이 연구는 LLM의 인과 추론 능력을 향상시키기 위한 추가 연구에 중요한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 인과 추론 능력을 평가하기 위해 실제 학술 문헌에서 추출한 벤치마크를 개발했습니다.

- 2. 이 연구는 LLM이 실제 텍스트에서 인과 관계를 추론하는 데 상당한 어려움을 겪고 있음을 보여줍니다.

- 3. 개발된 벤치마크는 다양한 길이와 복잡성을 가진 텍스트를 포함하며, 이는 인과 관계 추론 연구에 새로운 통찰을 제공합니다.

- 4. 실험 결과, 가장 성능이 좋은 모델도 평균 F1 점수가 0.477에 불과하여 LLM의 인과 추론 능력에 한계가 있음을 시사합니다.

- 5. 이 연구는 LLM 인과 추론을 발전시키기 위한 추가 연구의 방향성을 제시합니다.

---

*Generated on 2025-09-22 14:31:57*