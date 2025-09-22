# Cross-Attention Speculative Decoding

**Korean Title:** 교차 주의 추론 디코딩

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-attention Speculative Decoding

## 🔗 유사한 논문
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (79.7% similar)
- [[2025-09-22/AttentionDrop_ A Novel Regularization Method for Transformer Models_20250922|AttentionDrop A Novel Regularization Method for Transformer Models]] (79.1% similar)
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (78.9% similar)
- [[2025-09-22/Attention Schema-based Attention Control (ASAC)_ A Cognitive-Inspired Approach for Attention Management in Transformers_20250922|Attention Schema-based Attention Control (ASAC) A Cognitive-Inspired Approach for Attention Management in Transformers]] (78.8% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.24544v2 Announce Type: replace-cross 
Abstract: Speculative decoding (SD) is a widely adopted approach for accelerating inference in large language models (LLMs), particularly when the draft and target models are well aligned. However, state-of-the-art SD methods typically rely on tightly coupled, self-attention-based Transformer decoders, often augmented with auxiliary pooling or fusion layers. This coupling makes them increasingly complex and harder to generalize across different models. We present Budget EAGLE (Beagle), the first, to our knowledge, cross-attention-based Transformer decoder SD model that achieves performance on par with leading self-attention SD models (EAGLE-v2) while eliminating the need for pooling or auxiliary components, simplifying the architecture, improving training efficiency, and maintaining stable memory usage during training-time simulation. To enable effective training of this novel architecture, we propose Two-Stage Block-Attention Training, a new method that achieves training stability and convergence efficiency in block-level attention scenarios. Extensive experiments across multiple LLMs and datasets show that Beagle achieves competitive inference speedups and higher training efficiency than EAGLE-v2, offering a strong alternative for architectures in speculative decoding.

## 🔍 Abstract (한글 번역)

arXiv:2505.24544v2 발표 유형: 교체-교차  
초록: 추론 속도를 높이기 위해 대형 언어 모델(LLMs)에서 널리 채택된 접근 방식인 추측 디코딩(SD)은 초안 모델과 목표 모델이 잘 정렬될 때 특히 효과적입니다. 그러나 최첨단 SD 방법은 일반적으로 보조 풀링 또는 융합 레이어로 보강된, 밀접하게 결합된 자기 주의 기반 Transformer 디코더에 의존합니다. 이러한 결합은 모델 간의 일반화가 점점 더 복잡하고 어려워지게 만듭니다. 우리는, 우리가 아는 한 최초로, 교차 주의 기반 Transformer 디코더 SD 모델인 Budget EAGLE (Beagle)을 제시합니다. 이는 풀링이나 보조 구성 요소의 필요성을 제거하면서, 아키텍처를 단순화하고, 훈련 효율성을 개선하며, 훈련 시간 시뮬레이션 동안 안정적인 메모리 사용을 유지하면서, 선도적인 자기 주의 SD 모델(EAGLE-v2)과 동등한 성능을 달성합니다. 이 새로운 아키텍처의 효과적인 훈련을 가능하게 하기 위해, 우리는 블록 수준 주의 시나리오에서 훈련 안정성과 수렴 효율성을 달성하는 새로운 방법인 이단계 블록 주의 훈련을 제안합니다. 여러 LLM과 데이터셋에 걸친 광범위한 실험은 Beagle이 EAGLE-v2보다 경쟁력 있는 추론 속도 향상과 더 높은 훈련 효율성을 달성하여 추측 디코딩 아키텍처에 대한 강력한 대안을 제공함을 보여줍니다.

## 📝 요약

Budget EAGLE(Beagle)은 최초로 교차 주의 기반의 Transformer 디코더를 사용한 추론 가속화 모델로, 기존의 자기 주의 기반 모델(EAGLE-v2)과 유사한 성능을 보입니다. Beagle은 보조 구성 요소 없이 간단한 구조로 훈련 효율성을 높이고 메모리 사용을 안정적으로 유지합니다. 이를 위해 새로운 Two-Stage Block-Attention Training 방법론을 제안하여 블록 수준 주의 시나리오에서 훈련 안정성과 수렴 효율성을 달성합니다. 다양한 대형 언어 모델과 데이터셋을 대상으로 한 실험에서 Beagle은 EAGLE-v2보다 높은 훈련 효율성과 경쟁력 있는 추론 속도를 보여, 추론 가속화 아키텍처의 강력한 대안이 됩니다.

## 🎯 주요 포인트

- 1. Budget EAGLE (Beagle)는 최초의 교차 주의 기반 Transformer 디코더 추론 모델로, 기존의 자기 주의 기반 모델과 유사한 성능을 유지하면서도 보조 구성 요소 없이 아키텍처를 단순화합니다.

- 2. Beagle은 훈련 효율성을 높이고 훈련 시뮬레이션 동안 메모리 사용의 안정성을 유지합니다.

- 3. 새로운 Two-Stage Block-Attention Training 방법을 제안하여 블록 수준 주의 시나리오에서 훈련 안정성과 수렴 효율성을 달성합니다.

- 4. 다양한 대형 언어 모델(LLM)과 데이터셋을 대상으로 한 실험에서 Beagle은 EAGLE-v2보다 경쟁력 있는 추론 속도 향상과 높은 훈련 효율성을 보였습니다.

---

*Generated on 2025-09-22 14:52:44*