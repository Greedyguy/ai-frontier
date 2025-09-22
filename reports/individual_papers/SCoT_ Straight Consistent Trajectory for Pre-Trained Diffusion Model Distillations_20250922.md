# SCoT: Straight Consistent Trajectory for Pre-Trained Diffusion Model Distillations

**Korean Title:** SCoT: 사전 훈련된 확산 모델 증류를 위한 직선 일관 궤적

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Consistent Projection Functions|Consistent Projection Functions]] [[keywords/specific/ODE Solvers|ODE Solvers]] [[keywords/broad/Diffusion Models|Diffusion Models]] [[keywords/unique/Straight Consistent Trajectory|Straight Consistent Trajectory]] [[categories/cs.LG|cs.LG]] [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (80.6% similar) [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (80.5% similar) [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery: Reinforced Distillation of Large Language Model Agents]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Consistent Projection Functions
**🔗 Specific Connectable**: Trajectory Consistency
**🔬 Broad Technical**: Diffusion Models
**⭐ Unique Technical**: Straight Consistent Trajectory
## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2 Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (80.6% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE Semantic-Aware Shared Sampling for Efficient Diffusion]] (80.5% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (80.3% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff Accelerating Diffusion Model Inference with Self-Speculation]] (80.0% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (79.8% similar)


**ArXiv ID**: [2502.16972](https://arxiv.org/abs/2502.16972)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2502.16972.pdf)


**ArXiv ID**: [2502.16972](https://arxiv.org/abs/2502.16972)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2502.16972.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Rectified Flow Method
**🔗 Specific Connectable**: Consistency Model Distillation
**⭐ Unique Technical**: Straight Consistent Trajectory
**🔬 Broad Technical**: Diffusion Models

## 🏷️ 추출된 키워드



`Diffusion Models` • 

`Consistency Model Distillation` • 

`Rectified Flow Method` • 

`Straight Consistent Trajectory`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.16972v2 Announce Type: replace-cross 
Abstract: Pre-trained diffusion models are commonly used to generate clean data (e.g., images) from random noises, effectively forming pairs of noises and corresponding clean images. Distillation on these pre-trained models can be viewed as the process of constructing advanced trajectories within the pair to accelerate sampling. For instance, consistency model distillation develops consistent projection functions to regulate trajectories, although sampling efficiency remains a concern. Rectified flow method enforces straight trajectories to enable faster sampling, yet relies on numerical ODE solvers, which may introduce approximation errors. In this work, we bridge the gap between the consistency model and the rectified flow method by proposing a Straight Consistent Trajectory~(SCoT) model. SCoT enjoys the benefits of both approaches for fast sampling, producing trajectories with consistent and straight properties simultaneously. These dual properties are strategically balanced by targeting two critical objectives: (1) regulating the gradient of SCoT's mapping to a constant, (2) ensuring trajectory consistency. Extensive experimental results demonstrate the effectiveness and efficiency of SCoT.

## 🔍 Abstract (한글 번역)

arXiv:2502.16972v2 발표 유형: 교체-교차  
초록: 사전 학습된 확산 모델은 일반적으로 무작위 노이즈로부터 깨끗한 데이터(예: 이미지)를 생성하는 데 사용되며, 이는 효과적으로 노이즈와 해당 깨끗한 이미지의 쌍을 형성합니다. 이러한 사전 학습된 모델에 대한 증류는 샘플링을 가속화하기 위해 쌍 내에서 고급 궤적을 구성하는 과정으로 볼 수 있습니다. 예를 들어, 일관성 모델 증류는 궤적을 조절하기 위해 일관된 투사 함수를 개발하지만 샘플링 효율성은 여전히 문제로 남아 있습니다. 수정된 흐름 방법은 더 빠른 샘플링을 가능하게 하기 위해 직선 궤적을 강제하지만, 근사 오류를 초래할 수 있는 수치적 ODE 해석기에 의존합니다. 본 연구에서는 일관성 모델과 수정된 흐름 방법 간의 간극을 연결하여 직선 일관 궤적(SCoT) 모델을 제안합니다. SCoT는 빠른 샘플링을 위해 두 접근 방식의 이점을 동시에 누리며, 일관성과 직선 속성을 가진 궤적을 생성합니다. 이러한 이중 속성은 두 가지 중요한 목표를 겨냥하여 전략적으로 균형을 맞춥니다: (1) SCoT의 매핑 기울기를 일정하게 조절, (2) 궤적의 일관성 보장. 광범위한 실험 결과는 SCoT의 효과성과 효율성을 입증합니다.

## 📝 요약

이 논문은 사전 학습된 확산 모델을 활용하여 노이즈로부터 깨끗한 데이터를 생성하는 과정에서 샘플링 효율성을 개선하는 방법을 제안합니다. 기존의 일관성 모델 증류와 수정된 흐름 방법의 장점을 결합한 SCoT(Straight Consistent Trajectory) 모델을 소개합니다. SCoT 모델은 일관성과 직선성을 동시에 유지하는 경로를 생성하여 빠른 샘플링을 가능하게 합니다. 이를 위해 SCoT의 매핑 기울기를 일정하게 조절하고 경로의 일관성을 보장하는 두 가지 목표를 설정합니다. 실험 결과, SCoT 모델은 효과적이고 효율적으로 작동함을 보여주었습니다.

## 🎯 주요 포인트


- 1. 사전 학습된 확산 모델은 무작위 노이즈에서 깨끗한 데이터를 생성하는 데 사용되며, 이는 노이즈와 대응되는 깨끗한 이미지의 쌍을 형성합니다.

- 2. 일관성 모델 증류는 일관된 투영 함수를 개발하여 샘플링 효율성 문제를 해결하려고 하지만, 여전히 샘플링 효율성은 문제로 남아 있습니다.

- 3. 교정된 흐름 방법은 직선 경로를 강제하여 더 빠른 샘플링을 가능하게 하지만, 수치적 ODE 해석기에 의존하여 근사 오류가 발생할 수 있습니다.

- 4. SCoT 모델은 일관성 모델과 교정된 흐름 방법의 장점을 결합하여 빠른 샘플링을 가능하게 하며, 일관성과 직선의 속성을 동시에 갖춘 경로를 생성합니다.

- 5. SCoT는 경로의 일관성을 보장하고, 매핑의 기울기를 일정하게 조절하는 두 가지 주요 목표를 통해 이러한 이중 속성을 전략적으로 균형 있게 유지합니다.


---

*Generated on 2025-09-22 16:10:48*