---
keywords:
  - Vision-Language Models
  - Multimodal Driver Attention Fusion
  - Attention Mechanism
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2502.18042
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:18:34.546321",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Models",
    "Multimodal Driver Attention Fusion",
    "Attention Mechanism"
  ],
  "rejected_keywords": [
    "Bird's-Eye-View"
  ],
  "similarity_scores": {
    "Vision-Language Models": 0.88,
    "Multimodal Driver Attention Fusion": 0.85,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# VLM-E2E: Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion

**Korean Title:** VLM-E2E: 다중 모달 운전자 주의 융합을 통한 종단 간 자율 주행 향상

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Multimodal Driver Attention Fusion|Multimodal Driver Attention Fusion]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Models|Vision-Language Models]]

## 🔗 유사한 논문
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (82.1% similar)
- [[BEVUDA++ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (82.1% similar)
- [[VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (81.8% similar)
- [[Embodied_Navigation_Foundation_Model_20250918|Embodied Navigation Foundation Model]] (81.3% similar)
- [[FishBEV Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.18042v2 Announce Type: replace-cross 
Abstract: Human drivers adeptly navigate complex scenarios by utilizing rich attentional semantics, but the current autonomous systems struggle to replicate this ability, as they often lose critical semantic information when converting 2D observations into 3D space. In this sense, it hinders their effective deployment in dynamic and complex environments. Leveraging the superior scene understanding and reasoning abilities of Vision-Language Models (VLMs), we propose VLM-E2E, a novel framework that uses the VLMs to enhance training by providing attentional cues. Our method integrates textual representations into Bird's-Eye-View (BEV) features for semantic supervision, which enables the model to learn richer feature representations that explicitly capture the driver's attentional semantics. By focusing on attentional semantics, VLM-E2E better aligns with human-like driving behavior, which is critical for navigating dynamic and complex environments. Furthermore, we introduce a BEV-Text learnable weighted fusion strategy to address the issue of modality importance imbalance in fusing multimodal information. This approach dynamically balances the contributions of BEV and text features, ensuring that the complementary information from visual and textual modalities is effectively utilized. By explicitly addressing the imbalance in multimodal fusion, our method facilitates a more holistic and robust representation of driving environments. We evaluate VLM-E2E on the nuScenes dataset and achieve significant improvements in perception, prediction, and planning over the baseline end-to-end model, showcasing the effectiveness of our attention-enhanced BEV representation in enabling more accurate and reliable autonomous driving tasks.

## 🔍 Abstract (한글 번역)

arXiv:2502.18042v2 발표 유형: 교차 교체  
초록: 인간 운전자는 풍부한 주의 의미를 활용하여 복잡한 상황을 능숙하게 탐색하지만, 현재의 자율 시스템은 2D 관찰을 3D 공간으로 변환할 때 중요한 의미 정보를 종종 잃어버리기 때문에 이 능력을 복제하는 데 어려움을 겪습니다. 이러한 점에서 이는 동적이고 복잡한 환경에서의 효과적인 배치를 방해합니다. Vision-Language Models (VLMs)의 뛰어난 장면 이해 및 추론 능력을 활용하여, 우리는 VLM-E2E라는 새로운 프레임워크를 제안합니다. 이는 VLMs를 사용하여 주의 단서를 제공함으로써 훈련을 향상시킵니다. 우리의 방법은 텍스트 표현을 Bird's-Eye-View (BEV) 특징에 통합하여 의미론적 감독을 가능하게 하며, 이를 통해 모델이 운전자의 주의 의미를 명시적으로 포착하는 더 풍부한 특징 표현을 학습할 수 있게 합니다. 주의 의미에 집중함으로써, VLM-E2E는 동적이고 복잡한 환경을 탐색하는 데 중요한 인간과 유사한 운전 행동과 더 잘 일치합니다. 또한, 우리는 다중 모달 정보 융합에서 모달리티 중요성 불균형 문제를 해결하기 위해 BEV-텍스트 학습 가능한 가중치 융합 전략을 도입합니다. 이 접근 방식은 BEV 및 텍스트 특징의 기여를 동적으로 균형 잡아, 시각 및 텍스트 모달리티의 보완적 정보를 효과적으로 활용할 수 있도록 합니다. 다중 모달 융합의 불균형을 명시적으로 해결함으로써, 우리의 방법은 운전 환경의 보다 전체적이고 견고한 표현을 촉진합니다. 우리는 nuScenes 데이터셋에서 VLM-E2E를 평가하고, 인식, 예측 및 계획에서 기본적인 종단 간 모델에 비해 상당한 개선을 달성하여, 주의 강화된 BEV 표현이 보다 정확하고 신뢰할 수 있는 자율 주행 작업을 가능하게 하는 효과를 입증합니다.

## 📝 요약

이 논문은 자율주행 시스템이 인간 운전자의 주의력 기반 운전 행동을 모방하기 어려운 문제를 해결하기 위해 VLM-E2E라는 새로운 프레임워크를 제안합니다. Vision-Language Models(VLMs)의 장점을 활용하여 주의력 단서를 제공함으로써 모델이 운전자의 주의력 의미를 포착하는 풍부한 특징 표현을 학습하도록 돕습니다. 또한, BEV-Text 가중치 융합 전략을 도입하여 시각 및 텍스트 모달리티의 중요성 불균형 문제를 해결하고, 이를 통해 운전 환경의 더 포괄적이고 강력한 표현을 가능하게 합니다. nuScenes 데이터셋을 통해 평가한 결과, 인식, 예측 및 계획에서 기존 모델보다 성능이 크게 향상되었음을 보여줍니다.

## 🎯 주요 포인트

- 1. VLM-E2E는 Vision-Language Models(VLMs)를 활용하여 운전자의 주의 의미를 학습하고, 복잡한 환경에서 인간과 유사한 운전 행동을 구현합니다.

- 2. Bird's-Eye-View(BEV) 특징에 텍스트 표현을 통합하여 의미적 감독을 제공함으로써, 모델이 운전자의 주의 의미를 명시적으로 포착하는 풍부한 특징 표현을 학습하도록 합니다.

- 3. BEV-Text 학습 가능한 가중치 융합 전략을 도입하여, 시각 및 텍스트 모달리티의 중요성 불균형 문제를 해결하고, 멀티모달 정보의 상호보완적 활용을 극대화합니다.

- 4. VLM-E2E는 nuScenes 데이터셋에서 평가되어, 인식, 예측, 계획 측면에서 기존의 엔드투엔드 모델보다 유의미한 성능 향상을 보여줍니다.

---

*Generated on 2025-09-19 15:12:19*