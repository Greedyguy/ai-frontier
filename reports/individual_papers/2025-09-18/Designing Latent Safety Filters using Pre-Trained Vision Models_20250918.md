---
keywords:
  - Vision Transformers
  - Hamilton-Jacobi Reachability
  - Latent World Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:33:09.170043",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision Transformers",
    "Hamilton-Jacobi Reachability",
    "Latent World Models"
  ],
  "rejected_keywords": [
    "Safety Filters"
  ],
  "similarity_scores": {
    "Vision Transformers": 0.8,
    "Hamilton-Jacobi Reachability": 0.78,
    "Latent World Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Designing Latent Safety Filters using Pre-Trained Vision Models

**Korean Title:** 사전 훈련된 비전 모델을 활용한 잠재적 안전 필터 설계

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision Transformers|Pre-trained vision models]]
**⚡ Unique Technical**: [[keywords/Hamilton-Jacobi Reachability|Hamilton-Jacobi reachability-based safety filters]], [[keywords/Latent World Models|latent world models]]

## 🔗 유사한 논문
- [[Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (80.4% similar)
- [[Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (78.9% similar)
- [[ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (78.4% similar)
- [[PA-MPPI_ Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments_20250919|PA-MPPI Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments]] (78.2% similar)
- [[ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (78.0% similar)

## 📋 저자 정보

**Authors:** Ihab Tabbara, Yuxuan Yang, Ahmad Hamzeh, Maxwell Astafyev, Hussein Sibai

## 📄 Abstract (원문)

Ensuring safety of vision-based control systems remains a major challenge
hindering their deployment in critical settings. Safety filters have gained
increased interest as effective tools for ensuring the safety of classical
control systems, but their applications in vision-based control settings have
so far been limited. Pre-trained vision models (PVRs) have been shown to be
effective perception backbones for control in various robotics domains. In this
paper, we are interested in examining their effectiveness when used for
designing vision-based safety filters. We use them as backbones for classifiers
defining failure sets, for Hamilton-Jacobi (HJ) reachability-based safety
filters, and for latent world models. We discuss the trade-offs between
training from scratch, fine-tuning, and freezing the PVRs when training the
models they are backbones for. We also evaluate whether one of the PVRs is
superior across all tasks, evaluate whether learned world models or Q-functions
are better for switching decisions to safe policies, and discuss practical
considerations for deploying these PVRs on resource-constrained devices.

## 🔍 Abstract (한글 번역)

비전 기반 제어 시스템의 안전성을 보장하는 것은 중요한 환경에서의 배치를 저해하는 주요 과제로 남아 있습니다. 안전 필터는 고전적 제어 시스템의 안전성을 보장하는 효과적인 도구로서 점점 더 많은 관심을 받고 있지만, 비전 기반 제어 환경에서의 적용은 아직 제한적입니다. 사전 학습된 비전 모델(PVR)은 다양한 로봇 공학 분야에서 제어를 위한 효과적인 인식 백본으로 입증되었습니다. 본 논문에서는 비전 기반 안전 필터 설계에 사용될 때 그 효과성을 검토하는 데 관심이 있습니다. 우리는 이를 실패 집합을 정의하는 분류기의 백본, 해밀턴-자코비(HJ) 도달 가능성 기반 안전 필터 및 잠재 세계 모델의 백본으로 사용합니다. 모델의 백본으로 사용되는 PVR을 학습할 때 처음부터 학습하는 것, 미세 조정하는 것, 고정하는 것 사이의 절충점을 논의합니다. 또한 모든 작업에서 하나의 PVR이 우수한지 여부를 평가하고, 학습된 세계 모델이나 Q-함수가 안전 정책으로 전환하는 결정에 더 나은지 평가하며, 자원이 제한된 장치에서 이러한 PVR을 배포하기 위한 실질적인 고려 사항을 논의합니다.

## 📝 요약

이 논문은 비전 기반 제어 시스템의 안전성을 보장하기 위한 연구로, 사전 학습된 비전 모델(PVR)을 활용한 안전 필터 설계의 효과를 분석합니다. PVR을 실패 집합을 정의하는 분류기, 해밀턴-자코비 도달 가능성 기반 안전 필터, 잠재 세계 모델의 백본으로 사용합니다. 모델 학습 시 PVR을 처음부터 학습, 미세 조정, 고정하는 방법 간의 장단점을 논의하고, PVR의 성능을 다양한 과제에서 평가합니다. 또한, 학습된 세계 모델과 Q-함수 중 안전 정책 전환에 더 적합한 것을 평가하고, 자원이 제한된 장치에서 PVR을 배포할 때의 실용적 고려사항을 다룹니다.

## 🎯 주요 포인트

- 1. 비전 기반 제어 시스템의 안전성을 보장하는 것은 중요한 과제로 남아 있으며, 안전 필터는 이러한 시스템의 안전성을 보장하는 효과적인 도구로 주목받고 있다.

- 2. 사전 학습된 비전 모델(PVR)은 다양한 로봇 공학 분야에서 제어를 위한 효과적인 인식 백본으로 입증되었다.

- 3. 본 논문에서는 PVR을 활용하여 비전 기반 안전 필터를 설계할 때의 효과성을 검토하고자 한다.

- 4. PVR을 기반으로 하는 분류기, Hamilton-Jacobi 도달 가능성 기반 안전 필터, 잠재 세계 모델을 사용하여 실패 집합을 정의한다.

- 5. PVR을 훈련할 때 처음부터 훈련, 미세 조정, 동결의 트레이드오프를 논의하고, 자원 제약이 있는 장치에 PVR을 배포할 때의 실용적 고려사항을 다룬다.

---

*Generated on 2025-09-20 05:42:29*