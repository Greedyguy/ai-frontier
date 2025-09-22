# reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs

**Korean Title:** reWordBench: 변환된 입력을 통해 보상 모델의 견고성을 벤치마킹하고 개선하기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Robust Reward Models|Robust Reward Models]] [[keywords/specific/Input Transformation|Input Transformation]] [[keywords/broad/Natural Language Processing|Natural Language Processing]] [[keywords/unique/reWordBench|reWordBench]] [[categories/cs.CL|cs.CL]] [[2025-09-22/MT-RewardTree_ A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling_20250922|MT-RewardTree: A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling]] (85.7% similar) [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (84.0% similar) [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robust Reward Models
**🔗 Specific Connectable**: Input Transformation
**🔬 Broad Technical**: Natural Language Processing
**⭐ Unique Technical**: reWordBench
## 🔗 유사한 논문
- [[2025-09-22/MT-RewardTree_ A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling_20250922|MT-RewardTree A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling]] (85.7% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (84.0% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (83.9% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (83.2% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (82.5% similar)


**ArXiv ID**: [2503.11751](https://arxiv.org/abs/2503.11751)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2503.11751.pdf)


**ArXiv ID**: [2503.11751](https://arxiv.org/abs/2503.11751)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2503.11751.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robust Reward Models
**🔗 Specific Connectable**: Input Transformation
**⭐ Unique Technical**: reWordBench
**🔬 Broad Technical**: Natural Language Processing

## 🏷️ 추출된 키워드



`Natural Language Processing` • 

`Input Transformation` • 

`reWordBench` • 

`Robust Reward Models`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.11751v2 Announce Type: replace 
Abstract: Reward models have become a staple in modern NLP, serving as not only a scalable text evaluator, but also an indispensable component in many alignment recipes and inference-time algorithms. However, while recent reward models increase performance on standard benchmarks, this may partly be due to overfitting effects, which would confound an understanding of their true capability. In this work, we scrutinize the robustness of reward models and the extent of such overfitting. We build **reWordBench**, which systematically transforms reward model inputs in meaning- or ranking-preserving ways. We show that state-of-the-art reward models suffer from substantial performance degradation even with minor input transformations, sometimes dropping to significantly below-random accuracy, suggesting brittleness. To improve reward model robustness, we propose to explicitly train them to assign similar scores to paraphrases, and find that this approach also improves robustness to other distinct kinds of transformations. For example, our robust reward model reduces such degradation by roughly half for the Chat Hard subset in RewardBench. Furthermore, when used in alignment, our robust reward models demonstrate better utility and lead to higher-quality outputs, winning in up to 59% of instances against a standardly trained RM.

## 🔍 Abstract (한글 번역)

arXiv:2503.11751v2 발표 유형: 교체  
초록: 보상 모델은 현대 자연어 처리(NLP)에서 중요한 요소로 자리 잡았으며, 확장 가능한 텍스트 평가 도구일 뿐만 아니라 많은 정렬 기법 및 추론 알고리즘의 필수 구성 요소로 사용됩니다. 그러나 최근의 보상 모델이 표준 벤치마크에서 성능을 향상시키는 것은 부분적으로 과적합 효과 때문일 수 있으며, 이는 이 모델의 진정한 능력을 이해하는 데 혼란을 줄 수 있습니다. 본 연구에서는 보상 모델의 견고성과 이러한 과적합의 정도를 면밀히 조사합니다. 우리는 보상 모델 입력을 의미 또는 순위를 보존하는 방식으로 체계적으로 변환하는 **reWordBench**를 구축했습니다. 최첨단 보상 모델은 사소한 입력 변환에도 상당한 성능 저하를 겪으며, 때로는 무작위 정확도보다 훨씬 낮은 수준으로 떨어지기도 하여 취약성을 시사합니다. 보상 모델의 견고성을 향상시키기 위해, 우리는 패러프레이즈에 유사한 점수를 할당하도록 명시적으로 훈련시키는 방법을 제안하며, 이 접근법이 다른 종류의 변환에 대한 견고성도 향상시킨다는 것을 발견했습니다. 예를 들어, 우리의 견고한 보상 모델은 RewardBench의 Chat Hard 하위 집합에서 이러한 성능 저하를 약 절반으로 줄였습니다. 더욱이, 정렬에 사용될 때, 우리의 견고한 보상 모델은 더 나은 유용성을 보여주며, 표준적으로 훈련된 보상 모델에 비해 최대 59%의 사례에서 더 높은 품질의 출력을 생성합니다.

## 📝 요약

이 논문에서는 보상 모델의 견고성과 과적합 문제를 분석합니다. 이를 위해 입력을 의미나 순위를 유지하면서 변형하는 **reWordBench**를 개발했습니다. 연구 결과, 최신 보상 모델은 입력 변형에 취약하여 성능이 크게 저하될 수 있음을 발견했습니다. 이를 개선하기 위해 패러프레이즈에 유사한 점수를 부여하도록 모델을 훈련시켰으며, 이 방법이 다양한 변형에 대한 견고성을 향상시켰습니다. 특히, Chat Hard 데이터셋에서 성능 저하를 절반으로 줄였고, 정렬 작업에서도 더 나은 결과를 보였습니다.

## 🎯 주요 포인트


- 1. 최신 보상 모델은 표준 벤치마크에서 성능을 향상시키지만, 이는 부분적으로 과적합 효과 때문일 수 있습니다.

- 2. **reWordBench**를 구축하여 보상 모델 입력을 의미나 순위를 유지하면서 체계적으로 변형하고, 보상 모델의 취약성을 분석합니다.

- 3. 최신 보상 모델은 입력의 사소한 변형에도 성능 저하를 겪으며, 때로는 무작위 정확도보다 낮은 결과를 보입니다.

- 4. 보상 모델의 강건성을 향상시키기 위해 유사한 문장에 유사한 점수를 할당하도록 명시적으로 훈련시키는 방법을 제안합니다.

- 5. 강건한 보상 모델은 정렬 시 더 나은 효용성을 보이며, 최대 59%의 경우에서 표준 훈련된 모델보다 높은 품질의 출력을 생성합니다.


---

*Generated on 2025-09-22 16:36:05*