---
keywords:
  - Continual Learning
  - Electroencephalography
  - Personalized Seizure Detection
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:48:13.837291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continual Learning",
    "Electroencephalography",
    "Personalized Seizure Detection"
  ],
  "rejected_keywords": [
    "Deep Learning"
  ],
  "similarity_scores": {
    "Continual Learning": 0.82,
    "Electroencephalography": 0.78,
    "Personalized Seizure Detection": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection

**Korean Title:** 예산 내 개인화: 자원 효율적인 발작 감지를 위한 최소 라벨 지속 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Continual Learning|continual learning]]
**⚡ Unique Technical**: [[keywords/Electroencephalography|electroencephalography]], [[keywords/Personalized Seizure Detection|personalized seizure detection]]

## 🔗 유사한 논문
- [[Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (81.2% similar)
- [[UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (80.1% similar)
- [[HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (79.9% similar)
- [[Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (79.4% similar)
- [[HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C Efficient Medical Data Classification for Embedded Devices]] (79.2% similar)

## 📋 저자 정보

**Authors:** Amirhossein Shahbazinia, Jonathan Dan, Jose A. Miranda, Giovanni Ansaloni, David Atienza

## 📄 Abstract (원문)

Objective: Epilepsy, a prevalent neurological disease, demands careful
diagnosis and continuous care. Seizure detection remains challenging, as
current clinical practice relies on expert analysis of electroencephalography,
which is a time-consuming process and requires specialized knowledge.
Addressing this challenge, this paper explores automated epileptic seizure
detection using deep learning, focusing on personalized continual learning
models that adapt to each patient's unique electroencephalography signal
features, which evolve over time. Methods: In this context, our approach
addresses the challenge of integrating new data into existing models without
catastrophic forgetting, a common issue in static deep learning models. We
propose EpiSMART, a continual learning framework for seizure detection that
uses a size-constrained replay buffer and an informed sample selection strategy
to incrementally adapt to patient-specific electroencephalography signals. By
selectively retaining high-entropy and seizure-predicted samples, our method
preserves critical past information while maintaining high performance with
minimal memory and computational requirements. Results: Validation on the
CHB-MIT dataset, shows that EpiSMART achieves a 21% improvement in the F1 score
over a trained baseline without updates in all other patients. On average,
EpiSMART requires only 6.46 minutes of labeled data and 6.28 updates per day,
making it suitable for real-time deployment in wearable systems.
Conclusion:EpiSMART enables robust and personalized seizure detection under
realistic and resource-constrained conditions by effectively integrating new
data into existing models without degrading past knowledge. Significance: This
framework advances automated seizure detection by providing a continual
learning approach that supports patient-specific adaptation and practical
deployment in wearable healthcare systems.

## 🔍 Abstract (한글 번역)

목적: 흔한 신경계 질환인 간질은 신중한 진단과 지속적인 관리가 필요합니다. 발작 감지는 여전히 도전적인 과제로, 현재의 임상 실무는 시간 소모적이며 전문 지식이 필요한 뇌파(EEG) 분석에 의존하고 있습니다. 이 문제를 해결하기 위해 본 논문은 심층 학습을 사용한 자동화된 간질 발작 감지를 탐구하며, 시간이 지남에 따라 변화하는 각 환자의 고유한 뇌파 신호 특성에 적응하는 개인 맞춤형 지속 학습 모델에 중점을 둡니다. 방법: 이러한 맥락에서, 우리의 접근법은 정적 심층 학습 모델에서 흔히 발생하는 문제인 파국적 망각 없이 기존 모델에 새로운 데이터를 통합하는 문제를 해결합니다. 우리는 발작 감지를 위한 지속 학습 프레임워크인 EpiSMART를 제안하며, 이는 크기 제한이 있는 재생 버퍼와 정보에 기반한 샘플 선택 전략을 사용하여 환자별 뇌파 신호에 점진적으로 적응합니다. 고엔트로피 및 발작 예측 샘플을 선택적으로 유지함으로써, 우리의 방법은 최소한의 메모리와 계산 요구 사항으로 높은 성능을 유지하면서 중요한 과거 정보를 보존합니다. 결과: CHB-MIT 데이터셋에 대한 검증 결과, EpiSMART는 다른 모든 환자에서 업데이트 없이 훈련된 기준선보다 F1 점수가 21% 향상되었습니다. 평균적으로 EpiSMART는 하루에 6.46분의 라벨링된 데이터와 6.28회의 업데이트만 필요로 하여, 웨어러블 시스템에서 실시간 배포에 적합합니다. 결론: EpiSMART는 새로운 데이터를 기존 모델에 효과적으로 통합하여 과거 지식을 저하시키지 않고 현실적이고 자원 제한된 조건에서 강력하고 개인화된 발작 감지를 가능하게 합니다. 의의: 이 프레임워크는 환자별 적응을 지원하고 웨어러블 헬스케어 시스템에서의 실용적인 배포를 가능하게 하는 지속 학습 접근 방식을 제공함으로써 자동화된 발작 감지를 발전시킵니다.

## 📝 요약

이 논문은 간질 발작을 자동으로 감지하기 위해 심층 학습을 활용한 방법을 제안합니다. 특히, 환자 개개인의 뇌파 신호 특성에 맞춰 지속적으로 학습하는 개인화된 모델을 개발했습니다. 기존 모델의 단점을 극복하기 위해, 새로운 데이터를 통합하면서도 이전 정보를 잃지 않는 EpiSMART라는 지속 학습 프레임워크를 제안합니다. 이 방법은 고엔트로피 및 발작 예측 샘플을 선택적으로 보존하여 높은 성능을 유지합니다. CHB-MIT 데이터셋을 통해 검증한 결과, EpiSMART는 기존 모델 대비 F1 점수가 21% 향상되었으며, 하루 평균 6.46분의 라벨링 데이터와 6.28회의 업데이트만으로도 실시간 적용이 가능합니다. 이 연구는 환자 맞춤형 적응과 웨어러블 시스템에서의 실용적 적용을 지원하는 지속 학습 접근 방식을 통해 자동 발작 감지를 발전시킵니다.

## 🎯 주요 포인트

- 1. 본 논문은 심층 학습을 활용하여 자동화된 간질 발작 탐지를 연구하며, 환자 개개인의 뇌파 신호 특징에 적응하는 개인화된 지속 학습 모델을 제안합니다.

- 2. EpiSMART라는 지속 학습 프레임워크를 통해 환자별 뇌파 신호에 점진적으로 적응하며, 과거 정보를 보존하면서도 높은 성능을 유지합니다.

- 3. CHB-MIT 데이터셋 검증 결과, EpiSMART는 다른 환자에서 업데이트 없이 훈련된 기준 모델에 비해 F1 점수가 21% 향상되었습니다.

- 4. EpiSMART는 하루 평균 6.46분의 라벨링된 데이터와 6.28회의 업데이트만으로 실시간 웨어러블 시스템에 적합한 성능을 제공합니다.

- 5. 이 프레임워크는 환자 맞춤형 적응과 실용적인 웨어러블 헬스케어 시스템 배포를 지원하는 지속 학습 접근 방식을 통해 자동 발작 탐지를 발전시킵니다.

---

*Generated on 2025-09-20 09:21:56*