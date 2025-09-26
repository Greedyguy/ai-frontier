---
keywords:
  - MolmoAct
  - Action Reasoning Models
  - Foundation Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2508.07917
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:33:46.114586",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MolmoAct",
    "Action Reasoning Models",
    "Foundation Models"
  ],
  "rejected_keywords": [
    "Trajectory Steering"
  ],
  "similarity_scores": {
    "MolmoAct": 0.85,
    "Action Reasoning Models": 0.8,
    "Foundation Models": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# MolmoAct: Action Reasoning Models that can Reason in Space

**Korean Title:** MolmoAct: 공간에서 추론할 수 있는 행동 추론 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/MolmoAct|MolmoAct]], [[keywords/Action Reasoning Models|Action Reasoning Models]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Robotic Foundation Models]]

## 🔗 유사한 논문
- [[ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (83.7% similar)
- [[Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation_20250918|Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (82.2% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (81.5% similar)
- [[CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (81.0% similar)
- [[ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (80.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.07917v4 Announce Type: replace 
Abstract: Reasoning is central to purposeful action, yet most robotic foundation models map perception and instructions directly to control, which limits adaptability, generalization, and semantic grounding. We introduce Action Reasoning Models (ARMs), a class of robotic foundation models that integrate perception, planning, and control through a structured three-stage pipeline. Our model, MolmoAct, encodes observations and instructions into depth-aware perception tokens, generates mid-level spatial plans as editable trajectory traces, and predicts precise low-level actions, enabling explainable and steerable behavior. MolmoAct-7B-D achieves strong performance across simulation and real-world settings: 70.5% zero-shot accuracy on SimplerEnv Visual Matching tasks, surpassing closed-source Pi-0 and GR00T N1.5; 86.6% average success on LIBERO, including an additional 6.3% gain over ThinkAct on long-horizon tasks; and in real-world fine-tuning, an additional 10% (single-arm) and an additional 22.7% (bimanual) task progression over Pi-0-FAST. It also outperforms baselines by an additional 23.3% on out-of-distribution generalization and achieves top human-preference scores for open-ended instruction following and trajectory steering. Furthermore, we release, for the first time, the MolmoAct Dataset -- a mid-training robot dataset comprising over 10,000 high quality robot trajectories across diverse scenarios and tasks. Training with this dataset yields an average 5.5% improvement in general performance over the base model. We release all model weights, training code, our collected dataset, and our action reasoning dataset, establishing MolmoAct as both a state-of-the-art robotics foundation model and an open blueprint for building ARMs that transform perception into purposeful action through structured reasoning. Blogpost: https://allenai.org/blog/molmoact

## 🔍 Abstract (한글 번역)

arXiv:2508.07917v4 발표 유형: 교체  
초록: 추론은 목적 있는 행동의 중심에 있지만, 대부분의 로봇 기반 모델은 인식과 지시를 직접 제어로 매핑하여 적응성, 일반화, 의미적 기반을 제한합니다. 우리는 인식, 계획, 제어를 구조화된 3단계 파이프라인을 통해 통합하는 로봇 기반 모델의 한 종류인 행동 추론 모델(ARMs)을 소개합니다. 우리의 모델 MolmoAct는 관찰과 지시를 깊이 인식 가능한 인식 토큰으로 인코딩하고, 편집 가능한 궤적 추적을 통해 중간 수준의 공간 계획을 생성하며, 정밀한 저수준 행동을 예측하여 설명 가능하고 조정 가능한 행동을 가능하게 합니다. MolmoAct-7B-D는 시뮬레이션 및 실제 환경에서 강력한 성능을 발휘합니다: SimplerEnv 시각적 매칭 작업에서 70.5%의 제로샷 정확도를 기록하며, 비공개 Pi-0 및 GR00T N1.5를 능가합니다; LIBERO에서 평균 86.6%의 성공률을 기록하며, 장기 과제에서 ThinkAct보다 추가로 6.3%의 향상을 보입니다; 실제 환경에서의 미세 조정에서는 Pi-0-FAST보다 단일 팔 작업에서 추가로 10%, 양손 작업에서 추가로 22.7%의 작업 진행을 기록합니다. 또한, 분포 외 일반화에서 기준 모델보다 추가로 23.3%를 능가하며, 개방형 지시 따르기 및 궤적 조정에서 최고 인간 선호 점수를 기록합니다. 더 나아가, 우리는 처음으로 MolmoAct 데이터셋을 공개합니다 -- 다양한 시나리오와 작업에 걸쳐 10,000개 이상의 고품질 로봇 궤적을 포함하는 중간 훈련 로봇 데이터셋입니다. 이 데이터셋으로 훈련하면 기본 모델 대비 평균 5.5%의 일반 성능 향상을 가져옵니다. 우리는 모든 모델 가중치, 훈련 코드, 수집된 데이터셋, 그리고 행동 추론 데이터셋을 공개하여 MolmoAct를 최첨단 로봇 기반 모델이자 인식을 구조화된 추론을 통해 목적 있는 행동으로 변환하는 ARMs 구축을 위한 개방형 청사진으로 확립합니다. 블로그 게시물: https://allenai.org/blog/molmoact

## 📝 요약

이 논문은 로봇의 인지, 계획, 제어를 통합하는 새로운 모델인 Action Reasoning Models (ARMs)을 소개합니다. 제안된 모델 MolmoAct는 관찰과 지시를 심층 인식 토큰으로 인코딩하고, 중간 수준의 공간 계획을 생성하며, 정확한 저수준 행동을 예측합니다. MolmoAct-7B-D는 시뮬레이션 및 실제 환경에서 높은 성능을 보이며, 다양한 작업에서 기존 모델을 능가합니다. 또한, MolmoAct Dataset을 공개하여 로봇 학습의 새로운 기준을 제시합니다. 이 연구는 로봇의 인식에서 목적 있는 행동으로의 전환을 위한 구조적 추론의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. Action Reasoning Models (ARMs)는 인식, 계획, 제어를 통합하여 로봇의 적응성과 일반화를 향상시킵니다.

- 2. MolmoAct 모델은 깊이 인식이 가능한 인식 토큰을 사용하여 중간 수준의 공간 계획을 생성하고, 정확한 저수준 행동을 예측합니다.

- 3. MolmoAct-7B-D는 SimplerEnv Visual Matching 작업에서 70.5%의 제로샷 정확도를 기록하며, LIBERO에서 평균 86.6%의 성공률을 달성합니다.

- 4. MolmoAct는 Pi-0-FAST보다 실제 환경에서 단일 및 양손 작업 진행률을 각각 10% 및 22.7% 향상시킵니다.

- 5. MolmoAct 데이터셋은 10,000개 이상의 로봇 경로를 포함하며, 이를 통해 일반 성능이 평균 5.5% 향상됩니다.

---

*Generated on 2025-09-19 16:38:45*