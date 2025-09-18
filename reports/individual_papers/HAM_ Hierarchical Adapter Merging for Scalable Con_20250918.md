
# HAM: Hierarchical Adapter Merging for Scalable Continual Learning

**Korean Title:** HAM: 확장 가능한 지속적 학습을 위한 계층적 어댑터 병합

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Dynamic Learning Scenarios|Dynamic Learning Scenarios]] [[keywords/broad/Continual Learning|Continual Learning]] [[keywords/broad/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]] [[keywords/specific/Hierarchical Adapters Merging|Hierarchical Adapters Merging]] [[keywords/unique/HAM|HAM]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Learning Scenarios
**🔬 Broad Technical**: Continual Learning, Parameter-Efficient Fine-Tuning
**🔗 Specific Connectable**: Hierarchical Adapters Merging
**⭐ Unique Technical**: HAM

**ArXiv ID**: [2509.13211](https://arxiv.org/abs/2509.13211)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13211.pdf)


## 🏷️ 추출된 키워드



`Continual Learning` • 

`Parameter-Efficient Fine-Tuning` • 

`Hierarchical Adapters Merging` • 

`HAM` • 

`Dynamic Learning Scenarios`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13211v2 Announce Type: replace 
Abstract: Continual learning is an essential capability of human cognition, yet it poses significant challenges for current deep learning models. The primary issue is that new knowledge can interfere with previously learned information, causing the model to forget earlier knowledge in favor of the new, a phenomenon known as catastrophic forgetting. Although large pre-trained models can partially mitigate forgetting by leveraging their existing knowledge and over-parameterization, they often struggle when confronted with novel data distributions. Parameter-Efficient Fine-Tuning (PEFT) methods, such as LoRA, enable efficient adaptation to new knowledge. However, they still face challenges in scaling to dynamic learning scenarios and long sequences of tasks, as maintaining one adapter per task introduces complexity and increases the potential for interference. In this paper, we introduce Hierarchical Adapters Merging (HAM), a novel framework that dynamically combines adapters from different tasks during training. This approach enables HAM to scale effectively, allowing it to manage more tasks than competing baselines with improved efficiency. To achieve this, HAM maintains a fixed set of groups that hierarchically consolidate new adapters. For each task, HAM trains a low-rank adapter along with an importance scalar, then dynamically groups tasks based on adapter similarity. Within each group, adapters are pruned, scaled and merge, facilitating transfer learning between related tasks. Extensive experiments on three vision benchmarks show that HAM significantly outperforms state-of-the-art methods, particularly as the number of tasks increases.

## 🔍 Abstract (한글 번역)

arXiv:2509.13211v2 발표 유형: 대체
요약: 지속적 학습은 인간 인지의 필수 능력이지만, 현재의 딥 러닝 모델에는 중요한 도전 과제를 제기합니다. 주요 문제는 새로운 지식이 이전에 학습한 정보와 간섭하여 모델이 새로운 지식을 선호하는 동안 이전 지식을 잊어버리는 현상인 재앙적인 잊혀짐(catastrophic forgetting)입니다. 대규모 사전 훈련된 모델은 기존 지식과 과적합을 활용하여 잊혀짐을 일부 완화할 수 있지만, 새로운 데이터 분포에 직면할 때 종종 어려움을 겪습니다. 매개변수 효율적 세밀 조정(Parameter-Efficient Fine-Tuning, PEFT) 방법인 LoRA와 같은 방법들은 새로운 지식에 효율적으로 적응할 수 있게 합니다. 그러나, 동적 학습 시나리오와 장기간의 작업 시퀀스로 확장하는 데 여전히 어려움을 겪으며, 각 작업 당 하나의 어댑터를 유지함으로써 복잡성을 도입하고 간섭 가능성을 증가시키는 문제가 있습니다. 본 논문에서는 HAM(Hierarchical Adapters Merging)이라는 새로운 프레임워크를 소개합니다. 이 접근 방식은 훈련 중에 서로 다른 작업에서 어댑터를 동적으로 결합함으로써 HAM이 효과적으로 확장되어 경쟁하는 기준선보다 더 많은 작업을 관리할 수 있도록 합니다. 이를 위해 HAM은 새로운 어댑터를 계층적으로 통합하는 고정된 그룹 세트를 유지합니다. 각 작업에 대해 HAM은 중요도 스칼라와 함께 저랭크 어댑터를 훈련하고, 그런 다음 어댑터 유사성에 기초하여 작업을 동적으로 그룹화합니다. 각 그룹 내에서 어댑터는 가지치기되고, 스케일링되며 병합되어 관련 작업 간의 전이 학습을 용이하게 합니다. 세 가지 시각 벤치마크에서 수행된 포괄적 실험은 HAM이 최첨단 방법을 크게 능가함을 보여주며, 특히 작업 수가 증가함에 따라 더욱 뛰어난 성능을 보입니다.

## 📝 요약

이 논문은 지속적 학습(continual learning)이 현재 심층학습 모델에 중요한 도전 과제를 제공하는데, 특히 새로운 지식이 이전에 학습한 정보와 간섭하여 이전 지식을 잊게 만드는 치명적인 잊혀짐(catastrophic forgetting) 현상에 대해 다룬다. 본 논문에서는 Parameter-Efficient Fine-Tuning (PEFT) 방법론 중 하나인 LoRA를 기반으로 한 새로운 프레임워크인 Hierarchical Adapters Merging (HAM)을 제안한다. HAM은 다른 작업의 어댑터를 동적으로 결합하여 효율적으로 확장 가능하며, 관련 작업 간의 전이 학습을 용이하게 한다. 실험 결과, HAM은 다른 기준선 방법보다 효율적으로 더 많은 작업을 관리하며 성능을 크게 향상시킨다.

## 🎯 주요 포인트


- 연속 학습은 인간 인지의 필수 능력이지만 현재의 심층 학습 모델에 중요한 도전 과제를 제기합니다.

- 새로운 지식이 이전에 학습한 정보와 간섭하여 이전 지식을 잊게 만드는 치명적인 잊음 현상이 발생합니다.

- HAM은 다른 작업에서 어댑터를 동적으로 결합하여 규모를 효과적으로 확장하고 경쟁 기준선보다 더 효율적으로 작업을 관리할 수 있도록 합니다.


---

*Generated on 2025-09-18 16:48:34*