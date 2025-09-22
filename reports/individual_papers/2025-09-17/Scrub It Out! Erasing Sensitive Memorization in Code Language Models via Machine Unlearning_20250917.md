# Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning

**Korean Title:** 민감한 암기를 제거하라! 기계적 비학습을 통한 코드 언어 모델에서의 민감한 암기 삭제

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Zhaoyang Chu|Zhaoyang Chu]] [[authors/Yao Wan|Yao Wan]] [[authors/Zhikun Zhang|Zhikun Zhang]] [[authors/Di Wang|Di Wang]] [[authors/Zhou Yang|Zhou Yang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Sensitive Memorization Erasure

## 🔗 유사한 논문
- [[Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (84.8% similar)
- [[CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (84.0% similar)
- [[LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (82.7% similar)
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (80.6% similar)
- [[Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems_20250919|Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems]] (79.6% similar)

## 📋 저자 정보

**Authors:** Zhaoyang Chu, Yao Wan, Zhikun Zhang, Di Wang, Zhou Yang, Hongyu Zhang, Pan Zhou, Xuanhua Shi, Hai Jin, David Lo

## 📄 Abstract (원문)

While Code Language Models (CLMs) have demonstrated superior performance in
software engineering tasks such as code generation and summarization, recent
empirical studies reveal a critical privacy vulnerability: these models exhibit
unintended memorization of sensitive training data, enabling verbatim
reproduction of confidential information when specifically prompted. To address
this issue, several approaches, including training data de-duplication and
differential privacy augmentation, have been proposed. However, these methods
require full-model retraining for deployed CLMs, which incurs substantial
computational costs. In this paper, we aim to answer the following research
question: Can sensitive information memorized by CLMs be erased effectively and
efficiently?
  We conduct a pioneering investigation into erasing sensitive memorization in
CLMs through machine unlearning - a post-hoc modification method that removes
specific information from trained models without requiring full retraining.
Specifically, we first quantify the memorization risks of sensitive data within
CLM training datasets and curate a high-risk dataset of 50,000 sensitive
memorized samples as unlearning targets. We study two widely used gradient
ascent-based unlearning approaches: the vanilla and constraint-based methods,
and introduce CodeEraser, an advanced variant that selectively unlearns
sensitive memorized segments in code while preserving the structural integrity
and functional correctness of the surrounding code. Extensive experiments on
three families of CLMs, i.e., CodeParrot, CodeGen-Mono, and Qwen2.5-Coder,
validate the effectiveness and efficiency of CodeEraser in erasing targeted
sensitive memorization while maintaining model utility.

## 🔍 Abstract (한글 번역)

코드 언어 모델(CLM)은 코드 생성 및 요약과 같은 소프트웨어 공학 작업에서 우수한 성능을 보여주었지만, 최근의 실증 연구들은 중요한 개인정보 취약성을 드러냈습니다. 이러한 모델은 민감한 훈련 데이터를 의도치 않게 암기하여 특정한 요청 시 기밀 정보를 문자 그대로 재현할 수 있습니다. 이 문제를 해결하기 위해 훈련 데이터 중복 제거 및 차등 개인정보 보호 강화와 같은 여러 접근법이 제안되었습니다. 그러나 이러한 방법들은 배포된 CLM에 대해 전체 모델 재훈련을 필요로 하며, 이는 상당한 계산 비용을 초래합니다. 본 논문에서는 다음의 연구 질문에 답하고자 합니다: CLM이 암기한 민감한 정보를 효과적이고 효율적으로 제거할 수 있는가? 우리는 기계 학습 제거를 통해 CLM의 민감한 암기를 제거하는 선구적인 연구를 수행합니다. 이는 훈련된 모델에서 특정 정보를 제거하는 사후 수정 방법으로, 전체 재훈련을 요구하지 않습니다. 구체적으로, 우리는 CLM 훈련 데이터셋 내 민감한 데이터의 암기 위험을 정량화하고, 학습 제거 대상으로 50,000개의 민감한 암기 샘플로 구성된 고위험 데이터셋을 큐레이션합니다. 우리는 두 가지 널리 사용되는 그래디언트 상승 기반 학습 제거 접근법인 기본 방법과 제약 기반 방법을 연구하고, 주변 코드의 구조적 무결성과 기능적 정확성을 유지하면서 코드 내 민감한 암기 세그먼트를 선택적으로 제거하는 고급 변형인 CodeEraser를 소개합니다. CodeParrot, CodeGen-Mono, Qwen2.5-Coder라는 세 가지 CLM 계열에 대한 광범위한 실험을 통해 CodeEraser가 모델의 유용성을 유지하면서 목표로 한 민감한 암기를 제거하는 데 있어 효과적이고 효율적임을 검증합니다.

## 📝 요약

이 논문은 코드 언어 모델(CLM)이 민감한 훈련 데이터를 의도치 않게 기억하여 기밀 정보를 재생산할 수 있는 프라이버시 취약성을 지적합니다. 이를 해결하기 위해, 전체 모델 재훈련 없이 특정 정보를 제거하는 사후 수정 방법인 머신 언러닝을 활용하여 민감한 정보의 기억을 지우는 방법을 연구했습니다. 연구에서는 50,000개의 민감한 데이터를 대상으로 두 가지 그라디언트 상승 기반 언러닝 방법과 CodeEraser라는 고급 변형 기법을 제안했습니다. CodeEraser는 코드의 구조적 무결성과 기능적 정확성을 유지하면서 민감한 기억 부분만 선택적으로 제거합니다. 실험 결과, CodeEraser는 모델의 유용성을 유지하면서도 민감한 기억을 효과적이고 효율적으로 지울 수 있음을 검증했습니다.

## 🎯 주요 포인트

- 1. 코드 언어 모델(CLMs)은 민감한 훈련 데이터를 의도치 않게 기억하여 특정 프롬프트에 따라 기밀 정보를 그대로 재생산할 수 있는 프라이버시 취약점을 가지고 있다.

- 2. 민감한 정보의 기억을 효과적이고 효율적으로 지울 수 있는지를 연구하기 위해 기계 학습 후 특정 정보를 제거하는 방법인 '기계 언러닝'을 조사하였다.

- 3. CodeEraser는 코드의 구조적 완전성과 기능적 정확성을 유지하면서 민감한 기억 세그먼트를 선택적으로 제거하는 고급 기법이다.

- 4. CodeEraser는 CodeParrot, CodeGen-Mono, Qwen2.5-Coder 등 세 가지 CLM 계열에서 광범위한 실험을 통해 목표로 한 민감한 기억을 지우면서도 모델의 유용성을 유지하는 데 효과적이고 효율적임을 입증하였다.

---

*Generated on 2025-09-20 09:36:00*