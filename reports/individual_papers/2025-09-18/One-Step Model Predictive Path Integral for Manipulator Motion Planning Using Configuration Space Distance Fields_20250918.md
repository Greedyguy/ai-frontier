
# One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields

**Korean Title:** 로봇 팔 동작 계획을 위한 구성 공간 거리 필드를 사용한 단계별 모델 예측 경로 적분법.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Joint-space Cost Unification

## 🔗 유사한 논문
- [[Meta-Optimization_and_Program_Search_using_Language_Models_for_Task_and_Motion_Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (82.4% similar)
- [[Disturbance-Aware_Dynamical_Trajectory_Planning_for_Air-Land_Bimodal_Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (82.1% similar)
- [[Flexible_and_Foldable_Workspace_Analysis_and_Object_Manipulation_Using_a_Soft,_Interconnected,_Origami-Inspired_Actuator_Array_20250918|Flexible and Foldable: Workspace Analysis and Object Manipulation Using a Soft, Interconnected, Origami-Inspired Actuator Array]] (82.0% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.8% similar)
- [[PRISM-DP_Spatial_Pose-based_Observations_for_Diffusion-Policies_via_Segmentation,_Mesh_Generation,_and_Pose_Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.00836v2 Announce Type: replace 
Abstract: Motion planning for robotic manipulators is a fundamental problem in robotics. Classical optimization-based methods typically rely on the gradients of signed distance fields (SDFs) to impose collision-avoidance constraints. However, these methods are susceptible to local minima and may fail when the SDF gradients vanish. Recently, Configuration Space Distance Fields (CDFs) have been introduced, which directly model distances in the robot's configuration space. Unlike workspace SDFs, CDFs are differentiable almost everywhere and thus provide reliable gradient information. On the other hand, gradient-free approaches such as Model Predictive Path Integral (MPPI) control leverage long-horizon rollouts to achieve collision avoidance. While effective, these methods are computationally expensive due to the large number of trajectory samples, repeated collision checks, and the difficulty of designing cost functions with heterogeneous physical units. In this paper, we propose a framework that integrates CDFs with MPPI to enable direct navigation in the robot's configuration space. Leveraging CDF gradients, we unify the MPPI cost in joint-space and reduce the horizon to one step, substantially cutting computation while preserving collision avoidance in practice. We demonstrate that our approach achieves nearly 100% success rates in 2D environments and consistently high success rates in challenging 7-DOF Franka manipulator simulations with complex obstacles. Furthermore, our method attains control frequencies exceeding 750 Hz, substantially outperforming both optimization-based and standard MPPI baselines. These results highlight the effectiveness and efficiency of the proposed CDF-MPPI framework for high-dimensional motion planning.

## 🔍 Abstract (한글 번역)

arXiv:2509.00836v2 발표 유형: 대체
요약: 로봇 조작기의 움직임 계획은 로봇 공학에서의 기본적인 문제입니다. 고전적인 최적화 기반 방법은 일반적으로 충돌 회피 제약 조건을 부과하기 위해 부호화된 거리 필드(SDFs)의 그래디언트에 의존합니다. 그러나 이러한 방법은 지역 최소점에 취약하며 SDF 그래디언트가 사라질 때 실패할 수 있습니다. 최근에는 로봇의 구성 공간에서 거리를 직접 모델링하는 Configuration Space Distance Fields (CDFs)가 소개되었습니다. 작업 공간 SDFs와 달리 CDFs는 거의 모든 곳에서 미분 가능하며 신뢰할 수 있는 그래디언트 정보를 제공합니다. 반면에 Model Predictive Path Integral (MPPI) 제어와 같은 그래디언트 없는 방법은 장기 롤아웃을 활용하여 충돌 회피를 달성합니다. 효과적이지만 이러한 방법은 궤적 샘플의 많은 수, 반복된 충돌 확인 및 이질적인 물리적 단위로 비용 함수를 설계하는 어려움으로 인해 계산적으로 비용이 많이 듭니다. 본 논문에서는 CDFs를 MPPI와 통합하여 로봇의 구성 공간에서의 직접적인 탐색을 가능케 하는 프레임워크를 제안합니다. CDF 그래디언트를 활용하여 우리는 MPPI 비용을 조인트 공간에서 통합하고 수평을 한 단계로 줄여 계산을 크게 줄이면서 실제에서 충돌 회피를 보존합니다. 우리의 접근 방식이 2D 환경에서 거의 100%의 성공률을 달성하고 복잡한 장애물이 있는 7-DOF Franka 조작기 시뮬레이션에서 일관되게 높은 성공률을 보여줍니다. 더 나아가 우리의 방법은 750 Hz를 초과하는 제어 주파수를 달성하여 최적화 기반 및 표준 MPPI 기준을 크게 능가합니다. 이러한 결과는 고차원 움직임 계획을 위한 제안된 CDF-MPPI 프레임워크의 효과성과 효율성을 강조합니다.

## 📝 요약

로봇 조작기의 움직임 계획은 로봇공학의 기본 문제이다. 기존 최적화 기반 방법은 충돌 회피 제약 조건을 부과하기 위해 부호화된 거리 필드(SDFs)의 그래디언트에 의존한다. 그러나 SDF 그래디언트가 사라지면 이러한 방법은 국소 최소값에 민감하고 실패할 수 있다. 최근에는 로봇의 구성 공간에서 거리를 직접 모델링하는 Configuration Space Distance Fields (CDFs)가 소개되었다. CDFs는 대부분의 곳에서 미분 가능하며 신뢰할 수 있는 그래디언트 정보를 제공한다. 본 논문에서는 CDFs를 MPPI와 통합하여 로봇의 구성 공간에서 직접 탐색할 수 있는 프레임워크를 제안한다. CDF 그래디언트를 활용하여 MPPI 비용을 통합하고 수평을 단계로 줄여 계산을 크게 줄이면서도 실제 충돌 회피를 보존한다. 이 방법은 2D 환경에서 거의 100%의 성공률을 달성하고 복잡한 장애물이 있는 7-DOF Franka 조작기 시뮬레이션에서 일관된 높은 성공률을 보여준다. 또한 제안된 CDF-MPPI 프레임워크는 최적화 기반 및 표준 MPPI 기준을 크게 능가하는 제어 주파수를 달성한다. 이러한 결과는 고차원 움직임 계획에 대한 제안된 CDF-MPPI 프레임워크의 효과성과 효율성을 강조한다.

## 🎯 주요 포인트

- 로봇 조작기의 움직임 계획은 로봇공학의 기본 문제이다.

- 기존의 최적화 기반 방법은 충돌 회피 제약 조건을 부과하기 위해 부호화된 거리 필드(SDFs)의 그래디언트에 의존한다.

- 최근에는 구성 공간 거리 필드(CDFs)가 소개되어 로봇의 구성 공간에서 거리를 직접 모델링한다.

- 우리는 CDF를 MPPI와 통합하는 프레임워크를 제안하여 로봇의 구성 공간에서 직접 탐색 가능하게 한다.

---

*Generated on 2025-09-18 17:20:45*