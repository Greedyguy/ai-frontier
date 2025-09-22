# SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning

**Korean Title:** SuPreME: 다중 모달 ECG 표현 학습을 위한 지도 사전 학습 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Zero-shot Classification

## 🔗 유사한 논문
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.4% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (80.1% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (79.4% similar)
- [[2025-09-18/Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (79.3% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (79.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.19668v4 Announce Type: replace-cross 
Abstract: Cardiovascular diseases are a leading cause of death and disability worldwide. Electrocardiogram (ECG) is critical for diagnosing and monitoring cardiac health, but obtaining large-scale annotated ECG datasets is labor-intensive and time-consuming. Recent ECG Self-Supervised Learning (eSSL) methods mitigate this by learning features without extensive labels but fail to capture fine-grained clinical semantics and require extensive task-specific fine-tuning. To address these challenges, we propose $\textbf{SuPreME}$, a $\textbf{Su}$pervised $\textbf{Pre}$-training framework for $\textbf{M}$ultimodal $\textbf{E}$CG representation learning. SuPreME is pre-trained using structured diagnostic labels derived from ECG report entities through a one-time offline extraction with Large Language Models (LLMs), which help denoise, standardize cardiac concepts, and improve clinical representation learning. By fusing ECG signals with textual cardiac queries instead of fixed labels, SuPreME enables zero-shot classification of unseen conditions without further fine-tuning. We evaluate SuPreME on six downstream datasets covering 106 cardiac conditions, achieving superior zero-shot AUC performance of $77.20\%$, surpassing state-of-the-art eSSLs by $4.98\%$. Results demonstrate SuPreME's effectiveness in leveraging structured, clinically relevant knowledge for high-quality ECG representations.

## 🔍 Abstract (한글 번역)

arXiv:2502.19668v4 발표 유형: 교차 대체  
초록: 심혈관 질환은 전 세계적으로 주요 사망 및 장애 원인입니다. 심전도(ECG)는 심장 건강을 진단하고 모니터링하는 데 필수적이지만, 대규모로 주석이 달린 심전도 데이터셋을 얻는 것은 노동 집약적이고 시간이 많이 소요됩니다. 최근의 ECG 자기 지도 학습(eSSL) 방법은 광범위한 레이블 없이 특징을 학습하여 이를 완화하지만, 세밀한 임상 의미를 포착하지 못하고 광범위한 작업별 미세 조정이 필요합니다. 이러한 문제를 해결하기 위해, 우리는 $\textbf{SuPreME}$, 즉 $\textbf{Su}$pervised $\textbf{Pre}$-training framework for $\textbf{M}$ultimodal $\textbf{E}$CG representation learning을 제안합니다. SuPreME는 대형 언어 모델(LLM)을 통해 ECG 보고서 엔티티에서 파생된 구조화된 진단 레이블을 사용하여 일회성 오프라인 추출을 통해 사전 훈련되며, 이는 심장 개념을 표준화하고 임상 표현 학습을 개선하는 데 도움을 줍니다. 고정된 레이블 대신 ECG 신호를 텍스트 심장 쿼리와 융합함으로써 SuPreME는 추가 미세 조정 없이 보지 못한 상태에 대한 제로샷 분류를 가능하게 합니다. 우리는 106개의 심장 상태를 다루는 6개의 다운스트림 데이터셋에서 SuPreME를 평가하여 $77.20\%$의 우수한 제로샷 AUC 성능을 달성했으며, 이는 최첨단 eSSL을 $4.98\%$ 초과합니다. 결과는 구조화된 임상 관련 지식을 활용하여 고품질의 ECG 표현을 생성하는 SuPreME의 효과를 입증합니다.

## 📝 요약

이 논문은 심혈관 질환 진단에 중요한 심전도(ECG) 데이터를 효과적으로 활용하기 위한 새로운 프레임워크 SuPreME를 제안합니다. 기존의 자기지도 학습 방법은 세밀한 임상적 의미를 포착하지 못하고, 많은 미세 조정이 필요하다는 한계를 가집니다. SuPreME는 대규모 언어 모델을 활용해 ECG 보고서에서 진단 라벨을 추출하고, 이를 통해 임상적 표현 학습을 개선합니다. ECG 신호와 텍스트 질의를 융합하여 추가적인 미세 조정 없이도 새로운 상태에 대한 제로샷 분류가 가능합니다. 106개의 심장 상태를 다루는 6개의 데이터셋에서 평가한 결과, SuPreME는 기존 방법을 능가하는 77.20%의 AUC 성능을 보였습니다. 이는 SuPreME가 구조화된 임상 지식을 효과적으로 활용하여 고품질의 ECG 표현을 학습할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 심혈관 질환 진단 및 모니터링에 중요한 ECG 데이터셋의 대규모 주석 작업은 시간과 노력이 많이 소요됩니다.

- 2. SuPreME는 ECG 보고서의 진단 레이블을 대형 언어 모델을 통해 추출하여 임상 표현 학습을 개선합니다.

- 3. SuPreME는 고정된 레이블 대신 ECG 신호와 텍스트 질의 융합을 통해 추가 미세 조정 없이 새로운 상태에 대한 제로샷 분류를 가능하게 합니다.

- 4. SuPreME는 106개의 심장 상태를 포함하는 6개의 다운스트림 데이터셋에서 제로샷 AUC 성능 77.20%를 달성하여 기존 eSSL 방법을 능가합니다.

- 5. SuPreME는 구조화된 임상 지식을 활용하여 고품질 ECG 표현을 학습하는 데 효과적임을 입증했습니다.

---

*Generated on 2025-09-22 14:43:37*