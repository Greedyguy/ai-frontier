---
keywords:
  - Large Language Models
  - Chain-of-thought Reasoning
  - Inference Optimization
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14004
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:31:40.620291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Chain-of-thought Reasoning",
    "Inference Optimization"
  ],
  "rejected_keywords": [
    "Self-consistency Prompting"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Chain-of-thought Reasoning": 0.78,
    "Inference Optimization": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Early Stopping Chain-of-thoughts in Large Language Models

**Korean Title:** 대형 언어 모델에서 조기 중단된 사고 연쇄

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Chain-of-thought Reasoning|Chain-of-thoughts]]
**🚀 Evolved Concepts**: [[keywords/Inference Optimization|Inference-time method]]

## 🔗 유사한 논문
- [[Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (90.1% similar)
- [[Uni-cot_Towards_Unified_Chain-of-Thought_Reasoning_Across_Text_and_Vision_20250918|Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (84.8% similar)
- [[MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (81.9% similar)
- [[Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness]] (80.7% similar)
- [[THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14004v1 Announce Type: new 
Abstract: Reasoning large language models (LLMs) have demonstrated superior capacities in solving complicated problems by generating long chain-of-thoughts (CoT), but such a lengthy CoT incurs high inference costs. In this study, we introduce ES-CoT, an inference-time method that shortens CoT generation by detecting answer convergence and stopping early with minimal performance loss. At the end of each reasoning step, we prompt the LLM to output its current final answer, denoted as a step answer. We then track the run length of consecutive identical step answers as a measure of answer convergence. Once the run length exhibits a sharp increase and exceeds a minimum threshold, the generation is terminated. We provide both empirical and theoretical support for this heuristic: step answers steadily converge to the final answer, and large run-length jumps reliably mark this convergence. Experiments on five reasoning datasets across three LLMs show that ES-CoT reduces the number of inference tokens by about 41\% on average while maintaining accuracy comparable to standard CoT. Further, ES-CoT integrates seamlessly with self-consistency prompting and remains robust across hyperparameter choices, highlighting it as a practical and effective approach for efficient reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2509.14004v1 발표 유형: 새로운
요약: 대규모 언어 모델 (LLMs)은 긴 사고 체인 (CoT)을 생성하여 복잡한 문제를 해결하는 뛰어난 능력을 보여주었지만, 이러한 긴 CoT은 높은 추론 비용을 초래합니다. 본 연구에서는 ES-CoT라는 추론 시간 방법을 소개하여 답변 수렴을 감지하고 최소의 성능 손실로 조기 중단하여 CoT 생성을 단축합니다. 각 추론 단계의 끝에서 LLM에게 현재 최종 답변을 출력하도록 유도하고, 이를 단계 답변이라고 표시합니다. 그런 다음 연속적으로 동일한 단계 답변의 실행 길이를 답변 수렴의 측정으로 추적합니다. 실행 길이가 급격히 증가하고 최소 임계값을 초과하면 생성이 종료됩니다. 이 휴리스틱에 대한 경험적 및 이론적 지원을 제공합니다: 단계 답변은 최종 답변으로 꾸준히 수렴하고 큰 실행 길이의 점프는 이 수렴을 신뢰할 수 있게 표시합니다. 세 가지 LLM을 통해 다섯 가지 추론 데이터셋에서 수행한 실험 결과, ES-CoT는 표준 CoT와 비교 가능한 정확도를 유지하면서 추론 토큰의 수를 평균적으로 약 41% 줄입니다. 더 나아가, ES-CoT는 자기 일관성 프롬프팅과 매끄럽게 통합되며 하이퍼파라미터 선택에 따라 견고하게 유지되어 효율적인 추론을 위한 실용적이고 효과적인 접근 방식으로 강조됩니다.

## 📝 요약

이 연구는 대규모 언어 모델이 복잡한 문제를 해결하는 능력을 보여주는 동안, 긴 사고 체인(Chain-of-Thoughts, CoT)을 생성하는 것이 추론 비용을 증가시킨다는 문제를 다룬다. 본 연구에서는 ES-CoT라는 추론 시간 방법을 소개하여 답변 수렴을 감지하고 최소한의 성능 손실로 일찍 중지시키는 방법을 제안한다. 실험 결과, ES-CoT는 평균적으로 추론 토큰 수를 약 41% 줄이면서 표준 CoT와 비교 가능한 정확도를 유지함을 보여주며, 자기 일관성 프롬프팅과 원활하게 통합되고 하이퍼파라미터 선택에 강건하다는 것을 강조한다.

## 🎯 주요 포인트

- ES-CoT는 답변 수렴을 감지하여 CoT 생성을 단축시키는 추론 시간 방법이다.

- ES-CoT는 추론 토큰 수를 평균 41% 줄이면서 정확도를 유지한다.

- ES-CoT는 자기 일관성 프롬프팅과 원활하게 통합되며 효율적인 추론을 위한 실용적이고 효과적인 방법이다.

---

*Generated on 2025-09-18 16:51:35*