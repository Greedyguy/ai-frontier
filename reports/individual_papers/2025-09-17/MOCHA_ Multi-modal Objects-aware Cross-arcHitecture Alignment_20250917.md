---
keywords:
  - MOCHA
  - Vision-Language Models
  - Few-Shot Learning
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:51:35.121509",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MOCHA",
    "Vision-Language Models",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [
    "Knowledge Distillation",
    "Object Detection"
  ],
  "similarity_scores": {
    "MOCHA": 0.85,
    "Vision-Language Models": 0.78,
    "Few-Shot Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment

**Korean Title:** MOCHA: 다중 모달 객체 인식 교차 아키텍처 정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|few-shot regimes]]
**⚡ Unique Technical**: [[keywords/MOCHA|MOCHA]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Models|vision-language teacher]]

## 🔗 유사한 논문
- [[Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (84.0% similar)
- [[Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (82.8% similar)
- [[VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (81.2% similar)
- [[Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.0% similar)
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.7% similar)

## 📋 저자 정보

**Authors:** Elena Camuffo, Francesco Barbato, Mete Ozay, Simone Milani, Umberto Michieli

## 📄 Abstract (원문)

We introduce MOCHA (Multi-modal Objects-aware Cross-arcHitecture Alignment),
a knowledge distillation approach that transfers region-level multimodal
semantics from a large vision-language teacher (e.g., LLaVa) into a lightweight
vision-only object detector student (e.g., YOLO). A translation module maps
student features into a joint space, where the training of the student and
translator is guided by a dual-objective loss that enforces both local
alignment and global relational consistency. Unlike prior approaches focused on
dense or global alignment, MOCHA operates at the object level, enabling
efficient transfer of semantics without modifying the teacher or requiring
textual input at inference. We validate our method across four personalized
detection benchmarks under few-shot regimes. Results show consistent gains over
baselines, with a +10.1 average score improvement. Despite its compact
architecture, MOCHA reaches performance on par with larger multimodal models,
proving its suitability for real-world deployment.

## 🔍 Abstract (한글 번역)

MOCHA(Multi-modal Objects-aware Cross-arcHitecture Alignment)를 소개합니다. 이는 대형 비전-언어 교사 모델(예: LLaVa)로부터 지역 수준의 다중 모달 의미를 경량 비전 전용 객체 탐지 학생 모델(예: YOLO)로 전이하는 지식 증류 접근법입니다. 번역 모듈은 학생 모델의 특징을 공동 공간으로 매핑하며, 학생 모델과 번역기의 학습은 지역 정렬과 전역 관계 일관성을 모두 강화하는 이중 목표 손실에 의해 안내됩니다. 이전의 밀집 또는 전역 정렬에 중점을 둔 접근법과 달리, MOCHA는 객체 수준에서 작동하여 교사를 수정하거나 추론 시 텍스트 입력을 요구하지 않고도 효율적인 의미 전이를 가능하게 합니다. 우리는 소수 샷 체제 하에서 네 가지 개인화된 탐지 벤치마크를 통해 우리의 방법을 검증했습니다. 결과는 기준선 대비 일관된 향상을 보여주며, 평균 점수가 +10.1 증가했습니다. MOCHA는 컴팩트한 아키텍처에도 불구하고, 더 큰 다중 모달 모델과 동등한 성능을 발휘하여 실제 환경에서의 배포에 적합함을 입증합니다.

## 📝 요약

MOCHA는 대형 비전-언어 모델의 지역 수준 멀티모달 의미를 경량 비전 전용 객체 탐지 모델로 전이하는 지식 증류 기법입니다. 학생 모델의 특징을 공동 공간으로 매핑하여 지역 정렬과 전역 관계 일관성을 동시에 유지하는 이중 목표 손실을 통해 학습을 진행합니다. 기존 방법과 달리 객체 수준에서 의미를 효율적으로 전이하며, 교사 모델 수정이나 추론 시 텍스트 입력이 필요하지 않습니다. 네 가지 개인화된 탐지 벤치마크에서 MOCHA는 기존 방법 대비 평균 10.1점 향상된 성능을 보였으며, 컴팩트한 구조임에도 대형 멀티모달 모델과 유사한 성능을 발휘하여 실제 적용에 적합함을 입증했습니다.

## 🎯 주요 포인트

- 1. MOCHA는 대형 비전-언어 모델의 지역 수준 멀티모달 의미를 경량 비전 전용 객체 탐지 모델로 전이하는 지식 증류 접근법입니다.

- 2. 학생 모델과 번역 모듈은 지역 정렬과 전역 관계 일관성을 동시에 강화하는 이중 목표 손실을 통해 훈련됩니다.

- 3. MOCHA는 객체 수준에서 작동하여 교사 모델을 수정하거나 추론 시 텍스트 입력이 필요하지 않으면서도 효율적인 의미 전이를 가능하게 합니다.

- 4. 네 가지 맞춤형 탐지 벤치마크에서 MOCHA는 기존 모델 대비 평균 10.1점 향상된 성능을 보여주었습니다.

- 5. MOCHA는 컴팩트한 구조에도 불구하고 대형 멀티모달 모델과 동등한 성능을 발휘하여 실제 환경에서의 적합성을 입증합니다.

---

*Generated on 2025-09-20 09:20:01*