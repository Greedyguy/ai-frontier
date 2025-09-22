# Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale

**Korean Title:** 로봇 제어 스택: 대규모 로봇 학습을 위한 효율적인 생태계

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Tobias Jülg|Tobias Jülg]] [[authors/Pierre Krack|Pierre Krack]] [[authors/Seongjin Bien|Seongjin Bien]] [[authors/Yannik Blei|Yannik Blei]] [[authors/Khaled Gamal|Khaled Gamal]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language-Action Models

## 🔗 유사한 논문
- [[CLAW_ A Vision-Language-Action Framework for Weight-Aware Robotic Grasping_20250918|CLAW A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (83.1% similar)
- [[CollabVLA_ Self-Reflective Vision-Language-Action Model Dreaming Together with Human_20250919|CollabVLA Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (81.9% similar)
- [[Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (81.7% similar)
- [[ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (81.6% similar)
- [[TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (81.1% similar)

## 📋 저자 정보

**Authors:** Tobias Jülg, Pierre Krack, Seongjin Bien, Yannik Blei, Khaled Gamal, Ken Nakahara, Johannes Hechtl, Roberto Calandra, Wolfram Burgard, Florian Walter

## 📄 Abstract (원문)

Vision-Language-Action models (VLAs) mark a major shift in robot learning.
They replace specialized architectures and task-tailored components of expert
policies with large-scale data collection and setup-specific fine-tuning. In
this machine learning-focused workflow that is centered around models and
scalable training, traditional robotics software frameworks become a
bottleneck, while robot simulations offer only limited support for
transitioning from and to real-world experiments. In this work, we close this
gap by introducing Robot Control Stack (RCS), a lean ecosystem designed from
the ground up to support research in robot learning with large-scale generalist
policies. At its core, RCS features a modular and easily extensible layered
architecture with a unified interface for simulated and physical robots,
facilitating sim-to-real transfer. Despite its minimal footprint and
dependencies, it offers a complete feature set, enabling both real-world
experiments and large-scale training in simulation. Our contribution is
twofold: First, we introduce the architecture of RCS and explain its design
principles. Second, we evaluate its usability and performance along the
development cycle of VLA and RL policies. Our experiments also provide an
extensive evaluation of Octo, OpenVLA, and Pi Zero on multiple robots and shed
light on how simulation data can improve real-world policy performance. Our
code, datasets, weights, and videos are available at:
https://robotcontrolstack.github.io/

## 🔍 Abstract (한글 번역)

비전-언어-행동 모델(VLAs)은 로봇 학습에 있어 중요한 변화를 나타냅니다. 이 모델들은 전문가 정책의 특화된 아키텍처와 작업 맞춤형 구성 요소를 대규모 데이터 수집과 설정별 미세 조정으로 대체합니다. 모델 중심의 확장 가능한 훈련에 중점을 둔 이 기계 학습 중심 워크플로우에서는 전통적인 로봇 소프트웨어 프레임워크가 병목 현상이 되며, 로봇 시뮬레이션은 현실 세계 실험으로의 전환을 지원하는 데 한계가 있습니다. 본 연구에서는 대규모 일반 정책을 통한 로봇 학습 연구를 지원하기 위해 처음부터 설계된 간결한 생태계인 로봇 제어 스택(RCS)을 소개하여 이 격차를 해소합니다. RCS의 핵심은 모듈식이고 쉽게 확장 가능한 계층형 아키텍처로, 시뮬레이션 및 실제 로봇에 대한 통합 인터페이스를 제공하여 시뮬레이션에서 현실로의 전환을 용이하게 합니다. 최소한의 설치 공간과 종속성을 가지면서도, RCS는 현실 세계 실험과 시뮬레이션에서의 대규모 훈련을 모두 가능하게 하는 완전한 기능 세트를 제공합니다. 우리의 기여는 두 가지로 요약됩니다. 첫째, RCS의 아키텍처를 소개하고 그 설계 원칙을 설명합니다. 둘째, VLA 및 RL 정책의 개발 주기에서의 사용성과 성능을 평가합니다. 우리의 실험은 또한 여러 로봇에서 Octo, OpenVLA, Pi Zero의 광범위한 평가를 제공하며, 시뮬레이션 데이터가 현실 세계 정책 성능을 어떻게 향상시킬 수 있는지를 조명합니다. 우리의 코드, 데이터셋, 가중치, 비디오는 다음에서 확인할 수 있습니다: https://robotcontrolstack.github.io/

## 📝 요약

Vision-Language-Action(VLA) 모델은 로봇 학습에 혁신을 가져왔으나, 기존 로봇 소프트웨어는 한계가 있습니다. 이를 해결하기 위해, 우리는 대규모 일반 정책 연구를 지원하는 'Robot Control Stack(RCS)'를 개발했습니다. RCS는 모듈형 구조와 통합 인터페이스를 통해 시뮬레이션과 실제 로봇 간의 전환을 용이하게 하며, 최소한의 의존성으로도 실험과 대규모 시뮬레이션 훈련을 지원합니다. 우리는 RCS의 설계 원칙과 성능을 VLA 및 강화 학습 정책 개발 과정에서 평가했으며, 시뮬레이션 데이터가 실제 정책 성능을 향상시킬 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. Vision-Language-Action 모델(VLAs)은 로봇 학습에서 주요한 변화를 이끌고 있습니다.

- 2. Robot Control Stack(RCS)는 대규모 일반화 정책을 지원하기 위해 설계된 모듈식 생태계입니다.

- 3. RCS는 시뮬레이션과 실제 로봇을 위한 통합 인터페이스를 제공하여 sim-to-real 전환을 용이하게 합니다.

- 4. RCS는 최소한의 종속성을 가지면서도 실제 실험과 대규모 시뮬레이션 훈련을 모두 지원하는 완전한 기능 세트를 제공합니다.

- 5. 실험 결과, 시뮬레이션 데이터가 실제 정책 성능을 향상시킬 수 있음을 보여줍니다.

---

*Generated on 2025-09-20 02:42:42*