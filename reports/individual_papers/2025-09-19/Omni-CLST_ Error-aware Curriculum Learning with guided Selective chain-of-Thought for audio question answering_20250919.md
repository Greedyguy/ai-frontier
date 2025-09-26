---
keywords:
  - Audio Question Answering
  - Large Audio-Language Models
  - Curriculum Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.12275
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:32:11.578620",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Audio Question Answering",
    "Large Audio-Language Models",
    "Curriculum Learning"
  ],
  "rejected_keywords": [
    "Chain-of-Thought",
    "Error-Aware Curriculum"
  ],
  "similarity_scores": {
    "Audio Question Answering": 0.78,
    "Large Audio-Language Models": 0.77,
    "Curriculum Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Omni-CLST: Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering

**Korean Title:** 옴니-CLST: 오디오 질문 응답을 위한 오류 인식 커리큘럼 학습과 유도된 선택적 사고의 연쇄

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Curriculum Learning|curriculum learning]]
**⚡ Unique Technical**: [[keywords/Audio Question Answering|audio question answering]]
**🚀 Evolved Concepts**: [[keywords/Large Audio-Language Models|large audio-language models]]

## 🔗 유사한 논문
- [[Cross-Modal_Knowledge_Distillation_for_Speech_Large_Language_Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (81.8% similar)
- [[Teacher-Guided_Pseudo_Supervision_and_Cross-Modal_Alignment_for_Audio-Visual_Video_Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (80.8% similar)
- [[TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (80.3% similar)
- [[A_Multi-To-One_Interview_Paradigm_for_Efficient_MLLM_Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (80.2% similar)
- [[MovieCORE COgnitive REasoning in Movies]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12275v3 Announce Type: replace-cross 
Abstract: With the rapid progress of large audio-language models (LALMs), audio question answering (AQA) has emerged as a challenging task requiring both fine-grained audio understanding and complex reasoning. While current methods mainly rely on constructing new datasets via captioning or reasoning traces, existing high-quality AQA data remains underutilized. To address this, we propose Omni-CLST, an error-aware Curriculum Learning framework with guided Selective Chain-of-Thought. The framework efficiently leverages existing high-quality dataset through two key strategies: an error-aware curriculum that organizes samples by difficulty, and a guided thought dropout mechanism that focuses reasoning on challenging cases. Experiments show that Omni-CLST achieves 73.80% on MMAU-mini and a new state of the art of 64.30% on MMAR, demonstrating robust generalization in multimodal audio-language understanding.

## 🔍 Abstract (한글 번역)

arXiv:2509.12275v3 발표 유형: 교체-크로스  
초록: 대형 오디오-언어 모델(LALMs)의 급속한 발전과 함께, 오디오 질문 응답(AQA)은 세밀한 오디오 이해와 복잡한 추론을 요구하는 도전적인 과제로 부상했습니다. 현재의 방법들은 주로 캡션 작성이나 추론 경로를 통해 새로운 데이터셋을 구축하는 데 의존하고 있지만, 기존의 고품질 AQA 데이터는 충분히 활용되지 않고 있습니다. 이를 해결하기 위해, 우리는 Omni-CLST라는 오류 인식 커리큘럼 학습 프레임워크를 제안합니다. 이 프레임워크는 두 가지 주요 전략을 통해 기존의 고품질 데이터셋을 효율적으로 활용합니다: 난이도에 따라 샘플을 조직하는 오류 인식 커리큘럼과 어려운 사례에 대한 추론에 집중하는 유도된 사고 드롭아웃 메커니즘입니다. 실험 결과, Omni-CLST는 MMAU-mini에서 73.80%를 달성하고 MMAR에서 새로운 최고 기록인 64.30%를 달성하여 멀티모달 오디오-언어 이해에서 강력한 일반화를 보여주었습니다.

## 📝 요약

이 논문은 대규모 오디오-언어 모델(LALMs)의 발전에 따라 오디오 질문 응답(AQA) 과제가 중요해졌음을 설명합니다. 기존 데이터셋의 활용이 부족한 문제를 해결하기 위해, 저자들은 Omni-CLST라는 오류 인식 커리큘럼 학습 프레임워크를 제안합니다. 이 프레임워크는 난이도에 따라 샘플을 조직하는 오류 인식 커리큘럼과 어려운 사례에 집중하는 유도적 사고 드롭아웃 메커니즘을 통해 고품질 데이터셋을 효율적으로 활용합니다. 실험 결과, Omni-CLST는 MMAU-mini에서 73.80%, MMAR에서 64.30%의 성과를 기록하며 멀티모달 오디오-언어 이해에서 강력한 일반화 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 오디오-언어 모델의 발전으로 오디오 질문 응답(AQA)이 세밀한 오디오 이해와 복잡한 추론을 요구하는 도전적인 과제로 부상하고 있다.

- 2. 기존의 고품질 AQA 데이터가 충분히 활용되지 않는 문제를 해결하기 위해 Omni-CLST라는 오류 인식 커리큘럼 학습 프레임워크를 제안한다.

- 3. Omni-CLST는 난이도에 따라 샘플을 조직하는 오류 인식 커리큘럼과 어려운 사례에 집중하는 유도된 사고 드롭아웃 메커니즘을 통해 고품질 데이터를 효율적으로 활용한다.

- 4. 실험 결과, Omni-CLST는 MMAU-mini에서 73.80%의 성과를, MMAR에서 64.30%의 새로운 최고 성과를 달성하여 다중 모달 오디오-언어 이해에서 강력한 일반화 능력을 입증했다.

---

*Generated on 2025-09-19 15:23:23*