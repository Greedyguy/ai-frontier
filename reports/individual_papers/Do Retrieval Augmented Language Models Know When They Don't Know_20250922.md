# Do Retrieval Augmented Language Models Know When They Don't Know?

**Korean Title:** 회수 증강 언어 모델은 자신이 모르는 것을 알고 있는가?

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: In-context Fine-tuning

## 🔗 유사한 논문
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (84.4% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (83.9% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (83.8% similar)
- [[2025-09-22/Efficient Real-time Refinement of Language Model Text Generation_20250922|Efficient Real-time Refinement of Language Model Text Generation]] (83.6% similar)
- [[2025-09-22/Knowledge-Driven Hallucination in Large Language Models_ An Empirical Study on Process Modeling_20250922|Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling]] (83.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01476v2 Announce Type: replace-cross 
Abstract: Existing Large Language Models (LLMs) occasionally generate plausible yet factually incorrect responses, known as hallucinations. Researchers are primarily using two approaches to mitigate hallucinations, namely Retrieval Augmented Language Models (RALMs) and refusal post-training. However, current research predominantly emphasizes their individual effectiveness while overlooking the evaluation of the refusal capability of RALMs. In this study, we ask the fundamental question: Do RALMs know when they don't know? Specifically, we ask three questions. First, are RALMs well-calibrated regarding different internal and external knowledge states? We examine the influence of various factors. Contrary to expectations, we find that LLMs exhibit significant \textbf{over-refusal} behavior. Then, how does refusal post-training affect the over-refusal issue? We investigate the Refusal-aware Instruction Tuning and In-Context Fine-tuning methods. Our results show that the over-refusal problem is mitigated by In-context fine-tuning. but magnified by R-tuning. However, we also find that the refusal ability may conflict with the quality of the answer. Finally, we develop a simple yet effective refusal method for refusal post-trained models to improve their overall answer quality in terms of refusal and correct answers. Our study provides a more comprehensive understanding of the influence of important factors on RALM systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.01476v2 발표 유형: 교차 대체  
초록: 기존의 대형 언어 모델(LLMs)은 때때로 그럴듯하지만 사실과 다른 응답을 생성하는데, 이를 환각(hallucinations)이라고 합니다. 연구자들은 주로 환각을 줄이기 위해 검색 증강 언어 모델(RALMs)과 거부 후 훈련이라는 두 가지 접근 방식을 사용하고 있습니다. 그러나 현재 연구는 주로 이들의 개별적인 효과에 중점을 두고 있으며, RALMs의 거부 능력 평가를 간과하고 있습니다. 본 연구에서는 근본적인 질문을 제기합니다: RALMs는 자신이 모를 때를 알고 있는가? 구체적으로, 우리는 세 가지 질문을 제기합니다. 첫째, RALMs는 다양한 내부 및 외부 지식 상태에 대해 잘 조정되어 있는가? 우리는 다양한 요인의 영향을 조사합니다. 기대와 달리, LLMs는 상당한 \textbf{과잉 거부} 행동을 보인다는 것을 발견했습니다. 그렇다면, 거부 후 훈련은 과잉 거부 문제에 어떻게 영향을 미치는가? 우리는 거부 인식 지시 조정(Refusal-aware Instruction Tuning)과 맥락 내 미세 조정(In-Context Fine-tuning) 방법을 조사합니다. 우리의 결과는 맥락 내 미세 조정이 과잉 거부 문제를 완화하지만, R-조정(R-tuning)에 의해 확대된다는 것을 보여줍니다. 그러나 우리는 또한 거부 능력이 응답의 질과 충돌할 수 있음을 발견했습니다. 마지막으로, 우리는 거부 후 훈련된 모델의 전반적인 응답 품질을 거부와 올바른 응답 측면에서 향상시키기 위한 간단하지만 효과적인 거부 방법을 개발했습니다. 우리의 연구는 RALM 시스템에 중요한 요인들이 미치는 영향을 보다 포괄적으로 이해하는 데 기여합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 환각 문제를 해결하기 위한 방법으로 검색 증강 언어 모델(RALM)과 거부 후 훈련을 탐구합니다. 연구는 RALM의 거부 능력을 평가하는 데 중점을 두고, RALM이 과도한 거부 행동을 보인다는 것을 발견했습니다. 거부 후 훈련이 이러한 과도한 거부 문제에 미치는 영향을 분석한 결과, 문맥 내 미세 조정은 문제를 완화하지만 R-튜닝은 문제를 악화시킵니다. 또한, 거부 능력과 답변의 질이 상충할 수 있음을 발견했습니다. 최종적으로, 거부 후 훈련된 모델의 답변 품질을 개선하기 위한 간단하고 효과적인 거부 방법을 개발했습니다. 이 연구는 RALM 시스템에 영향을 미치는 중요한 요인들에 대한 포괄적인 이해를 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 때때로 사실과 다른 응답을 생성하는 환각 문제를 겪는다.

- 2. 환각 문제를 완화하기 위해 주로 검색 보강 언어 모델(RALM)과 거부 후 훈련 방법이 사용된다.

- 3. 연구 결과, RALM은 과도한 거부(over-refusal) 행동을 보이는 것으로 나타났다.

- 4. In-context 미세 조정은 과도한 거부 문제를 완화하지만, R-tuning은 이를 악화시킨다.

- 5. 거부 후 훈련된 모델의 전반적인 응답 품질을 향상시키기 위한 간단하면서도 효과적인 거부 방법을 개발하였다.

---

*Generated on 2025-09-22 15:01:07*