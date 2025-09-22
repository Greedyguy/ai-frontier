
# HAM: Hierarchical Adapter Merging for Scalable Continual Learning

**Korean Title:** HAM: 확장 가능한 지속 학습을 위한 계층적 어댑터 병합

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Adapter Grouping

## 🔗 유사한 논문
- [[Superpose_Task-specific_Features_for_Model_Merging_20250919|Superpose Task-specific Features for Model Merging]] (81.9% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (80.8% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (80.6% similar)
- [[FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (80.5% similar)
- [[Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13211v3 Announce Type: replace 
Abstract: Continual learning is an essential capability of human cognition, yet it poses significant challenges for current deep learning models. The primary issue is that new knowledge can interfere with previously learned information, causing the model to forget earlier knowledge in favor of the new, a phenomenon known as catastrophic forgetting. Although large pre-trained models can partially mitigate forgetting by leveraging their existing knowledge and over-parameterization, they often struggle when confronted with novel data distributions. Parameter-Efficient Fine-Tuning (PEFT) methods, such as LoRA, enable efficient adaptation to new knowledge. However, they still face challenges in scaling to dynamic learning scenarios and long sequences of tasks, as maintaining one adapter per task introduces complexity and increases the potential for interference. In this paper, we introduce Hierarchical Adapters Merging (HAM), a novel framework that dynamically combines adapters from different tasks during training. This approach enables HAM to scale effectively, allowing it to manage more tasks than competing baselines with improved efficiency. To achieve this, HAM maintains a fixed set of groups that hierarchically consolidate new adapters. For each task, HAM trains a low-rank adapter along with an importance scalar, then dynamically groups tasks based on adapter similarity. Within each group, adapters are pruned, scaled and merge, facilitating transfer learning between related tasks. Extensive experiments on three vision benchmarks show that HAM significantly outperforms state-of-the-art methods, particularly as the number of tasks increases.

## 🔍 Abstract (한글 번역)

arXiv:2509.13211v3 발표 유형: 교체  
초록: 지속적 학습은 인간 인지의 필수적인 능력이지만, 현재의 심층 학습 모델에는 상당한 도전 과제를 제시합니다. 주요 문제는 새로운 지식이 이전에 학습한 정보를 방해하여, 모델이 새로운 지식을 선호하면서 이전 지식을 잊어버리는 현상인 치명적 망각(catatastrophic forgetting)을 초래할 수 있다는 점입니다. 대규모 사전 학습된 모델은 기존 지식과 과매개변수를 활용하여 망각을 부분적으로 완화할 수 있지만, 새로운 데이터 분포에 직면했을 때 종종 어려움을 겪습니다. LoRA와 같은 파라미터 효율적 미세 조정(PEFT) 방법은 새로운 지식에 대한 효율적인 적응을 가능하게 합니다. 그러나 이러한 방법은 동적 학습 시나리오와 긴 작업 시퀀스에 확장하는 데 여전히 어려움을 겪습니다. 작업당 하나의 어댑터를 유지하는 것은 복잡성을 증가시키고 간섭의 가능성을 높이기 때문입니다. 본 논문에서는 훈련 중에 다양한 작업의 어댑터를 동적으로 결합하는 새로운 프레임워크인 계층적 어댑터 병합(HAM)을 소개합니다. 이 접근 방식은 HAM이 경쟁 기법보다 더 많은 작업을 효율적으로 관리할 수 있도록 확장성을 제공합니다. 이를 위해 HAM은 새로운 어댑터를 계층적으로 통합하는 고정된 그룹 세트를 유지합니다. 각 작업에 대해 HAM은 저랭크 어댑터와 중요도 스칼라를 훈련한 후, 어댑터 유사성에 기반하여 작업을 동적으로 그룹화합니다. 각 그룹 내에서 어댑터는 가지치기, 스케일링 및 병합되어 관련 작업 간의 전이 학습을 촉진합니다. 세 가지 비전 벤치마크에 대한 광범위한 실험 결과, HAM은 특히 작업 수가 증가할수록 최첨단 방법을 크게 능가하는 것으로 나타났습니다.

## 📝 요약

이 논문은 인간 인지의 중요한 능력인 지속적 학습을 다루며, 기존 딥러닝 모델이 직면한 문제인 '파국적 망각'을 해결하기 위한 새로운 방법론을 제안합니다. 대규모 사전 학습 모델은 기존 지식을 활용하여 망각을 부분적으로 완화할 수 있지만, 새로운 데이터 분포에 적응하는 데 어려움을 겪습니다. 이를 해결하기 위해, 논문은 새로운 지식에 효율적으로 적응할 수 있는 계층적 어댑터 병합(HAM) 프레임워크를 소개합니다. HAM은 다양한 작업의 어댑터를 동적으로 결합하여 효율성을 높이고, 작업 간 전이 학습을 촉진합니다. 실험 결과, HAM은 특히 작업 수가 증가할수록 기존 최첨단 방법들보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 지속적 학습은 인간 인지의 필수 능력이지만, 현재의 딥러닝 모델에서는 새로운 지식이 이전에 학습한 정보를 방해하는 '파국적 망각' 현상이 발생한다.

- 2. 대규모 사전 학습 모델은 기존 지식과 과매개변수를 활용하여 망각을 부분적으로 완화할 수 있지만, 새로운 데이터 분포에 직면했을 때는 여전히 어려움을 겪는다.

- 3. LoRA와 같은 파라미터 효율적 미세 조정(PEFT) 방법은 새로운 지식에 대한 효율적 적응을 가능하게 하지만, 동적 학습 시나리오와 긴 작업 시퀀스에 확장하는 데 어려움이 있다.

- 4. 본 논문에서는 다양한 작업의 어댑터를 동적으로 결합하는 새로운 프레임워크인 HAM(Hierarchical Adapters Merging)을 소개하며, 이는 더 많은 작업을 효율적으로 관리할 수 있게 한다.

- 5. HAM은 세 가지 비전 벤치마크 실험에서 작업 수가 증가할수록 최첨단 방법보다 성능이 뛰어난 것으로 나타났다.

---

*Generated on 2025-09-19 15:41:26*