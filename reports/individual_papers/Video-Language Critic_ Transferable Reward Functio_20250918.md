
# Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics

**Korean Title:** 비디오-언어 비평가: 언어-조건화된 로봇학을 위한 이전 가능한 보상 기능유지하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Temporal Ranking Objective|Temporal Ranking Objective]] [[keywords/broad/Language Grounding|Language Grounding]] [[keywords/broad/Contrastive Learning|Contrastive Learning]] [[keywords/specific/Meta-World tasks|Meta-World tasks]] [[keywords/unique/Video-Language Critic|Video-Language Critic]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temporal Ranking Objective
**🔬 Broad Technical**: Language Grounding, Contrastive Learning
**🔗 Specific Connectable**: Meta-World tasks
**⭐ Unique Technical**: Video-Language Critic

**ArXiv ID**: [2405.19988](https://arxiv.org/abs/2405.19988)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2405.19988.pdf)


## 🏷️ 추출된 키워드



`Language Grounding` • 

`Contrastive Learning` • 

`Meta-World tasks` • 

`Video-Language Critic` • 

`Temporal Ranking Objective`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.19988v3 Announce Type: replace-cross 
Abstract: Natural language is often the easiest and most convenient modality for humans to specify tasks for robots. However, learning to ground language to behavior typically requires impractical amounts of diverse, language-annotated demonstrations collected on each target robot. In this work, we aim to separate the problem of what to accomplish from how to accomplish it, as the former can benefit from substantial amounts of external observation-only data, and only the latter depends on a specific robot embodiment. To this end, we propose Video-Language Critic, a reward model that can be trained on readily available cross-embodiment data using contrastive learning and a temporal ranking objective, and use it to score behavior traces from a separate actor. When trained on Open X-Embodiment data, our reward model enables 2x more sample-efficient policy training on Meta-World tasks than a sparse reward only, despite a significant domain gap. Using in-domain data but in a challenging task generalization setting on Meta-World, we further demonstrate more sample-efficient training than is possible with prior language-conditioned reward models that are either trained with binary classification, use static images, or do not leverage the temporal information present in video data.

## 🔍 Abstract (한글 번역)

arXiv:2405.19988v3 발표 유형: 대체-교차
요약: 자연어는 종종 사람들이 로봇에게 작업을 지정하는 가장 쉽고 편리한 방법입니다. 그러나 언어를 행동에 연결하는 학습은 일반적으로 각 대상 로봇에서 수집된 다양한 언어 주석이 달린 데모가 비현실적인 양으로 필요합니다. 본 연구에서는 무엇을 달성할 것인지와 어떻게 달성할 것인지라는 문제를 분리하고자 합니다. 전자는 외부 관찰 데이터의 상당한 양에서 이점을 얻을 수 있으며, 후자는 특정 로봇 구현에 의존합니다. 이를 위해 우리는 비디오-언어 평가자를 제안합니다. 이 보상 모델은 대조 학습과 시간 순위 목표를 사용하여 사용 가능한 교차 구현 데이터에서 훈련될 수 있으며, 별도의 배우로부터 행동 추적을 점수화하는 데 사용됩니다. Open X-Embodiment 데이터에서 훈련된 경우, 우리의 보상 모델은 상당한 도메인 갭에도 불구하고 Meta-World 작업에서 희소 보상만큼의 2배 더 효율적인 샘플 효율적인 정책 훈련을 가능하게 합니다. Meta-World에서 도메인 데이터를 사용하지만 도전적인 작업 일반화 설정에서, 이전의 언어 조건부 보상 모델보다 더 샘플 효율적인 훈련을 더 나은 것을 더 증명합니다. 이전 모델은 이진 분류로 훈련되었거나 정적 이미지를 사용하거나 비디오 데이터의 시간 정보를 활용하지 않습니다.

## 📝 요약

로봇에게 작업을 명시하는 가장 쉽고 편리한 방법은 자연어입니다. 그러나 언어를 행동에 매핑하는 것은 일반적으로 각 로봇에 대해 수집된 다양한 언어 주석이 달린 데모가 필요하여 실용적이지 않습니다. 본 연구에서는 어떤 작업을 수행할지 결정하는 문제와 어떻게 수행할지 결정하는 문제를 분리하고자 합니다. 이를 위해 Video-Language Critic를 제안하여 외부 관찰 데이터를 사용하여 교차 구현 데이터로 훈련시킬 수 있는 보상 모델을 제안합니다. 이 모델은 Meta-World 작업에서 이전의 언어 조건부 보상 모델보다 2배 더 효율적인 정책 훈련을 가능하게 합니다.

## 🎯 주요 포인트


- 언어를 행동에 연결하는 학습은 다양한 언어 주석이 담긴 데모가 필요하지만, 외부 관찰 데이터를 사용하여 목표를 달성하는 문제와 로봇 구현에 따른 방법을 분리하는 것이 중요하다.

- Video-Language Critic은 외부 관찰 데이터를 사용하여 훈련되며, Meta-World 작업에서 sparse reward만 사용하는 것보다 2배 더 효율적인 정책 훈련을 가능하게 한다.

- 이 모델은 이전 언어 조건부 보상 모델보다 도메인 갭이 크더라도 더 효율적인 훈련이 가능하며, 비디오 데이터의 시간 정보를 활용한다.


---

*Generated on 2025-09-18 16:28:34*