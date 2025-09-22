# IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs

**Korean Title:** IMPQ: 대형 언어 모델(LLMs)을 위한 상호작용 인식 계층별 혼합 정밀도 양자화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interaction-aware Mixed-Precision Quantization

## 🔗 유사한 논문
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony On Multilingual Data Allocation for Large Language Models Pretraining]] (83.9% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM Language of Browsing]] (83.1% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.7% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.5% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO A Framework for Confidence-Aware Routing of Large Language Models]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15455v1 Announce Type: new 
Abstract: Large Language Models (LLMs) promise impressive capabilities, yet their multi-billion-parameter scale makes on-device or low-resource deployment prohibitive. Mixed-precision quantization offers a compelling solution, but existing methods struggle when the average precision drops below four bits, as they rely on isolated, layer-specific metrics that overlook critical inter-layer interactions affecting overall performance. In this paper, we propose two innovations to address these limitations. First, we frame the mixed-precision quantization problem as a cooperative game among layers and introduce Shapley-based Progressive Quantization Estimation (SPQE) to efficiently obtain accurate Shapley estimates of layer sensitivities and inter-layer interactions. Second, building upon SPQE, we propose Interaction-aware Mixed-Precision Quantization (IMPQ) which translates these Shapley estimates into a binary quadratic optimization formulation, assigning either 2 or 4-bit precision to layers under strict memory constraints. Comprehensive experiments conducted on Llama-3, Gemma-2, and Qwen-3 models across three independent PTQ backends (Quanto, HQQ, GPTQ) demonstrate IMPQ's scalability and consistently superior performance compared to methods relying solely on isolated metrics. Across average precisions spanning 4 bit down to 2 bit, IMPQ cuts Perplexity by 20 to 80 percent relative to the best baseline, with the margin growing as the bit-width tightens.

## 🔍 Abstract (한글 번역)

arXiv:2509.15455v1 발표 유형: 새로운  
초록: 대형 언어 모델(LLMs)은 인상적인 능력을 약속하지만, 수십억 개의 매개변수 규모로 인해 장치 내 또는 저자원 환경에서의 배포가 어렵습니다. 혼합 정밀도 양자화는 매력적인 해결책을 제공하지만, 기존 방법들은 평균 정밀도가 4비트 이하로 떨어질 때 고립된 계층별 메트릭에 의존하여 전체 성능에 영향을 미치는 중요한 계층 간 상호작용을 간과합니다. 본 논문에서는 이러한 제한점을 해결하기 위한 두 가지 혁신을 제안합니다. 첫째, 혼합 정밀도 양자화 문제를 계층 간의 협력 게임으로 설정하고, 계층 민감도와 계층 간 상호작용에 대한 정확한 샤플리 추정치를 효율적으로 얻기 위해 샤플리 기반 점진적 양자화 추정(SPQE)을 도입합니다. 둘째, SPQE를 기반으로, 이러한 샤플리 추정치를 이진 이차 최적화 공식으로 변환하여 엄격한 메모리 제약 하에서 계층에 2비트 또는 4비트 정밀도를 할당하는 상호작용 인식 혼합 정밀도 양자화(IMPQ)를 제안합니다. Llama-3, Gemma-2, Qwen-3 모델에서 세 가지 독립적인 PTQ 백엔드(Quanto, HQQ, GPTQ)를 대상으로 수행된 종합적인 실험은 IMPQ의 확장성과 고립된 메트릭에만 의존하는 방법에 비해 일관되게 우수한 성능을 보여줍니다. 평균 정밀도가 4비트에서 2비트로 내려가는 동안, IMPQ는 최상의 기준선에 비해 당혹도를 20%에서 80%까지 줄이며, 비트 폭이 좁아질수록 그 차이는 더욱 커집니다.

## 📝 요약

대형 언어 모델(LLM)의 활용은 인상적이지만, 수십억 개의 매개변수로 인해 기기 내 또는 저자원 환경에서의 배포가 어렵습니다. 혼합 정밀도 양자화는 이를 해결할 수 있는 방법이지만, 기존 방법은 평균 정밀도가 4비트 이하로 떨어질 때 성능이 저하됩니다. 본 논문에서는 이러한 문제를 해결하기 위해 두 가지 혁신을 제안합니다. 첫째, 혼합 정밀도 양자화 문제를 계층 간 협력 게임으로 보고, Shapley 기반의 점진적 양자화 추정(SPQE)을 도입하여 계층 민감도와 상호작용을 효율적으로 추정합니다. 둘째, SPQE를 기반으로 상호작용 인식 혼합 정밀도 양자화(IMPQ)를 제안하여, 이를 이진 이차 최적화 문제로 변환해 엄격한 메모리 제약 하에서 계층에 2비트 또는 4비트 정밀도를 할당합니다. Llama-3, Gemma-2, Qwen-3 모델을 대상으로 한 실험에서 IMPQ는 기존 방법보다 일관되게 우수한 성능을 보였으며, 평균 정밀도가 4비트에서 2비트로 감소할수록 Perplexity를 20%에서 80%까지 줄였습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLMs)의 장치 내 배포를 위한 혼합 정밀도 양자화의 필요성을 강조합니다.

- 2. 기존 방법의 한계를 극복하기 위해 Shapley 기반의 점진적 양자화 추정(SPQE)을 도입하여 계층 민감도와 상호작용을 효율적으로 추정합니다.

- 3. SPQE를 기반으로 상호작용을 고려한 혼합 정밀도 양자화(IMPQ)를 제안하여 메모리 제약 하에서 2비트 또는 4비트 정밀도를 할당합니다.

- 4. Llama-3, Gemma-2, Qwen-3 모델에서의 실험 결과, IMPQ는 기존 방법보다 일관되게 우수한 성능을 보이며, 비트 폭이 좁아질수록 퍼플렉시티를 20~80% 감소시킵니다.

---

*Generated on 2025-09-22 15:14:41*