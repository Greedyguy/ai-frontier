
# Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection

**Korean Title:** 예산 내에서의 개인화: 자원 효율적 발작 감지를 위한 최소 레이블 지속적 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Personalized Continual Learning|Personalized Continual Learning]] [[keywords/broad/Deep Learning|Deep Learning]] [[keywords/broad/Continual Learning|Continual Learning]] [[keywords/specific/Seizure Detection|Seizure Detection]] [[keywords/unique/EpiSMART|EpiSMART]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Personalized Continual Learning
**🔬 Broad Technical**: Deep Learning, Continual Learning
**🔗 Specific Connectable**: Seizure Detection
**⭐ Unique Technical**: EpiSMART

**ArXiv ID**: [2509.13974](https://arxiv.org/abs/2509.13974)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13974.pdf)


## 🏷️ 추출된 키워드



`Deep Learning` • 

`Continual Learning` • 

`EpiSMART` • 

`Resource-Efficient Seizure Detection` • 

`Personalized Continual Learning`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13974v1 Announce Type: new 
Abstract: Objective: Epilepsy, a prevalent neurological disease, demands careful diagnosis and continuous care. Seizure detection remains challenging, as current clinical practice relies on expert analysis of electroencephalography, which is a time-consuming process and requires specialized knowledge. Addressing this challenge, this paper explores automated epileptic seizure detection using deep learning, focusing on personalized continual learning models that adapt to each patient's unique electroencephalography signal features, which evolve over time. Methods: In this context, our approach addresses the challenge of integrating new data into existing models without catastrophic forgetting, a common issue in static deep learning models. We propose EpiSMART, a continual learning framework for seizure detection that uses a size-constrained replay buffer and an informed sample selection strategy to incrementally adapt to patient-specific electroencephalography signals. By selectively retaining high-entropy and seizure-predicted samples, our method preserves critical past information while maintaining high performance with minimal memory and computational requirements. Results: Validation on the CHB-MIT dataset, shows that EpiSMART achieves a 21% improvement in the F1 score over a trained baseline without updates in all other patients. On average, EpiSMART requires only 6.46 minutes of labeled data and 6.28 updates per day, making it suitable for real-time deployment in wearable systems. Conclusion:EpiSMART enables robust and personalized seizure detection under realistic and resource-constrained conditions by effectively integrating new data into existing models without degrading past knowledge. Significance: This framework advances automated seizure detection by providing a continual learning approach that supports patient-specific adaptation and practical deployment in wearable healthcare systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.13974v1 발표 유형: 새로운
요약: 목적: 일반적인 신경학적 질환인 간질은 주의 깊은 진단과 지속적인 관리를 요구합니다. 발작 감지는 현재 임상 실무가 전문가의 뇌파 분석에 의존하는 시간이 많이 소요되고 전문 지식이 필요한 과정으로 여전히 어려운 과제입니다. 이 논문은 이러한 도전에 대처하기 위해 딥 러닝을 사용한 자동 간질 발작 감지를 탐구하며, 시간이 지남에 따라 변화하는 각 환자의 고유한 뇌파 신호 특성에 적응하는 개인화된 지속적 학습 모델에 초점을 맞춥니다. 방법: 이 문맥에서 우리의 접근 방식은 정적 딥 러닝 모델에서 발생하는 일반적인 문제인 잊혀지지 않는 재앙을 방지하면서 새로운 데이터를 기존 모델에 통합하는 도전에 대응합니다. 우리는 EpiSMART라는 간질 발작 감지를 위한 지속적 학습 프레임워크를 제안하며, 크기 제한된 재생 버퍼와 정보화된 샘플 선택 전략을 사용하여 환자별 뇌파 신호에 점진적으로 적응합니다. 고엔트로피와 발작 예측 샘플을 선택적으로 유지함으로써 우리의 방법은 중요한 과거 정보를 보존하면서 최소한의 메모리 및 계산 요구 사항으로 높은 성능을 유지합니다. 결과: CHB-MIT 데이터셋에서의 검증 결과, EpiSMART는 다른 모든 환자에 대한 업데이트 없이 훈련된 기준선 대비 F1 점수에서 21%의 향상을 달성합니다. 평균적으로 EpiSMART는 레이블이 지정된 데이터 6.46분과 하루에 6.28회의 업데이트만 필요로 하여 웨어러블 시스템에서 실시간 배포에 적합합니다. 결론: EpiSMART는 새로운 데이터를 기존 모델에 효과적으로 통합하여 과거 지식을 저하시키지 않고 현실적이고 자원 제한적인 조건에서 견고하고 개인화된 발작 감지를 가능하게 합니다. 의의: 이 프레임워크는 환자별 적응을 지원하고 웨어러블 헬스케어 시스템에서의 실용적 배포를 지원하는 지속적 학습 접근 방식을 제공함으로써 자동화된 발작 감지를 발전시킵니다.

## 📝 요약

이 연구는 깊은 학습을 사용하여 자동 간질 발작 감지를 탐구하며, 각 환자의 고유한 뇌파 신호 특징에 적응하는 개인 맞춤형 지속적 학습 모델에 초점을 맞추었습니다. EpiSMART라는 지속적 학습 프레임워크를 제안하여 새로운 데이터를 기존 모델에 통합하면서 중요한 과거 정보를 보존하고 높은 성능을 유지하는 방법을 제시했습니다. CHB-MIT 데이터셋을 통한 검증 결과, EpiSMART는 다른 모든 환자에 대해 업데이트 없이 학습된 기준선 대비 F1 점수가 21% 향상되었습니다. 이러한 방법은 실시간으로 착용 가능한 시스템에 적합하며, 자원이 제한된 조건에서 효과적으로 새로운 데이터를 기존 모델에 통합하여 안정적이고 개인 맞춤형 간질 발작 감지를 가능케 합니다.

## 🎯 주요 포인트


- 1. 심각한 신경학적 질환인 간질에 대한 개인 맞춤형 지속적인 학습 모델을 사용한 자동 간질 발작 감지에 대한 연구

- 2. EpiSMART는 새로운 데이터를 기존 모델에 통합하면서도 중요한 과거 정보를 보존하는 간질 감지를 위한 지속적 학습 프레임워크

- 3. CHB-MIT 데이터셋을 통한 실험 결과, EpiSMART는 F1 점수에서 21%의 향상을 보이며 실시간 배포에 적합한 성능을 보임.


---

*Generated on 2025-09-18 16:39:39*