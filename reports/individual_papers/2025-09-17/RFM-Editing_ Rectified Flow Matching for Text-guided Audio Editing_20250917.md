---
keywords:
  - Diffusion Models
  - Text-guided Audio Editing
  - Rectified Flow Matching
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:46:43.212995",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Text-guided Audio Editing",
    "Rectified Flow Matching"
  ],
  "rejected_keywords": [
    "Generative Models"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.8,
    "Text-guided Audio Editing": 0.78,
    "Rectified Flow Matching": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# RFM-Editing: Rectified Flow Matching for Text-guided Audio Editing

**Korean Title:** RFM-편집: 텍스트 기반 오디오 편집을 위한 수정된 흐름 매칭

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion models]]
**⚡ Unique Technical**: [[keywords/Text-guided Audio Editing|Text-guided audio editing]], [[keywords/Rectified Flow Matching|Rectified flow matching]]

## 🔗 유사한 논문
- [[Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (82.4% similar)
- [[Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (80.9% similar)
- [[Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (80.5% similar)
- [[DPDEdit_ Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing_20250918|DPDEdit Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing]] (80.1% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (79.9% similar)

## 📋 저자 정보

**Authors:** Liting Gao, Yi Yuan, Yaru Chen, Yuelan Cheng, Zhenbo Li, Juan Wen, Shubin Zhang, Wenwu Wang

## 📄 Abstract (원문)

Diffusion models have shown remarkable progress in text-to-audio generation.
However, text-guided audio editing remains in its early stages. This task
focuses on modifying the target content within an audio signal while preserving
the rest, thus demanding precise localization and faithful editing according to
the text prompt. Existing training-based and zero-shot methods that rely on
full-caption or costly optimization often struggle with complex editing or lack
practicality. In this work, we propose a novel end-to-end efficient rectified
flow matching-based diffusion framework for audio editing, and construct a
dataset featuring overlapping multi-event audio to support training and
benchmarking in complex scenarios. Experiments show that our model achieves
faithful semantic alignment without requiring auxiliary captions or masks,
while maintaining competitive editing quality across metrics.

## 🔍 Abstract (한글 번역)

확산 모델은 텍스트-오디오 생성에서 놀라운 발전을 보여주었습니다. 그러나 텍스트 기반 오디오 편집은 아직 초기 단계에 머물러 있습니다. 이 작업은 오디오 신호 내의 목표 콘텐츠를 수정하면서 나머지는 보존하는 데 중점을 두며, 따라서 텍스트 프롬프트에 따라 정확한 위치 지정과 충실한 편집을 요구합니다. 전체 캡션이나 비용이 많이 드는 최적화에 의존하는 기존의 학습 기반 및 제로샷 방법은 복잡한 편집에서 종종 어려움을 겪거나 실용성이 부족합니다. 본 연구에서는 오디오 편집을 위한 새로운 엔드 투 엔드 효율적인 수정된 흐름 매칭 기반 확산 프레임워크를 제안하고, 복잡한 시나리오에서의 학습 및 벤치마킹을 지원하기 위해 중첩된 다중 이벤트 오디오를 특징으로 하는 데이터셋을 구축합니다. 실험 결과, 우리의 모델은 보조 캡션이나 마스크 없이도 충실한 의미적 정렬을 달성하며, 다양한 지표에서 경쟁력 있는 편집 품질을 유지함을 보여줍니다.

## 📝 요약

이 논문은 텍스트 기반 오디오 편집을 위한 새로운 확산 모델을 제안합니다. 기존 방법들이 복잡한 편집에 어려움을 겪는 반면, 제안된 모델은 효율적인 정류 흐름 매칭 기반의 확산 프레임워크를 사용하여 오디오 신호 내에서 목표 콘텐츠를 정확히 수정하면서 나머지를 보존합니다. 또한, 중첩된 다중 이벤트 오디오 데이터셋을 구축하여 복잡한 시나리오에서의 훈련과 벤치마킹을 지원합니다. 실험 결과, 보조 캡션이나 마스크 없이도 의미 정렬을 충실히 수행하며, 다양한 지표에서 경쟁력 있는 편집 품질을 유지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 텍스트 기반 오디오 편집은 초기 단계에 있으며, 정확한 위치 지정과 텍스트 프롬프트에 따른 충실한 편집이 요구된다.

- 2. 기존 방법들은 복잡한 편집에서 어려움을 겪거나 실용성이 부족하다.

- 3. 본 연구는 오디오 편집을 위한 새로운 효율적인 정류 흐름 매칭 기반 확산 프레임워크를 제안한다.

- 4. 중첩된 다중 이벤트 오디오를 포함하는 데이터셋을 구축하여 복잡한 시나리오에서의 훈련 및 벤치마킹을 지원한다.

- 5. 제안된 모델은 보조 캡션이나 마스크 없이도 충실한 의미 정렬을 달성하면서 경쟁력 있는 편집 품질을 유지한다.

---

*Generated on 2025-09-20 09:19:39*