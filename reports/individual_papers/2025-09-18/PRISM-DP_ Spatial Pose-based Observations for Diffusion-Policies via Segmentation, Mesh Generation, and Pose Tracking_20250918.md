---
keywords:
  - Diffusion Models
  - Spatial Poses
  - Pose Tracking
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2504.20359
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:16:49.114446",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Spatial Poses",
    "Pose Tracking"
  ],
  "rejected_keywords": [
    "Mesh Generation"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "Spatial Poses": 0.72,
    "Pose Tracking": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking

**Korean Title:** PRISM-DP: 분할, 메쉬 생성 및 포즈 추적을 통한 확산 정책을 위한 공간 포즈 기반 관측

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Policies]]
**⚡ Unique Technical**: [[keywords/Spatial Poses|Spatial Poses]], [[keywords/Pose Tracking|Pose Tracking]]

## 🔗 유사한 논문
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (84.2% similar)
- [[FlightDiffusion_Revolutionising_Autonomous_Drone_Training_with_Diffusion_Models_Generating_FPV_Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (82.6% similar)
- [[One-Step_Model_Predictive_Path_Integral_for_Manipulator_Motion_Planning_Using_Configuration_Space_Distance_Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (81.3% similar)
- [[MIMIC-D: Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (81.2% similar)
- [[GWM: Towards Scalable Gaussian World Models for Robotic Manipulation]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.20359v3 Announce Type: replace 
Abstract: Diffusion policies generate robot motions by learning to denoise action-space trajectories conditioned on observations. These observations are commonly streams of RGB images, whose high dimensionality includes substantial task-irrelevant information, requiring large models to extract relevant patterns. In contrast, using structured observations like the spatial poses of key objects enables training more compact policies with fewer parameters. However, obtaining accurate object poses in open-set, real-world environments remains challenging, as 6D pose estimation and tracking methods often depend on markers placed on objects beforehand or pre-scanned object meshes that require manual reconstruction. We propose PRISM-DP, an approach that leverages segmentation, mesh generation, and pose tracking models to enable compact diffusion policy learning directly from the spatial poses of task-relevant objects. Crucially, by using a mesh generation model, PRISM-DP eliminates the need for manual mesh creation, improving scalability in open-set environments. Experiments in simulation and the real world show that PRISM-DP outperforms high-dimensional image-based policies and achieves performance comparable to policies trained with ground-truth state information.

## 🔍 Abstract (한글 번역)

arXiv:2504.20359v3 발표 유형: 대체
요약: 확산 정책은 관측에 의존하는 행동 공간 경로를 소음 제거하여 로봇 동작을 생성합니다. 이러한 관측은 일반적으로 RGB 이미지 스트림으로, 높은 차원의 정보를 포함하고 있어 대규모 모델이 필요하며, 관련 패턴을 추출하기 위해 큰 모델이 필요합니다. 반면, 주요 객체의 공간 위치와 같은 구조화된 관측을 사용하면 더 적은 매개변수로 더 조밀한 정책을 훈련할 수 있습니다. 그러나 오픈셋, 실제 환경에서 정확한 객체 위치를 얻는 것은 여전히 어렵습니다. 왜냐하면 6D 포즈 추정 및 추적 방법은 종종 미리 객체에 배치된 마커나 수동 재구성이 필요한 사전 스캔된 객체 메쉬에 의존하기 때문입니다. 우리는 PRISM-DP라는 접근 방식을 제안합니다. 이 접근 방식은 분할, 메쉬 생성 및 포즈 추적 모델을 활용하여 작업 관련 객체의 공간 위치에서 직접 조밀한 확산 정책 학습을 가능하게 합니다. 중요한 점은 메쉬 생성 모델을 사용하여 PRISM-DP가 수동 메쉬 생성의 필요성을 제거하여 오픈셋 환경에서 확장성을 향상시킨다는 것입니다. 시뮬레이션 및 실제 환경에서의 실험 결과는 PRISM-DP가 고차원 이미지 기반 정책을 능가하며, 지면 진실 상태 정보로 훈련된 정책과 유사한 성능을 달성한다는 것을 보여줍니다.

## 📝 요약

로봇의 움직임을 생성하는 확산 정책은 관측에 의존하는 행동 공간 경로를 소음 제거하는 방식으로 학습합니다. 일반적으로 RGB 이미지 스트림을 관측으로 사용하는데, 이는 상당한 작업 관련 정보 이외의 정보를 포함하므로 관련 패턴을 추출하기 위해 대규모 모델이 필요합니다. 반면, 주요 객체의 공간 자세와 같은 구조화된 관측을 사용하면 더 적은 매개변수로 더 조밀한 정책을 학습할 수 있습니다. PRISM-DP는 세분화, 메시 생성 및 자세 추적 모델을 활용하여 작업 관련 객체의 공간 자세로부터 직접 조밀한 확산 정책 학습을 가능케 합니다. PRISM-DP는 수동 메시 생성의 필요성을 제거하여 개방형 환경에서의 확장성을 향상시킵니다. 시뮬레이션 및 실제 환경에서의 실험 결과, PRISM-DP는 고차원 이미지 기반 정책을 능가하며 지면 실존 상태 정보로 학습된 정책과 유사한 성능을 달성합니다.

## 🎯 주요 포인트

- 1. 환경에서 효율적인 로봇 동작을 위해 PRISM-DP 방법을 제안하였다.

- 2. PRISM-DP는 객체의 공간 위치를 직접 학습하여 더 적은 파라미터로 더 효율적인 정책을 학습한다.

- 3. PRISM-DP는 이미지 기반 정책보다 우수한 성능을 보이며, 상태 정보를 사용한 정책과 유사한 성능을 달성한다.

---

*Generated on 2025-09-18 17:18:46*