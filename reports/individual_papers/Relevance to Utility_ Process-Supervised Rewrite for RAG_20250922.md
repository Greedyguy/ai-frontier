# Relevance to Utility: Process-Supervised Rewrite for RAG

**Korean Title:** 유용성에 대한 관련성: RAG를 위한 프로세스 감독 재작성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Efficient Distillation Pipeline

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (86.1% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG Retrieval-Augmented Generation with Implicit Queries]] (85.7% similar)
- [[2025-09-19/AIP_ Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt_20250919|AIP Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (85.5% similar)
- [[2025-09-19/GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA Graph-based Reranking against Adversarial Documents Attack]] (85.3% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (84.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15577v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation systems often suffer from a gap between optimizing retrieval relevance and generative utility: retrieved documents may be topically relevant but still lack the content needed for effective reasoning during generation. While existing "bridge" modules attempt to rewrite the retrieved text for better generation, we show how they fail to capture true document utility. In this work, we propose R2U, with a key distinction of directly optimizing to maximize the probability of generating a correct answer through process supervision. As such direct observation is expensive, we also propose approximating an efficient distillation pipeline by scaling the supervision from LLMs, which helps the smaller rewriter model generalize better. We evaluate our method across multiple open-domain question-answering benchmarks. The empirical results demonstrate consistent improvements over strong bridging baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15577v1 발표 유형: 교차  
초록: 검색-증강 생성 시스템은 종종 검색 관련성과 생성 유용성 간의 격차로 인해 고통받습니다. 검색된 문서는 주제적으로 관련성이 있을 수 있지만 생성 중 효과적인 추론에 필요한 내용을 여전히 결여할 수 있습니다. 기존의 "브리지" 모듈은 더 나은 생성을 위해 검색된 텍스트를 재작성하려고 시도하지만, 우리는 이들이 진정한 문서 유용성을 포착하지 못하는 방식을 보여줍니다. 본 연구에서는 R2U를 제안하며, 올바른 답변을 생성할 확률을 최대화하기 위해 프로세스 감독을 통해 직접 최적화하는 것을 주요 차별점으로 삼습니다. 이러한 직접 관찰은 비용이 많이 들기 때문에, 우리는 또한 LLM에서 감독을 확장하여 더 작은 리라이터 모델이 더 잘 일반화할 수 있도록 돕는 효율적인 증류 파이프라인을 근사하는 방법을 제안합니다. 우리는 여러 오픈 도메인 질문-응답 벤치마크에서 우리의 방법을 평가합니다. 실험 결과는 강력한 브리지 기준선을 초과하는 일관된 개선을 보여줍니다.

## 📝 요약

이 논문은 검색 기반 생성 시스템의 문제점을 해결하기 위해 R2U라는 새로운 방법을 제안합니다. 기존의 "브릿지" 모듈은 검색된 문서의 내용을 재작성하여 생성의 효용성을 높이려 하지만, 실제 문서의 유용성을 제대로 반영하지 못합니다. R2U는 정답 생성 확률을 최대화하도록 직접 최적화하는 프로세스 감독 방식을 도입하여 이 문제를 해결합니다. 또한, 대규모 언어 모델(LLM)에서 감독을 확장하여 효율적인 증류 파이프라인을 제안함으로써 작은 재작성 모델의 일반화 능력을 향상시킵니다. 여러 오픈 도메인 질문-응답 벤치마크에서 평가한 결과, R2U는 기존의 강력한 브릿지 기법들보다 일관된 성능 향상을 보였습니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation 시스템은 검색 관련성과 생성 유용성 간의 격차로 인해 어려움을 겪습니다.

- 2. 기존의 "브리지" 모듈은 검색된 텍스트를 재작성하려 하지만, 문서의 실제 유용성을 포착하는 데 실패합니다.

- 3. R2U는 정답을 생성할 확률을 최대화하기 위해 프로세스 감독을 통해 직접 최적화하는 방법을 제안합니다.

- 4. LLMs로부터 감독을 확장하여 효율적인 증류 파이프라인을 근사함으로써 작은 재작성 모델이 더 잘 일반화할 수 있도록 돕습니다.

- 5. 여러 오픈 도메인 질문-응답 벤치마크에서 평가한 결과, 강력한 브리지 기준선보다 일관된 성능 향상을 보여줍니다.

---

*Generated on 2025-09-22 14:03:55*