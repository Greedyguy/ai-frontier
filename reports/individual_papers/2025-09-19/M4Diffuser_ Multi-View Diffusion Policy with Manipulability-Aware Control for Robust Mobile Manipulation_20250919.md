---
keywords:
  - Diffusion Models
  - Manipulability-Aware Control
  - Mobile Manipulation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14980
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:37:10.154403",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Manipulability-Aware Control",
    "Mobile Manipulation"
  ],
  "rejected_keywords": [
    "Proprioceptive States"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Manipulability-Aware Control": 0.78,
    "Mobile Manipulation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation

**Korean Title:** M4Diffuser: 견고한 이동 조작을 위한 조작 가능성 인식 제어를 갖춘 다중 시점 확산 정책

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Multi-View Diffusion Policy]]
**⚡ Unique Technical**: [[keywords/Manipulability-Aware Control|Manipulability-Aware Control]]
**🚀 Evolved Concepts**: [[keywords/Mobile Manipulation|Mobile Manipulation]]

## 🔗 유사한 논문
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (82.9% similar)
- [[PRISM-DP Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (82.0% similar)
- [[Motion_Adaptation_Across_Users_and_Tasks_for_Exoskeletons_via_Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (81.3% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (81.2% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14980v1 Announce Type: cross 
Abstract: Mobile manipulation requires the coordinated control of a mobile base and a robotic arm while simultaneously perceiving both global scene context and fine-grained object details. Existing single-view approaches often fail in unstructured environments due to limited fields of view, exploration, and generalization abilities. Moreover, classical controllers, although stable, struggle with efficiency and manipulability near singularities. To address these challenges, we propose M4Diffuser, a hybrid framework that integrates a Multi-View Diffusion Policy with a novel Reduced and Manipulability-aware QP (ReM-QP) controller for mobile manipulation. The diffusion policy leverages proprioceptive states and complementary camera perspectives with both close-range object details and global scene context to generate task-relevant end-effector goals in the world frame. These high-level goals are then executed by the ReM-QP controller, which eliminates slack variables for computational efficiency and incorporates manipulability-aware preferences for robustness near singularities. Comprehensive experiments in simulation and real-world environments show that M4Diffuser achieves 7 to 56 percent higher success rates and reduces collisions by 3 to 31 percent over baselines. Our approach demonstrates robust performance for smooth whole-body coordination, and strong generalization to unseen tasks, paving the way for reliable mobile manipulation in unstructured environments. Details of the demo and supplemental material are available on our project website https://sites.google.com/view/m4diffuser.

## 🔍 Abstract (한글 번역)

arXiv:2509.14980v1 발표 유형: 교차  
초록: 모바일 조작은 모바일 기반과 로봇 팔의 조정된 제어를 요구하며, 동시에 전반적인 장면 맥락과 세밀한 객체 세부사항을 인식해야 합니다. 기존의 단일 뷰 접근 방식은 제한된 시야, 탐색 및 일반화 능력 때문에 비구조화된 환경에서 종종 실패합니다. 게다가, 고전적인 제어기는 안정적이지만, 특이점 근처에서의 효율성과 조작 가능성에 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 모바일 조작을 위한 다중 뷰 확산 정책과 새로운 축소 및 조작 가능성 인식 QP(ReM-QP) 제어기를 통합한 하이브리드 프레임워크인 M4Diffuser를 제안합니다. 확산 정책은 고유 수용 상태와 근거리 객체 세부사항 및 전반적인 장면 맥락을 포함한 보완적인 카메라 관점을 활용하여 세계 프레임에서 작업 관련 엔드 이펙터 목표를 생성합니다. 이러한 고수준 목표는 ReM-QP 제어기에 의해 실행되며, 이는 계산 효율성을 위해 슬랙 변수를 제거하고 특이점 근처에서의 강건성을 위한 조작 가능성 인식 선호도를 통합합니다. 시뮬레이션 및 실제 환경에서의 포괄적인 실험은 M4Diffuser가 기준선 대비 7%에서 56% 더 높은 성공률을 달성하고 충돌을 3%에서 31% 줄임을 보여줍니다. 우리의 접근 방식은 매끄러운 전신 조정을 위한 강력한 성능과 보지 못한 작업에 대한 강한 일반화를 보여주며, 비구조화된 환경에서의 신뢰할 수 있는 모바일 조작을 위한 길을 열어줍니다. 데모 및 보충 자료의 세부사항은 프로젝트 웹사이트 https://sites.google.com/view/m4diffuser에서 확인할 수 있습니다.

## 📝 요약

M4Diffuser는 이동 기반과 로봇 팔의 조정 제어를 위한 하이브리드 프레임워크로, Multi-View Diffusion Policy와 Reduced and Manipulability-aware QP (ReM-QP) 컨트롤러를 통합하여 비정형 환경에서의 모바일 조작 문제를 해결합니다. 이 방법은 근거리 객체 세부사항과 전반적인 장면 맥락을 결합하여 작업 관련 목표를 생성하며, ReM-QP 컨트롤러는 계산 효율성을 높이고 특이점 근처에서의 강건성을 제공합니다. 실험 결과, M4Diffuser는 기존 방법보다 성공률을 7~56% 향상시키고 충돌을 3~31% 감소시켰으며, 새로운 작업에 대한 강력한 일반화 성능을 보여주었습니다.

## 🎯 주요 포인트

- 1. M4Diffuser는 Multi-View Diffusion Policy와 Reduced and Manipulability-aware QP (ReM-QP) 컨트롤러를 통합한 하이브리드 프레임워크로, 모바일 매니퓰레이션의 효율성을 높입니다.

- 2. 이 프레임워크는 proprioceptive 상태와 다양한 카메라 시점을 활용하여 작업 관련 엔드 이펙터 목표를 생성하고, ReM-QP 컨트롤러가 이를 실행하여 계산 효율성과 강건성을 제공합니다.

- 3. M4Diffuser는 시뮬레이션 및 실제 환경 실험에서 기존 방법들보다 7%에서 56% 높은 성공률을 기록하고, 충돌을 3%에서 31% 감소시켰습니다.

- 4. 이 접근법은 부드러운 전신 조정과 미지의 작업에 대한 강력한 일반화 성능을 보여주며, 비구조적 환경에서의 신뢰할 수 있는 모바일 매니퓰레이션을 가능하게 합니다.

---

*Generated on 2025-09-19 15:03:17*