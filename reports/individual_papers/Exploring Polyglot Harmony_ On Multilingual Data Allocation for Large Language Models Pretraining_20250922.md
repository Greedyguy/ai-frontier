# Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining

**Korean Title:** 다중언어 조화 탐구: 대형 언어 모델 사전 훈련을 위한 다중언어 데이터 할당

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multilingual Data Allocation

## 🔗 유사한 논문
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (85.9% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (85.3% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.6% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (84.1% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (83.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15556v1 Announce Type: cross 
Abstract: Large language models (LLMs) have become integral to a wide range of applications worldwide, driving an unprecedented global demand for effective multilingual capabilities. Central to achieving robust multilingual performance is the strategic allocation of language proportions within training corpora. However, determining optimal language ratios is highly challenging due to intricate cross-lingual interactions and sensitivity to dataset scale. This paper introduces Climb (Cross-Lingual Interaction-aware Multilingual Balancing), a novel framework designed to systematically optimize multilingual data allocation. At its core, Climb introduces a cross-lingual interaction-aware language ratio, explicitly quantifying each language's effective allocation by capturing inter-language dependencies. Leveraging this ratio, Climb proposes a principled two-step optimization procedure--first equalizing marginal benefits across languages, then maximizing the magnitude of the resulting language allocation vectors--significantly simplifying the inherently complex multilingual optimization problem. Extensive experiments confirm that Climb can accurately measure cross-lingual interactions across various multilingual settings. LLMs trained with Climb-derived proportions consistently achieve state-of-the-art multilingual performance, even achieving competitive performance with open-sourced LLMs trained with more tokens.

## 🔍 Abstract (한글 번역)

arXiv:2509.15556v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)은 전 세계적으로 다양한 응용 분야에 필수적인 요소가 되었으며, 효과적인 다국어 기능에 대한 전례 없는 글로벌 수요를 이끌고 있습니다. 강력한 다국어 성능을 달성하기 위해서는 훈련 코퍼스 내에서 언어 비율의 전략적 할당이 중요합니다. 그러나 최적의 언어 비율을 결정하는 것은 복잡한 언어 간 상호작용과 데이터셋 규모에 대한 민감성 때문에 매우 어렵습니다. 이 논문에서는 체계적으로 다국어 데이터 할당을 최적화하기 위해 설계된 새로운 프레임워크인 Climb (Cross-Lingual Interaction-aware Multilingual Balancing)을 소개합니다. Climb의 핵심은 언어 간 종속성을 포착하여 각 언어의 효과적인 할당을 명시적으로 정량화하는 언어 간 상호작용 인식 언어 비율을 도입하는 것입니다. 이 비율을 활용하여 Climb은 먼저 언어 간 한계 이익을 균등화한 다음, 결과 언어 할당 벡터의 크기를 최대화하는 원칙적인 2단계 최적화 절차를 제안하여 본질적으로 복잡한 다국어 최적화 문제를 크게 단순화합니다. 광범위한 실험을 통해 Climb이 다양한 다국어 환경에서 언어 간 상호작용을 정확하게 측정할 수 있음을 확인했습니다. Climb에서 도출된 비율로 훈련된 LLM은 일관되게 최첨단 다국어 성능을 달성하며, 더 많은 토큰으로 훈련된 오픈 소스 LLM과도 경쟁력 있는 성능을 발휘합니다.

## 📝 요약

이 논문은 다국어 성능을 최적화하기 위한 새로운 프레임워크인 Climb을 소개합니다. Climb은 언어 간 상호작용을 고려한 언어 비율을 도입하여 각 언어의 효과적인 할당을 정량화합니다. 이를 통해 언어 할당을 최적화하는 두 단계 절차를 제안하며, 복잡한 다국어 최적화 문제를 단순화합니다. 실험 결과, Climb을 사용한 LLM은 다양한 다국어 환경에서 뛰어난 성능을 보였으며, 더 많은 토큰으로 훈련된 공개 LLM과도 경쟁력 있는 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 다국어 성능을 최적화하기 위해 언어 비율의 전략적 할당이 중요하다.

- 2. Climb는 언어 간 상호작용을 고려한 새로운 언어 비율을 도입하여 다국어 데이터 할당을 체계적으로 최적화하는 프레임워크이다.

- 3. Climb는 언어 간 상호작용을 정확히 측정하고, 이를 통해 다국어 최적화 문제를 단순화한다.

- 4. Climb로 훈련된 LLM은 최첨단 다국어 성능을 일관되게 달성하며, 더 많은 토큰으로 훈련된 공개 LLM과도 경쟁력을 갖춘다.

---

*Generated on 2025-09-22 14:01:49*