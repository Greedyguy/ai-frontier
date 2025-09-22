# On Optimal Steering to Achieve Exact Fairness

**Korean Title:** 정확한 공정성을 달성하기 위한 최적 조정에 관하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Group-fair Outcomes

## 🔗 유사한 논문
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (83.7% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (83.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.1% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.2% similar)
- [[2025-09-19/Optimal Learning from Label Proportions with General Loss Functions_20250919|Optimal Learning from Label Proportions with General Loss Functions]] (82.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15759v1 Announce Type: cross 
Abstract: To fix the 'bias in, bias out' problem in fair machine learning, it is important to steer feature distributions of data or internal representations of Large Language Models (LLMs) to ideal ones that guarantee group-fair outcomes. Previous work on fair generative models and representation steering could greatly benefit from provable fairness guarantees on the model output. We define a distribution as ideal if the minimizer of any cost-sensitive risk on it is guaranteed to have exact group-fair outcomes (e.g., demographic parity, equal opportunity)-in other words, it has no fairness-utility trade-off. We formulate an optimization program for optimal steering by finding the nearest ideal distribution in KL-divergence, and provide efficient algorithms for it when the underlying distributions come from well-known parametric families (e.g., normal, log-normal). Empirically, our optimal steering techniques on both synthetic and real-world datasets improve fairness without diminishing utility (and sometimes even improve utility). We demonstrate affine steering of LLM representations to reduce bias in multi-class classification, e.g., occupation prediction from a short biography in Bios dataset (De-Arteaga et al.). Furthermore, we steer internal representations of LLMs towards desired outputs so that it works equally well across different groups.

## 🔍 Abstract (한글 번역)

arXiv:2509.15759v1 발표 유형: 교차  
초록: 공정한 기계 학습에서 '편향 입력, 편향 출력' 문제를 해결하기 위해, 데이터의 특징 분포나 대형 언어 모델(LLMs)의 내부 표현을 그룹 공정한 결과를 보장하는 이상적인 분포로 조정하는 것이 중요합니다. 공정 생성 모델과 표현 조정에 대한 이전 연구는 모델 출력에 대한 증명 가능한 공정성 보장으로부터 크게 이익을 얻을 수 있습니다. 우리는 어떤 비용 민감한 위험의 최소화자가 정확한 그룹 공정한 결과(예: 인구 통계적 평등, 기회 평등)를 보장하는 경우 그 분포를 이상적이라고 정의합니다. 즉, 공정성과 유용성 간의 트레이드오프가 없습니다. 우리는 KL-발산에서 가장 가까운 이상적 분포를 찾아 최적 조정을 위한 최적화 프로그램을 수립하고, 기본 분포가 잘 알려진 파라메트릭 계열(예: 정규 분포, 로그 정규 분포)에서 나올 때 이를 위한 효율적인 알고리즘을 제공합니다. 실험적으로, 우리의 최적 조정 기법은 합성 및 실제 데이터 세트에서 유용성을 감소시키지 않으면서 공정성을 개선하며, 때로는 유용성을 향상시키기도 합니다. 우리는 LLM 표현의 아핀 조정을 통해 다중 클래스 분류에서의 편향을 줄이는 것을 입증하며, 예를 들어 Bios 데이터셋(De-Arteaga et al.)에서 짧은 전기에서 직업 예측을 수행합니다. 또한, LLM의 내부 표현을 원하는 출력으로 조정하여 다양한 그룹에 걸쳐 동일하게 잘 작동하도록 합니다.

## 📝 요약

이 논문은 공정한 머신러닝에서 '편향된 입력, 편향된 출력' 문제를 해결하기 위해 데이터의 특징 분포나 대형 언어 모델(LLM)의 내부 표현을 이상적인 분포로 조정하는 방법을 제안합니다. 이상적인 분포는 비용 민감 위험의 최소화가 정확한 그룹 공정성을 보장하는 분포로 정의됩니다. 저자들은 KL-발산을 사용하여 최적의 이상적 분포를 찾는 최적화 프로그램을 제시하고, 이를 위한 효율적인 알고리즘을 개발했습니다. 실험 결과, 이 방법은 합성 및 실제 데이터셋에서 공정성을 개선하면서도 유용성을 유지하거나 향상시켰습니다. 특히, LLM의 표현을 조정하여 직업 예측 등에서 편향을 줄이는 데 성공했습니다.

## 🎯 주요 포인트

- 1. 공정한 기계 학습에서 '편향된 입력, 편향된 출력' 문제를 해결하기 위해 데이터의 특징 분포나 대형 언어 모델(LLM)의 내부 표현을 그룹 공정한 결과를 보장하는 이상적인 분포로 조정하는 것이 중요합니다.

- 2. 이상적인 분포는 비용 민감 위험의 최소화가 정확한 그룹 공정 결과를 보장하는 분포로 정의되며, 이는 공정성과 유용성 간의 트레이드오프가 없음을 의미합니다.

- 3. KL-발산에서 가장 가까운 이상적인 분포를 찾는 최적화 프로그램을 공식화하고, 잘 알려진 매개변수적 분포(예: 정규, 로그 정규)에서 효율적인 알고리즘을 제공합니다.

- 4. 합성 및 실제 데이터셋에서 최적의 조정 기술을 통해 공정성을 개선하면서도 유용성을 저해하지 않으며, 때로는 유용성을 향상시키기도 합니다.

- 5. 대형 언어 모델의 내부 표현을 원하는 출력으로 조정하여 다양한 그룹에서 동일하게 잘 작동하도록 합니다.

---

*Generated on 2025-09-22 14:10:09*