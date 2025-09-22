# Space Group Equivariant Crystal Diffusion

**Korean Title:** 공간군 등변 결정 확산

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Space Group Equivariant Diffusion

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2 Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (80.4% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (78.6% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff Accelerating Diffusion Model Inference with Self-Speculation]] (78.4% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (77.9% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (77.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.10994v2 Announce Type: replace-cross 
Abstract: Accelerating inverse design of crystalline materials with generative models has significant implications for a range of technologies. Unlike other atomic systems, 3D crystals are invariant to discrete groups of isometries called the space groups. Crucially, these space group symmetries are known to heavily influence materials properties. We propose SGEquiDiff, a crystal generative model which naturally handles space group constraints with space group invariant likelihoods. SGEquiD-iff consists of an SE(3)-invariant, telescoping discrete sampler of crystal lattices; permutation-invariant, transformer-based autoregressive sampling of Wyckoff positions, elements, and numbers of symmetrically unique atoms; and space group equivariant diffusion of atomic coordinates. We show that space group equivariant vector fields automatically live in the tangent spaces of the Wyckoff positions. SGEquiDiff achieves state-of-the-art performance on standard benchmark datasets as assessed by quantitative proxy metrics and quantum mechanical calculations. Our code is available at https://github.com/rees-c/sgequidiff.

## 🔍 Abstract (한글 번역)

arXiv:2505.10994v2 발표 유형: 교차 대체  
초록: 생성 모델을 활용한 결정성 물질의 역설계 가속화는 다양한 기술에 중대한 영향을 미칩니다. 다른 원자 시스템과 달리, 3D 결정은 공간군이라 불리는 이산 등거리 변환 그룹에 대해 불변성을 가집니다. 특히, 이러한 공간군 대칭은 물질의 특성에 큰 영향을 미치는 것으로 알려져 있습니다. 우리는 공간군 불변 가능성을 통해 공간군 제약을 자연스럽게 처리하는 결정 생성 모델인 SGEquiDiff를 제안합니다. SGEquiDiff는 SE(3)-불변의 망원경식 이산 샘플러를 사용하여 결정 격자를 생성하며, Wyckoff 위치, 원소, 대칭적으로 고유한 원자의 수에 대한 순열 불변의 트랜스포머 기반 자기회귀 샘플링 및 원자 좌표의 공간군 등변 확산을 포함합니다. 우리는 공간군 등변 벡터장이 자동으로 Wyckoff 위치의 접공간에 존재함을 보여줍니다. SGEquiDiff는 정량적 대리 메트릭과 양자 역학 계산에 의해 평가된 표준 벤치마크 데이터셋에서 최첨단 성능을 달성합니다. 우리의 코드는 https://github.com/rees-c/sgequidiff에서 확인할 수 있습니다.

## 📝 요약

SGEquiDiff는 결정질 물질의 역설계를 가속화하기 위한 생성 모델로, 공간군 대칭성을 자연스럽게 처리합니다. 이 모델은 SE(3) 불변성을 갖춘 결정 격자 샘플러와 변환기 기반의 Wyckoff 위치, 원소, 대칭적으로 독특한 원자의 순열 불변 샘플링, 그리고 원자 좌표의 공간군 등가 확산으로 구성됩니다. SGEquiDiff는 Wyckoff 위치의 접공간에서 자동으로 작동하는 공간군 등가 벡터장을 활용하여, 표준 벤치마크 데이터셋에서 최첨단 성능을 달성했습니다. 이 연구의 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. SGEquiDiff는 공간군 대칭을 자연스럽게 처리하는 결정 생성 모델로, 공간군 불변 가능성을 갖추고 있습니다.

- 2. 이 모델은 SE(3)-불변의 결정 격자 샘플러와 순열 불변의 트랜스포머 기반 오토리그레시브 샘플링을 통해 Wyckoff 위치, 원소, 대칭적으로 고유한 원자의 수를 처리합니다.

- 3. SGEquiDiff는 원자 좌표의 공간군 등가 확산을 수행하며, Wyckoff 위치의 접공간에 자동으로 존재하는 공간군 등가 벡터 필드를 보여줍니다.

- 4. 이 모델은 정량적 프록시 메트릭과 양자역학적 계산을 통해 표준 벤치마크 데이터셋에서 최첨단 성능을 달성했습니다.

- 5. SGEquiDiff의 코드는 https://github.com/rees-c/sgequidiff에서 공개되어 있습니다.

---

*Generated on 2025-09-22 14:48:22*