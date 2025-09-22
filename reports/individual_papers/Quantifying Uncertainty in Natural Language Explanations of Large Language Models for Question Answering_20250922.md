# Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering

**Korean Title:** 대형 언어 모델의 질문 응답에 대한 자연어 설명에서 불확실성 정량화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robust Uncertainty Estimation

## 🔗 유사한 논문
- [[2025-09-22/Efficient Real-time Refinement of Language Model Text Generation_20250922|Efficient Real-time Refinement of Language Model Text Generation]] (84.0% similar)
- [[2025-09-22/Knowledge-Driven Hallucination in Large Language Models_ An Empirical Study on Process Modeling_20250922|Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling]] (83.5% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (82.8% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (82.6% similar)
- [[2025-09-17/Do Large Language Models Understand Word Senses_20250917|Do Large Language Models Understand Word Senses]] (82.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15403v1 Announce Type: cross 
Abstract: Large language models (LLMs) have shown strong capabilities, enabling concise, context-aware answers in question answering (QA) tasks. The lack of transparency in complex LLMs has inspired extensive research aimed at developing methods to explain large language behaviors. Among existing explanation methods, natural language explanations stand out due to their ability to explain LLMs in a self-explanatory manner and enable the understanding of model behaviors even when the models are closed-source. However, despite these promising advancements, there is no existing work studying how to provide valid uncertainty guarantees for these generated natural language explanations. Such uncertainty quantification is critical in understanding the confidence behind these explanations. Notably, generating valid uncertainty estimates for natural language explanations is particularly challenging due to the auto-regressive generation process of LLMs and the presence of noise in medical inquiries. To bridge this gap, in this work, we first propose a novel uncertainty estimation framework for these generated natural language explanations, which provides valid uncertainty guarantees in a post-hoc and model-agnostic manner. Additionally, we also design a novel robust uncertainty estimation method that maintains valid uncertainty guarantees even under noise. Extensive experiments on QA tasks demonstrate the desired performance of our methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.15403v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)은 질문 응답(QA) 작업에서 간결하고 맥락에 맞는 답변을 제공할 수 있는 강력한 능력을 보여주었습니다. 복잡한 LLM의 투명성 부족은 대형 언어 행동을 설명하는 방법을 개발하기 위한 광범위한 연구를 촉발했습니다. 기존의 설명 방법 중에서 자연어 설명은 LLM을 자기 설명 방식으로 설명하고 모델이 비공개 소스일 때도 모델 행동을 이해할 수 있게 해준다는 점에서 두드러집니다. 그러나 이러한 유망한 발전에도 불구하고, 생성된 자연어 설명에 대해 유효한 불확실성 보장을 제공하는 방법을 연구한 기존 연구는 없습니다. 이러한 불확실성 정량화는 이러한 설명의 신뢰도를 이해하는 데 중요합니다. 특히, 자연어 설명에 대한 유효한 불확실성 추정치를 생성하는 것은 LLM의 자동 회귀 생성 과정과 의료 문의에서의 잡음 존재로 인해 특히 어렵습니다. 이러한 격차를 해소하기 위해, 본 연구에서는 먼저 생성된 자연어 설명에 대해 사후적이고 모델 비종속적인 방식으로 유효한 불확실성 보장을 제공하는 새로운 불확실성 추정 프레임워크를 제안합니다. 또한, 잡음이 있는 상황에서도 유효한 불확실성 보장을 유지하는 새로운 강력한 불확실성 추정 방법을 설계했습니다. QA 작업에 대한 광범위한 실험은 우리의 방법이 원하는 성능을 보여줍니다.

## 📝 요약

대형 언어 모델(LLM)은 질문 응답(QA) 작업에서 뛰어난 능력을 보이지만, 그 복잡성으로 인해 투명성이 부족합니다. 본 연구는 LLM의 자연어 설명에 대한 유효한 불확실성 보장을 제공하는 방법을 제안합니다. 자연어 설명은 모델의 행동을 이해하는 데 유리하지만, 불확실성 정량화가 필요합니다. 특히, LLM의 자동 회귀 생성 과정과 의료 문의의 노이즈로 인해 불확실성 추정이 어렵습니다. 이를 해결하기 위해, 우리는 사후적이고 모델에 구애받지 않는 불확실성 추정 프레임워크를 제안하고, 노이즈 환경에서도 유효한 불확실성 보장을 유지하는 강력한 추정 방법을 설계했습니다. QA 작업에 대한 실험 결과, 제안된 방법의 성능이 입증되었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 질문 응답(QA) 작업에서 강력한 능력을 보여주며, 간결하고 맥락을 고려한 답변을 제공할 수 있습니다.

- 2. 자연어 설명은 LLM의 행동을 자체 설명 방식으로 이해할 수 있게 하며, 모델이 비공개 소스일 때도 이해를 돕습니다.

- 3. 자연어 설명에 대한 유효한 불확실성 보장을 제공하는 연구는 아직 없으며, 이는 설명의 신뢰도를 이해하는 데 중요합니다.

- 4. 본 연구에서는 생성된 자연어 설명에 대해 유효한 불확실성 보장을 제공하는 새로운 불확실성 추정 프레임워크를 제안합니다.

- 5. 제안된 방법은 노이즈가 있는 상황에서도 유효한 불확실성 보장을 유지하는 강력한 불확실성 추정 방법을 포함합니다.

---

*Generated on 2025-09-22 15:38:07*