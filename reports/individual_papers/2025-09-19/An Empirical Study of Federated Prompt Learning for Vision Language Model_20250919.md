
# An Empirical Study of Federated Prompt Learning for Vision Language Model

**Korean Title:** 연합 프롬프트 학습을 위한 비전 언어 모델에 대한 실증적 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision Prompt Learning

## 🔗 유사한 논문
- [[An Empirical Analysis of VLM-based OOD Detection Mechanisms, Advantages, and Sensitivity]] (82.6% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (81.9% similar)
- [[Communication-Efficient and Privacy-Adaptable Mech_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (81.7% similar)
- [[Visible Yet Unreadable A Systematic Blind Spot of Vision Language Models Across Writing Systems]] (80.8% similar)
- [[A_Multi-Agent_LLM_Defense_Pipeline_Against_Prompt_Injection_Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23024v2 Announce Type: replace 
Abstract: The Vision Language Model (VLM) excels in aligning vision and language representations, and prompt learning has emerged as a key technique for adapting such models to downstream tasks. However, the application of prompt learning with VLM in federated learning (FL) scenarios remains underexplored. This paper systematically investigates the behavioral differences between language prompt learning (LPT) and vision prompt learning (VPT) under data heterogeneity challenges, including label skew and domain shift. We conduct extensive experiments to evaluate the impact of various FL and prompt configurations, such as client scale, aggregation strategies, and prompt length, to assess the robustness of Federated Prompt Learning (FPL). Furthermore, we explore strategies for enhancing prompt learning in complex scenarios where label skew and domain shift coexist, including leveraging both prompt types when computational resources allow. Our findings offer practical insights into optimizing prompt learning in federated settings, contributing to the broader deployment of VLMs in privacy-preserving environments.

## 🔍 Abstract (한글 번역)

arXiv:2505.23024v2 발표 유형: 교체  
초록: 비전 언어 모델(Vision Language Model, VLM)은 비전과 언어 표현을 정렬하는 데 뛰어나며, 프롬프트 학습은 이러한 모델을 다운스트림 작업에 적응시키는 주요 기술로 부상하고 있습니다. 그러나 연합 학습(FL) 시나리오에서 VLM과 함께 프롬프트 학습을 적용하는 것은 아직 충분히 탐구되지 않았습니다. 본 논문은 레이블 편향과 도메인 이동을 포함한 데이터 이질성 문제 하에서 언어 프롬프트 학습(LPT)과 비전 프롬프트 학습(VPT) 간의 행동 차이를 체계적으로 조사합니다. 우리는 클라이언트 규모, 집계 전략, 프롬프트 길이와 같은 다양한 FL 및 프롬프트 구성의 영향을 평가하기 위해 광범위한 실험을 수행하여 연합 프롬프트 학습(FPL)의 견고성을 평가합니다. 또한, 레이블 편향과 도메인 이동이 공존하는 복잡한 시나리오에서 프롬프트 학습을 향상시키기 위한 전략을 탐구하며, 계산 자원이 허용될 때 두 프롬프트 유형을 모두 활용하는 방법을 포함합니다. 우리의 연구 결과는 프라이버시를 보호하는 환경에서 VLM의 보다 광범위한 배포에 기여하며, 연합 설정에서 프롬프트 학습을 최적화하기 위한 실질적인 통찰력을 제공합니다.

## 📝 요약

이 논문은 비전 언어 모델(VLM)에서 프롬프트 학습을 연합 학습(FL) 시나리오에 적용하는 것에 대한 연구를 수행했습니다. 특히, 데이터의 불균형 문제인 레이블 편향과 도메인 이동 상황에서 언어 프롬프트 학습(LPT)과 비전 프롬프트 학습(VPT)의 행동 차이를 체계적으로 조사했습니다. 다양한 FL 및 프롬프트 설정, 클라이언트 규모, 집계 전략, 프롬프트 길이 등을 통해 연합 프롬프트 학습(FPL)의 강건성을 평가했습니다. 또한, 레이블 편향과 도메인 이동이 공존하는 복잡한 상황에서 프롬프트 학습을 향상시키기 위한 전략을 탐구했습니다. 연구 결과는 프라이버시를 보호하는 환경에서 VLM의 활용을 최적화하는 데 실질적인 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. Vision Language Model(VLM)은 시각과 언어 표현을 정렬하는 데 뛰어나며, 프롬프트 학습은 이러한 모델을 다운스트림 작업에 적응시키는 핵심 기술로 부상하고 있습니다.

- 2. 프롬프트 학습과 VLM의 연합 학습(FL) 시나리오에서의 적용은 아직 충분히 탐구되지 않았습니다.

- 3. 본 논문은 데이터 이질성 문제(레이블 편향 및 도메인 이동 포함) 하에서 언어 프롬프트 학습(LPT)과 시각 프롬프트 학습(VPT)의 행동 차이를 체계적으로 조사합니다.

- 4. 다양한 FL 및 프롬프트 구성(클라이언트 규모, 집계 전략, 프롬프트 길이 등)의 영향을 평가하여 연합 프롬프트 학습(FPL)의 강건성을 평가합니다.

- 5. 레이블 편향과 도메인 이동이 공존하는 복잡한 시나리오에서 프롬프트 학습을 향상시키기 위한 전략을 탐구하며, 이는 프라이버시를 보호하는 환경에서 VLM의 폭넓은 배포에 기여합니다.

---

*Generated on 2025-09-19 15:39:41*