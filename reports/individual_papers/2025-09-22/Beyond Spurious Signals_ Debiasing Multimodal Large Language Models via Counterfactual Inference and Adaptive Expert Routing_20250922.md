# Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing

**Korean Title:** 스퓨리어스 신호를 넘어: 반사실적 추론과 적응형 전문가 라우팅을 통한 다중 모달 대형 언어 모델의 편향 제거

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Causal Mediation-based Debiasing

## 🔗 유사한 논문
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (87.2% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (86.1% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (85.8% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.1% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (85.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15361v1 Announce Type: cross 
Abstract: Multimodal Large Language Models (MLLMs) have shown substantial capabilities in integrating visual and textual information, yet frequently rely on spurious correlations, undermining their robustness and generalization in complex multimodal reasoning tasks. This paper addresses the critical challenge of superficial correlation bias in MLLMs through a novel causal mediation-based debiasing framework. Specially, we distinguishing core semantics from spurious textual and visual contexts via counterfactual examples to activate training-stage debiasing and employ a Mixture-of-Experts (MoE) architecture with dynamic routing to selectively engages modality-specific debiasing experts. Empirical evaluation on multimodal sarcasm detection and sentiment analysis tasks demonstrates that our framework significantly surpasses unimodal debiasing strategies and existing state-of-the-art models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15361v1 발표 유형: 교차  
초록: 다중 모달 대형 언어 모델(Multimodal Large Language Models, MLLMs)은 시각적 정보와 텍스트 정보를 통합하는 데 있어 상당한 능력을 보여주었지만, 종종 잘못된 상관관계에 의존하여 복잡한 다중 모달 추론 작업에서의 견고성과 일반화를 저해합니다. 본 논문은 MLLMs에서의 피상적 상관 편향 문제를 새로운 인과 매개 기반 편향 제거 프레임워크를 통해 해결합니다. 특히, 반사실적 예제를 통해 핵심 의미를 잘못된 텍스트 및 시각적 맥락에서 구별하여 훈련 단계에서의 편향 제거를 활성화하고, 동적 라우팅을 갖춘 전문가 혼합(Mixture-of-Experts, MoE) 아키텍처를 사용하여 모달리티별 편향 제거 전문가를 선택적으로 참여시킵니다. 다중 모달 풍자 감지 및 감정 분석 작업에 대한 실증적 평가 결과, 본 프레임워크가 단일 모달 편향 제거 전략 및 기존 최첨단 모델을 크게 능가함을 보여줍니다.

## 📝 요약

이 논문은 다중 모달 대형 언어 모델(MLLMs)의 피상적 상관 편향 문제를 해결하기 위해 새로운 인과 매개 기반 디바이싱 프레임워크를 제안합니다. 핵심 기여는 반사실적 예제를 통해 핵심 의미를 구별하고, Mixture-of-Experts(MoE) 아키텍처를 활용하여 모달리티별 디바이싱 전문가를 선택적으로 활성화하는 것입니다. 실험 결과, 제안된 프레임워크는 다중 모달 풍자 탐지 및 감정 분석 작업에서 기존의 단일 모달 디바이싱 전략과 최신 모델을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 다중모달 대형 언어 모델(MLLMs)은 시각적 및 텍스트 정보를 통합하는 데 뛰어난 능력을 보이지만, 종종 피상적인 상관관계에 의존하여 복잡한 다중모달 추론 작업에서의 견고성과 일반화가 저하됩니다.

- 2. 본 논문은 인과 매개 기반의 새로운 디바이싱 프레임워크를 통해 MLLMs의 피상적 상관관계 편향 문제를 해결합니다.

- 3. 반사실적 예제를 통해 핵심 의미를 피상적인 텍스트 및 시각적 맥락에서 구분하여 훈련 단계에서의 디바이싱을 활성화합니다.

- 4. Mixture-of-Experts (MoE) 아키텍처와 동적 라우팅을 사용하여 모달리티별 디바이싱 전문가를 선택적으로 참여시킵니다.

- 5. 다중모달 풍자 감지 및 감정 분석 작업에 대한 실증적 평가에서 제안된 프레임워크가 단일 모달 디바이싱 전략 및 기존 최신 모델을 크게 능가하는 것으로 나타났습니다.

---

*Generated on 2025-09-22 13:53:56*