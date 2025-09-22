
# Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM

**Korean Title:** 디커플드 프록시 정렬: MLLM에서 다중 모달 정렬을 위한 언어 선행 충돌 완화

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Language Prior Conflict Mitigation

## 🔗 유사한 논문
- [[Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (87.6% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.9% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (86.9% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (85.5% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (84.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14735v1 Announce Type: new 
Abstract: Multimodal large language models (MLLMs) have gained significant attention due to their impressive ability to integrate vision and language modalities. Recent advancements in MLLMs have primarily focused on improving performance through high-quality datasets, novel architectures, and optimized training strategies. However, in this paper, we identify a previously overlooked issue, language prior conflict, a mismatch between the inherent language priors of large language models (LLMs) and the language priors in training datasets. This conflict leads to suboptimal vision-language alignment, as MLLMs are prone to adapting to the language style of training samples. To address this issue, we propose a novel training method called Decoupled Proxy Alignment (DPA). DPA introduces two key innovations: (1) the use of a proxy LLM during pretraining to decouple the vision-language alignment process from language prior interference, and (2) dynamic loss adjustment based on visual relevance to strengthen optimization signals for visually relevant tokens. Extensive experiments demonstrate that DPA significantly mitigates the language prior conflict, achieving superior alignment performance across diverse datasets, model families, and scales. Our method not only improves the effectiveness of MLLM training but also shows exceptional generalization capabilities, making it a robust approach for vision-language alignment. Our code is available at https://github.com/fnlp-vision/DPA.

## 🔍 Abstract (한글 번역)

arXiv:2509.14735v1 발표 유형: 신규  
초록: 다중 모달 대형 언어 모델(Multimodal Large Language Models, MLLMs)은 시각과 언어 모달리티를 통합하는 뛰어난 능력으로 인해 큰 주목을 받고 있습니다. 최근 MLLMs의 발전은 주로 고품질 데이터셋, 새로운 아키텍처, 최적화된 학습 전략을 통해 성능을 향상시키는 데 초점을 맞추고 있습니다. 그러나 본 논문에서는 이전에 간과된 문제인 언어 선험 충돌(language prior conflict)을 식별합니다. 이는 대형 언어 모델(LLMs)의 고유한 언어 선험과 학습 데이터셋의 언어 선험 사이의 불일치로, MLLMs이 학습 샘플의 언어 스타일에 적응하기 쉬워 최적이 아닌 시각-언어 정렬을 초래합니다. 이 문제를 해결하기 위해 우리는 Decoupled Proxy Alignment (DPA)라는 새로운 학습 방법을 제안합니다. DPA는 두 가지 주요 혁신을 도입합니다: (1) 프록시 LLM을 사전 학습 동안 사용하여 시각-언어 정렬 과정을 언어 선험 간섭으로부터 분리하고, (2) 시각적 관련성에 기반한 동적 손실 조정을 통해 시각적으로 관련된 토큰에 대한 최적화 신호를 강화합니다. 광범위한 실험을 통해 DPA가 언어 선험 충돌을 크게 완화하여 다양한 데이터셋, 모델 계열, 규모에 걸쳐 우수한 정렬 성능을 달성함을 입증합니다. 우리의 방법은 MLLM 학습의 효과를 향상시킬 뿐만 아니라 뛰어난 일반화 능력을 보여주어 시각-언어 정렬을 위한 강력한 접근법이 됩니다. 우리의 코드는 https://github.com/fnlp-vision/DPA에서 이용할 수 있습니다.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MLLM)의 언어 선행 충돌 문제를 다룹니다. 기존 연구는 고품질 데이터셋과 새로운 아키텍처에 집중했지만, 이 논문은 대형 언어 모델(LLM)의 언어 선행과 훈련 데이터셋의 언어 선행 간 불일치가 시각-언어 정렬을 저해한다고 지적합니다. 이를 해결하기 위해 저자들은 '분리 프록시 정렬(DPA)'이라는 새로운 훈련 방법을 제안합니다. DPA는 프록시 LLM을 사용해 시각-언어 정렬을 언어 선행 간섭에서 분리하고, 시각적 관련성에 기반한 동적 손실 조정을 통해 최적화 신호를 강화합니다. 실험 결과, DPA는 언어 선행 충돌을 효과적으로 완화하며, 다양한 데이터셋과 모델에서 우수한 정렬 성능과 일반화 능력을 보여줍니다.

## 🎯 주요 포인트

- 1. 멀티모달 대형 언어 모델(MLLMs)은 시각과 언어 모달리티를 통합하는 능력으로 주목받고 있습니다.

- 2. 기존 연구는 고품질 데이터셋, 새로운 아키텍처, 최적화된 훈련 전략을 통해 성능 향상에 주력해왔습니다.

- 3. 본 논문에서는 대형 언어 모델(LLMs)의 고유 언어 선험과 훈련 데이터셋의 언어 선험 간의 불일치인 언어 선험 충돌 문제를 식별했습니다.

- 4. 이를 해결하기 위해 Decoupled Proxy Alignment (DPA)라는 새로운 훈련 방법을 제안하였으며, 이는 시각적 관련성에 기반한 동적 손실 조정을 포함합니다.

- 5. DPA는 다양한 데이터셋, 모델 계열 및 규모에서 우수한 정렬 성능을 달성하며, MLLM 훈련의 효과성을 향상시키고 뛰어난 일반화 능력을 보여줍니다.

---

*Generated on 2025-09-19 15:51:16*