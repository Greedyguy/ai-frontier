# KVCompose: Efficient Structured KV Cache Compression with Composite Tokens

**Korean Title:** KVCompose: 합성 토큰을 활용한 효율적인 구조적 KV 캐시 압축

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Layer-adaptive Composite Tokens|Layer-adaptive Composite Tokens]] [[keywords/specific/Attention Mechanism|Attention Mechanism]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/unique/KVCompose|KVCompose]] [[categories/cs.LG|cs.LG]] [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (89.9% similar) [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (83.3% similar) [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Layer Adaptive Compression
**🔗 Specific Connectable**: Attention Mechanism
**🔬 Broad Technical**: Large Language Models
**⭐ Unique Technical**: Composite Tokens
## 🔗 유사한 논문
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (89.9% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE Confidence-guided Compression in Step-by-step Efficient Reasoning]] (83.3% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (83.2% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (82.7% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (82.1% similar)


**ArXiv ID**: [2509.05165](https://arxiv.org/abs/2509.05165)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.05165.pdf)


**ArXiv ID**: [2509.05165](https://arxiv.org/abs/2509.05165)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.05165.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Layer-adaptive Composite Tokens
**🔗 Specific Connectable**: Attention Mechanism
**⭐ Unique Technical**: KVCompose
**🔬 Broad Technical**: Large Language Models

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Attention Mechanism` • 

`KVCompose` • 

`Layer-adaptive Composite Tokens`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.05165v2 Announce Type: replace 
Abstract: Large language models (LLMs) rely on key-value (KV) caches for efficient autoregressive decoding; however, cache size grows linearly with context length and model depth, becoming a major bottleneck in long-context inference. Prior KV cache compression methods either enforce rigid heuristics, disrupt tensor layouts with per-attention-head variability, or require specialized compute kernels.
  We propose a simple, yet effective, KV cache compression framework based on attention-guided, layer-adaptive composite tokens. Our method aggregates attention scores to estimate token importance, selects head-specific tokens independently, and aligns them into composite tokens that respect the uniform cache structure required by existing inference engines. A global allocation mechanism further adapts retention budgets across layers, assigning more capacity to layers with informative tokens. This approach achieves significant memory reduction while preserving accuracy, consistently outperforming prior structured and semi-structured methods. Crucially, our approach remains fully compatible with standard inference pipelines, offering a practical and scalable solution for efficient long-context LLM deployment.

## 🔍 Abstract (한글 번역)

arXiv:2509.05165v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)은 효율적인 자기 회귀 디코딩을 위해 키-값(KV) 캐시를 사용합니다. 그러나 캐시 크기는 문맥 길이와 모델 깊이에 따라 선형적으로 증가하여 긴 문맥 추론에서 주요 병목 현상이 됩니다. 이전의 KV 캐시 압축 방법은 엄격한 휴리스틱을 강요하거나, 주의 헤드별 변동성으로 인해 텐서 레이아웃을 방해하거나, 특수한 계산 커널을 필요로 합니다.  
우리는 주의 기반의 계층 적응형 복합 토큰을 기반으로 한 간단하면서도 효과적인 KV 캐시 압축 프레임워크를 제안합니다. 우리의 방법은 주의 점수를 집계하여 토큰의 중요성을 추정하고, 헤드별로 독립적으로 토큰을 선택하며, 기존 추론 엔진이 요구하는 균일한 캐시 구조를 존중하는 복합 토큰으로 정렬합니다. 전역 할당 메커니즘은 계층 간 유지 예산을 적응적으로 조정하여 정보가 많은 토큰을 가진 계층에 더 많은 용량을 할당합니다. 이 접근 방식은 정확성을 유지하면서 메모리를 크게 줄이며, 이전의 구조적 및 반구조적 방법보다 일관되게 우수한 성능을 발휘합니다. 중요한 것은, 우리의 접근 방식이 표준 추론 파이프라인과 완전히 호환되어, 효율적인 긴 문맥 LLM 배포를 위한 실용적이고 확장 가능한 솔루션을 제공합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 효율적인 오토리그레시브 디코딩을 위한 KV 캐시 압축 방법을 제안합니다. 기존 방법들은 비효율적이거나 특수한 계산 커널을 요구하는 반면, 제안된 방법은 주의 메커니즘을 기반으로 한 레이어 적응형 복합 토큰을 사용하여 간단하면서도 효과적인 압축을 구현합니다. 주의 점수를 통해 토큰의 중요도를 추정하고, 헤드별로 독립적으로 토큰을 선택하여 기존 추론 엔진의 캐시 구조를 유지합니다. 또한, 글로벌 할당 메커니즘을 통해 레이어별로 저장 용량을 조정하여 메모리 사용을 줄이면서 정확도를 유지합니다. 이 방법은 기존의 구조적 및 반구조적 방법보다 우수하며, 표준 추론 파이프라인과 완전히 호환되어 실용적이고 확장 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트


- 1. 대형 언어 모델(LLM)의 효율적인 오토리그레시브 디코딩을 위해 KV 캐시가 필요하지만, 캐시 크기는 문맥 길이와 모델 깊이에 따라 선형적으로 증가하여 긴 문맥 추론에서 주요 병목 현상이 된다.

- 2. 기존의 KV 캐시 압축 방법은 엄격한 휴리스틱을 강요하거나, 주의 헤드별 변동성으로 텐서 레이아웃을 방해하거나, 특수한 계산 커널을 요구한다.

- 3. 제안된 방법은 주의 기반, 레이어 적응형 복합 토큰을 사용하여 간단하면서도 효과적인 KV 캐시 압축 프레임워크를 제공한다.

- 4. 이 방법은 주의 점수를 집계하여 토큰 중요성을 추정하고, 헤드별 토큰을 독립적으로 선택하여 기존 추론 엔진이 요구하는 균일한 캐시 구조에 맞게 복합 토큰으로 정렬한다.

- 5. 제안된 방법은 메모리 사용량을 크게 줄이면서 정확성을 유지하며, 기존의 구조적 및 반구조적 방법을 일관되게 능가한다.


---

*Generated on 2025-09-22 16:02:26*