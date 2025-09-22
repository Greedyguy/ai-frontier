# Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning

**Korean Title:** 검색 및 사고 중 정제: 검색 증강 추론을 위한 지식 정제 촉진

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Search-and-Refine Paradigm

## 🔗 유사한 논문
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (84.3% similar)
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE Faithful Logic-Aided Reasoning and Exploration]] (84.3% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility Process-Supervised Rewrite for RAG]] (84.1% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (83.8% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11277v5 Announce Type: replace-cross 
Abstract: Large language models have demonstrated impressive reasoning capabilities but are inherently limited by their knowledge reservoir. Retrieval-augmented reasoning mitigates this limitation by allowing LLMs to query external resources, but existing methods often retrieve irrelevant or noisy information, hindering accurate reasoning. In this paper, we propose AutoRefine, a reinforcement learning post-training framework that adopts a new "search-and-refine-during-think" paradigm. AutoRefine introduces explicit knowledge refinement steps between successive search calls, enabling the model to iteratively filter, distill, and organize evidence before generating an answer. Furthermore, we incorporate tailored retrieval-specific rewards alongside answer correctness rewards using group relative policy optimization. Experiments on single-hop and multi-hop QA benchmarks demonstrate that AutoRefine significantly outperforms existing approaches, particularly in complex, multi-hop reasoning scenarios. Detailed analysis shows that AutoRefine issues frequent, higher-quality searches and synthesizes evidence effectively.

## 🔍 Abstract (한글 번역)

arXiv:2505.11277v5 발표 유형: 교차 교체  
초록: 대형 언어 모델은 인상적인 추론 능력을 보여주었지만, 본질적으로 지식 저장소의 한계가 있습니다. 검색 보강 추론은 LLM이 외부 자원을 질의할 수 있도록 하여 이러한 한계를 완화하지만, 기존 방법은 종종 관련 없거나 잡음이 많은 정보를 검색하여 정확한 추론을 방해합니다. 본 논문에서는 "생각하는 동안 검색 및 정제"라는 새로운 패러다임을 채택한 강화 학습 후처리 프레임워크인 AutoRefine을 제안합니다. AutoRefine은 연속적인 검색 호출 사이에 명시적인 지식 정제 단계를 도입하여 모델이 답변을 생성하기 전에 증거를 반복적으로 필터링, 정제 및 조직화할 수 있도록 합니다. 또한, 그룹 상대 정책 최적화를 사용하여 답변의 정확성 보상과 함께 검색 특화 보상을 통합합니다. 단일 홉 및 다중 홉 QA 벤치마크에 대한 실험은 AutoRefine이 특히 복잡한 다중 홉 추론 시나리오에서 기존 접근 방식을 크게 능가함을 보여줍니다. 자세한 분석 결과, AutoRefine은 빈번하고 높은 품질의 검색을 수행하며 증거를 효과적으로 종합함을 보여줍니다.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM)의 한계를 극복하기 위해 AutoRefine이라는 강화 학습 기반의 사후 훈련 프레임워크를 제안합니다. AutoRefine는 "생각 중 검색 및 정제"라는 새로운 패러다임을 도입하여 검색 호출 사이에 명시적인 지식 정제 단계를 추가합니다. 이를 통해 모델은 답변을 생성하기 전에 증거를 반복적으로 필터링, 정제, 조직화할 수 있습니다. 또한, 검색 특화 보상과 답변 정확성 보상을 결합한 그룹 상대 정책 최적화를 활용합니다. 실험 결과, AutoRefine는 단일 및 다중 단계의 질의응답(QA) 벤치마크에서 특히 복잡한 다중 단계 추론 시나리오에서 기존 방법보다 뛰어난 성능을 보였습니다. 분석 결과, AutoRefine는 더 빈번하고 고품질의 검색을 수행하며 증거를 효과적으로 종합하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. AutoRefine는 "생각 중 검색 및 정제" 패러다임을 채택하여 대형 언어 모델의 외부 자원 검색 시 발생하는 비관련 정보 문제를 해결합니다.

- 2. 이 프레임워크는 연속적인 검색 호출 사이에 명시적인 지식 정제 단계를 도입하여 답변 생성 전에 증거를 필터링, 증류 및 조직화합니다.

- 3. 그룹 상대 정책 최적화를 사용하여 검색 특화 보상과 답변 정확성 보상을 결합하여 성능을 향상시킵니다.

- 4. 단일 및 다중 단계의 질문 응답 벤치마크 실험에서 AutoRefine는 특히 복잡한 다중 단계 추론 시나리오에서 기존 방법보다 뛰어난 성능을 보입니다.

- 5. AutoRefine는 빈번하고 높은 품질의 검색을 수행하며, 효과적으로 증거를 종합하는 것으로 나타났습니다.

---

*Generated on 2025-09-22 14:48:46*