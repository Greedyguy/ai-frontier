# LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs

**Korean Title:** LiteLong: LLM을 위한 자원 효율적인 장기 문맥 데이터 합성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent Debate

## 🔗 유사한 논문
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.1% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (80.8% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.8% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (80.6% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony On Multilingual Data Allocation for Large Language Models Pretraining]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15568v1 Announce Type: cross 
Abstract: High-quality long-context data is essential for training large language models (LLMs) capable of processing extensive documents, yet existing synthesis approaches using relevance-based aggregation face challenges of computational efficiency. We present LiteLong, a resource-efficient method for synthesizing long-context data through structured topic organization and multi-agent debate. Our approach leverages the BISAC book classification system to provide a comprehensive hierarchical topic organization, and then employs a debate mechanism with multiple LLMs to generate diverse, high-quality topics within this structure. For each topic, we use lightweight BM25 retrieval to obtain relevant documents and concatenate them into 128K-token training samples. Experiments on HELMET and Ruler benchmarks demonstrate that LiteLong achieves competitive long-context performance and can seamlessly integrate with other long-dependency enhancement methods. LiteLong makes high-quality long-context data synthesis more accessible by reducing both computational and data engineering costs, facilitating further research in long-context language training.

## 🔍 Abstract (한글 번역)

arXiv:2509.15568v1 발표 유형: 교차  
초록: 고품질의 긴 문맥 데이터를 생성하는 것은 광범위한 문서를 처리할 수 있는 대형 언어 모델(LLMs)을 훈련하는 데 필수적이지만, 기존의 관련성 기반 집계를 사용하는 합성 접근 방식은 계산 효율성 문제에 직면하고 있습니다. 우리는 구조화된 주제 조직과 다중 에이전트 토론을 통해 긴 문맥 데이터를 합성하는 자원 효율적인 방법인 LiteLong을 제시합니다. 우리의 접근 방식은 BISAC 도서 분류 시스템을 활용하여 포괄적인 계층적 주제 조직을 제공한 후, 여러 LLM을 사용한 토론 메커니즘을 통해 이 구조 내에서 다양하고 고품질의 주제를 생성합니다. 각 주제에 대해 경량 BM25 검색을 사용하여 관련 문서를 얻고 이를 128K-토큰 훈련 샘플로 연결합니다. HELMET 및 Ruler 벤치마크에 대한 실험 결과, LiteLong은 경쟁력 있는 긴 문맥 성능을 달성하며 다른 긴 종속성 강화 방법과 원활하게 통합될 수 있음을 보여줍니다. LiteLong은 계산 및 데이터 엔지니어링 비용을 줄임으로써 고품질의 긴 문맥 데이터 합성을 보다 쉽게 접근할 수 있게 하여, 긴 문맥 언어 훈련에 대한 추가 연구를 촉진합니다.

## 📝 요약

LiteLong은 대규모 언어 모델(LLM)이 긴 문서를 처리할 수 있도록 고품질의 긴 문맥 데이터를 효율적으로 합성하는 방법을 제안합니다. BISAC 도서 분류 시스템을 활용하여 주제를 체계적으로 조직하고, 여러 LLM 간의 토론 메커니즘을 통해 다양한 고품질 주제를 생성합니다. 각 주제에 대해 BM25 검색을 사용하여 관련 문서를 가져와 128K 토큰의 학습 샘플로 결합합니다. HELMET 및 Ruler 벤치마크 실험에서 LiteLong은 경쟁력 있는 성능을 보였으며, 다른 긴 의존성 강화 방법과도 원활하게 통합될 수 있음을 입증했습니다. 이 방법은 계산 및 데이터 엔지니어링 비용을 절감하여 긴 문맥 언어 학습 연구를 촉진합니다.

## 🎯 주요 포인트

- 1. LiteLong은 구조화된 주제 조직화와 다중 에이전트 토론을 통해 긴 문맥 데이터를 효율적으로 합성하는 방법을 제안합니다.

- 2. BISAC 도서 분류 시스템을 활용하여 포괄적인 계층적 주제 조직화를 제공하고, 여러 LLM의 토론 메커니즘을 통해 다양한 고품질 주제를 생성합니다.

- 3. 각 주제에 대해 경량 BM25 검색을 사용하여 관련 문서를 얻고 이를 128K-토큰 훈련 샘플로 연결합니다.

- 4. HELMET 및 Ruler 벤치마크 실험에서 LiteLong은 경쟁력 있는 긴 문맥 성능을 보여주며, 다른 긴 의존성 강화 방법과 원활하게 통합될 수 있습니다.

- 5. LiteLong은 계산 및 데이터 엔지니어링 비용을 줄여 고품질 긴 문맥 데이터 합성을 보다 접근 가능하게 하여 긴 문맥 언어 훈련 연구를 촉진합니다.

---

*Generated on 2025-09-22 14:02:56*