# Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets

**Korean Title:** 배터리 열화의 점진적 다단계 예측을 위한 의사 목표 사용

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Pseudo Targets

## 🔗 유사한 논문
- [[2025-09-22/CBPNet_ A Continual Backpropagation Prompt Network for Alleviating Plasticity Loss on Edge Devices_20250922|CBPNet A Continual Backpropagation Prompt Network for Alleviating Plasticity Loss on Edge Devices]] (81.5% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (81.5% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (80.6% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (80.6% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15740v1 Announce Type: new 
Abstract: Data-driven models accurately perform early battery prognosis to prevent equipment failure and further safety hazards. Most existing machine learning (ML) models work in offline mode which must consider their retraining post-deployment every time new data distribution is encountered. Hence, there is a need for an online ML approach where the model can adapt to varying distributions. However, existing online incremental multistep forecasts are a great challenge as there is no way to correct the model of its forecasts at the current instance. Also, these methods need to wait for a considerable amount of time to acquire enough streaming data before retraining. In this study, we propose iFSNet (incremental Fast and Slow learning Network) which is a modified version of FSNet for a single-pass mode (sample-by-sample) to achieve multistep forecasting using pseudo targets. It uses a simple linear regressor of the input sequence to extrapolate pseudo future samples (pseudo targets) and calculate the loss from the rest of the forecast and keep updating the model. The model benefits from the associative memory and adaptive structure mechanisms of FSNet, at the same time the model incrementally improves by using pseudo targets. The proposed model achieved 0.00197 RMSE and 0.00154 MAE on datasets with smooth degradation trajectories while it achieved 0.01588 RMSE and 0.01234 MAE on datasets having irregular degradation trajectories with capacity regeneration spikes.

## 🔍 Abstract (한글 번역)

arXiv:2509.15740v1 발표 유형: 신규  
초록: 데이터 기반 모델은 장비 고장 및 추가적인 안전 위험을 방지하기 위해 초기 배터리 예측을 정확하게 수행합니다. 대부분의 기존 머신러닝(ML) 모델은 오프라인 모드에서 작동하며, 새로운 데이터 분포가 발생할 때마다 배포 후 재학습을 고려해야 합니다. 따라서 모델이 다양한 분포에 적응할 수 있는 온라인 ML 접근 방식이 필요합니다. 그러나 기존의 온라인 증분 다단계 예측은 현재 시점에서 모델의 예측을 수정할 방법이 없기 때문에 큰 도전 과제입니다. 또한, 이러한 방법들은 재학습을 위해 충분한 스트리밍 데이터를 획득할 때까지 상당한 시간을 기다려야 합니다. 본 연구에서는 단일 패스 모드(샘플별)에서 의사 타겟을 사용하여 다단계 예측을 달성하기 위해 FSNet의 수정 버전인 iFSNet(증분 빠르고 느린 학습 네트워크)을 제안합니다. 이는 입력 시퀀스의 간단한 선형 회귀자를 사용하여 의사 미래 샘플(의사 타겟)을 외삽하고 나머지 예측에서 손실을 계산하여 모델을 지속적으로 업데이트합니다. 모델은 FSNet의 연관 기억 및 적응 구조 메커니즘의 이점을 누리면서, 동시에 의사 타겟을 사용하여 점진적으로 개선됩니다. 제안된 모델은 매끄러운 열화 경로를 가진 데이터셋에서 0.00197 RMSE와 0.00154 MAE를 달성했으며, 용량 재생 스파이크가 있는 불규칙한 열화 경로를 가진 데이터셋에서는 0.01588 RMSE와 0.01234 MAE를 달성했습니다.

## 📝 요약

이 논문은 배터리의 조기 예측을 위한 데이터 기반 모델을 제안합니다. 기존의 머신러닝 모델은 새로운 데이터 분포에 맞춰 재학습이 필요하지만, 이 연구에서는 온라인 방식의 iFSNet을 제안하여 모델이 변화하는 데이터 분포에 적응할 수 있도록 했습니다. iFSNet은 FSNet을 수정한 버전으로, 단일 패스 모드에서 의사 목표를 사용하여 다단계 예측을 수행합니다. 이 모델은 입력 시퀀스의 선형 회귀를 통해 의사 미래 샘플을 추정하고, 이를 기반으로 손실을 계산하여 모델을 지속적으로 업데이트합니다. 연구 결과, iFSNet은 매끄러운 열화 경로를 가진 데이터셋에서 0.00197 RMSE와 0.00154 MAE를, 불규칙한 열화 경로를 가진 데이터셋에서는 0.01588 RMSE와 0.01234 MAE를 기록했습니다.

## 🎯 주요 포인트

- 1. 데이터 기반 모델은 초기 배터리 예측을 통해 장비 고장과 안전 위험을 예방할 수 있다.

- 2. 기존의 머신러닝 모델은 오프라인 모드로 작동하며, 새로운 데이터 분포가 발생할 때마다 재훈련이 필요하다.

- 3. iFSNet은 FSNet의 수정 버전으로, 단일 패스 모드에서 의사 목표를 사용하여 다단계 예측을 수행한다.

- 4. iFSNet은 입력 시퀀스의 단순 선형 회귀를 사용하여 의사 미래 샘플을 추정하고, 이를 통해 모델을 지속적으로 업데이트한다.

- 5. 제안된 모델은 매끄러운 열화 경로 데이터셋에서 0.00197 RMSE와 0.00154 MAE를, 불규칙한 열화 경로 데이터셋에서 0.01588 RMSE와 0.01234 MAE를 달성했다.

---

*Generated on 2025-09-22 15:23:28*