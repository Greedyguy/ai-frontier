---
keywords:
  - Large Language Models
  - Constrained Decoding
  - Instruction Recommendation
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:51:47.741413",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Constrained Decoding",
    "Instruction Recommendation"
  ],
  "rejected_keywords": [
    "Template-Augmented Reasoning"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Constrained Decoding": 0.75,
    "Instruction Recommendation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# MIRA: Empowering One-Touch AI Services on Smartphones with MLLM-based Instruction Recommendation

**Korean Title:** MIRA: MLLM 기반의 지시 추천을 통해 스마트폰에서 원터치 AI 서비스를 강화하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Constrained Decoding|prefix-tree-based constrained decoding]]
**⚡ Unique Technical**: [[keywords/Instruction Recommendation|instruction recommendation]]

## 🔗 유사한 논문
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (80.6% similar)
- [[AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (79.4% similar)
- [[WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (79.4% similar)
- [[Synthetic Data Generation for Screen Time and App Usage_20250917|Synthetic Data Generation for Screen Time and App Usage]] (79.3% similar)
- [[MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (79.3% similar)

## 📋 저자 정보

**Authors:** Zhipeng Bian, Jieming Zhu, Xuyang Xie, Quanyu Dai, Zhou Zhao, Zhenhua Dong

## 📄 Abstract (원문)

The rapid advancement of generative AI technologies is driving the
integration of diverse AI-powered services into smartphones, transforming how
users interact with their devices. To simplify access to predefined AI
services, this paper introduces MIRA, a pioneering framework for task
instruction recommendation that enables intuitive one-touch AI tasking on
smartphones. With MIRA, users can long-press on images or text objects to
receive contextually relevant instruction recommendations for executing AI
tasks. Our work introduces three key innovations: 1) A multimodal large
language model (MLLM)-based recommendation pipeline with structured reasoning
to extract key entities, infer user intent, and generate precise instructions;
2) A template-augmented reasoning mechanism that integrates high-level
reasoning templates, enhancing task inference accuracy; 3) A prefix-tree-based
constrained decoding strategy that restricts outputs to predefined instruction
candidates, ensuring coherent and intent-aligned suggestions. Through
evaluation using a real-world annotated datasets and a user study, MIRA has
demonstrated substantial improvements in the accuracy of instruction
recommendation. The encouraging results highlight MIRA's potential to
revolutionize the way users engage with AI services on their smartphones,
offering a more seamless and efficient experience.

## 🔍 Abstract (한글 번역)

생성 AI 기술의 급속한 발전은 다양한 AI 기반 서비스를 스마트폰에 통합하여 사용자가 기기와 상호작용하는 방식을 변화시키고 있습니다. 이 논문에서는 사전 정의된 AI 서비스에 대한 접근을 간소화하기 위해 스마트폰에서 직관적인 원터치 AI 작업을 가능하게 하는 작업 지시 추천을 위한 선구적인 프레임워크인 MIRA를 소개합니다. MIRA를 통해 사용자는 이미지나 텍스트 객체를 길게 눌러 AI 작업을 실행하기 위한 맥락에 맞는 지시 추천을 받을 수 있습니다. 우리의 연구는 세 가지 주요 혁신을 도입합니다: 1) 주요 엔티티를 추출하고 사용자 의도를 추론하며 정확한 지시를 생성하기 위한 구조적 추론을 갖춘 다중 모달 대형 언어 모델(MLLM) 기반 추천 파이프라인; 2) 고급 추론 템플릿을 통합하여 작업 추론 정확성을 향상시키는 템플릿 보강 추론 메커니즘; 3) 사전 정의된 지시 후보로 출력을 제한하여 일관되고 의도에 맞는 제안을 보장하는 접두사 트리 기반 제한 디코딩 전략. 실제 주석 데이터셋과 사용자 연구를 통한 평가를 통해 MIRA는 지시 추천의 정확성을 크게 향상시켰음을 입증했습니다. 고무적인 결과는 MIRA가 스마트폰에서 AI 서비스를 이용하는 방식을 혁신할 잠재력을 지니고 있으며, 보다 원활하고 효율적인 경험을 제공할 수 있음을 강조합니다.

## 📝 요약

이 논문은 스마트폰에서 AI 서비스의 직관적인 사용을 돕기 위한 MIRA라는 프레임워크를 소개합니다. MIRA는 사용자가 이미지나 텍스트 객체를 길게 눌러 AI 작업을 위한 맥락에 맞는 지침을 추천받을 수 있게 합니다. 주요 기여는 다음과 같습니다: 1) 멀티모달 대형 언어 모델(MLLM)을 기반으로 한 추천 파이프라인을 통해 사용자 의도를 추론하고 정확한 지침을 생성합니다. 2) 고수준의 추론 템플릿을 통합하여 작업 추론의 정확성을 높이는 템플릿 보강 추론 메커니즘을 도입했습니다. 3) 접두사 트리 기반의 제한된 디코딩 전략을 사용하여 일관되고 의도에 맞는 지침을 제공합니다. 실제 데이터셋과 사용자 연구를 통해 MIRA는 지침 추천의 정확성을 크게 향상시켰으며, 이는 스마트폰에서 AI 서비스와의 상호작용을 혁신할 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. MIRA는 스마트폰에서 직관적인 원터치 AI 작업을 가능하게 하는 혁신적인 프레임워크입니다.

- 2. MIRA는 멀티모달 대형 언어 모델(MLLM)을 기반으로 사용자 의도를 추론하고 정확한 지시를 생성하는 추천 파이프라인을 도입합니다.

- 3. 고차원 추론 템플릿을 통합한 템플릿 보강 추론 메커니즘을 통해 작업 추론 정확도를 향상시킵니다.

- 4. 접두사 트리 기반의 제한된 디코딩 전략을 사용하여 사전 정의된 지시 후보로 출력을 제한하여 일관되고 의도에 맞는 제안을 보장합니다.

- 5. 실제 데이터셋과 사용자 연구를 통해 MIRA는 지시 추천의 정확성을 크게 향상시켰음을 입증했습니다.

---

*Generated on 2025-09-20 09:34:07*