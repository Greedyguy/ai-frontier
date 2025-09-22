
# SPATIALGEN: Layout-guided 3D Indoor Scene Generation

**Korean Title:** SPATIALGEN: 레이아웃 기반 3D 실내 장면 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Layout-guided Scene Generation

## 🔗 유사한 논문
- [[Evolution Meets Diffusion Efficient Neural Architecture Generation]] (80.3% similar)
- [[Imagined Autocurricula]] (80.2% similar)
- [[Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.1% similar)
- [[StyleSculptor Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance]] (80.0% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14981v1 Announce Type: new 
Abstract: Creating high-fidelity 3D models of indoor environments is essential for applications in design, virtual reality, and robotics. However, manual 3D modeling remains time-consuming and labor-intensive. While recent advances in generative AI have enabled automated scene synthesis, existing methods often face challenges in balancing visual quality, diversity, semantic consistency, and user control. A major bottleneck is the lack of a large-scale, high-quality dataset tailored to this task. To address this gap, we introduce a comprehensive synthetic dataset, featuring 12,328 structured annotated scenes with 57,440 rooms, and 4.7M photorealistic 2D renderings. Leveraging this dataset, we present SpatialGen, a novel multi-view multi-modal diffusion model that generates realistic and semantically consistent 3D indoor scenes. Given a 3D layout and a reference image (derived from a text prompt), our model synthesizes appearance (color image), geometry (scene coordinate map), and semantic (semantic segmentation map) from arbitrary viewpoints, while preserving spatial consistency across modalities. SpatialGen consistently generates superior results to previous methods in our experiments. We are open-sourcing our data and models to empower the community and advance the field of indoor scene understanding and generation.

## 🔍 Abstract (한글 번역)

arXiv:2509.14981v1 발표 유형: 신규  
초록: 실내 환경의 고충실도 3D 모델을 만드는 것은 디자인, 가상 현실, 로봇 공학 분야의 응용에 필수적입니다. 그러나 수동 3D 모델링은 여전히 시간이 많이 걸리고 노동 집약적입니다. 최근 생성형 AI의 발전으로 자동 장면 합성이 가능해졌지만, 기존 방법들은 시각적 품질, 다양성, 의미론적 일관성, 사용자 제어 간의 균형을 맞추는 데 어려움을 겪고 있습니다. 주요 병목 현상은 이 작업에 맞춘 대규모 고품질 데이터셋의 부족입니다. 이 격차를 해소하기 위해, 우리는 12,328개의 구조화된 주석이 달린 장면과 57,440개의 방, 그리고 470만 개의 사진 실사 2D 렌더링을 특징으로 하는 포괄적인 합성 데이터셋을 소개합니다. 이 데이터셋을 활용하여, 우리는 현실적이고 의미론적으로 일관된 3D 실내 장면을 생성하는 새로운 다중 뷰 다중 모달 확산 모델인 SpatialGen을 제시합니다. 3D 레이아웃과 참조 이미지(텍스트 프롬프트에서 파생된)를 주어지면, 우리의 모델은 임의의 관점에서 외관(컬러 이미지), 기하학(장면 좌표 맵), 의미론적(의미론적 분할 맵)을 합성하며, 모달리티 간의 공간적 일관성을 유지합니다. SpatialGen은 우리의 실험에서 이전 방법들보다 일관되게 우수한 결과를 생성합니다. 우리는 실내 장면 이해 및 생성 분야를 발전시키고 커뮤니티를 지원하기 위해 우리의 데이터와 모델을 오픈 소스로 공개하고 있습니다.

## 📝 요약

이 논문은 실내 환경의 고품질 3D 모델 생성을 위한 새로운 접근법을 제시합니다. 기존의 자동 장면 생성 방법은 시각적 품질, 다양성, 의미적 일관성, 사용자 제어 간의 균형을 맞추는 데 어려움을 겪고 있습니다. 이를 해결하기 위해, 12,328개의 주석이 달린 장면과 57,440개의 방, 470만 개의 사실적인 2D 렌더링을 포함한 대규모 합성 데이터셋을 소개합니다. 이 데이터셋을 활용하여, SpatialGen이라는 새로운 다중 뷰 다중 모달 확산 모델을 개발하였습니다. 이 모델은 3D 레이아웃과 참조 이미지를 기반으로, 다양한 관점에서 실내 장면의 색상 이미지, 장면 좌표 지도, 의미적 분할 지도를 생성하며, 공간적 일관성을 유지합니다. 실험 결과, SpatialGen은 기존 방법들보다 우수한 결과를 보여주었으며, 데이터와 모델을 공개하여 실내 장면 이해 및 생성 분야의 발전을 도모하고자 합니다.

## 🎯 주요 포인트

- 1. 실내 환경의 고품질 3D 모델 생성은 디자인, 가상 현실, 로봇 공학에 필수적이다.

- 2. 기존의 자동 장면 합성 방법은 시각적 품질, 다양성, 의미적 일관성, 사용자 제어 간의 균형을 맞추는 데 어려움을 겪고 있다.

- 3. 이 문제를 해결하기 위해 12,328개의 구조화된 주석 장면과 57,440개의 방, 470만 개의 사실적인 2D 렌더링을 포함한 종합적인 합성 데이터셋을 소개한다.

- 4. SpatialGen은 다중 뷰 다중 모달 확산 모델로, 현실적이고 의미적으로 일관된 3D 실내 장면을 생성한다.

- 5. 데이터와 모델을 오픈 소스로 제공하여 실내 장면 이해 및 생성 분야의 발전을 도모한다.

---

*Generated on 2025-09-19 16:08:27*