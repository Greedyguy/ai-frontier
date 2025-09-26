---
keywords:
  - Multi-Modal Learning
  - Multi-Modal Learning
  - Self-Supervised Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14097
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:06:13.247019",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Multi-Modal Learning",
    "Self-Supervised Learning"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.79,
    "Self-Supervised Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing

**Korean Title:** 교사 지도를 통한 가짜 감독 및 오디오-비주얼 비디오 파싱을 위한 교차 모달 정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-Supervised Learning|class-aware cross-modal agreement]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|audio-visual video parsing]], [[keywords/Multi-Modal Learning|cross-modal alignment]]

## 🔗 유사한 논문
- [[VocSegMRI: Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (81.7% similar)
- [[VSE-MOT_Multi-Object_Tracking_in_Low-Quality_Video_Scenes_Guided_by_Visual_Semantic_Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (81.1% similar)
- [[Omni-CLST_Error-aware_Curriculum_Learning_with_guided_Selective_chain-of-Thought_for_audio_question_answering_20250919|Omni-CLST: Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (80.8% similar)
- [[Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (79.4% similar)
- [[MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (78.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14097v1 Announce Type: new 
Abstract: Weakly-supervised audio-visual video parsing (AVVP) seeks to detect audible, visible, and audio-visual events without temporal annotations. Previous work has emphasized refining global predictions through contrastive or collaborative learning, but neglected stable segment-level supervision and class-aware cross-modal alignment. To address this, we propose two strategies: (1) an exponential moving average (EMA)-guided pseudo supervision framework that generates reliable segment-level masks via adaptive thresholds or top-k selection, offering stable temporal guidance beyond video-level labels; and (2) a class-aware cross-modal agreement (CMA) loss that aligns audio and visual embeddings at reliable segment-class pairs, ensuring consistency across modalities while preserving temporal structure. Evaluations on LLP and UnAV-100 datasets shows that our method achieves state-of-the-art (SOTA) performance across multiple metrics.

## 🔍 Abstract (한글 번역)

arXiv:2509.14097v1 발표 유형: 새로운
요약: 약하게 지도된 오디오-시각적 비디오 구문 분석 (AVVP)은 시간 주석 없이 듣고 보이는 오디오-시각적 이벤트를 감지하려고 합니다. 이전 연구는 대조적이거나 협력적 학습을 통해 전역 예측을 개선하는 데 중점을 두었지만, 안정적인 세그먼트 수준 감독 및 클래스 인식 교차 모달 정렬을 무시했습니다. 이를 해결하기 위해 우리는 두 가지 전략을 제안합니다: (1) 지수 이동 평균 (EMA)로 안내된 가짜 감독 프레임워크는 적응 임계값 또는 상위 k 선택을 통해 안정적인 세그먼트 수준 마스크를 생성하여 비디오 수준 레이블 이상의 안정적인 시간적 안내를 제공합니다; 그리고 (2) 클래스 인식 교차 모달 일치 (CMA) 손실은 신뢰할 수 있는 세그먼트-클래스 쌍에서 오디오와 시각적 임베딩을 정렬하여 모달 간 일관성을 보장하면서 시간 구조를 보존합니다. LLP 및 UnAV-100 데이터셋에서의 평가 결과, 우리의 방법이 다중 메트릭을 통해 최첨단 성능을 달성한다는 것을 보여줍니다.

## 📝 요약

본 연구는 약한 지도 학습을 이용한 오디오-시각 비디오 구문 분석(AVVP)에 초점을 맞추고 있습니다. 이전 연구들은 대부분 대조적이거나 협력적 학습을 통해 전역 예측을 개선하는 데 중점을 두었지만, 안정적인 세그먼트 수준 감독 및 클래스에 대한 교차 모달 정렬을 간과했습니다. 이를 해결하기 위해 우리는 두 가지 전략을 제안합니다: (1) 지수 이동 평균 (EMA)으로 안정적인 세그먼트 수준 가짜 감독을 생성하고 안정적인 시간적 안내를 제공하는 프레임워크; (2) 신뢰할 수 있는 세그먼트-클래스 쌍에서 오디오와 시각 임베딩을 정렬하는 클래스에 대한 교차 모달 일치 (CMA) 손실. LLP 및 UnAV-100 데이터셋에서의 평가 결과, 우리의 방법은 다중 메트릭을 통해 최고 수준의 성능을 달성했습니다.

## 🎯 주요 포인트

- 비감독 오디오-비주얼 비디오 파싱에 안정적인 세그먼트 수퍼바이전을 제안함

- 클래스-인식 교차 모달 일치 손실을 통해 오디오와 비주얼 임베딩을 정렬

- LLP 및 UnAV-100 데이터셋에서 최고 수준의 성능을 달성함

---

*Generated on 2025-09-18 17:03:26*