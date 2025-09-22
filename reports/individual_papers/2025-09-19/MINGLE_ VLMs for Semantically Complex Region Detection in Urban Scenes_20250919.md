
# MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes

**Korean Title:** MINGLE: 도시 장면에서 의미적으로 복잡한 영역 감지를 위한 VLMs

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision Language Models

## 🔗 유사한 논문
- [[From Pixels to Urban Policy-Intelligence Recovering Legacy Effects of Redlining with a Multimodal LLM]] (79.0% similar)
- [[Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (77.7% similar)
- [[Re-purposing SAM into Efficient Visual Projectors for MLLM-Based Referring Image Segmentation]] (77.5% similar)
- [[V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (77.5% similar)
- [[Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (77.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13484v2 Announce Type: replace 
Abstract: Understanding group-level social interactions in public spaces is crucial for urban planning, informing the design of socially vibrant and inclusive environments. Detecting such interactions from images involves interpreting subtle visual cues such as relations, proximity, and co-movement - semantically complex signals that go beyond traditional object detection. To address this challenge, we introduce a social group region detection task, which requires inferring and spatially grounding visual regions defined by abstract interpersonal relations. We propose MINGLE (Modeling INterpersonal Group-Level Engagement), a modular three-stage pipeline that integrates: (1) off-the-shelf human detection and depth estimation, (2) VLM-based reasoning to classify pairwise social affiliation, and (3) a lightweight spatial aggregation algorithm to localize socially connected groups. To support this task and encourage future research, we present a new dataset of 100K urban street-view images annotated with bounding boxes and labels for both individuals and socially interacting groups. The annotations combine human-created labels and outputs from the MINGLE pipeline, ensuring semantic richness and broad coverage of real-world scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.13484v2 발표 유형: 교체  
초록: 공공장소에서의 그룹 수준의 사회적 상호작용을 이해하는 것은 사회적으로 활기차고 포용적인 환경을 설계하는 데 중요한 도시 계획에 필수적입니다. 이미지에서 이러한 상호작용을 감지하는 것은 관계, 근접성, 공동 이동과 같은 미묘한 시각적 단서를 해석하는 것을 포함하며, 이는 전통적인 객체 감지를 넘어서는 의미적으로 복잡한 신호입니다. 이 문제를 해결하기 위해, 우리는 추상적인 대인 관계로 정의된 시각적 영역을 추론하고 공간적으로 구체화하는 것을 요구하는 사회적 그룹 영역 감지 작업을 소개합니다. 우리는 MINGLE(Modeling INterpersonal Group-Level Engagement)이라는 모듈식 3단계 파이프라인을 제안하며, 이는 다음을 통합합니다: (1) 기성품 인간 감지 및 깊이 추정, (2) VLM 기반 추론을 통한 쌍별 사회적 소속 분류, (3) 사회적으로 연결된 그룹을 지역화하기 위한 경량의 공간 집계 알고리즘. 이 작업을 지원하고 향후 연구를 장려하기 위해, 우리는 개인과 사회적 상호작용 그룹 모두에 대한 경계 상자와 레이블로 주석이 달린 10만 개의 도시 거리 뷰 이미지로 구성된 새로운 데이터셋을 제공합니다. 이 주석은 인간이 만든 레이블과 MINGLE 파이프라인의 출력을 결합하여 의미적 풍부함과 실제 시나리오의 광범위한 적용 범위를 보장합니다.

## 📝 요약

이 논문은 공공장소에서의 그룹 수준 사회적 상호작용을 이해하는 것이 도시 계획에 중요하다는 점을 강조합니다. 이를 위해 이미지에서 미묘한 시각적 신호를 해석하는 새로운 과제인 '사회적 그룹 영역 탐지'를 제안합니다. 이를 해결하기 위해 MINGLE이라는 모듈형 3단계 파이프라인을 소개합니다. MINGLE은 (1) 기존의 인간 탐지 및 깊이 추정, (2) VLM 기반의 추론을 통한 쌍방향 사회적 관계 분류, (3) 경량의 공간 집계 알고리즘을 통한 사회적으로 연결된 그룹의 위치 파악을 통합합니다. 또한, 10만 개의 도시 거리 이미지 데이터셋을 새롭게 제공하여, 개인 및 사회적 상호작용 그룹에 대한 주석을 포함하고 있어 실제 시나리오에 대한 폭넓은 적용 가능성을 보장합니다.

## 🎯 주요 포인트

- 1. 공공장소에서의 그룹 수준 사회적 상호작용 이해는 도시 계획에 필수적이며, 사회적으로 활기차고 포용적인 환경 설계에 기여한다.

- 2. 이미지에서 이러한 상호작용을 감지하는 것은 전통적인 객체 탐지를 넘어 관계, 근접성, 공동 이동과 같은 미묘한 시각적 신호를 해석하는 것을 포함한다.

- 3. MINGLE은 인간 탐지 및 깊이 추정, VLM 기반의 사회적 관계 분류, 경량 공간 집계 알고리즘을 통합하여 사회적 그룹을 감지하는 모듈형 파이프라인이다.

- 4. 10만 개의 도시 거리 이미지 데이터셋은 개인과 사회적 상호작용 그룹에 대한 경계 상자와 레이블로 주석이 달려 있으며, 이는 MINGLE 파이프라인의 출력과 인간이 생성한 레이블을 결합하여 실세계 시나리오를 포괄한다.

---

*Generated on 2025-09-19 16:19:31*