---
keywords:
  - In-Context Learning
  - Text-Embedding KNN
  - Foundation Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13395
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:07:17.067191",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "In-Context Learning",
    "Text-Embedding KNN",
    "Foundation Models"
  ],
  "rejected_keywords": [
    "Speech Recognition"
  ],
  "similarity_scores": {
    "In-Context Learning": 0.88,
    "Text-Embedding KNN": 0.82,
    "Foundation Models": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# TICL: Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models

**Korean Title:** TICL: 대규모 다중모달 모델의 음성 인식 능력을 활성화하는 음성 맥락 내 학습을 위한 텍스트 임베딩 KNN

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Foundation Models|Large Multimodal Models]]
**⚡ Unique Technical**: [[keywords/Text-Embedding KNN|Text-Embedding KNN]]
**🚀 Evolved Concepts**: [[keywords/In-Context Learning|Speech In-Context Learning]]

## 🔗 유사한 논문
- [[Singular_Value_Few-shot_Adaptation_of_Vision-Language_Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (80.4% similar)
- [[Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (80.3% similar)
- [[Privacy-Aware In-Context Learning for Large Language Models]] (79.1% similar)
- [[Self-Guided_Function_Calling_in_Large_Language_Models_via_Stepwise_Experience_Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (79.0% similar)
- [[Iterative_Prompt_Refinement_for_Safer_Text-to-Image_Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (78.4% similar)

또는 더 자연스러운 한국어 표현으로:

TICL: 텍스트 임베딩 KNN을 활용한 음성 맥락 내 학습 - 대규모 다중모달 모델의 음성 인식 능력 발현

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13395v1 Announce Type: cross 
Abstract: Speech foundation models have recently demonstrated the ability to perform Speech In-Context Learning (SICL). Selecting effective in-context examples is crucial for SICL performance, yet selection methodologies remain underexplored. In this work, we propose Text-Embedding KNN for SICL (TICL), a simple pipeline that uses semantic context to enhance off-the-shelf large multimodal models' speech recognition ability without fine-tuning. Across challenging automatic speech recognition tasks, including accented English, multilingual speech, and children's speech, our method enables models to surpass zero-shot performance with up to 84.7% relative WER reduction. We conduct ablation studies to show the robustness and efficiency of our method.

## 🔍 Abstract (한글 번역)

arXiv:2509.13395v1 발표 유형: cross
초록: 음성 기반 모델들은 최근 음성 문맥 내 학습(Speech In-Context Learning, SICL)을 수행할 수 있는 능력을 보여주었다. 효과적인 문맥 내 예시를 선택하는 것은 SICL 성능에 있어 매우 중요하지만, 선택 방법론은 여전히 충분히 탐구되지 않은 상태이다. 본 연구에서는 SICL을 위한 텍스트 임베딩 KNN(Text-Embedding KNN for SICL, TICL)을 제안한다. 이는 의미적 맥락을 활용하여 파인튜닝 없이 기존의 대규모 다중모달 모델의 음성 인식 능력을 향상시키는 간단한 파이프라인이다. 억양이 있는 영어, 다국어 음성, 그리고 아동 음성을 포함한 도전적인 자동 음성 인식 과제들에서, 본 방법은 모델이 최대 84.7%의 상대적 단어 오류율(WER) 감소로 제로샷 성능을 능가할 수 있게 한다. 우리는 본 방법의 강건성과 효율성을 보이기 위해 절제 연구(ablation studies)를 수행하였다.

## 📝 요약

이 논문은 음성 기초 모델이 최근 음성 맥락 학습(SICL)을 수행할 수 있는 능력을 보여주었으나, 효과적인 맥락 예시 선택 방법은 충분히 탐구되지 않았다는 점을 지적합니다. 이를 해결하기 위해, 저자들은 Text-Embedding KNN for SICL (TICL)이라는 간단한 파이프라인을 제안합니다. 이 방법은 대형 멀티모달 모델의 음성 인식 능력을 강화하며, 별도의 파인튜닝 없이도 다양한 자동 음성 인식 과제에서 최대 84.7%의 상대적 WER 감소를 달성합니다. 또한, 저자들은 이 방법의 견고성과 효율성을 입증하기 위해 소거 연구를 수행했습니다.

## 🎯 주요 포인트

- 1. 최근 음성 기반 모델들은 음성 내 맥락 학습(SICL)을 수행할 수 있는 능력을 보여주고 있습니다.

- 2. 효과적인 맥락 내 예시 선택이 SICL 성능에 중요하지만, 이에 대한 연구는 아직 부족한 상태입니다.

- 3. 본 연구에서는 텍스트 임베딩 KNN을 활용한 SICL(TICL) 방법을 제안하여, 대형 멀티모달 모델의 음성 인식 능력을 향상시킵니다.

- 4. 제안된 방법은 악센트가 있는 영어, 다국어 음성, 아동 음성 등 다양한 자동 음성 인식 과제에서 최대 84.7%의 상대적 WER 감소를 달성합니다.

- 5. 소거 연구를 통해 제안된 방법의 견고성과 효율성을 입증하였습니다.

---

*Generated on 2025-09-19 10:34:58*