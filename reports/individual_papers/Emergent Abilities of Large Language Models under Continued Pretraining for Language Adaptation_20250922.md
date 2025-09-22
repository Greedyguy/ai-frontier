# Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation

**Korean Title:** 대규모 언어 모델의 언어 적응을 위한 지속적인 사전 훈련 하에서의 발현 능력

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Curriculum Learning

## 🔗 유사한 논문
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony On Multilingual Data Allocation for Large Language Models Pretraining]] (84.1% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (82.9% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (82.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.2% similar)
- [[2025-09-17/Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning_20250917|Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning]] (82.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00288v3 Announce Type: replace-cross 
Abstract: Continued pretraining (CPT) is a popular approach to adapt existing large language models (LLMs) to new languages. When doing so, it is common practice to include a portion of English data in the mixture, but its role has not been carefully studied to date. In this work, we show that including English does not impact validation perplexity, yet it is critical for the emergence of downstream capabilities in the target language. We introduce a language-agnostic benchmark for in-context learning (ICL), which reveals catastrophic forgetting early on CPT when English is not included. This in turn damages the ability of the model to generalize to downstream prompts in the target language as measured by perplexity, even if it does not manifest in terms of accuracy until later in training, and can be tied to a big shift in the model parameters. Based on these insights, we introduce curriculum learning and exponential moving average (EMA) of weights as effective alternatives to mitigate the need for English. All in all, our work sheds light into the dynamics by which emergent abilities arise when doing CPT for language adaptation, and can serve as a foundation to design more effective methods in the future.

## 🔍 Abstract (한글 번역)

arXiv:2506.00288v3 발표 유형: 교차 대체  
초록: 지속적 사전 학습(CPT)은 기존의 대형 언어 모델(LLM)을 새로운 언어에 적응시키기 위한 인기 있는 접근 방식입니다. 이를 수행할 때, 영어 데이터를 혼합물에 포함하는 것이 일반적인 관행이지만, 그 역할은 지금까지 신중하게 연구되지 않았습니다. 이 연구에서는 영어를 포함하는 것이 검증 퍼플렉시티에 영향을 미치지 않지만, 목표 언어에서의 다운스트림 기능의 출현에 필수적임을 보여줍니다. 우리는 맥락 내 학습(ICL)을 위한 언어 비의존적 벤치마크를 도입하며, 영어가 포함되지 않을 때 CPT 초기에 발생하는 치명적인 망각을 드러냅니다. 이는 목표 언어의 다운스트림 프롬프트에 대한 모델의 일반화 능력을 손상시키며, 이는 훈련 후반까지 정확도 측면에서 나타나지 않더라도 퍼플렉시티로 측정됩니다. 이는 모델 매개변수의 큰 변화와 관련이 있습니다. 이러한 통찰을 바탕으로, 우리는 영어의 필요성을 줄이기 위한 효과적인 대안으로 커리큘럼 학습과 가중치의 지수 이동 평균(EMA)을 도입합니다. 종합적으로, 우리의 연구는 언어 적응을 위한 CPT를 수행할 때 출현 능력이 발생하는 역학에 대한 통찰을 제공하며, 미래에 더 효과적인 방법을 설계하는 기초가 될 수 있습니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 새로운 언어에 적응시키기 위한 지속적 사전 학습(CPT)에서 영어 데이터를 포함하는 것의 중요성을 분석합니다. 연구 결과, 영어 데이터는 검증 퍼플렉시티에는 영향을 미치지 않지만, 목표 언어에서의 다운스트림 능력 발현에 필수적임을 발견했습니다. 영어를 포함하지 않으면 초기 CPT 단계에서 망각이 발생하여 모델의 일반화 능력이 손상됩니다. 이를 해결하기 위해 커리큘럼 학습과 지수 이동 평균(EMA) 기법을 제안합니다. 이 연구는 언어 적응을 위한 CPT 과정에서 발생하는 능력 발현의 역학을 이해하는 데 기여하며, 향후 효과적인 방법 설계의 기초가 될 수 있습니다.

## 🎯 주요 포인트

- 1. 기존 대형 언어 모델을 새로운 언어에 적응시키기 위한 CPT에서 영어 데이터의 포함 여부가 검증 퍼플렉시티에는 영향을 미치지 않지만, 목표 언어에서의 다운스트림 능력 발현에는 중요하다.

- 2. 영어를 포함하지 않을 경우, CPT 초기에 망각 현상이 발생하여 목표 언어의 다운스트림 프롬프트에 대한 일반화 능력이 손상된다.

- 3. 커리큘럼 학습과 가중치의 지수 이동 평균(EMA)을 통해 영어의 필요성을 줄이는 효과적인 대안을 제시한다.

- 4. 본 연구는 언어 적응을 위한 CPT 수행 시 발현 능력이 나타나는 동적 과정을 밝히고, 향후 더 효과적인 방법을 설계하는 기초를 제공한다.

---

*Generated on 2025-09-22 14:53:03*