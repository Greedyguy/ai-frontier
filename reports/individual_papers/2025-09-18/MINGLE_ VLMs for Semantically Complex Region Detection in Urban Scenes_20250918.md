---
keywords:
  - Social Group Region Detection
  - Vision-Language Models
  - Urban Street-View Images
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13484
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:20:22.086920",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Social Group Region Detection",
    "Vision-Language Models",
    "Urban Street-View Images"
  ],
  "rejected_keywords": [
    "Computer Vision",
    "Spatial Aggregation Algorithm"
  ],
  "similarity_scores": {
    "Social Group Region Detection": 0.78,
    "Vision-Language Models": 0.8,
    "Urban Street-View Images": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes

**Korean Title:** MINGLE: 도시 장면에서 의미론적으로 복잡한 지역 감지를 위한 VLMs

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision-Language Models|Vision-Language Models]]
**⚡ Unique Technical**: [[keywords/Social Group Region Detection|social group region detection]], [[keywords/Urban Street-View Images|urban street-view images]]

## 🔗 유사한 논문
- [[Semi-MoE_Mixture-of-Experts_meets_Semi-Supervised_Histopathology_Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (77.7% similar)
- [[Re-purposing SAM into Efficient Visual Projectors for MLLM-Based Referring Image Segmentation]] (77.5% similar)
- [[Improving_Generalized_Visual_Grounding_with_Instance-aware_Joint_Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (77.2% similar)
- [[Semantic-Enhanced_Cross-Modal_Place_Recognition_for_Robust_Robot_Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (76.8% similar)
- [[VSE-MOT_Multi-Object_Tracking_in_Low-Quality_Video_Scenes_Guided_by_Visual_Semantic_Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (76.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13484v1 Announce Type: new 
Abstract: Understanding group-level social interactions in public spaces is crucial for urban planning, informing the design of socially vibrant and inclusive environments. Detecting such interactions from images involves interpreting subtle visual cues such as relations, proximity, and co-movement - semantically complex signals that go beyond traditional object detection. To address this challenge, we introduce a social group region detection task, which requires inferring and spatially grounding visual regions defined by abstract interpersonal relations. We propose MINGLE (Modeling INterpersonal Group-Level Engagement), a modular three-stage pipeline that integrates: (1) off-the-shelf human detection and depth estimation, (2) VLM-based reasoning to classify pairwise social affiliation, and (3) a lightweight spatial aggregation algorithm to localize socially connected groups. To support this task and encourage future research, we present a new dataset of 100K urban street-view images annotated with bounding boxes and labels for both individuals and socially interacting groups. The annotations combine human-created labels and outputs from the MINGLE pipeline, ensuring semantic richness and broad coverage of real-world scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.13484v1 발표 유형: 새로운
요약: 공공 공간에서의 집단 수준의 사회적 상호작용을 이해하는 것은 도시 계획에 중요하며, 사회적 활발하고 포용적인 환경의 설계에 정보를 제공합니다. 이미지에서 이러한 상호작용을 감지하는 것은 관계, 근접성 및 공동 이동과 같은 섬세한 시각적 단서를 해석하는 것을 포함하며, 이는 전통적인 객체 감지를 넘어서는 의미론적으로 복잡한 신호입니다. 이러한 도전에 대처하기 위해, 우리는 추상적인 대인적 관계에 의해 정의된 시각적 영역을 추론하고 공간적으로 기반을 둔 사회적 그룹 영역 감지 작업을 소개합니다. 우리는 MINGLE (Modeling INterpersonal Group-Level Engagement)이라는 모듈식 세 단계 파이프라인을 제안합니다. 이는 (1) 오프더셀프 인간 감지 및 깊이 추정, (2) VLM 기반 추론을 통한 쌍별 사회적 소속 분류, (3) 가벼운 공간 집계 알고리즘을 통해 사회적으로 연결된 그룹을 지역화합니다. 이 작업을 지원하고 향후 연구를 촉진하기 위해, 우리는 10만 개의 도시 거리 전경 이미지 데이터셋을 제시합니다. 이 데이터셋은 개인과 사회적 상호작용 그룹 모두에 대한 바운딩 박스와 레이블이 주석이 달려 있습니다. 이 주석은 인간이 작성한 레이블과 MINGLE 파이프라인의 출력을 결합하여 의미론적 풍부함과 현실 세계 시나리오의 넓은 범위를 보장합니다.

## 📝 요약

이 연구는 공공 공간에서의 집단적 사회 상호작용을 이해하는 것이 도시 계획에 중요하며 사회적 활발하고 포용적인 환경을 설계하는 데 도움이 된다는 점을 강조한다. 이미지에서 이러한 상호작용을 감지하는 것은 관계, 근접성 및 공동 이동과 같은 세밀한 시각적 단서를 해석하는 것을 포함하며 전통적인 객체 감지를 넘어선 의미론적으로 복잡한 신호이다. 이 연구에서는 사회적 집단 영역 감지 작업을 소개하며 추상적인 대인적 관계로 정의된 시각적 영역을 추론하고 공간적으로 기준을 제시하는 것을 요구한다. 이를 위해 우리는 MINGLE (Modeling INterpersonal Group-Level Engagement)이라는 모듈화된 세 단계 파이프라인을 제안한다. 이 연구를 지원하고 향후 연구를 촉진하기 위해 10만 개의 도시 거리 사진으로 구성된 새로운 데이터셋을 제시한다.

## 🎯 주요 포인트

- 1. 공공 공간에서의 집단적 사회 상호작용을 이해하는 것은 도시 계획에 중요하다.

- 2. 이미지에서의 사회적 그룹 영역 감지 작업을 소개한다.

- 3. MINGLE은 사회적 연결 그룹을 지역화하기 위한 경량화된 공간 집계 알고리즘을 제안한다.

---

*Generated on 2025-09-18 16:58:36*