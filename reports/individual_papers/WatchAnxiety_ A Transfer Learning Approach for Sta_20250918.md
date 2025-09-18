
# WatchAnxiety: A Transfer Learning Approach for State Anxiety Prediction from Smartwatch Data

**Korean Title:** 스마트워치 데이터로부터 상태 불안을 예측하기 위한 전이 학습 접근 방식인 WatchAnxiety.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Probabilistic Predictions|Probabilistic Predictions]] [[keywords/broad/Transfer Learning|Transfer Learning]] [[keywords/broad/Smartwatch Data|Smartwatch Data]] [[keywords/specific/Ecological Momentary Assessments (EMAs|Ecological Momentary Assessments (EMAs]] [[keywords/unique/Just-In-Time Adaptive Interventions (JITAIs|Just-In-Time Adaptive Interventions (JITAIs]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Meta-learner
**🔬 Broad Technical**: Transfer Learning, Smartwatch Data
**🔗 Specific Connectable**: Ecological Momentary Assessments
**⭐ Unique Technical**: Just-In-Time Adaptive Interventions

**ArXiv ID**: [2509.13725](https://arxiv.org/abs/2509.13725)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13725.pdf)


## 🏷️ 추출된 키워드



`Transfer Learning` • 

`Smartwatch Data` • 

`Ecological Momentary Assessments (EMAs` • 

`Just-In-Time Adaptive Interventions (JITAIs` • 

`Probabilistic Predictions`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13725v1 Announce Type: new 
Abstract: Social anxiety is a common mental health condition linked to significant challenges in academic, social, and occupational functioning. A core feature is elevated momentary (state) anxiety in social situations, yet little prior work has measured or predicted fluctuations in this anxiety throughout the day. Capturing these intra-day dynamics is critical for designing real-time, personalized interventions such as Just-In-Time Adaptive Interventions (JITAIs). To address this gap, we conducted a study with socially anxious college students (N=91; 72 after exclusions) using our custom smartwatch-based system over an average of 9.03 days (SD = 2.95). Participants received seven ecological momentary assessments (EMAs) per day to report state anxiety. We developed a base model on over 10,000 days of external heart rate data, transferred its representations to our dataset, and fine-tuned it to generate probabilistic predictions. These were combined with trait-level measures in a meta-learner. Our pipeline achieved 60.4% balanced accuracy in state anxiety detection in our dataset. To evaluate generalizability, we applied the training approach to a separate hold-out set from the TILES-18 dataset-the same dataset used for pretraining. On 10,095 once-daily EMAs, our method achieved 59.1% balanced accuracy, outperforming prior work by at least 7%.

## 🔍 Abstract (한글 번역)

arXiv:2509.13725v1 발표 유형: 새로운
요약: 사회 불안은 학업, 사회 및 직업 기능에서 중요한 어려움과 관련된 일반적인 정신 건강 상태입니다. 핵심 특징은 사회 상황에서 과도한 순간적 불안(상태)이지만, 이러한 불안의 변동을 하루 내내 측정하거나 예측한 이전 연구는 거의 없습니다. 이러한 하루 중 역학을 포착하는 것은 Just-In-Time Adaptive Interventions (JITAIs)와 같은 실시간 맞춤형 개입을 설계하는 데 중요합니다. 이 간극을 해결하기 위해 우리는 우리의 맞춤형 스마트워치 기반 시스템을 사용하여 사회적으로 불안한 대학생들(N=91; 제외 후 72명)과 평균 9.03일(표준편차 = 2.95) 동안 연구를 수행했습니다. 참가자들은 매일 7회의 생태학적 순간평가(EMAs)를 받아 상태 불안을 보고했습니다. 우리는 10,000일 이상의 외부 심박수 데이터에서 기본 모델을 개발하고 해당 표현을 우리 데이터셋으로 이전하여 확률적 예측을 생성하기 위해 세밀하게 조정했습니다. 이러한 예측은 메타-학습자와 특성 수준 측정값과 결합되었습니다. 우리의 파이프라인은 데이터셋에서 상태 불안을 감지하는 데 60.4%의 균형 잘못된 정확도를 달성했습니다. 일반화를 평가하기 위해 우리는 훈련 접근법을 사전 훈련에 사용된 동일한 TILES-18 데이터셋의 별도의 보류 집합에 적용했습니다. 10,095회의 일일 EMAs에서 우리 방법은 59.1%의 균형 잘못된 정확도를 달성하여 이전 연구를 적어도 7% 이상 능가했습니다.

## 📝 요약

이 연구는 사회 불안이라는 흔한 정신 건강 상태가 사회적, 학업적, 직업적 기능에 중요한 어려움을 초래하는 것과 관련이 있다. 이 연구에서는 사회적 불안을 가진 대학생을 대상으로 스마트워치 기반 시스템을 활용하여 하루 중 불안 상태의 변동을 측정하고 예측하는 방법을 제안하였다. 외부 심박수 데이터를 활용한 기본 모델을 개발하고 이를 우리 데이터셋에 맞게 조정하여 확률적 예측을 생성하였다. 이를 트레이트 수준 측정값과 결합하여 메타-러너로 사용하였고, 이를 통해 우리 데이터셋에서 60.4%의 균형 재현율을 달성하였다. 이 방법은 TILES-18 데이터셋을 사용하여 사전 훈련한 후보 데이터셋에도 적용되어 59.1%의 균형 재현율을 달성하였으며, 이전 연구보다 최소 7% 이상 우수한 성과를 보였다.

## 🎯 주요 포인트


- 사회 불안은 학업, 사회, 직업 기능에 중요한 도전을 일으키는 일반적인 정신 건강 상태이다.

- 사회 불안은 사회 상황에서 상승하는 순간적 불안이라는 핵심 특징을 가지고 있다.

- 실시간, 맞춤형 개입을 위해 하루 중 불안의 변동을 측정하고 예측하는 것이 중요하다.


---

*Generated on 2025-09-18 16:38:39*