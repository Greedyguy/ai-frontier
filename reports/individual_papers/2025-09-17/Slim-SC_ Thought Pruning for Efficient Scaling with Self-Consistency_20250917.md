# Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency

**Korean Title:** 슬림-SC: 자기 일관성을 통한 효율적인 확장을 위한 사고 가지치기

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Colin Hong|Colin Hong]] [[authors/Xu Guo|Xu Guo]] [[authors/Anand Chaanan Singh|Anand Chaanan Singh]] [[authors/Esha Choukse|Esha Choukse]] [[authors/Dmitrii Ustiugov|Dmitrii Ustiugov]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Thought Pruning

## 🔗 유사한 논문
- [[Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression A Self-Optimizing Framework]] (83.8% similar)
- [[ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (83.4% similar)
- [[Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (82.5% similar)
- [[Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies_20250918|Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies]] (80.9% similar)
- [[From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (80.2% similar)

## 📋 저자 정보

**Authors:** Colin Hong, Xu Guo, Anand Chaanan Singh, Esha Choukse, Dmitrii Ustiugov

## 📄 Abstract (원문)

Recently, Test-Time Scaling (TTS) has gained increasing attention for
improving LLM reasoning performance at test time without retraining the model.
A notable TTS technique is Self-Consistency (SC), which generates multiple
reasoning chains in parallel and selects the final answer via majority voting.
While effective, the order-of-magnitude computational overhead limits its broad
deployment. Prior attempts to accelerate SC mainly rely on model-based
confidence scores or heuristics with limited empirical support. For the first
time, we theoretically and empirically analyze the inefficiencies of SC and
reveal actionable opportunities for improvement. Building on these insights, we
propose Slim-SC, a step-wise pruning strategy that identifies and removes
redundant chains using inter-chain similarity at the thought level. Experiments
on three STEM reasoning datasets and two recent LLM architectures show that
Slim-SC reduces inference latency and KVC usage by up to 45% and 26%,
respectively, with R1-Distill, while maintaining or improving accuracy, thus
offering a simple yet efficient TTS alternative for SC.

## 🔍 Abstract (한글 번역)

최근 테스트 시 확장(Test-Time Scaling, TTS)은 모델을 재훈련하지 않고도 테스트 시 대형 언어 모델(LLM)의 추론 성능을 향상시키기 위한 방법으로 점점 더 많은 주목을 받고 있습니다. 주목할 만한 TTS 기법 중 하나는 자기 일관성(Self-Consistency, SC)으로, 여러 개의 추론 체인을 병렬로 생성하고 다수결 투표를 통해 최종 답변을 선택합니다. 효과적이긴 하지만, 대규모의 계산 오버헤드는 광범위한 배포를 제한합니다. SC를 가속화하려는 이전의 시도들은 주로 모델 기반의 신뢰도 점수나 경험적 지원이 제한적인 휴리스틱에 의존했습니다. 본 연구에서는 처음으로 SC의 비효율성을 이론적 및 경험적으로 분석하고 개선을 위한 실질적인 기회를 밝혀냅니다. 이러한 통찰을 바탕으로, 우리는 Slim-SC라는 단계별 가지치기 전략을 제안하며, 이는 사고 수준에서 체인 간 유사성을 사용하여 중복된 체인을 식별하고 제거합니다. 세 가지 STEM 추론 데이터셋과 두 가지 최신 LLM 아키텍처에 대한 실험 결과, Slim-SC는 R1-Distill을 통해 추론 지연 시간과 KVC 사용을 각각 최대 45% 및 26%까지 줄이면서도 정확도를 유지하거나 향상시켜 SC에 대한 간단하면서도 효율적인 TTS 대안을 제공합니다.

## 📝 요약

이 논문은 LLM의 추론 성능을 향상시키기 위한 Test-Time Scaling(TTS) 기법 중 하나인 Self-Consistency(SC)의 비효율성을 이론적, 실험적으로 분석하고 개선 방안을 제시합니다. SC는 다수결을 통해 최종 답변을 선택하는 방식으로 효과적이지만, 높은 계산 비용이 문제입니다. 이를 해결하기 위해 제안된 Slim-SC는 사고 수준에서의 유사성을 활용하여 불필요한 추론 체인을 제거하는 단계적 가지치기 전략입니다. 실험 결과, Slim-SC는 세 가지 STEM 추론 데이터셋과 두 가지 LLM 아키텍처에서 추론 지연과 KVC 사용을 각각 최대 45%와 26% 줄이면서도 정확도를 유지하거나 향상시켰습니다. 이는 SC의 효율적인 대안으로 제시됩니다.

## 🎯 주요 포인트

- 1. Test-Time Scaling (TTS)는 모델을 재훈련하지 않고 테스트 시 LLM의 추론 성능을 향상시키는 방법으로 주목받고 있습니다.

- 2. Self-Consistency (SC)는 병렬로 여러 추론 체인을 생성하고 다수결로 최종 답을 선택하는 TTS 기법이지만, 계산 비용이 높아 널리 사용되기 어렵습니다.

- 3. Slim-SC는 체인 간 유사성을 활용하여 불필요한 체인을 제거하는 단계별 가지치기 전략으로, SC의 비효율성을 개선합니다.

- 4. Slim-SC는 세 가지 STEM 추론 데이터셋과 두 가지 최신 LLM 아키텍처 실험에서 추론 지연과 KVC 사용을 각각 최대 45%와 26% 줄이면서 정확도를 유지하거나 향상시켰습니다.

- 5. Slim-SC는 SC를 위한 간단하면서도 효율적인 TTS 대안으로 제안됩니다.

---

*Generated on 2025-09-20 09:20:54*