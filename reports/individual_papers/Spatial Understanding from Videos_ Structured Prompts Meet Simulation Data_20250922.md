# Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

**Korean Title:** 비디오로부터의 공간 이해: 구조화된 프롬프트와 시뮬레이션 데이터의 만남

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language Models

## 🔗 유사한 논문
- [[2025-09-22/See&Trek_ Training-Free Spatial Prompting for Multimodal Large Language Model_20250922|See&Trek Training-Free Spatial Prompting for Multimodal Large Language Model]] (85.3% similar)
- [[2025-09-22/GRE Suite_ Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains_20250922|GRE Suite Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains]] (84.7% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (83.1% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (83.0% similar)
- [[2025-09-22/SmolRGPT_ Efficient Spatial Reasoning for Warehouse Environments with 600M Parameters_20250922|SmolRGPT Efficient Spatial Reasoning for Warehouse Environments with 600M Parameters]] (82.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.03642v2 Announce Type: replace-cross 
Abstract: Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction. However, existing methods face spatial uncertainty and data scarcity, limiting the 3D spatial reasoning capability of pre-trained vision-language models (VLMs). To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture. This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built from diverse 3D simulation scenes through an automated construction process designed for fine-tuning. Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research on visual-spatial understanding.

## 🔍 Abstract (한글 번역)

arXiv:2506.03642v2 발표 유형: 교차 교체  
초록: 시각-공간적 이해, 즉 시각 입력으로부터 객체 관계와 배치를 추론하는 능력은 로봇 내비게이션 및 구현된 상호작용과 같은 후속 작업에 필수적입니다. 그러나 기존 방법들은 공간적 불확실성과 데이터 부족에 직면하여 사전 학습된 비전-언어 모델(VLMs)의 3D 공간 추론 능력을 제한합니다. 이러한 문제를 해결하기 위해, 우리는 사전 학습된 VLMs의 아키텍처를 수정하지 않고 3D 공간 추론을 향상시키기 위한 통합 프레임워크를 제시합니다. 이 프레임워크는 복잡한 장면과 질문을 해석 가능한 추론 단계로 분해하는 구조화된 프롬프트 전략인 SpatialMind와, 미세 조정을 위해 설계된 자동화된 구축 과정을 통해 다양한 3D 시뮬레이션 장면에서 구축된 확장 가능한 질문-응답 데이터셋인 ScanForgeQA를 결합합니다. 여러 벤치마크에 걸친 광범위한 실험은 우리의 프롬프트 및 미세 조정 전략의 개별적 및 결합된 효과를 입증하며, 시각-공간적 이해에 대한 미래 연구에 영감을 줄 수 있는 통찰력을 제공합니다.

## 📝 요약

이 논문은 사전 학습된 비전-언어 모델(VLM)의 3D 공간 추론 능력을 향상시키기 위한 통합 프레임워크를 제안합니다. 기존 방법들이 공간적 불확실성과 데이터 부족 문제를 겪는 반면, 이 연구는 VLM의 구조를 변경하지 않고도 이러한 문제를 해결하고자 합니다. 제안된 프레임워크는 복잡한 장면과 질문을 해석 가능한 추론 단계로 분해하는 구조적 프롬프트 전략인 SpatialMind와 다양한 3D 시뮬레이션 장면에서 자동으로 구축된 대규모 질문-응답 데이터셋인 ScanForgeQA를 결합합니다. 여러 벤치마크를 통한 실험 결과, 프롬프트와 미세 조정 전략의 개별적 및 결합적 효과가 입증되었으며, 이는 향후 시각-공간 이해 연구에 영감을 줄 수 있는 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 시각-공간적 이해는 로봇 내비게이션 및 구현된 상호작용과 같은 다운스트림 작업에 필수적이다.

- 2. 기존 방법은 공간적 불확실성과 데이터 부족 문제로 인해 사전 학습된 비전-언어 모델의 3D 공간 추론 능력이 제한된다.

- 3. SpatialMind는 복잡한 장면과 질문을 해석 가능한 추론 단계로 분해하는 구조화된 프롬프트 전략이다.

- 4. ScanForgeQA는 다양한 3D 시뮬레이션 장면에서 자동화된 구축 과정을 통해 만들어진 확장 가능한 질문-응답 데이터셋이다.

- 5. 여러 벤치마크에서의 광범위한 실험은 프롬프트 및 미세 조정 전략의 개별 및 결합된 효과를 입증한다.

---

*Generated on 2025-09-22 14:53:20*