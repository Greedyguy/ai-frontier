---
keywords:
  - Few-Shot Learning
  - Attention Mechanism
  - Cross-Modal Geometric Rectification
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14958
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:24:57.748324",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Attention Mechanism",
    "Cross-Modal Geometric Rectification"
  ],
  "rejected_keywords": [
    "Texture Amplification Module",
    "Base-Novel Discriminator"
  ],
  "similarity_scores": {
    "Few-Shot Learning": 0.82,
    "Attention Mechanism": 0.8,
    "Cross-Modal Geometric Rectification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification

**Korean Title:** 2D 렌즈를 통해 3D를 보다: 교차 모달 기하학적 보정을 통한 3D 소수 샷 클래스 증분 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|3D Few-Shot Class-Incremental Learning]], [[keywords/Attention Mechanism|Attention-Driven Geometric Fusion]]
**⚡ Unique Technical**: [[keywords/Cross-Modal Geometric Rectification|Cross-Modal Geometric Rectification]]

## 🔗 유사한 논문
- [[Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (82.5% similar)
- [[Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (81.3% similar)
- [[Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (81.1% similar)
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.9% similar)
- [[Generalizable Geometric Image Caption Synthesis_20250919|Generalizable Geometric Image Caption Synthesis]] (80.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14958v1 Announce Type: new 
Abstract: The rapid growth of 3D digital content necessitates expandable recognition systems for open-world scenarios. However, existing 3D class-incremental learning methods struggle under extreme data scarcity due to geometric misalignment and texture bias. While recent approaches integrate 3D data with 2D foundation models (e.g., CLIP), they suffer from semantic blurring caused by texture-biased projections and indiscriminate fusion of geometric-textural cues, leading to unstable decision prototypes and catastrophic forgetting. To address these issues, we propose Cross-Modal Geometric Rectification (CMGR), a framework that enhances 3D geometric fidelity by leveraging CLIP's hierarchical spatial semantics. Specifically, we introduce a Structure-Aware Geometric Rectification module that hierarchically aligns 3D part structures with CLIP's intermediate spatial priors through attention-driven geometric fusion. Additionally, a Texture Amplification Module synthesizes minimal yet discriminative textures to suppress noise and reinforce cross-modal consistency. To further stabilize incremental prototypes, we employ a Base-Novel Discriminator that isolates geometric variations. Extensive experiments demonstrate that our method significantly improves 3D few-shot class-incremental learning, achieving superior geometric coherence and robustness to texture bias across cross-domain and within-domain settings.

## 🔍 Abstract (한글 번역)

arXiv:2509.14958v1 발표 유형: 신규  
초록: 3D 디지털 콘텐츠의 급속한 성장은 개방형 세계 시나리오에 적합한 확장 가능한 인식 시스템을 필요로 합니다. 그러나 기존의 3D 클래스 증분 학습 방법은 기하학적 불일치와 텍스처 편향으로 인해 극단적인 데이터 부족 상황에서 어려움을 겪습니다. 최근 접근법들은 3D 데이터를 2D 기초 모델(예: CLIP)과 통합하지만, 텍스처 편향 투영과 기하학적-텍스처적 단서의 무차별적인 융합으로 인한 의미적 흐림 현상으로 인해 불안정한 결정 프로토타입과 치명적인 망각을 초래합니다. 이러한 문제를 해결하기 위해, 우리는 CLIP의 계층적 공간 의미를 활용하여 3D 기하학적 충실도를 향상시키는 프레임워크인 교차 모달 기하학적 보정(Cross-Modal Geometric Rectification, CMGR)을 제안합니다. 구체적으로, 우리는 주의 기반의 기하학적 융합을 통해 CLIP의 중간 공간 사전과 3D 부품 구조를 계층적으로 정렬하는 구조 인식 기하학적 보정 모듈을 도입합니다. 추가적으로, 텍스처 증폭 모듈은 최소한의 차별적 텍스처를 합성하여 노이즈를 억제하고 교차 모달 일관성을 강화합니다. 증분 프로토타입을 더욱 안정화하기 위해, 우리는 기하학적 변화를 분리하는 기본-신규 판별기를 사용합니다. 광범위한 실험을 통해 우리의 방법이 3D 소수 샷 클래스 증분 학습을 크게 개선하고, 교차 도메인 및 도메인 내 설정에서 기하학적 일관성과 텍스처 편향에 대한 강건성을 달성함을 입증합니다.

## 📝 요약

이 논문은 3D 디지털 콘텐츠의 급속한 성장에 대응하여 확장 가능한 인식 시스템을 제안합니다. 기존의 3D 클래스 증분 학습 방법은 데이터 부족 시 기하학적 불일치와 텍스처 편향으로 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 CLIP의 계층적 공간 의미를 활용한 Cross-Modal Geometric Rectification(CMGR) 프레임워크를 제안합니다. 이 프레임워크는 주의 기반의 기하학적 융합을 통해 3D 구조를 정렬하고, 최소한의 텍스처를 증폭하여 잡음을 억제합니다. 또한, Base-Novel Discriminator를 사용하여 기하학적 변화를 분리합니다. 실험 결과, 제안된 방법은 3D 소수 샷 클래스 증분 학습에서 기하학적 일관성과 텍스처 편향에 대한 강건성을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 3D 디지털 콘텐츠의 급속한 성장으로 인해 확장 가능한 인식 시스템이 필요하지만, 기존의 3D 클래스 증분 학습 방법은 데이터 부족 상황에서 어려움을 겪고 있습니다.

- 2. 최근 접근 방식은 3D 데이터를 2D 기반 모델과 통합하지만, 텍스처 편향 투영과 기하학적-텍스처적 단서의 무차별 결합으로 인해 의미적 흐림 문제가 발생합니다.

- 3. 제안된 Cross-Modal Geometric Rectification (CMGR) 프레임워크는 CLIP의 계층적 공간 의미를 활용하여 3D 기하학적 충실도를 향상시킵니다.

- 4. Structure-Aware Geometric Rectification 모듈은 주의 기반의 기하학적 융합을 통해 3D 부분 구조를 CLIP의 중간 공간 우선순위와 계층적으로 정렬합니다.

- 5. 제안된 방법은 3D few-shot 클래스 증분 학습에서 기하학적 일관성과 텍스처 편향에 대한 강건성을 크게 향상시킵니다.

---

*Generated on 2025-09-19 16:07:32*