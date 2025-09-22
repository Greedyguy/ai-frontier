# SEMMA: A Semantic Aware Knowledge Graph Foundation Model

**Korean Title:** SEMMA: 의미 인식 지식 그래프 기초 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Semantic Embeddings

## 🔗 유사한 논문
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (83.7% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text]] (82.7% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (81.6% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (81.6% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.20422v2 Announce Type: replace-cross 
Abstract: Knowledge Graph Foundation Models (KGFMs) have shown promise in enabling zero-shot reasoning over unseen graphs by learning transferable patterns. However, most existing KGFMs rely solely on graph structure, overlooking the rich semantic signals encoded in textual attributes. We introduce SEMMA, a dual-module KGFM that systematically integrates transferable textual semantics alongside structure. SEMMA leverages Large Language Models (LLMs) to enrich relation identifiers, generating semantic embeddings that subsequently form a textual relation graph, which is fused with the structural component. Across 54 diverse KGs, SEMMA outperforms purely structural baselines like ULTRA in fully inductive link prediction. Crucially, we show that in more challenging generalization settings, where the test-time relation vocabulary is entirely unseen, structural methods collapse while SEMMA is 2x more effective. Our findings demonstrate that textual semantics are critical for generalization in settings where structure alone fails, highlighting the need for foundation models that unify structural and linguistic signals in knowledge reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2505.20422v2 발표 유형: 교차 교체  
초록: 지식 그래프 기초 모델(KGFMs)은 전이 가능한 패턴을 학습하여 보지 못한 그래프에 대한 제로샷 추론을 가능하게 함으로써 잠재력을 보여주고 있습니다. 그러나 대부분의 기존 KGFMs은 그래프 구조에만 의존하며, 텍스트 속성에 인코딩된 풍부한 의미 신호를 간과하고 있습니다. 우리는 구조와 함께 전이 가능한 텍스트 의미를 체계적으로 통합하는 이중 모듈 KGFM인 SEMMA를 소개합니다. SEMMA는 대형 언어 모델(LLMs)을 활용하여 관계 식별자를 풍부하게 하고, 이를 통해 생성된 의미 임베딩이 텍스트 관계 그래프를 형성하여 구조적 구성 요소와 융합됩니다. 54개의 다양한 KGs에 걸쳐, SEMMA는 완전 귀납적 링크 예측에서 ULTRA와 같은 순수 구조적 기준선을 능가합니다. 특히, 테스트 시 관계 어휘가 완전히 보지 못한 경우와 같은 더 어려운 일반화 설정에서 구조적 방법이 붕괴되는 반면, SEMMA는 두 배 더 효과적임을 보여줍니다. 우리의 연구 결과는 구조만으로 실패하는 설정에서 일반화를 위해 텍스트 의미가 중요하다는 것을 보여주며, 지식 추론에서 구조적 및 언어적 신호를 통합하는 기초 모델의 필요성을 강조합니다.

## 📝 요약

이 논문에서는 새로운 지식 그래프 기반 모델인 SEMMA를 소개합니다. SEMMA는 그래프 구조뿐만 아니라 텍스트 속에 담긴 의미를 함께 활용하여, 이전에 보지 못한 그래프에서도 효과적으로 추론할 수 있습니다. 이 모델은 대형 언어 모델(LLM)을 사용하여 관계 식별자를 풍부하게 하고, 이를 통해 생성된 의미적 임베딩을 구조적 요소와 결합합니다. 54개의 다양한 지식 그래프에서 SEMMA는 기존의 구조적 모델보다 뛰어난 성능을 보였으며, 특히 테스트 시점에 완전히 새로운 관계가 주어지는 어려운 일반화 환경에서도 두 배 더 효과적임을 입증했습니다. 이 연구는 텍스트 의미가 구조만으로는 해결할 수 없는 일반화 문제에서 중요하다는 점을 강조하며, 구조와 언어적 신호를 통합한 모델의 필요성을 제시합니다.

## 🎯 주요 포인트

- 1. SEMMA는 구조와 함께 전이 가능한 텍스트 의미를 체계적으로 통합하는 이중 모듈 KGFM입니다.

- 2. SEMMA는 대형 언어 모델(LLMs)을 활용하여 관계 식별자를 풍부하게 하고, 이를 통해 생성된 의미 임베딩을 구조적 구성 요소와 융합합니다.

- 3. 54개의 다양한 지식 그래프(KG)에서 SEMMA는 완전 유도 링크 예측에서 순수 구조적 기준선인 ULTRA보다 뛰어난 성능을 보입니다.

- 4. 테스트 시점의 관계 어휘가 전혀 보이지 않는 더 어려운 일반화 설정에서 구조적 방법이 실패하는 반면, SEMMA는 두 배 더 효과적입니다.

- 5. 우리의 연구 결과는 구조만으로 실패하는 설정에서 일반화를 위해 텍스트 의미가 중요하다는 것을 보여주며, 지식 추론에서 구조적 및 언어적 신호를 통합하는 기초 모델의 필요성을 강조합니다.

---

*Generated on 2025-09-22 14:51:37*