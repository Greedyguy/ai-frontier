---
keywords:
  - Self-Supervised Learning
  - Attention Mechanism
  - Sigmoid Self-Attention Weighting
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:46:19.893032",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-Supervised Learning",
    "Attention Mechanism",
    "Sigmoid Self-Attention Weighting"
  ],
  "rejected_keywords": [
    "Question-based Sign Language Translation"
  ],
  "similarity_scores": {
    "Self-Supervised Learning": 0.8,
    "Attention Mechanism": 0.75,
    "Sigmoid Self-Attention Weighting": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation

**Korean Title:** SSL-SSAW: 질문 기반 수어 번역을 위한 시그모이드 자기 주의 가중치를 활용한 자가 지도 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-Supervised Learning|Self-Supervised Learning]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Sigmoid Self-Attention Weighting|Sigmoid Self-Attention Weighting]]

## 🔗 유사한 논문
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (83.1% similar)
- [[DeKeyNLU_ Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction_20250919|DeKeyNLU Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction]] (78.9% similar)
- [[Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (78.8% similar)
- [[Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (78.7% similar)
- [[Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (78.6% similar)

## 📋 저자 정보

**Authors:** Zekang Liu, Wei Feng, Fanhua Shang, Lianyu Hu, Jichao Feng, Liqing Gao

## 📄 Abstract (원문)

Sign Language Translation (SLT) bridges the communication gap between deaf
people and hearing people, where dialogue provides crucial contextual cues to
aid in translation. Building on this foundational concept, this paper proposes
Question-based Sign Language Translation (QB-SLT), a novel task that explores
the efficient integration of dialogue. Unlike gloss (sign language
transcription) annotations, dialogue naturally occurs in communication and is
easier to annotate. The key challenge lies in aligning multimodality features
while leveraging the context of the question to improve translation. To address
this issue, we propose a cross-modality Self-supervised Learning with Sigmoid
Self-attention Weighting (SSL-SSAW) fusion method for sign language
translation. Specifically, we employ contrastive learning to align
multimodality features in QB-SLT, then introduce a Sigmoid Self-attention
Weighting (SSAW) module for adaptive feature extraction from question and sign
language sequences. Additionally, we leverage available question text through
self-supervised learning to enhance representation and translation
capabilities. We evaluated our approach on newly constructed CSL-Daily-QA and
PHOENIX-2014T-QA datasets, where SSL-SSAW achieved SOTA performance. Notably,
easily accessible question assistance can achieve or even surpass the
performance of gloss assistance. Furthermore, visualization results demonstrate
the effectiveness of incorporating dialogue in improving translation quality.

## 🔍 Abstract (한글 번역)

수화 번역(SLT)은 청각 장애인과 청인 간의 의사소통 격차를 해소하며, 대화는 번역을 돕는 중요한 맥락적 단서를 제공합니다. 이 기본 개념을 바탕으로 본 논문은 대화의 효율적 통합을 탐구하는 새로운 과제인 질문 기반 수화 번역(QB-SLT)을 제안합니다. 수화 전사(gloss) 주석과 달리, 대화는 자연스럽게 의사소통에서 발생하며 주석을 달기가 더 쉽습니다. 주요 과제는 질문의 맥락을 활용하여 번역을 개선하면서 다중 모달리티 특징을 정렬하는 데 있습니다. 이를 해결하기 위해, 우리는 수화 번역을 위한 시그모이드 자기 주의 가중치(SSAW)를 사용한 교차 모달리티 자기 지도 학습(SSL-SSAW) 융합 방법을 제안합니다. 구체적으로, 우리는 QB-SLT에서 다중 모달리티 특징을 정렬하기 위해 대조 학습을 사용하고, 질문과 수화 시퀀스로부터 적응형 특징 추출을 위한 시그모이드 자기 주의 가중치(SSAW) 모듈을 도입합니다. 또한, 자기 지도 학습을 통해 사용 가능한 질문 텍스트를 활용하여 표현 및 번역 능력을 향상시킵니다. 우리는 새로 구축된 CSL-Daily-QA 및 PHOENIX-2014T-QA 데이터셋에서 우리의 접근 방식을 평가했으며, SSL-SSAW가 SOTA 성능을 달성했습니다. 특히, 쉽게 접근할 수 있는 질문 지원이 글로스 지원의 성능을 달성하거나 심지어 초과할 수 있습니다. 또한, 시각화 결과는 번역 품질을 개선하는 데 있어 대화 통합의 효과를 입증합니다.

## 📝 요약

이 논문은 청각 장애인과 비장애인 간의 의사소통을 돕는 수어 번역(SLT)에서 대화의 중요성을 강조하며, 새로운 과제로 질문 기반 수어 번역(QB-SLT)을 제안합니다. 기존의 수어 기록 대신 자연스럽게 발생하는 대화를 활용하여 번역의 효율성을 높이고자 합니다. 이를 위해 교차 모달리티 자가 지도 학습과 시그모이드 자기 주의 가중치(SSL-SSAW) 융합 방법을 제시합니다. 대조 학습을 통해 다중 모달리티 특징을 정렬하고, 질문과 수어 시퀀스로부터 적응적 특징을 추출합니다. 또한, 질문 텍스트를 활용한 자가 지도 학습으로 표현력과 번역 능력을 강화합니다. 제안된 방법은 CSL-Daily-QA와 PHOENIX-2014T-QA 데이터셋에서 최첨단 성능을 보였으며, 질문의 도움만으로도 수어 기록의 도움을 뛰어넘는 성과를 달성했습니다. 시각화 결과는 대화 통합이 번역 품질 향상에 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 대화의 효율적 통합을 탐구하는 새로운 과제인 질문 기반 수어 번역(QB-SLT)을 제안합니다.

- 2. QB-SLT에서는 대화가 자연스럽게 발생하고 주석이 더 쉬운 점을 활용하여 번역을 개선하고자 합니다.

- 3. 우리는 교차 모달리티 자가 지도 학습과 시그모이드 자가 주의 가중치(SSAW) 융합 방법을 제안하여 수어 번역의 다중 모달리티 특징을 정렬합니다.

- 4. 제안된 방법은 새로 구축된 CSL-Daily-QA 및 PHOENIX-2014T-QA 데이터셋에서 SOTA 성능을 달성했습니다.

- 5. 질문을 통한 보조는 글로스 보조의 성능을 달성하거나 초과할 수 있으며, 대화 통합이 번역 품질을 향상시키는 데 효과적임을 시각화 결과로 보여줍니다.

---

*Generated on 2025-09-20 09:15:24*