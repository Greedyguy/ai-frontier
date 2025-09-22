
# Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes

**Korean Title:** 인공지능 기반 심전도 연령: 향후 불리한 임신 결과 예측을 위한 디지털 바이오마커

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Digital Biomarker

## 🔗 유사한 논문
- [[Data-Driven_Prediction_of_Maternal_Nutritional_Status_in_Ethiopia_Using_Ensemble_Machine_Learning_Models_20250919|Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models]] (79.9% similar)
- [[Towards Trustworthy Vital Sign Forecasting Leveraging Uncertainty for Prediction Intervals]] (78.5% similar)
- [[Brain_age_identification_from_diffusion_MRI_synergistically_predicts_neurodegenerative_disease_20250918|Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease]] (77.3% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (76.3% similar)
- [[ModalSurv A Multimodal Deep Survival Framework for Prostate and Bladder Cancer]] (76.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14242v1 Announce Type: cross 
Abstract: Cardiotocography (CTG) is a low-cost, non-invasive fetal health assessment technique used globally, especially in underdeveloped countries. However, it is currently mainly used to identify the fetus's current status (e.g., fetal acidosis or hypoxia), and the potential of CTG in predicting future adverse pregnancy outcomes has not been fully explored. We aim to develop an AI-based model that predicts biological age from CTG time series (named CTGage), then calculate the age gap between CTGage and actual age (named CTGage-gap), and use this gap as a new digital biomarker for future adverse pregnancy outcomes. The CTGage model is developed using 61,140 records from 11,385 pregnant women, collected at Peking University People's Hospital between 2018 and 2022. For model training, a structurally designed 1D convolutional neural network is used, incorporating distribution-aligned augmented regression technology. The CTGage-gap is categorized into five groups: < -21 days (underestimation group), -21 to -7 days, -7 to 7 days (normal group), 7 to 21 days, and > 21 days (overestimation group). We further defined the underestimation group and overestimation group together as the high-risk group. We then compare the incidence of adverse outcomes and maternal diseases across these groups. The average absolute error of the CTGage model is 10.91 days. When comparing the overestimation group with the normal group, premature infants incidence is 5.33% vs. 1.42% (p < 0.05) and gestational diabetes mellitus (GDM) incidence is 31.93% vs. 20.86% (p < 0.05). When comparing the underestimation group with the normal group, low birth weight incidence is 0.17% vs. 0.15% (p < 0.05) and anaemia incidence is 37.51% vs. 34.74% (p < 0.05). Artificial intelligence-derived CTGage can predict the future risk of adverse pregnancy outcomes and hold potential as a novel, non-invasive, and easily accessible digital biomarker.

## 🔍 Abstract (한글 번역)

arXiv:2509.14242v1 발표 유형: 교차  
초록: 심전도(CTG)는 저비용, 비침습적 태아 건강 평가 기법으로, 특히 개발도상국에서 전 세계적으로 사용됩니다. 그러나 현재 CTG는 주로 태아의 현재 상태(예: 태아 산증 또는 저산소증)를 식별하는 데 사용되며, 미래의 불리한 임신 결과를 예측하는 데 있어 CTG의 잠재력은 충분히 탐구되지 않았습니다. 우리는 CTG 시계열로부터 생물학적 나이를 예측하는 AI 기반 모델(CTGage라 명명)을 개발하고, CTGage와 실제 나이 간의 나이 차이(CTGage-gap라 명명)를 계산하여 이를 미래의 불리한 임신 결과에 대한 새로운 디지털 바이오마커로 사용하고자 합니다. CTGage 모델은 2018년부터 2022년까지 베이징 대학교 인민병원에서 수집된 11,385명의 임산부로부터 61,140개의 기록을 사용하여 개발되었습니다. 모델 훈련을 위해 구조적으로 설계된 1D 합성곱 신경망이 사용되며, 분포 정렬 증강 회귀 기술이 포함됩니다. CTGage-gap은 다섯 그룹으로 분류됩니다: < -21일(과소평가 그룹), -21일에서 -7일, -7일에서 7일(정상 그룹), 7일에서 21일, > 21일(과대평가 그룹). 우리는 과소평가 그룹과 과대평가 그룹을 함께 고위험 그룹으로 정의했습니다. 그런 다음 이러한 그룹 간의 불리한 결과와 모성 질환의 발생률을 비교합니다. CTGage 모델의 평균 절대 오차는 10.91일입니다. 과대평가 그룹과 정상 그룹을 비교할 때, 조산아 발생률은 5.33% 대 1.42%(p < 0.05)이고, 임신성 당뇨병(GDM) 발생률은 31.93% 대 20.86%(p < 0.05)입니다. 과소평가 그룹과 정상 그룹을 비교할 때, 저체중아 발생률은 0.17% 대 0.15%(p < 0.05)이고, 빈혈 발생률은 37.51% 대 34.74%(p < 0.05)입니다. 인공지능으로 도출된 CTGage는 미래의 불리한 임신 결과의 위험을 예측할 수 있으며, 새로운 비침습적이고 쉽게 접근할 수 있는 디지털 바이오마커로서의 잠재력을 지니고 있습니다.

## 📝 요약

이 연구는 심장태아감시(CTG)를 이용한 AI 기반 모델 CTGage를 개발하여 태아의 생물학적 연령을 예측하고, 실제 연령과의 차이인 CTGage-gap을 새로운 디지털 바이오마커로 활용하여 향후 임신 합병증을 예측하는 방법을 제안합니다. 2018-2022년 북경대학 인민병원에서 수집된 11,385명의 임산부 데이터를 바탕으로 1D CNN을 사용해 모델을 훈련했습니다. CTGage-gap을 5개 그룹으로 분류하고, 고위험군으로 정의된 과대 및 과소평가 그룹에서 조산과 임신성 당뇨병 발생률이 높음을 발견했습니다. CTGage는 비침습적이고 접근 가능한 새로운 예측 도구로서의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. CTG는 저비용, 비침습적 태아 건강 평가 기법으로, 특히 저개발 국가에서 널리 사용됩니다.

- 2. CTGage 모델은 CTG 시계열 데이터를 기반으로 생물학적 나이를 예측하여, 실제 나이와의 차이를 새로운 디지털 바이오마커로 활용합니다.

- 3. CTGage 모델은 2018년부터 2022년까지 북경대학교 인민병원에서 수집된 11,385명의 임산부의 61,140개의 기록을 사용하여 개발되었습니다.

- 4. CTGage-gap의 고위험 그룹에서는 조산아 발생률과 임신성 당뇨병 발생률이 정상 그룹에 비해 유의미하게 높습니다.

- 5. 인공지능 기반 CTGage는 향후 임신 합병증의 위험을 예측할 수 있는 잠재력을 지닌 새로운 디지털 바이오마커로서의 가능성을 보여줍니다.

---

*Generated on 2025-09-19 15:33:52*