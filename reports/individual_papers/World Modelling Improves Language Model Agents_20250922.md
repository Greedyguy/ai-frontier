# World Modelling Improves Language Model Agents

**Korean Title:** 세계 모델링이 언어 모델 에이전트를 개선한다

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Scalable Planning RL Methods

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (85.6% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.4% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (84.9% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (84.8% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02918v2 Announce Type: replace 
Abstract: Tool use in stateful environments presents unique challenges for large language models (LLMs), where existing test-time compute strategies relying on repeated trials in the environment are impractical. We propose dynamics modelling (DyMo), a method that augments LLMs with a state prediction capability alongside function calling during post-training. This enables LLMs to predict the future states of their actions through an internal environment model. On the Berkeley Function Calling Leaderboard V2, DyMo improves success rates and significantly reduces hallucinations. We further integrate the internal environment model into self-verification sampling (SVS), and show that this substantially improves pass^k over number of trials k, and allows the model to refuse unreliable outputs. Together, DyMo and SVS greatly enhance the effectiveness and reliability of LLMs for tool use. We believe this work charts a path towards scalable planning RL methods for LLM inference without repeatedly querying the oracle environment.

## 🔍 Abstract (한글 번역)

arXiv:2506.02918v2 발표 유형: 교체  
초록: 상태 기반 환경에서의 도구 사용은 대형 언어 모델(LLMs)에게 독특한 도전 과제를 제시하며, 환경에서 반복적인 시도를 필요로 하는 기존의 테스트 시간 계산 전략은 비실용적입니다. 우리는 LLMs를 사후 훈련 중 함수 호출과 함께 상태 예측 기능으로 보강하는 방법인 동적 모델링(DyMo)을 제안합니다. 이를 통해 LLMs는 내부 환경 모델을 통해 자신의 행동의 미래 상태를 예측할 수 있습니다. Berkeley Function Calling Leaderboard V2에서 DyMo는 성공률을 향상시키고 환각을 크게 줄입니다. 우리는 내부 환경 모델을 자기 검증 샘플링(SVS)에 통합하여, 시도 횟수 k에 대한 pass^k를 크게 향상시키고, 모델이 신뢰할 수 없는 출력을 거부할 수 있도록 합니다. DyMo와 SVS는 함께 LLMs의 도구 사용에 대한 효과성과 신뢰성을 크게 향상시킵니다. 우리는 이 연구가 오라클 환경을 반복적으로 쿼리하지 않고 LLM 추론을 위한 확장 가능한 계획 강화 학습(RL) 방법으로 나아가는 길을 제시한다고 믿습니다.

## 📝 요약

이 논문은 상태가 있는 환경에서 도구를 사용하는 데 있어 대형 언어 모델(LLM)이 직면하는 문제를 해결하기 위해 DyMo라는 방법을 제안합니다. DyMo는 LLM에 상태 예측 기능을 추가하여, 훈련 후 함수 호출과 함께 내부 환경 모델을 통해 미래 상태를 예측할 수 있게 합니다. 이를 통해 Berkeley Function Calling Leaderboard V2에서 성공률을 높이고 환각을 줄였습니다. 또한, 내부 환경 모델을 자기 검증 샘플링(SVS)과 통합하여, 신뢰할 수 없는 출력을 거부하고, 시도 횟수 k에 따른 pass^k를 크게 개선했습니다. DyMo와 SVS는 LLM의 도구 사용 효과와 신뢰성을 크게 향상시키며, 반복적인 환경 쿼리 없이 확장 가능한 계획 강화 학습 방법으로의 길을 제시합니다.

## 🎯 주요 포인트

- 1. DyMo는 대형 언어 모델(LLM)에 상태 예측 기능을 추가하여 도구 사용 시 미래 상태를 예측할 수 있게 합니다.

- 2. Berkeley Function Calling Leaderboard V2에서 DyMo는 성공률을 높이고 환각 현상을 크게 줄였습니다.

- 3. DyMo와 SVS를 통합하여 모델이 신뢰할 수 없는 출력을 거부할 수 있도록 하며, pass^k 성능을 개선합니다.

- 4. 이 연구는 반복적인 환경 쿼리 없이 LLM 추론을 위한 확장 가능한 계획 RL 방법의 가능성을 제시합니다.

---

*Generated on 2025-09-22 14:32:16*