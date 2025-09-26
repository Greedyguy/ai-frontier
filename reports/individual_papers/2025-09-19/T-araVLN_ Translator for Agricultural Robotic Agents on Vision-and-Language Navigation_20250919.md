---
keywords:
  - Vision-and-Language Navigation
  - Natural Language Processing
  - Agricultural Robotic Agents
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.06644
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:22:29.907454",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-and-Language Navigation",
    "Natural Language Processing",
    "Agricultural Robotic Agents"
  ],
  "rejected_keywords": [
    "Instruction Translator"
  ],
  "similarity_scores": {
    "Vision-and-Language Navigation": 0.78,
    "Natural Language Processing": 0.7,
    "Agricultural Robotic Agents": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# T-araVLN: Translator for Agricultural Robotic Agents on Vision-and-Language Navigation

**Korean Title:** 타라VLN: 시각 및 언어 내비게이션을 위한 농업 로봇 에이전트 번역기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Instructions]]
**⚡ Unique Technical**: [[keywords/Vision-and-Language Navigation|Vision-and-Language Navigation]], [[keywords/Agricultural Robotic Agents|Agricultural Robotic Agents]]

## 🔗 유사한 논문
- [[FSR-VLN Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (83.5% similar)
- [[CollabVLA Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (82.6% similar)
- [[Search-TTA A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (82.1% similar)
- [[Ask-to-Clarify Resolving Instruction Ambiguity through Multi-turn Dialogue]] (80.4% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06644v4 Announce Type: replace 
Abstract: Agricultural robotic agents have been becoming powerful helpers in a wide range of agricultural tasks, however, still heavily rely on manual operation or fixed railways for movement. To address this limitation, the AgriVLN method and the A2A benchmark pioneeringly extend Vision-and-Language Navigation (VLN) to the agricultural domain, enabling agents to navigate to the target positions following the natural language instructions. AgriVLN effectively understands the simple instructions, but often misunderstands the complex ones. To bridge this gap, we propose the method of Translator for Agricultural Robotic Agents on Vision-and-Language Navigation (T-araVLN), in which the Instruction Translator module translates the original instruction to be more refined and precise. When evaluated on the A2A benchmark, our T-araVLN effectively improves Success Rate from 0.47 to 0.63 and reduces Navigation Error from 2.91m to 2.28m, demonstrating the state-of-the-art performance in the agricultural domain. Code: https://github.com/AlexTraveling/T-araVLN.

## 🔍 Abstract (한글 번역)

arXiv:2509.06644v4 발표 유형: 교체  
초록: 농업 로봇 에이전트는 다양한 농업 작업에서 강력한 도우미로 자리 잡고 있지만, 여전히 수동 조작이나 고정된 철로에 의존하여 이동하는 경우가 많습니다. 이러한 한계를 극복하기 위해, AgriVLN 방법과 A2A 벤치마크는 비전-언어 내비게이션(VLN)을 농업 분야로 확장하여 에이전트가 자연어 지시를 따라 목표 위치로 이동할 수 있도록 합니다. AgriVLN은 간단한 지시를 효과적으로 이해하지만, 복잡한 지시를 종종 오해합니다. 이 격차를 해소하기 위해, 우리는 비전-언어 내비게이션에서 농업 로봇 에이전트를 위한 번역기 방법(T-araVLN)을 제안합니다. 이 방법에서 지시 번역 모듈은 원래 지시를 더 정제되고 정확하게 번역합니다. A2A 벤치마크에서 평가한 결과, 우리의 T-araVLN은 성공률을 0.47에서 0.63으로 효과적으로 향상시키고, 내비게이션 오류를 2.91m에서 2.28m로 줄여 농업 분야에서 최첨단 성능을 입증했습니다. 코드: https://github.com/AlexTraveling/T-araVLN.

## 📝 요약

이 논문은 농업 분야에서 로봇 에이전트의 이동성을 개선하기 위해 Vision-and-Language Navigation(VLN)을 적용한 AgriVLN 방법과 A2A 벤치마크를 소개합니다. AgriVLN은 간단한 지시를 이해하는 데는 효과적이지만 복잡한 지시에서는 오해가 발생하는 한계를 보입니다. 이를 해결하기 위해, 본 연구는 T-araVLN이라는 방법을 제안하여 Instruction Translator 모듈을 통해 지시를 더 정교하고 명확하게 번역합니다. A2A 벤치마크 평가 결과, T-araVLN은 성공률을 0.47에서 0.63으로 향상시키고, 내비게이션 오류를 2.91m에서 2.28m로 줄이며 최첨단 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. AgriVLN 방법과 A2A 벤치마크는 농업 분야에서 Vision-and-Language Navigation(VLN)을 확장하여 에이전트가 자연어 지시를 따라 목표 위치로 이동할 수 있도록 합니다.

- 2. AgriVLN은 간단한 지시를 효과적으로 이해하지만 복잡한 지시에서는 오해가 발생할 수 있습니다.

- 3. T-araVLN은 Instruction Translator 모듈을 통해 원래 지시를 더 정교하고 정확하게 번역하여 이러한 오해를 줄입니다.

- 4. T-araVLN은 A2A 벤치마크 평가에서 성공률을 0.47에서 0.63으로 개선하고 내비게이션 오류를 2.91m에서 2.28m로 줄였습니다.

- 5. T-araVLN은 농업 분야에서 최첨단 성능을 입증하였습니다.

---

*Generated on 2025-09-19 16:39:07*