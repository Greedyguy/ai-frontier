---
keywords:
  - Stochastic Zero-Order Optimization
  - Neural Networks
  - Hybrid Architectures
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:21:01.708043",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Zero-Order Optimization",
    "Neural Networks",
    "Hybrid Architectures"
  ],
  "rejected_keywords": [
    "Low-Rank Surrogate Modeling",
    "Computer Vision"
  ],
  "similarity_scores": {
    "Stochastic Zero-Order Optimization": 0.85,
    "Neural Networks": 0.9,
    "Hybrid Architectures": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers

**Korean Title:** 저차원 대리 모델링 및 확률적 제로 차수 최적화를 통한 블랙박스 계층을 가진 신경망의 훈련

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|Neural Networks]]
**⚡ Unique Technical**: [[keywords/Stochastic Zero-Order Optimization|Stochastic Zero-Order Optimization]]
**🚀 Evolved Concepts**: [[keywords/Hybrid Architectures|Hybrid Architectures]]

## 🔗 유사한 논문
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (82.5% similar)
- [[MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (81.4% similar)
- [[Reinforcement Learning Agent for a 2D Shooter Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (81.1% similar)
- [[Physically-based Lighting Generation for Robotic Manipulation_20250919|Physically-based Lighting Generation for Robotic Manipulation]] (80.6% similar)
- [[Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (80.4% similar)

## 📋 저자 정보

**Authors:** Andrei Chertkov, Artem Basharin, Mikhail Saygin, Evgeny Frolov, Stanislav Straupe, Ivan Oseledets

## 📄 Abstract (원문)

The growing demand for energy-efficient, high-performance AI systems has led
to increased attention on alternative computing platforms (e.g., photonic,
neuromorphic) due to their potential to accelerate learning and inference.
However, integrating such physical components into deep learning pipelines
remains challenging, as physical devices often offer limited expressiveness,
and their non-differentiable nature renders on-device backpropagation difficult
or infeasible. This motivates the development of hybrid architectures that
combine digital neural networks with reconfigurable physical layers, which
effectively behave as black boxes. In this work, we present a framework for the
end-to-end training of such hybrid networks. This framework integrates
stochastic zeroth-order optimization for updating the physical layer's internal
parameters with a dynamic low-rank surrogate model that enables gradient
propagation through the physical layer. A key component of our approach is the
implicit projector-splitting integrator algorithm, which updates the
lightweight surrogate model after each forward pass with minimal hardware
queries, thereby avoiding costly full matrix reconstruction. We demonstrate our
method across diverse deep learning tasks, including: computer vision, audio
classification, and language modeling. Notably, across all modalities, the
proposed approach achieves near-digital baseline accuracy and consistently
enables effective end-to-end training of hybrid models incorporating various
non-differentiable physical components (spatial light modulators, microring
resonators, and Mach-Zehnder interferometers). This work bridges hardware-aware
deep learning and gradient-free optimization, thereby offering a practical
pathway for integrating non-differentiable physical components into scalable,
end-to-end trainable AI systems.

## 🔍 Abstract (한글 번역)

에너지 효율적이고 고성능의 AI 시스템에 대한 수요가 증가함에 따라 학습과 추론을 가속화할 잠재력을 가진 대체 컴퓨팅 플랫폼(예: 광자, 뉴로모픽)에 대한 관심이 증가하고 있습니다. 그러나 이러한 물리적 구성 요소를 딥러닝 파이프라인에 통합하는 것은 여전히 도전적입니다. 이는 물리적 장치가 종종 표현력이 제한적이며, 비미분 가능성으로 인해 장치 내 역전파가 어렵거나 불가능하기 때문입니다. 이러한 문제는 디지털 신경망과 재구성 가능한 물리적 층을 결합한 하이브리드 아키텍처의 개발을 촉진합니다. 이러한 물리적 층은 효과적으로 블랙박스처럼 작동합니다. 본 연구에서는 이러한 하이브리드 네트워크의 종단 간 훈련을 위한 프레임워크를 제시합니다. 이 프레임워크는 물리적 층의 내부 매개변수를 업데이트하기 위한 확률적 영차 최적화와 물리적 층을 통한 그래디언트 전파를 가능하게 하는 동적 저랭크 대리 모델을 통합합니다. 우리의 접근 방식의 핵심 요소는 암시적 프로젝터-분할 적분 알고리즘으로, 각 순방향 패스 후에 최소한의 하드웨어 쿼리로 경량 대리 모델을 업데이트하여 비용이 많이 드는 전체 행렬 재구성을 피합니다. 우리는 컴퓨터 비전, 오디오 분류, 언어 모델링을 포함한 다양한 딥러닝 작업에서 우리의 방법을 입증합니다. 특히 모든 모달리티에서 제안된 접근 방식은 거의 디지털 기준 정확도를 달성하며, 다양한 비미분 가능 물리적 구성 요소(공간 광 변조기, 마이크로링 공진기, 마하-젠더 간섭계)를 통합한 하이브리드 모델의 효과적인 종단 간 훈련을 일관되게 가능하게 합니다. 이 연구는 하드웨어 인식 딥러닝과 그래디언트 없는 최적화를 연결하여, 비미분 가능 물리적 구성 요소를 확장 가능하고 종단 간 훈련 가능한 AI 시스템에 통합하기 위한 실용적인 경로를 제공합니다.

## 📝 요약

이 논문은 에너지 효율적이고 고성능인 AI 시스템을 위해 디지털 신경망과 재구성 가능한 물리적 계층을 결합한 하이브리드 아키텍처의 종단 간 훈련 프레임워크를 제안합니다. 물리적 계층의 내부 매개변수를 업데이트하기 위해 확률적 영차 최적화를 사용하고, 동적 저랭크 대리 모델을 통해 물리적 계층의 그래디언트 전파를 가능하게 합니다. 핵심은 암시적 투영 분할 적분 알고리즘으로, 하드웨어 쿼리를 최소화하여 경량 대리 모델을 업데이트합니다. 이 방법은 컴퓨터 비전, 오디오 분류, 언어 모델링 등 다양한 딥러닝 작업에서 디지털 기준과 유사한 정확도를 달성하며, 비분화 가능한 물리적 구성 요소를 포함한 하이브리드 모델의 효과적인 훈련을 가능하게 합니다. 이를 통해 하드웨어 인식 딥러닝과 그래디언트 없는 최적화를 연결하여 확장 가능한 AI 시스템에 물리적 구성 요소를 통합할 수 있는 실용적인 경로를 제공합니다.

## 🎯 주요 포인트

- 1. 에너지 효율적이고 고성능인 AI 시스템에 대한 수요 증가로 인해 광자 및 신경형 컴퓨팅 플랫폼과 같은 대안적 컴퓨팅 플랫폼에 대한 관심이 증가하고 있습니다.

- 2. 비차별화 물리적 장치의 통합은 어려움을 초래하며, 이를 해결하기 위해 디지털 신경망과 재구성 가능한 물리적 레이어를 결합한 하이브리드 아키텍처가 제안되었습니다.

- 3. 본 연구는 하이브리드 네트워크의 종단 간 훈련을 위한 프레임워크를 제시하며, 이는 물리적 레이어의 내부 매개변수를 업데이트하기 위한 확률적 영차 최적화와 동적 저랭크 대리 모델을 통합합니다.

- 4. 암시적 투영 분할 적분기 알고리즘을 사용하여 하드웨어 쿼리를 최소화하면서 경량 대리 모델을 업데이트하여 비용이 많이 드는 전체 행렬 재구성을 피합니다.

- 5. 제안된 방법은 컴퓨터 비전, 오디오 분류, 언어 모델링 등 다양한 딥러닝 작업에서 거의 디지털 기준 정확도를 달성하며, 비차별화 물리적 구성 요소를 통합한 하이브리드 모델의 효과적인 종단 간 훈련을 가능하게 합니다.

---

*Generated on 2025-09-20 01:00:40*