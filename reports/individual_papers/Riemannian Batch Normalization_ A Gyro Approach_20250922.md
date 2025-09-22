# Riemannian Batch Normalization: A Gyro Approach

**Korean Title:** 리만 배치 정규화: 자이로 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Riemannian Batch Normalization

## 🔗 유사한 논문
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (81.5% similar)
- [[2025-09-17/A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (79.5% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (78.9% similar)
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3 A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (78.8% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (78.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07115v2 Announce Type: replace-cross 
Abstract: Normalization layers are crucial for deep learning, but their Euclidean formulations are inadequate for data on manifolds. On the other hand, many Riemannian manifolds in machine learning admit gyro-structures, enabling principled extensions of Euclidean neural networks to non-Euclidean domains. Inspired by this, we introduce GyroBN, a principled Riemannian batch normalization framework for gyrogroups. We establish two necessary conditions, namely \emph{pseudo-reduction} and \emph{gyroisometric gyrations}, that guarantee GyroBN with theoretical control over sample statistics, and show that these conditions hold for all known gyrogroups in machine learning. Our framework also incorporates several existing Riemannian normalization methods as special cases. We further instantiate GyroBN on seven representative geometries, including the Grassmannian, five constant curvature spaces, and the correlation manifold, and derive novel gyro and Riemannian structures to enable these instantiations. Experiments across these geometries demonstrate the effectiveness of GyroBN. The code is available at https://github.com/GitZH-Chen/GyroBN.git.

## 🔍 Abstract (한글 번역)

arXiv:2509.07115v2 발표 유형: 교차 교체  
초록: 정규화 계층은 딥러닝에서 중요하지만, 유클리드 공식은 다양체 상의 데이터에 적합하지 않습니다. 반면, 머신러닝의 많은 리만 다양체는 자이로 구조를 허용하여 유클리드 신경망을 비유클리드 영역으로 원칙적으로 확장할 수 있게 합니다. 이에 영감을 받아, 우리는 자이로그룹을 위한 원칙적인 리만 배치 정규화 프레임워크인 GyroBN을 소개합니다. 우리는 샘플 통계에 대한 이론적 제어를 보장하는 두 가지 필수 조건, 즉 \emph{의사 축소}와 \emph{자이로등거리 자이레이션}을 확립하고, 이러한 조건이 머신러닝의 모든 알려진 자이로그룹에 대해 성립함을 보여줍니다. 우리의 프레임워크는 또한 여러 기존의 리만 정규화 방법을 특수 사례로 포함합니다. 우리는 또한 Grassmann 다양체, 다섯 개의 상수 곡률 공간, 상관 다양체를 포함한 일곱 가지 대표적인 기하학에 GyroBN을 구현하고, 이러한 구현을 가능하게 하는 새로운 자이로 및 리만 구조를 도출합니다. 이러한 기하학 전반에 걸친 실험은 GyroBN의 효과를 입증합니다. 코드는 https://github.com/GitZH-Chen/GyroBN.git에서 사용할 수 있습니다.

## 📝 요약

이 논문은 비유클리드 도메인에서의 신경망 확장을 위해 고안된 Riemannian 배치 정규화 프레임워크인 GyroBN을 소개합니다. GyroBN은 gyro-구조를 활용하여 유클리드 신경망을 Riemannian 다양체로 확장하며, \emph{pseudo-reduction}과 \emph{gyroisometric gyrations}라는 두 가지 조건을 통해 샘플 통계에 대한 이론적 제어를 보장합니다. 이 프레임워크는 기존의 여러 Riemannian 정규화 방법을 포함하며, Grassmannian, 상수 곡률 공간, 상관성 다양체 등 7개의 대표적인 기하학에 적용됩니다. 실험 결과, GyroBN의 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. GyroBN은 비유클리드 영역으로의 신경망 확장을 위한 리만 배치 정규화 프레임워크입니다.

- 2. GyroBN은 \emph{pseudo-reduction}과 \emph{gyroisometric gyrations}라는 두 가지 조건을 통해 샘플 통계에 대한 이론적 제어를 보장합니다.

- 3. 이 프레임워크는 기존의 여러 리만 정규화 방법을 특수한 경우로 포함합니다.

- 4. GyroBN은 Grassmannian, 상수 곡률 공간, 상관 행렬 다양체를 포함한 7개의 대표적인 기하학에 적용되었습니다.

- 5. 실험 결과, 다양한 기하학에서 GyroBN의 효과가 입증되었습니다.

---

*Generated on 2025-09-22 15:02:27*