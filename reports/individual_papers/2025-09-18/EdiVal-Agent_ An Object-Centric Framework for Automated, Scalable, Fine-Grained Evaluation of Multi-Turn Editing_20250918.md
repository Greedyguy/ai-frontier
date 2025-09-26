---
keywords:
  - Vision-Language Models
  - Object Detectors
  - Human Preference Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13399
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:31:33.028212",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Models",
    "Object Detectors",
    "Human Preference Models"
  ],
  "rejected_keywords": [
    "Instruction-Based Image Editing",
    "Semantic-Level Feature Extractors"
  ],
  "similarity_scores": {
    "Vision-Language Models": 0.78,
    "Object Detectors": 0.77,
    "Human Preference Models": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# EdiVal-Agent: An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing

**Korean Title:** EdiVal-Agent: 다중 턴 편집의 자동화되고 확장 가능한 세밀한 평가를 위한 객체 중심 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision-Language Models|Vision-Language Models]], [[keywords/Object Detectors|Object Detectors]]
**⚡ Unique Technical**: [[keywords/Human Preference Models|Human Preference Models]]

## 🔗 유사한 논문
- [[Embodied Image Captioning Self-supervised Learning Agents for Spatially Coherent Image Descriptions]] (81.2% similar)
- [[DPDEdit Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing]] (80.6% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (80.4% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.2% similar)
- [[Iterative_Prompt_Refinement_for_Safer_Text-to-Image_Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (79.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13399v1 Announce Type: cross 
Abstract: Instruction-based image editing has advanced rapidly, yet reliable and interpretable evaluation remains a bottleneck. Current protocols either (i) depend on paired reference images -- resulting in limited coverage and inheriting biases from prior generative models -- or (ii) rely solely on zero-shot vision-language models (VLMs), whose prompt-based assessments of instruction following, content consistency, and visual quality are often imprecise.
  To address this, we introduce EdiVal-Agent, an automated, scalable, and fine-grained evaluation framework for multi-turn instruction-based editing from an object-centric perspective, supported by a suite of expert tools. Given an image, EdiVal-Agent first decomposes it into semantically meaningful objects, then synthesizes diverse, context-aware editing instructions. For evaluation, it integrates VLMs with open-vocabulary object detectors to assess instruction following, uses semantic-level feature extractors to evaluate content consistency, and leverages human preference models to judge visual quality. We show that combining VLMs with object detectors yields stronger agreement with human judgments in instruction-following evaluation compared to using VLMs alone and CLIP-based metrics. Furthermore, the pipeline's modular design allows future tools to be seamlessly integrated, enhancing evaluation accuracy over time.
  Instantiating this pipeline, we build EdiVal-Bench, a multi-turn editing benchmark covering 9 instruction types and 11 state-of-the-art editing models spanning autoregressive (AR) (including Nano Banana, GPT-Image-1), flow-matching, and diffusion paradigms. We demonstrate that EdiVal-Agent can be used to identify existing failure modes, thereby informing the development of the next generation of editing models. Project page: https://tianyucodings.github.io/EdiVAL-page/.

## 🔍 Abstract (한글 번역)

arXiv:2509.13399v1 공지 유형: 교차 분야
초록: 지시 기반 이미지 편집 기술은 빠르게 발전하고 있지만, 신뢰할 수 있고 해석 가능한 평가는 여전히 병목 현상으로 남아있다. 현재의 프로토콜은 (i) 쌍을 이루는 참조 이미지에 의존하여 제한적인 적용 범위를 가지며 기존 생성 모델의 편향을 계승하거나, (ii) 제로샷 비전-언어 모델(VLM)에만 의존하여 지시 수행, 내용 일관성, 시각적 품질에 대한 프롬프트 기반 평가가 종종 부정확하다는 문제점을 가지고 있다.

이러한 문제를 해결하기 위해, 우리는 전문가 도구 모음의 지원을 받는 객체 중심 관점에서 다중 턴 지시 기반 편집을 위한 자동화되고 확장 가능하며 세분화된 평가 프레임워크인 EdiVal-Agent를 소개한다. 이미지가 주어지면, EdiVal-Agent는 먼저 이를 의미론적으로 의미 있는 객체들로 분해한 다음, 다양하고 맥락을 고려한 편집 지시를 합성한다. 평가를 위해, VLM을 개방 어휘 객체 탐지기와 통합하여 지시 수행을 평가하고, 의미론적 수준의 특징 추출기를 사용하여 내용 일관성을 평가하며, 인간 선호도 모델을 활용하여 시각적 품질을 판단한다. 우리는 VLM과 객체 탐지기를 결합하는 것이 VLM만 사용하는 것과 CLIP 기반 지표에 비해 지시 수행 평가에서 인간 판단과 더 강한 일치를 보임을 입증한다. 또한, 파이프라인의 모듈식 설계는 미래의 도구들이 원활하게 통합될 수 있도록 하여 시간이 지남에 따라 평가 정확도를 향상시킨다.

이 파이프라인을 구현하여, 우리는 자기회귀(AR)(Nano Banana, GPT-Image-1 포함), 플로우 매칭, 확산 패러다임에 걸친 9가지 지시 유형과 11개의 최신 편집 모델을 다루는 다중 턴 편집 벤치마크인 EdiVal-Bench를 구축한다. 우리는 EdiVal-Agent가 기존의 실패 모드를 식별하는 데 사용될 수 있으며, 이를 통해 차세대 편집 모델의 개발에 도움을 줄 수 있음을 입증한다. 프로젝트 페이지: https://tianyucodings.github.io/EdiVAL-page/.

## 📝 요약

이 논문은 이미지 편집의 평가 문제를 해결하기 위해 EdiVal-Agent라는 자동화된 평가 프레임워크를 제안합니다. 기존 평가 방식은 참조 이미지에 의존하거나, 비전-언어 모델(VLM)에만 의존하여 정확성이 떨어지는 문제가 있었습니다. EdiVal-Agent는 객체 중심의 접근 방식을 통해 이미지를 의미 있는 객체로 분해하고, 다양한 편집 지시를 생성합니다. 평가 과정에서는 VLM과 객체 탐지기를 결합하여 지시 수행 여부를 평가하고, 내용 일관성을 위해 의미 수준의 특징 추출기를 사용하며, 시각적 품질은 인간 선호 모델을 활용해 평가합니다. 이 방법은 VLM 단독 사용보다 인간 판단과의 일치도가 높으며, 모듈식 설계로 향후 도구 통합이 용이합니다. 이를 바탕으로 EdiVal-Bench라는 벤치마크를 구축하여 9가지 지시 유형과 11개의 최신 편집 모델을 평가합니다. EdiVal-Agent는 기존 모델의 한계를 식별하고 차세대 편집 모델 개발에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. EdiVal-Agent는 객체 중심의 관점에서 다중 턴 지시 기반 편집을 위한 자동화되고 확장 가능한 평가 프레임워크를 제공합니다.

- 2. 이 시스템은 이미지의 의미 있는 객체를 분해하고, 다양한 맥락 인식 편집 지시를 생성합니다.

- 3. VLM과 객체 탐지기를 결합하여 지시 수행 평가에서 인간 판단과의 일치도를 높였습니다.

- 4. EdiVal-Bench는 9가지 지시 유형과 11개의 최첨단 편집 모델을 포함하는 다중 턴 편집 벤치마크를 제공합니다.

- 5. EdiVal-Agent는 기존의 실패 모드를 식별하여 차세대 편집 모델 개발에 기여할 수 있습니다.

---

*Generated on 2025-09-19 10:35:28*