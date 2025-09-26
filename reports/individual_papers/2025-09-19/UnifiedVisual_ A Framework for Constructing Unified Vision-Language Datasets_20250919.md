---
keywords:
  - Large Language Models
  - Multi-Modal Learning
  - Generative Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14738
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:19:12.348428",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Multi-Modal Learning",
    "Generative Models"
  ],
  "rejected_keywords": [
    "Computer Vision"
  ],
  "similarity_scores": {
    "Large Language Models": 0.88,
    "Multi-Modal Learning": 0.84,
    "Generative Models": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets

**Korean Title:** 통합비주얼: 통합 비전-언어 데이터셋 구축을 위한 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Generative Models|text-guided image synthesis]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Unified vision large language models]], [[keywords/Multi-Modal Learning|cross-modal reasoning]]

## 🔗 유사한 논문
- [[Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.4% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.8% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (83.6% similar)
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (83.4% similar)
- [[Visible Yet Unreadable A Systematic Blind Spot of Vision Language Models Across Writing Systems]] (83.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14738v1 Announce Type: new 
Abstract: Unified vision large language models (VLLMs) have recently achieved impressive advancements in both multimodal understanding and generation, powering applications such as visual question answering and text-guided image synthesis. However, progress in unified VLLMs remains constrained by the lack of datasets that fully exploit the synergistic potential between these two core abilities. Existing datasets typically address understanding and generation in isolation, thereby limiting the performance of unified VLLMs. To bridge this critical gap, we introduce a novel dataset construction framework, UnifiedVisual, and present UnifiedVisual-240K, a high-quality dataset meticulously designed to facilitate mutual enhancement between multimodal understanding and generation. UnifiedVisual-240K seamlessly integrates diverse visual and textual inputs and outputs, enabling comprehensive cross-modal reasoning and precise text-to-image alignment. Our dataset encompasses a wide spectrum of tasks and data sources, ensuring rich diversity and addressing key shortcomings of prior resources. Extensive experiments demonstrate that models trained on UnifiedVisual-240K consistently achieve strong performance across a wide range of tasks. Notably, these models exhibit significant mutual reinforcement between multimodal understanding and generation, further validating the effectiveness of our framework and dataset. We believe UnifiedVisual represents a new growth point for advancing unified VLLMs and unlocking their full potential. Our code and datasets is available at https://github.com/fnlp-vision/UnifiedVisual.

## 🔍 Abstract (한글 번역)

arXiv:2509.14738v1 발표 유형: 신규  
초록: 통합 비전 대형 언어 모델(VLLM)은 최근 다중 모드 이해 및 생성에서 인상적인 발전을 이루어, 시각적 질문 응답 및 텍스트 기반 이미지 생성과 같은 응용 프로그램을 가능하게 하고 있습니다. 그러나 통합 VLLM의 발전은 이러한 두 가지 핵심 능력 간의 시너지 잠재력을 완전히 활용하는 데이터셋의 부족으로 인해 제한되고 있습니다. 기존 데이터셋은 일반적으로 이해와 생성을 개별적으로 다루어, 통합 VLLM의 성능을 제한합니다. 이 중요한 격차를 해소하기 위해, 우리는 새로운 데이터셋 구성 프레임워크인 UnifiedVisual을 소개하고, 다중 모드 이해와 생성 간의 상호 향상을 촉진하도록 세심하게 설계된 고품질 데이터셋 UnifiedVisual-240K를 제시합니다. UnifiedVisual-240K는 다양한 시각적 및 텍스트 입력과 출력을 원활하게 통합하여 포괄적인 교차 모드 추론과 정확한 텍스트-이미지 정렬을 가능하게 합니다. 우리의 데이터셋은 광범위한 작업과 데이터 소스를 포함하여 풍부한 다양성을 보장하고 이전 자원의 주요 결점을 해결합니다. 광범위한 실험을 통해 UnifiedVisual-240K로 훈련된 모델이 다양한 작업에서 일관되게 강력한 성능을 발휘함을 보여줍니다. 특히, 이러한 모델은 다중 모드 이해와 생성 간의 상당한 상호 강화 효과를 나타내어, 우리의 프레임워크와 데이터셋의 효과성을 더욱 입증합니다. 우리는 UnifiedVisual이 통합 VLLM을 발전시키고 그들의 잠재력을 최대한 발휘할 수 있는 새로운 성장점을 나타낸다고 믿습니다. 우리의 코드와 데이터셋은 https://github.com/fnlp-vision/UnifiedVisual에서 이용 가능합니다.

## 📝 요약

최근 통합 비전 대형 언어 모델(VLLMs)은 멀티모달 이해와 생성에서 뛰어난 발전을 이루었으나, 이를 동시에 활용할 수 있는 데이터셋의 부족으로 한계가 있었습니다. 이를 해결하기 위해, 우리는 새로운 데이터셋 구축 프레임워크인 UnifiedVisual과 고품질 데이터셋 UnifiedVisual-240K를 소개합니다. 이 데이터셋은 다양한 시각 및 텍스트 입력과 출력을 통합하여, 멀티모달 이해와 생성 간의 상호 강화 효과를 촉진합니다. 실험 결과, UnifiedVisual-240K로 훈련된 모델은 다양한 작업에서 강력한 성능을 보였으며, 멀티모달 이해와 생성 간의 상호 보강이 두드러졌습니다. 이러한 결과는 우리의 프레임워크와 데이터셋의 효과성을 입증하며, 통합 VLLMs의 발전에 중요한 기여를 할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. 통합 비전 대형 언어 모델(VLLM)은 멀티모달 이해와 생성에서 뛰어난 발전을 이루었으나, 이를 동시에 활용할 수 있는 데이터셋의 부족으로 한계가 있다.

- 2. UnifiedVisual-240K는 멀티모달 이해와 생성을 상호 증진시키기 위해 설계된 고품질 데이터셋으로, 다양한 시각 및 텍스트 입력과 출력을 통합하여 포괄적인 교차 모달 추론을 가능하게 한다.

- 3. UnifiedVisual-240K를 기반으로 훈련된 모델은 다양한 작업에서 일관되게 강력한 성능을 보이며, 멀티모달 이해와 생성 간의 상호 강화 효과를 나타낸다.

- 4. UnifiedVisual은 통합 VLLM의 발전과 잠재력 극대화를 위한 새로운 성장 포인트를 제공한다.

---

*Generated on 2025-09-19 15:51:53*