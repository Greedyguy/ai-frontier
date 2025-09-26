---
keywords:
  - Diffusion Models
  - Vision-Language-Action
  - Reflective Reasoning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14889
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:52:34.932004",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Vision-Language-Action",
    "Reflective Reasoning"
  ],
  "rejected_keywords": [
    "Mixture-of-Experts Design",
    "Self-Reflection"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Vision-Language-Action": 0.78,
    "Reflective Reasoning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# CollabVLA: Self-Reflective Vision-Language-Action Model Dreaming Together with Human

**Korean Title:** CollabVLA: 인간과 함께 꿈꾸는 자기 반성적 비전-언어-행동 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion-based Action Generation]]
**⚡ Unique Technical**: [[keywords/Vision-Language-Action|Vision-Language-Action]]
**🚀 Evolved Concepts**: [[keywords/Reflective Reasoning|Reflective Reasoning]]

## 🔗 유사한 논문
- [[ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (88.6% similar)
- [[CLAW A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (85.4% similar)
- [[ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (84.9% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (84.9% similar)
- [[GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (84.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14889v1 Announce Type: new 
Abstract: In this work, we present CollabVLA, a self-reflective vision-language-action framework that transforms a standard visuomotor policy into a collaborative assistant. CollabVLA tackles key limitations of prior VLAs, including domain overfitting, non-interpretable reasoning, and the high latency of auxiliary generative models, by integrating VLM-based reflective reasoning with diffusion-based action generation under a mixture-of-experts design. Through a two-stage training recipe of action grounding and reflection tuning, it supports explicit self-reflection and proactively solicits human guidance when confronted with uncertainty or repeated failure. It cuts normalized Time by ~2x and Dream counts by ~4x vs. generative agents, achieving higher success rates, improved interpretability, and balanced low latency compared with existing methods. This work takes a pioneering step toward shifting VLAs from opaque controllers to genuinely assistive agents capable of reasoning, acting, and collaborating with humans.

## 🔍 Abstract (한글 번역)

arXiv:2509.14889v1 발표 유형: 신규  
초록: 본 연구에서는 표준 시각-운동 정책을 협력적 보조자로 변환하는 자기 반영적 시각-언어-행동(CollabVLA) 프레임워크를 제시합니다. CollabVLA는 VLM 기반의 반영적 추론과 혼합 전문가 설계 하의 확산 기반 행동 생성을 통합하여, 이전 VLA의 주요 한계인 도메인 과적합, 비해석적 추론, 보조 생성 모델의 높은 지연 시간을 해결합니다. 행동 기반 및 반영 조정의 두 단계 훈련 방식을 통해 명시적인 자기 반영을 지원하며, 불확실성이나 반복적인 실패에 직면했을 때 인간의 지도를 적극적으로 요청합니다. 이는 생성 에이전트에 비해 정규화된 시간을 약 2배, Dream 횟수를 약 4배 절감하며, 기존 방법에 비해 더 높은 성공률, 개선된 해석 가능성, 균형 잡힌 낮은 지연 시간을 달성합니다. 이 연구는 VLA를 불투명한 제어기에서 인간과의 추론, 행동, 협력이 가능한 진정한 보조 에이전트로 전환하는 데 있어 선구적인 발걸음을 내딛습니다.

## 📝 요약

이 연구는 CollabVLA라는 자가 반영 비전-언어-행동(VLA) 프레임워크를 제안하여 기존의 비주모터 정책을 협력적 보조 장치로 변환합니다. CollabVLA는 도메인 과적합, 비해석적 추론, 보조 생성 모델의 높은 지연 시간 등 기존 VLA의 주요 한계를 극복합니다. VLM 기반의 반영적 추론과 확산 기반의 행동 생성 방식을 혼합 전문가 설계로 통합하여 이를 실현합니다. 두 단계의 훈련 과정인 행동 기반 및 반영 조정을 통해 명시적인 자가 반영을 지원하고, 불확실성이나 반복된 실패 시 인간의 지도를 적극적으로 요청합니다. 기존 생성 에이전트에 비해 정상화된 시간을 약 2배, Dream 횟수를 약 4배 줄이며, 성공률, 해석 가능성, 낮은 지연 시간에서 개선된 성과를 보입니다. 이 연구는 VLA를 불투명한 제어 장치에서 인간과 협력할 수 있는 진정한 보조 에이전트로 전환하는 데 선구적인 역할을 합니다.

## 🎯 주요 포인트

- 1. CollabVLA는 표준 시각-운동 정책을 협력적인 보조자로 변환하는 자가 반영 비전-언어-행동 프레임워크입니다.

- 2. 이 프레임워크는 VLM 기반의 반영적 추론과 확산 기반의 행동 생성을 혼합 전문가 설계로 통합하여 기존 VLAs의 주요 한계를 해결합니다.

- 3. 행동 기반 및 반영 조정의 두 단계 훈련을 통해 명시적인 자가 반영을 지원하고 불확실성이나 반복된 실패 시 인간의 지도를 능동적으로 요청합니다.

- 4. 기존 생성 에이전트 대비 정규화된 시간을 약 2배, Dream 횟수를 약 4배 줄이며 성공률, 해석 가능성, 낮은 대기 시간을 개선합니다.

- 5. 이 연구는 VLAs를 불투명한 제어기에서 인간과의 추론, 행동, 협력이 가능한 진정한 보조 에이전트로 전환하는 데 있어 선구적인 역할을 합니다.

---

*Generated on 2025-09-19 16:32:58*