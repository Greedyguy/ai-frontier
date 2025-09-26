---
keywords:
  - Transfer Learning
  - State Anxiety Prediction
  - Ecological Momentary Assessments
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:42:57.467133",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transfer Learning",
    "State Anxiety Prediction",
    "Ecological Momentary Assessments"
  ],
  "rejected_keywords": [
    "Smartwatch Data"
  ],
  "similarity_scores": {
    "Transfer Learning": 0.8,
    "State Anxiety Prediction": 0.75,
    "Ecological Momentary Assessments": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# WatchAnxiety: A Transfer Learning Approach for State Anxiety Prediction from Smartwatch Data

**Korean Title:** 스마트워치 데이터로부터 상태 불안 예측을 위한 전이 학습 접근법: WatchAnxiety

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transfer Learning|Transfer Learning]]
**⚡ Unique Technical**: [[keywords/State Anxiety Prediction|State Anxiety Prediction]], [[keywords/Ecological Momentary Assessments|Ecological Momentary Assessments]]

## 🔗 유사한 논문
- [[Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (79.7% similar)
- [[Towards Trustworthy Vital Sign Forecasting_ Leveraging Uncertainty for Prediction Intervals_20250918|Towards Trustworthy Vital Sign Forecasting Leveraging Uncertainty for Prediction Intervals]] (77.9% similar)
- [[SMART_ Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction_20250919|SMART Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction]] (75.9% similar)
- [[Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes_20250919|Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes]] (75.8% similar)
- [[An Attention-Based Denoising Framework for Personality Detection in Social Media Texts_20250918|An Attention-Based Denoising Framework for Personality Detection in Social Media Texts]] (75.7% similar)

## 📋 저자 정보

**Authors:** Md Sabbir Ahmed, Noah French, Mark Rucker, Zhiyuan Wang, Taylor Myers-Brower, Kaitlyn Petz, Mehdi Boukhechba, Bethany A. Teachman, Laura E. Barnes

## 📄 Abstract (원문)

Social anxiety is a common mental health condition linked to significant
challenges in academic, social, and occupational functioning. A core feature is
elevated momentary (state) anxiety in social situations, yet little prior work
has measured or predicted fluctuations in this anxiety throughout the day.
Capturing these intra-day dynamics is critical for designing real-time,
personalized interventions such as Just-In-Time Adaptive Interventions
(JITAIs). To address this gap, we conducted a study with socially anxious
college students (N=91; 72 after exclusions) using our custom smartwatch-based
system over an average of 9.03 days (SD = 2.95). Participants received seven
ecological momentary assessments (EMAs) per day to report state anxiety. We
developed a base model on over 10,000 days of external heart rate data,
transferred its representations to our dataset, and fine-tuned it to generate
probabilistic predictions. These were combined with trait-level measures in a
meta-learner. Our pipeline achieved 60.4% balanced accuracy in state anxiety
detection in our dataset. To evaluate generalizability, we applied the training
approach to a separate hold-out set from the TILES-18 dataset-the same dataset
used for pretraining. On 10,095 once-daily EMAs, our method achieved 59.1%
balanced accuracy, outperforming prior work by at least 7%.

## 🔍 Abstract (한글 번역)

사회 불안은 학업, 사회적, 직업적 기능에서 상당한 어려움을 초래하는 흔한 정신 건강 상태입니다. 핵심 특징은 사회적 상황에서 순간적으로 증가하는 불안(상태 불안)이며, 이러한 불안의 일중 변동을 측정하거나 예측한 이전 연구는 거의 없습니다. 이러한 일중 역학을 포착하는 것은 Just-In-Time Adaptive Interventions (JITAIs)와 같은 실시간 맞춤형 중재를 설계하는 데 중요합니다. 이 격차를 해결하기 위해, 우리는 사회 불안을 가진 대학생들(N=91; 제외 후 72명)을 대상으로 평균 9.03일(SD = 2.95) 동안 맞춤형 스마트워치 기반 시스템을 사용하여 연구를 수행했습니다. 참가자들은 하루에 일곱 번의 생태학적 순간 평가(EMA)를 통해 상태 불안을 보고했습니다. 우리는 외부 심박수 데이터 10,000일 이상의 데이터를 기반으로 기본 모델을 개발하고, 그 표현을 우리의 데이터셋에 전이하여 미세 조정을 통해 확률적 예측을 생성했습니다. 이러한 예측은 특성 수준의 측정과 결합되어 메타 학습자에서 사용되었습니다. 우리의 파이프라인은 데이터셋에서 상태 불안 감지에 60.4%의 균형 정확도를 달성했습니다. 일반화 가능성을 평가하기 위해, 우리는 TILES-18 데이터셋에서 별도의 보류 집합에 훈련 접근법을 적용했습니다. 이 데이터셋은 사전 훈련에 사용된 동일한 데이터셋입니다. 10,095개의 하루 한 번의 EMA에서 우리의 방법은 59.1%의 균형 정확도를 달성하여 이전 연구보다 최소 7% 이상 우수한 성과를 보였습니다.

## 📝 요약

이 연구는 사회 불안이 있는 대학생들을 대상으로 스마트워치 기반 시스템을 활용하여 하루 동안의 순간적 불안 변동을 측정하고 예측하는 방법을 제안합니다. 연구는 72명의 참가자를 대상으로 평균 9일 동안 하루 7번의 생태학적 순간 평가(EMA)를 통해 불안 상태를 보고하도록 했습니다. 외부 심박수 데이터로 개발된 기본 모델을 사용하여 데이터셋에 전이 학습을 수행하고, 확률적 예측을 생성하기 위해 미세 조정했습니다. 이 방법은 데이터셋에서 60.4%의 균형 정확도를 달성했으며, TILES-18 데이터셋의 별도 검증 세트에서도 59.1%의 균형 정확도를 기록하여 이전 연구보다 최소 7% 더 높은 성능을 보였습니다. 연구는 실시간 개인 맞춤형 중재 설계에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 사회적 불안은 학업, 사회적, 직업적 기능에 중대한 도전을 초래하는 흔한 정신 건강 상태입니다.

- 2. 본 연구는 사회적 불안이 있는 대학생들을 대상으로 맞춤형 스마트워치 시스템을 사용하여 하루 평균 9.03일 동안 연구를 진행했습니다.

- 3. 참가자들은 하루에 7번의 생태학적 순간 평가(EMA)를 통해 상태 불안을 보고했습니다.

- 4. 외부 심박수 데이터 10,000일 이상을 기반으로 한 모델을 개발하고, 이를 데이터셋에 전이 학습하여 확률적 예측을 생성했습니다.

- 5. 본 연구의 방법은 TILES-18 데이터셋의 별도 검증 세트에서 59.1%의 균형 정확도를 달성하며, 이전 연구보다 최소 7% 향상된 성과를 보였습니다.

---

*Generated on 2025-09-20 09:37:50*