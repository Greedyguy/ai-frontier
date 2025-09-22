# GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation

**Korean Title:** GP3: 로봇 조작을 위한 다중 뷰 이미지를 활용한 3D 기하학 인식 정책

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multi-view Observations, Spatial Encoder

## 🔗 유사한 논문
- [[2025-09-19/GAF_ Gaussian Action Field as a Dynamic World Model for Robotic Manipulation_20250919|GAF Gaussian Action Field as a Dynamic World Model for Robotic Manipulation]] (85.0% similar)
- [[2025-09-17/Prompt2Auto_ From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning_20250917|Prompt2Auto From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning]] (84.6% similar)
- [[2025-09-18/PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (84.2% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (84.0% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (82.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15733v1 Announce Type: cross 
Abstract: Effective robotic manipulation relies on a precise understanding of 3D scene geometry, and one of the most straightforward ways to acquire such geometry is through multi-view observations. Motivated by this, we present GP3 -- a 3D geometry-aware robotic manipulation policy that leverages multi-view input. GP3 employs a spatial encoder to infer dense spatial features from RGB observations, which enable the estimation of depth and camera parameters, leading to a compact yet expressive 3D scene representation tailored for manipulation. This representation is fused with language instructions and translated into continuous actions via a lightweight policy head. Comprehensive experiments demonstrate that GP3 consistently outperforms state-of-the-art methods on simulated benchmarks. Furthermore, GP3 transfers effectively to real-world robots without depth sensors or pre-mapped environments, requiring only minimal fine-tuning. These results highlight GP3 as a practical, sensor-agnostic solution for geometry-aware robotic manipulation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15733v1 발표 유형: 교차  
초록: 효과적인 로봇 조작은 3D 장면 기하학에 대한 정확한 이해에 의존하며, 이러한 기하학을 획득하는 가장 간단한 방법 중 하나는 다중 시점 관찰을 통해서입니다. 이에 영감을 받아, 우리는 다중 시점 입력을 활용하는 3D 기하학 인식 로봇 조작 정책인 GP3를 제안합니다. GP3는 RGB 관찰로부터 밀집 공간 특징을 추론하기 위해 공간 인코더를 사용하며, 이를 통해 깊이 및 카메라 매개변수를 추정하여 조작에 적합한 간결하면서도 표현력 있는 3D 장면 표현을 생성합니다. 이 표현은 언어 지시와 결합되어 경량 정책 헤드를 통해 연속적인 행동으로 변환됩니다. 종합적인 실험을 통해 GP3가 시뮬레이션 벤치마크에서 최첨단 방법들을 일관되게 능가함을 보여줍니다. 더욱이, GP3는 깊이 센서나 사전 매핑된 환경 없이도 실제 로봇에 효과적으로 전이되며, 최소한의 미세 조정만 필요로 합니다. 이러한 결과는 GP3가 기하학 인식 로봇 조작을 위한 실용적이고 센서에 구애받지 않는 솔루션임을 강조합니다.

## 📝 요약

이 논문에서는 다중 관찰을 활용한 3D 기하학적 이해를 통해 로봇 조작을 개선하는 GP3라는 정책을 제안합니다. GP3는 RGB 관찰에서 밀도 있는 공간 특징을 추론하는 공간 인코더를 사용하여 깊이와 카메라 매개변수를 추정하고, 이를 통해 조작에 적합한 3D 장면 표현을 생성합니다. 이 표현은 언어 지시와 결합되어 연속적인 행동으로 변환됩니다. 실험 결과, GP3는 시뮬레이션 벤치마크에서 최신 기법들을 능가하며, 깊이 센서나 사전 매핑된 환경 없이도 실제 로봇에 효과적으로 적용될 수 있음을 보여주었습니다. 이는 GP3가 센서에 구애받지 않는 실용적인 기하학 인식 로봇 조작 솔루션임을 강조합니다.

## 🎯 주요 포인트

- 1. GP3는 다중 시점 입력을 활용하여 3D 기하학적 정보를 이해하는 로봇 조작 정책을 제안합니다.

- 2. GP3는 RGB 관찰에서 밀집 공간 특징을 추론하여 깊이 및 카메라 매개변수를 추정합니다.

- 3. 이 시스템은 언어 지침과 결합하여 연속적인 행동으로 변환하는 경량 정책 헤드를 사용합니다.

- 4. GP3는 시뮬레이션 벤치마크에서 최첨단 방법들을 일관되게 능가하는 성능을 보입니다.

- 5. GP3는 깊이 센서나 사전 매핑된 환경 없이도 최소한의 미세 조정으로 실제 로봇에 효과적으로 적용됩니다.

---

*Generated on 2025-09-22 14:09:33*