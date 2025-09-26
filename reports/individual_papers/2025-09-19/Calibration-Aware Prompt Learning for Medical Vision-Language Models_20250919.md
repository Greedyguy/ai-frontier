---
keywords:
  - Multi-Modal Learning
  - Optimization
  - Uncertainty Quantification
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15226
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:53:57.955483",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Optimization",
    "Uncertainty Quantification"
  ],
  "rejected_keywords": [
    "Few-Shot Learning"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.82,
    "Optimization": 0.75,
    "Uncertainty Quantification": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Calibration-Aware Prompt Learning for Medical Vision-Language Models

**Korean Title:** 의료 비전-언어 모델을 위한 보정 인식 프롬프트 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|angular separation loss]]
**🔗 Specific Connectable**: [[keywords/Multi-Modal Learning|Medical Vision-Language Models]], [[keywords/Uncertainty Quantification|confidence calibration]]

## 🔗 유사한 논문
- [[MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (85.0% similar)
- [[An Empirical Study of Federated Prompt Learning for Vision Language Model_20250919|An Empirical Study of Federated Prompt Learning for Vision Language Model]] (81.3% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (81.1% similar)
- [[PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (80.6% similar)
- [[Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15226v1 Announce Type: new 
Abstract: Medical Vision-Language Models (Med-VLMs) have demonstrated remarkable performance across diverse medical imaging tasks by leveraging large-scale image-text pretraining. However, their confidence calibration is largely unexplored, and so remains a significant challenge. As such, miscalibrated predictions can lead to overconfident errors, undermining clinical trust and decision-making reliability. To address this, we introduce CalibPrompt, the first framework to calibrate Med-VLMs during prompt tuning. CalibPrompt optimizes a small set of learnable prompts with carefully designed calibration objectives under scarce labeled data regime. First, we study a regularizer that attempts to align the smoothed accuracy with the predicted model confidences. Second, we introduce an angular separation loss to maximize textual feature proximity toward improving the reliability in confidence estimates of multimodal Med-VLMs. Extensive experiments on four publicly available Med-VLMs and five diverse medical imaging datasets reveal that CalibPrompt consistently improves calibration without drastically affecting clean accuracy. Our code is available at https://github.com/iabh1shekbasu/CalibPrompt.

## 🔍 Abstract (한글 번역)

arXiv:2509.15226v1 발표 유형: 신규  
초록: 의료 비전-언어 모델(Med-VLMs)은 대규모 이미지-텍스트 사전 학습을 활용하여 다양한 의료 영상 작업에서 뛰어난 성능을 보여주었습니다. 그러나 이들의 신뢰도 보정은 거의 탐구되지 않았으며, 여전히 중요한 과제로 남아 있습니다. 따라서 잘못 보정된 예측은 과도한 자신감의 오류를 초래하여 임상 신뢰와 의사 결정의 신뢰성을 저해할 수 있습니다. 이를 해결하기 위해, 우리는 프롬프트 튜닝 동안 Med-VLMs를 보정하는 최초의 프레임워크인 CalibPrompt를 소개합니다. CalibPrompt는 제한된 라벨 데이터 환경에서 신중하게 설계된 보정 목표를 통해 학습 가능한 프롬프트의 작은 집합을 최적화합니다. 첫째, 우리는 예측된 모델의 신뢰도와 부드러운 정확도를 맞추려는 정규화 기법을 연구합니다. 둘째, 다중 모달 Med-VLMs의 신뢰도 추정의 신뢰성을 향상시키기 위해 텍스트 특징의 근접성을 최대화하는 각도 분리 손실을 도입합니다. 네 가지 공개적으로 이용 가능한 Med-VLMs와 다섯 가지 다양한 의료 영상 데이터셋에 대한 광범위한 실험을 통해 CalibPrompt가 깨끗한 정확도에 큰 영향을 미치지 않으면서도 일관되게 보정을 개선함을 보여줍니다. 우리의 코드는 https://github.com/iabh1shekbasu/CalibPrompt에서 이용할 수 있습니다.

## 📝 요약

Med-VLMs는 대규모 이미지-텍스트 사전 학습을 통해 다양한 의료 영상 작업에서 뛰어난 성능을 보였지만, 신뢰도 보정은 거의 탐구되지 않았습니다. 이러한 문제를 해결하기 위해, 우리는 CalibPrompt라는 프레임워크를 도입하여 프롬프트 튜닝 중 Med-VLMs를 보정합니다. CalibPrompt는 제한된 라벨 데이터 환경에서 학습 가능한 프롬프트를 최적화하며, 부드러운 정확도와 예측된 모델 신뢰도를 정렬하는 정규화 기법과 텍스트 특징의 근접성을 극대화하는 각도 분리 손실을 도입합니다. 네 가지 공개 Med-VLMs와 다섯 가지 의료 영상 데이터셋에 대한 실험 결과, CalibPrompt는 정확도를 크게 저하시키지 않으면서도 일관되게 보정을 향상시킵니다.

## 🎯 주요 포인트

- 1. 의료 비전-언어 모델(Med-VLMs)은 대규모 이미지-텍스트 사전 학습을 통해 다양한 의료 영상 작업에서 뛰어난 성능을 보여주고 있습니다.

- 2. Med-VLMs의 신뢰도 보정은 아직 충분히 탐구되지 않았으며, 이는 임상 신뢰성과 의사 결정의 신뢰성을 저해할 수 있는 중요한 문제로 남아 있습니다.

- 3. CalibPrompt는 프롬프트 튜닝 중 Med-VLMs를 보정하기 위한 최초의 프레임워크로, 제한된 라벨 데이터 환경에서 학습 가능한 프롬프트를 최적화하여 신뢰도 보정을 수행합니다.

- 4. CalibPrompt는 모델의 예측 신뢰도와 정확도를 조화시키는 정규화 기법과 다중 모달 Med-VLMs의 신뢰도 추정치를 개선하기 위한 각도 분리 손실을 도입합니다.

- 5. CalibPrompt는 네 가지 공개 Med-VLMs와 다섯 가지 다양한 의료 영상 데이터셋에서 실험을 통해 신뢰도 보정을 개선하면서도 정확성에 큰 영향을 미치지 않는다는 것을 입증했습니다.

---

*Generated on 2025-09-19 16:11:51*