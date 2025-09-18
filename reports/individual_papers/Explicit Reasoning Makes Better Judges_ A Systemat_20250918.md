
# Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness

**Korean Title:** 명시적 추론은 더 나은 판사를 만든다: 정확성, 효율성 및 견고성에 대한 체계적 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multilingual setting|Multilingual setting]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/RewardBench tasks|RewardBench tasks]] [[keywords/specific/Few-shot Learning|Few-shot Learning]] [[keywords/unique/Qwen 3 models|Qwen 3 models]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multilingual Setting
**🔬 Broad Technical**: Large Language Models, RewardBench tasks
**🔗 Specific Connectable**: Few-shot Learning
**⭐ Unique Technical**: Qwen 3 models

**ArXiv ID**: [2509.13332](https://arxiv.org/abs/2509.13332)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13332.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`RewardBench tasks` • 

`Few-shot Learning` • 

`Qwen 3 models` • 

`Multilingual Setting`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13332v1 Announce Type: new 
Abstract: As Large Language Models (LLMs) are increasingly adopted as automated judges in benchmarking and reward modeling, ensuring their reliability, efficiency, and robustness has become critical. In this work, we present a systematic comparison of "thinking" and "non-thinking" LLMs in the LLM-as-a-judge paradigm using open-source Qwen 3 models of relatively small sizes (0.6B, 1.7B, and 4B parameters). We evaluate both accuracy and computational efficiency (FLOPs) on RewardBench tasks, and further examine augmentation strategies for non-thinking models, including in-context learning, rubric-guided judging, reference-based evaluation, and n-best aggregation. Our results show that despite these enhancements, non-thinking models generally fall short of their thinking counterparts. Our results show that thinking models achieve approximately 10% points higher accuracy with little overhead (under 2x), in contrast to augmentation strategies like few-shot learning, which deliver modest gains at a higher cost (>8x). Bias and robustness analyses further demonstrate that thinking models maintain significantly greater consistency under a variety of bias conditions such as positional, bandwagon, identity, diversity, and random biases (6% higher on average). We further extend our experiments to the multilingual setting and our results confirm that explicit reasoning extends its benefits beyond English. Overall, our work results in several important findings that provide systematic evidence that explicit reasoning offers clear advantages in the LLM-as-a-judge paradigm not only in accuracy and efficiency but also in robustness.

## 🔍 Abstract (한글 번역)

arXiv:2509.13332v1 발표 유형: 새로운
요약: 대규모 언어 모델 (LLMs)이 벤치마킹 및 보상 모델링에서 자동 심사관으로 채택되면서, 그들의 신뢰성, 효율성 및 견고성을 보장하는 것이 중요해졌습니다. 본 연구에서는 상대적으로 작은 크기의 오픈 소스 Qwen 3 모델 (0.6B, 1.7B 및 4B 매개변수)를 사용하여 LLM-심사관 패러다임에서 "사고" 및 "비사고" LLM을 체계적으로 비교합니다. RewardBench 작업에서 정확도와 계산 효율성 (FLOPs)을 평가하고, 비사고 모델에 대한 증강 전략을 더 자세히 조사합니다. 이러한 증강 전략에는 문맥 내 학습, 루브릭 안내 심사, 참조 기반 평가 및 n-best 집계가 포함됩니다. 결과는 이러한 향상에도 불구하고, 비사고 모델이 일반적으로 사고 모델에 비해 성과가 떨어진다는 것을 보여줍니다. 결과는 사고 모델이 소규모의 추가 부담 없이 (2배 미만) 약 10% 포인트 더 높은 정확도를 달성하는 반면, 소수 학습과 같은 증강 전략은 높은 비용으로 조금씩 성과를 끌어내는 것을 확인합니다. 편향 및 견고성 분석은 또한 사고 모델이 위치, 무리 따름, 정체성, 다양성 및 무작위 편향과 같은 다양한 편향 조건 하에서 상당히 더 큰 일관성을 유지한다는 것을 보여줍니다 (평균 6% 더 높음). 우리는 다국어 환경으로 실험을 확장하고 결과는 명시적 추론이 영어 이상의 이점을 제공한다는 것을 확인합니다. 전반적으로, 우리의 연구는 명시적 추론이 LLM-심사관 패러다임에서 정확성과 효율성뿐만 아니라 견고성에서도 명확한 장점을 제공한다는 체계적인 증거를 제공합니다.

## 📝 요약

이 연구는 대형 언어 모델이 벤치마킹 및 보상 모델링에서 자동 심사관으로 채택됨에 따라 그 신뢰성, 효율성 및 견고성을 보장하는 것이 중요해졌다. 작은 크기의 오픈 소스 Qwen 3 모델(0.6B, 1.7B 및 4B 매개변수)을 사용하여 "사고" 및 "비사고" 대형 언어 모델을 LLM-심사관 패러다임에서 체계적으로 비교한다. RewardBench 작업에서 정확도와 계산 효율성(FLOPs)을 평가하고, 비사고 모델에 대한 증강 전략을 검토한다. 결과는 사고 모델이 비사고 모델보다 약 10% 포인트 높은 정확도를 달성하며 적은 오버헤드로(2배 미만) 유지되는 것을 보여준다. 몇몇 샷 학습과 같은 증강 전략은 높은 비용(8배 이상)에도 미미한 이득을 제공한다. 사고 모델은 다양한 편향 조건에서 더 큰 일관성을 유지한다. 명시적 추론은 영어 이외의 다국어 환경에서도 이점을 제공함을 확인한다. 이 연구는 명시적 추론이 LLM-심사관 패러다임에서 정확성, 효율성 및 견고성 측면에서 명확한 장점을 제공함을 시스템적으로 입증하는 중요한 발견을 제공한다.

## 🎯 주요 포인트


- 1. 대형 언어 모델을 판단자로 사용할 때 명시적 추론이 정확성, 효율성 및 견고성에서 유리함을 입증

- 2. 비판적 사고 모델은 비판적이지 않은 모델보다 약 10% 높은 정확도를 보임

- 3. 명시적 추론은 다양한 편향 조건에서 더 큰 일관성을 유지하며 다국어 설정에서도 효과적으로 작동함.


---

*Generated on 2025-09-18 16:13:13*