# Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning

**Korean Title:** 적응형 LoRA 전문가 할당 및 선택을 위한 연합 미세 조정

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Lei Wang|Lei Wang]] [[authors/Jieming Bian|Jieming Bian]] [[authors/Letian Zhang|Letian Zhang]] [[authors/Jie Xu|Jie Xu]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Mixture-of-Experts

## 🔗 유사한 논문
- [[LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (82.6% similar)
- [[FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (82.1% similar)
- [[Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (81.8% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.8% similar)
- [[FURINA_ Free from Unmergeable Router via LINear Aggregation of mixed experts_20250919|FURINA Free from Unmergeable Router via LINear Aggregation of mixed experts]] (81.4% similar)

## 📋 저자 정보

**Authors:** Lei Wang, Jieming Bian, Letian Zhang, Jie Xu

## 📄 Abstract (원문)

Large Language Models (LLMs) have demonstrated impressive capabilities across
various tasks, but fine-tuning them for domain-specific applications often
requires substantial domain-specific data that may be distributed across
multiple organizations. Federated Learning (FL) offers a privacy-preserving
solution, but faces challenges with computational constraints when applied to
LLMs. Low-Rank Adaptation (LoRA) has emerged as a parameter-efficient
fine-tuning approach, though a single LoRA module often struggles with
heterogeneous data across diverse domains. This paper addresses two critical
challenges in federated LoRA fine-tuning: 1. determining the optimal number and
allocation of LoRA experts across heterogeneous clients, and 2. enabling
clients to selectively utilize these experts based on their specific data
characteristics. We propose FedLEASE (Federated adaptive LoRA Expert Allocation
and SElection), a novel framework that adaptively clusters clients based on
representation similarity to allocate and train domain-specific LoRA experts.
It also introduces an adaptive top-$M$ Mixture-of-Experts mechanism that allows
each client to select the optimal number of utilized experts. Our extensive
experiments on diverse benchmark datasets demonstrate that FedLEASE
significantly outperforms existing federated fine-tuning approaches in
heterogeneous client settings while maintaining communication efficiency.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)은 다양한 작업에서 인상적인 능력을 보여주었지만, 특정 분야에 맞춘 응용 프로그램을 위해 미세 조정하는 데는 여러 조직에 분산되어 있을 수 있는 상당한 양의 분야별 데이터가 필요합니다. 연합 학습(FL)은 프라이버시를 보호하는 솔루션을 제공하지만, LLM에 적용할 때는 계산 제약과 같은 문제에 직면합니다. 저랭크 적응(LoRA)은 매개변수 효율적인 미세 조정 접근법으로 부상했지만, 단일 LoRA 모듈은 다양한 도메인에 걸친 이질적인 데이터에서 종종 어려움을 겪습니다. 본 논문은 연합 LoRA 미세 조정에서 두 가지 중요한 과제를 다룹니다: 1. 이질적인 클라이언트 간의 최적의 LoRA 전문가 수와 할당을 결정하는 것, 2. 클라이언트가 특정 데이터 특성에 따라 이러한 전문가를 선택적으로 활용할 수 있도록 하는 것. 우리는 FedLEASE(Federated adaptive LoRA Expert Allocation and SElection)라는 새로운 프레임워크를 제안하며, 이는 표현 유사성에 기반하여 클라이언트를 적응적으로 클러스터링하여 분야별 LoRA 전문가를 할당하고 훈련합니다. 또한 각 클라이언트가 최적의 전문가 수를 선택할 수 있도록 하는 적응형 상위-$M$ 전문가 혼합 메커니즘을 도입합니다. 다양한 벤치마크 데이터셋에 대한 우리의 광범위한 실험은 FedLEASE가 이질적인 클라이언트 환경에서 기존의 연합 미세 조정 접근법보다 통신 효율성을 유지하면서도 성능이 크게 향상됨을 보여줍니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 도메인 특화 애플리케이션을 위한 연합 학습(FL)과 저랭크 적응(LoRA)의 결합을 다룹니다. 주요 기여는 FedLEASE라는 새로운 프레임워크를 제안한 것으로, 이는 클라이언트를 표현 유사성에 따라 클러스터링하여 도메인 특화 LoRA 전문가를 할당하고 훈련합니다. 또한, 클라이언트가 데이터 특성에 맞는 최적의 전문가 수를 선택할 수 있는 적응형 전문가 선택 메커니즘을 도입했습니다. 다양한 벤치마크 데이터셋에서의 실험 결과, FedLEASE는 기존의 연합 미세 조정 방법보다 이질적인 클라이언트 환경에서 성능이 뛰어나고 통신 효율성도 유지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 도메인 특화 애플리케이션을 위한 미세 조정에는 다수의 조직에 분산된 상당한 양의 도메인 특화 데이터가 필요합니다.

- 2. 연합 학습(FL)은 프라이버시를 보장하는 솔루션을 제공하지만, LLM에 적용할 때 계산 제약 문제에 직면합니다.

- 3. LoRA는 파라미터 효율적인 미세 조정 접근법으로 부상했으나, 단일 LoRA 모듈은 다양한 도메인의 이질적인 데이터 처리에 어려움을 겪습니다.

- 4. FedLEASE는 표현 유사성에 기반하여 클라이언트를 적응적으로 클러스터링하고 도메인 특화 LoRA 전문가를 할당 및 훈련하는 새로운 프레임워크입니다.

- 5. FedLEASE는 다양한 벤치마크 데이터셋에서 기존의 연합 미세 조정 접근법보다 뛰어난 성능을 보이며, 통신 효율성을 유지합니다.

---

*Generated on 2025-09-20 01:04:15*