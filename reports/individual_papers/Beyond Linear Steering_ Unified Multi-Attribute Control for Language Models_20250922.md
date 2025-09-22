# Beyond Linear Steering: Unified Multi-Attribute Control for Language Models

**Korean Title:** 선형 조정을 넘어서: 언어 모델을 위한 통합 다중 속성 제어

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Compositional Behavioral Control

## 🔗 유사한 논문
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (85.9% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (85.2% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (83.7% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.4% similar)
- [[2025-09-22/World Modelling Improves Language Model Agents_20250922|World Modelling Improves Language Model Agents]] (82.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.24535v2 Announce Type: replace-cross 
Abstract: Controlling multiple behavioral attributes in large language models (LLMs) at inference time is a challenging problem due to interference between attributes and the limitations of linear steering methods, which assume additive behavior in activation space and require per-attribute tuning. We introduce K-Steering, a unified and flexible approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time. This avoids linearity assumptions, removes the need for storing and tuning separate attribute vectors, and allows dynamic composition of behaviors without retraining. To evaluate our method, we propose two new benchmarks, ToneBank and DebateMix, targeting compositional behavioral control. Empirical results across 3 model families, validated by both activation-based classifiers and LLM-based judges, demonstrate that K-Steering outperforms strong baselines in accurately steering multiple behaviors.

## 🔍 Abstract (한글 번역)

arXiv:2505.24535v2 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)에서 여러 행동 속성을 추론 시간에 제어하는 것은 속성 간의 간섭과 활성화 공간에서의 가산적 행동을 가정하고 속성별 조정을 요구하는 선형 조정 방법의 한계로 인해 어려운 문제입니다. 우리는 숨겨진 활성화에 대해 단일 비선형 다중 레이블 분류기를 훈련하고 추론 시간에 그래디언트를 통해 개입 방향을 계산하는 통합적이고 유연한 접근 방식인 K-Steering을 소개합니다. 이는 선형성 가정을 피하고, 별도의 속성 벡터를 저장하고 조정할 필요를 제거하며, 재훈련 없이 행동의 동적 구성을 허용합니다. 우리의 방법을 평가하기 위해, 우리는 구성적 행동 제어를 목표로 하는 두 가지 새로운 벤치마크인 ToneBank와 DebateMix를 제안합니다. 활성화 기반 분류기와 LLM 기반 판사 모두에 의해 검증된 3개의 모델 계열에 걸친 실증적 결과는 K-Steering이 여러 행동을 정확하게 조정하는 데 있어 강력한 기준선을 능가함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서 여러 행동 속성을 제어하는 문제를 다룹니다. 기존의 선형 조정 방법은 속성 간 간섭 문제와 속성별 조정이 필요하다는 한계가 있습니다. 이를 해결하기 위해, 비선형 다중 라벨 분류기를 사용하여 숨겨진 활성화에서 개입 방향을 계산하는 K-Steering 방법을 제안합니다. 이 방법은 선형 가정 없이 동적 행동 조합이 가능하며, 별도의 속성 벡터 저장 및 조정이 필요하지 않습니다. ToneBank와 DebateMix라는 두 가지 새로운 벤치마크를 통해 평가한 결과, K-Steering은 여러 행동을 정확하게 조정하는 데 있어 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. K-Steering은 대형 언어 모델에서 여러 행동 속성을 제어하기 위한 비선형 다중 레이블 분류기를 활용한 통합적 접근법을 제안합니다.

- 2. 이 방법은 활성화 공간에서의 선형성을 가정하지 않으며, 속성 벡터의 저장 및 조정이 필요 없고, 재훈련 없이 행동의 동적 구성이 가능합니다.

- 3. ToneBank와 DebateMix라는 두 가지 새로운 벤치마크를 제안하여 K-Steering의 성능을 평가합니다.

- 4. K-Steering은 3개의 모델 계열에서 강력한 기준선을 능가하여 여러 행동을 정확하게 조정하는 데 뛰어난 성능을 보입니다.

---

*Generated on 2025-09-22 14:52:25*