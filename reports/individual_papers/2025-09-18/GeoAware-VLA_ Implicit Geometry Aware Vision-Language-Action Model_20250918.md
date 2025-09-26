---
keywords:
  - 3D Geometry
  - Zero-Shot Learning
  - Geometric Vision Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14117
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:26:40.764829",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Geometry",
    "Zero-Shot Learning",
    "Geometric Vision Models"
  ],
  "rejected_keywords": [
    "Vision-Language-Action Models",
    "Robotic Agents"
  ],
  "similarity_scores": {
    "3D Geometry": 0.82,
    "Zero-Shot Learning": 0.79,
    "Geometric Vision Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model

**Korean Title:** GeoAware-VLA: 암시적 기하 인식 비전-언어-행동 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/3D Geometry|3D geometry]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|zero-shot generalization]], [[keywords/Geometric Vision Models|geometric vision model]]

## 🔗 유사한 논문
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (86.1% similar)
- [[CLAW_A_Vision-Language-Action_Framework_for_Weight-Aware_Robotic_Grasping_20250918|CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (83.9% similar)
- [[Embodied_Navigation_Foundation_Model_20250918|Embodied Navigation Foundation Model]] (82.8% similar)
- [[TrajBooster_Boosting_Humanoid_Whole-Body_Manipulation_via_Trajectory-Centric_Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.7% similar)
- [[Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14117v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) models often fail to generalize to novel camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on LIBERO benchmark subsets, we show GeoAware-VLA achieves substantial improvements in zero-shot generalization to novel camera poses, boosting success rates by over 2x in simulation. Crucially, these benefits translate to the physical world; our model shows a significant performance gain on a real robot, especially when evaluated from unseen camera angles. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key component for creating more generalizable robotic agents.

## 🔍 Abstract (한글 번역)

arXiv:2509.14117v1 발표 유형: 새로운
요약: Vision-Language-Action (VLA) 모델은 종종 새로운 카메라 시점에 대한 일반화에 실패하는데, 이는 2D 이미지에서 강력한 3D 기하학을 추론하는 데 어려움을 겪기 때문입니다. 우리는 GeoAware-VLA를 소개합니다. 이는 강력한 기하학적 사전 지식을 시각 백본에 통합하여 시점 불변성을 향상시키는 간단하면서도 효과적인 방법입니다. 시각 인코더를 훈련하거나 명시적인 3D 데이터에 의존하는 대신, 우리는 얼어붙은, 사전 훈련된 기하학적 시각 모델을 특징 추출기로 활용합니다. 그런 다음 학습 가능한 투영 레이어가 이러한 기하학적으로 풍부한 특징을 정책 디코더에 적응시켜, 3D 일관성을 처음부터 배우는 부담을 덜어줍니다. LIBERO 벤치마크 하위 집합에서의 광범위한 평가를 통해, GeoAware-VLA가 시뮬레이션에서 새로운 카메라 위치에 대한 제로샷 일반화에서 큰 개선을 달성함을 보여줍니다. 이는 성공률을 2배 이상 향상시킵니다. 중요한 점은 이러한 이점이 물리적 세계로 이어지는데, 우리 모델은 실제 로봇에서 특히 보이지 않은 카메라 각도에서 평가될 때 상당한 성능 향상을 보여줍니다. 우리의 접근 방식은 연속적이고 이산적인 행동 공간 모두에서 효과적임을 강조하며, 견고한 기하학적 기반은 보다 일반화 가능한 로봇 에이전트를 만드는 데 중요한 구성 요소임을 강조합니다.

## 📝 요약

이 연구는 새로운 카메라 시점에 일반화하는 데 어려움을 겪는 Vision-Language-Action (VLA) 모델의 한계를 극복하기 위해 GeoAware-VLA를 제안한다. 이 방법은 강력한 기하학적 사전 지식을 시각 백본에 통합하여 시점 불변성을 향상시킨다. 기존의 기하학적 비전 모델을 특징 추출기로 활용하고, 학습 가능한 투영 계층을 통해 이러한 기하학적으로 풍부한 특징을 정책 디코더에 적응시킨다. LIBERO 벤치마크 하위 집합에서의 평가를 통해 GeoAware-VLA가 새로운 카메라 위치에 대한 제로샷 일반화 성능을 크게 향상시키는 것을 보여주었으며, 이는 시뮬레이션에서 성공률을 2배 이상 향상시켰다. 또한, 이 모델은 실제 로봇에서도 유의한 성능 향상을 보여주었으며, 특히 본 적 없는 카메라 각도에서 평가할 때 더 큰 효과를 보였다. 연속 및 이산 행동 공간에서 효과적인 것으로 나타나며, 견고한 기하학적 기반은 보다 일반화된 로봇 에이전트를 만드는 데 중요한 구성 요소임을 강조한다.

## 🎯 주요 포인트

- 1. GeoAware-VLA는 강력한 기하학적 사전 지식을 시각 백본에 통합하여 새로운 카메라 시점에 대한 일반화 능력을 향상시킵니다.

- 2. 기하학적으로 풍부한 특징을 활용하여 3D 일관성을 학습하는 부담을 줄이는 trainable projection layer를 도입합니다.

- 3. GeoAware-VLA는 실제 로봇에서도 높은 성능을 보이며, 특히 보이지 않는 카메라 각도에서의 성능 향상을 확인합니다.

---

*Generated on 2025-09-18 17:17:29*