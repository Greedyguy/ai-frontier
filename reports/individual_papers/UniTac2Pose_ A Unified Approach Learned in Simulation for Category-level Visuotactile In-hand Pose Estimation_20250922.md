# UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

**Korean Title:** UniTac2Pose: 범주 수준의 시각-촉각 내 손 자세 추정을 위한 시뮬레이션에서 학습된 통합 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Sim-to-real Performance

## 🔗 유사한 논문
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (81.4% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (80.0% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (79.9% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (79.7% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15934v1 Announce Type: new 
Abstract: Accurate estimation of the in-hand pose of an object based on its CAD model is crucial in both industrial applications and everyday tasks, ranging from positioning workpieces and assembling components to seamlessly inserting devices like USB connectors. While existing methods often rely on regression, feature matching, or registration techniques, achieving high precision and generalizability to unseen CAD models remains a significant challenge. In this paper, we propose a novel three-stage framework for in-hand pose estimation. The first stage involves sampling and pre-ranking pose candidates, followed by iterative refinement of these candidates in the second stage. In the final stage, post-ranking is applied to identify the most likely pose candidates. These stages are governed by a unified energy-based diffusion model, which is trained solely on simulated data. This energy model simultaneously generates gradients to refine pose estimates and produces an energy scalar that quantifies the quality of the pose estimates. Additionally, borrowing the idea from the computer vision domain, we incorporate a render-compare architecture within the energy-based score network to significantly enhance sim-to-real performance, as demonstrated by our ablation studies. We conduct comprehensive experiments to show that our method outperforms conventional baselines based on regression, matching, and registration techniques, while also exhibiting strong intra-category generalization to previously unseen CAD models. Moreover, our approach integrates tactile object pose estimation, pose tracking, and uncertainty estimation into a unified framework, enabling robust performance across a variety of real-world conditions.

## 🔍 Abstract (한글 번역)

arXiv:2509.15934v1 발표 유형: 신규  
요약: CAD 모델을 기반으로 한 물체의 손 안에서의 자세를 정확하게 추정하는 것은 산업 응용 및 일상 작업에서 매우 중요합니다. 이는 작업물의 위치 조정, 부품 조립, USB 커넥터와 같은 장치의 원활한 삽입에 이르기까지 다양합니다. 기존 방법들은 주로 회귀, 특징 매칭, 또는 등록 기술에 의존하지만, 높은 정밀도와 보지 못한 CAD 모델에 대한 일반화 가능성을 달성하는 것은 여전히 큰 도전 과제입니다. 본 논문에서는 손 안에서의 자세 추정을 위한 새로운 3단계 프레임워크를 제안합니다. 첫 번째 단계에서는 자세 후보를 샘플링하고 사전 순위를 매기며, 두 번째 단계에서는 이러한 후보를 반복적으로 정제합니다. 마지막 단계에서는 사후 순위를 적용하여 가장 가능성이 높은 자세 후보를 식별합니다. 이러한 단계들은 통합된 에너지 기반 확산 모델에 의해 관리되며, 이 모델은 오직 시뮬레이션 데이터로만 훈련됩니다. 이 에너지 모델은 동시에 자세 추정을 정제하기 위한 그래디언트를 생성하고, 자세 추정의 품질을 정량화하는 에너지 스칼라를 생성합니다. 또한, 컴퓨터 비전 분야의 아이디어를 차용하여, 에너지 기반 점수 네트워크 내에 렌더-비교 아키텍처를 통합하여 시뮬레이션에서 실제로의 성능을 크게 향상시켰으며, 이는 우리의 소거 연구에서 입증되었습니다. 우리는 포괄적인 실험을 통해 우리의 방법이 회귀, 매칭, 등록 기술에 기반한 기존의 기준선을 능가하며, 이전에 보지 못한 CAD 모델에 대한 강력한 범주 내 일반화를 나타냄을 보여줍니다. 더 나아가, 우리의 접근법은 촉각 물체 자세 추정, 자세 추적, 불확실성 추정을 통합된 프레임워크로 통합하여 다양한 실제 조건에서 강력한 성능을 가능하게 합니다.

## 📝 요약

이 논문에서는 CAD 모델을 기반으로 한 물체의 손안 자세 추정을 위한 새로운 3단계 프레임워크를 제안합니다. 첫 번째 단계에서는 자세 후보를 샘플링하고 사전 순위를 매기며, 두 번째 단계에서는 후보를 반복적으로 개선합니다. 마지막 단계에서는 사후 순위를 통해 가장 가능성 높은 자세 후보를 식별합니다. 이 과정은 에너지 기반 확산 모델에 의해 통합되며, 시뮬레이션 데이터로만 훈련됩니다. 이 모델은 자세 추정을 개선하기 위한 그래디언트를 생성하고, 자세 추정의 품질을 평가하는 에너지 스칼라를 제공합니다. 또한, 컴퓨터 비전 분야의 아이디어를 차용하여 렌더-비교 아키텍처를 도입해 시뮬레이션에서 실제 환경으로의 성능을 크게 향상시켰습니다. 실험 결과, 제안된 방법은 기존의 회귀, 매칭, 등록 기법을 능가하며, 새로운 CAD 모델에 대한 강력한 일반화 능력을 보였습니다. 또한, 촉각 기반 물체 자세 추정, 자세 추적, 불확실성 추정을 통합하여 다양한 실제 조건에서 견고한 성능을 제공합니다.

## 🎯 주요 포인트

- 1. 본 논문은 CAD 모델 기반의 물체의 손 안에서의 자세 추정을 위한 새로운 3단계 프레임워크를 제안합니다.

- 2. 제안된 프레임워크는 포즈 후보군의 샘플링 및 사전 순위 결정, 반복적 세부 조정, 최종 순위 결정을 포함합니다.

- 3. 통합된 에너지 기반 확산 모델을 통해 포즈 추정의 정밀도를 높이고, 시뮬레이션 데이터로만 훈련됩니다.

- 4. 에너지 기반 점수 네트워크에 렌더-비교 아키텍처를 도입하여 시뮬레이션에서 실제 환경으로의 성능을 크게 향상시켰습니다.

- 5. 제안된 방법은 기존의 회귀, 매칭, 등록 기술을 능가하며, 새로운 CAD 모델에 대한 강력한 범주 내 일반화 성능을 보입니다.

---

*Generated on 2025-09-22 15:28:23*