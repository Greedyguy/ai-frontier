---
keywords:
  - Supervised Domain Adaptation
  - Spacecraft Pose Estimation
  - Learning Invariant Representation and Risk
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:59:43.087522",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Supervised Domain Adaptation",
    "Spacecraft Pose Estimation",
    "Learning Invariant Representation and Risk"
  ],
  "rejected_keywords": [
    "Computer Vision"
  ],
  "similarity_scores": {
    "Supervised Domain Adaptation": 0.82,
    "Spacecraft Pose Estimation": 0.78,
    "Learning Invariant Representation and Risk": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Bridging the Synthetic-Real Gap: Supervised Domain Adaptation for Robust Spacecraft 6-DoF Pose Estimation

**Korean Title:** 합성-실제 간극 연결: 견고한 우주선 6-자유도 자세 추정을 위한 지도형 도메인 적응

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Spacecraft Pose Estimation|Spacecraft Pose Estimation]], [[keywords/Learning Invariant Representation and Risk|Learning Invariant Representation and Risk]]
**🚀 Evolved Concepts**: [[keywords/Supervised Domain Adaptation|Supervised Domain Adaptation]]

## 🔗 유사한 논문
- [[BEVUDA++_ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection_20250918|BEVUDA++ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (82.4% similar)
- [[Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (79.2% similar)
- [[SPAR_ Scalable LLM-based PDDL Domain Generation for Aerial Robotics_20250918|SPAR Scalable LLM-based PDDL Domain Generation for Aerial Robotics]] (79.1% similar)
- [[Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (78.8% similar)
- [[PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (78.4% similar)

## 📋 저자 정보

**Authors:** Inder Pal Singh, Nidhal Eddine Chenni, Abd El Rahman Shabayek, Arunkumar Rathinam, Djamila Aouada

## 📄 Abstract (원문)

Spacecraft Pose Estimation (SPE) is a fundamental capability for autonomous
space operations such as rendezvous, docking, and in-orbit servicing. Hybrid
pipelines that combine object detection, keypoint regression, and
Perspective-n-Point (PnP) solvers have recently achieved strong results on
synthetic datasets, yet their performance deteriorates sharply on real or
lab-generated imagery due to the persistent synthetic-to-real domain gap.
Existing unsupervised domain adaptation approaches aim to mitigate this issue
but often underperform when a modest number of labeled target samples are
available. In this work, we propose the first Supervised Domain Adaptation
(SDA) framework tailored for SPE keypoint regression. Building on the Learning
Invariant Representation and Risk (LIRR) paradigm, our method jointly optimizes
domain-invariant representations and task-specific risk using both labeled
synthetic and limited labeled real data, thereby reducing generalization error
under domain shift. Extensive experiments on the SPEED+ benchmark demonstrate
that our approach consistently outperforms source-only, fine-tuning, and oracle
baselines. Notably, with only 5% labeled target data, our method matches or
surpasses oracle performance trained on larger fractions of labeled data. The
framework is lightweight, backbone-agnostic, and computationally efficient,
offering a practical pathway toward robust and deployable spacecraft pose
estimation in real-world space environments.

## 🔍 Abstract (한글 번역)

우주선 자세 추정(Spacecraft Pose Estimation, SPE)은 랑데부, 도킹, 궤도 내 서비스와 같은 자율 우주 작전을 위한 기본 능력입니다. 객체 탐지, 키포인트 회귀, 그리고 Perspective-n-Point (PnP) 솔버를 결합한 하이브리드 파이프라인은 최근 합성 데이터셋에서 강력한 결과를 달성했지만, 합성에서 실제로의 도메인 격차가 지속되기 때문에 실제 또는 실험실 생성 이미지에서는 성능이 급격히 저하됩니다. 기존의 비지도 도메인 적응 접근법은 이 문제를 완화하려고 하지만, 소량의 라벨이 있는 대상 샘플이 있을 때는 종종 성능이 떨어집니다. 본 연구에서는 SPE 키포인트 회귀를 위해 맞춤 설계된 최초의 지도 도메인 적응(Supervised Domain Adaptation, SDA) 프레임워크를 제안합니다. 학습 불변 표현 및 위험(Learning Invariant Representation and Risk, LIRR) 패러다임을 기반으로, 본 방법은 라벨이 있는 합성 데이터와 제한된 라벨이 있는 실제 데이터를 사용하여 도메인 불변 표현과 과제별 위험을 공동으로 최적화함으로써 도메인 이동 하에서의 일반화 오류를 줄입니다. SPEED+ 벤치마크에서의 광범위한 실험은 본 접근법이 소스 전용, 미세 조정, 오라클 기준선보다 일관되게 우수한 성능을 보임을 증명합니다. 특히, 라벨이 있는 대상 데이터의 5%만으로도 본 방법은 더 많은 라벨 데이터로 학습된 오라클 성능과 동등하거나 이를 초과합니다. 이 프레임워크는 경량이며, 백본에 구애받지 않고 계산 효율성이 높아 실제 우주 환경에서 강력하고 배포 가능한 우주선 자세 추정을 위한 실용적인 경로를 제공합니다.

## 📝 요약

이 논문은 우주선 자세 추정(SPE)의 성능을 향상시키기 위한 최초의 감독형 도메인 적응(SDA) 프레임워크를 제안합니다. 기존의 하이브리드 파이프라인은 합성 데이터셋에서는 우수한 성과를 보였지만, 실제 이미지에서는 성능이 저하되었습니다. 제안된 방법은 LIRR 패러다임을 기반으로 합성 및 제한된 실제 데이터의 레이블을 활용하여 도메인 불변 표현과 작업별 위험을 최적화합니다. SPEED+ 벤치마크 실험에서 이 방법은 소스 전용, 미세 조정 및 오라클 기준을 능가했으며, 5%의 레이블된 타겟 데이터만으로도 오라클 성능에 도달했습니다. 이 프레임워크는 경량, 백본 비의존적이며, 실제 우주 환경에서의 우주선 자세 추정을 위한 실용적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 우주선 자세 추정(SPE)은 자율 우주 작전을 위한 필수적인 기능이다.

- 2. 기존의 하이브리드 파이프라인은 합성 데이터셋에서 강력한 성능을 보이지만, 실제 이미지에서는 성능이 저하된다.

- 3. 본 연구는 SPE 키포인트 회귀를 위한 최초의 지도 학습 기반 도메인 적응(SDA) 프레임워크를 제안한다.

- 4. 제안된 방법은 합성 및 제한된 실제 데이터의 라벨을 활용하여 도메인 불변 표현과 과제별 위험을 최적화한다.

- 5. SPEED+ 벤치마크 실험에서 제안된 방법은 소스 전용, 파인튜닝, 오라클 기준선을 일관되게 능가한다.

---

*Generated on 2025-09-20 09:32:20*