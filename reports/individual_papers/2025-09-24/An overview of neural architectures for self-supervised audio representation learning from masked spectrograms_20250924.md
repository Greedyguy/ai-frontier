<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:00:10.903178",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Masked Spectrogram Modeling",
    "Transformer",
    "Selective Structured State Space Models",
    "Audio Foundation Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Masked Spectrogram Modeling": 0.78,
    "Transformer": 0.8,
    "Selective Structured State Space Models": 0.75,
    "Audio Foundation Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a key approach in the paper, linking it to broader trends in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "masked spectrogram modeling",
        "canonical": "Masked Spectrogram Modeling",
        "aliases": [
          "MSM"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach discussed in the paper, relevant for audio representation learning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are central to the paper's discussion on neural architectures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Selective structured state space models",
        "canonical": "Selective Structured State Space Models",
        "aliases": [
          "S4 Models"
        ],
        "category": "unique_technical",
        "rationale": "These models represent a novel approach to sequence modeling in the context of the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "audio foundation models",
        "canonical": "Audio Foundation Models",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "The concept of audio foundation models is emerging and connects to broader AI model discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "deep neural representations",
      "recurrent sequence modeling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "masked spectrogram modeling",
      "resolved_canonical": "Masked Spectrogram Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Selective structured state space models",
      "resolved_canonical": "Selective Structured State Space Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "audio foundation models",
      "resolved_canonical": "Audio Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# An overview of neural architectures for self-supervised audio representation learning from masked spectrograms

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18691.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18691](https://arxiv.org/abs/2509.18691)

## 🔗 유사한 논문
- [[2025-09-23/Achilles' Heel of Mamba_ Essential difficulties of the Mamba architecture demonstrated by synthetic data_20250923|Achilles' Heel of Mamba: Essential difficulties of the Mamba architecture demonstrated by synthetic data]] (83.5% similar)
- [[2025-09-23/Scaling Efficient LLMs_20250923|Scaling Efficient LLMs]] (83.1% similar)
- [[2025-09-23/Inceptive Transformers_ Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages_20250923|Inceptive Transformers: Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages]] (82.1% similar)
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (82.1% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Masked Spectrogram Modeling|Masked Spectrogram Modeling]], [[keywords/Selective Structured State Space Models|Selective Structured State Space Models]]
**🚀 Evolved Concepts**: [[keywords/Audio Foundation Models|Audio Foundation Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18691v1 Announce Type: cross 
Abstract: In recent years, self-supervised learning has amassed significant interest for training deep neural representations without labeled data. One such self-supervised learning approach is masked spectrogram modeling, where the objective is to learn semantically rich contextual representations by predicting removed or hidden portions of the input audio spectrogram. With the Transformer neural architecture at its core, masked spectrogram modeling has emerged as the prominent approach for learning general purpose audio representations, a.k.a. audio foundation models. Meanwhile, addressing the issues of the Transformer architecture, in particular the underlying Scaled Dot-product Attention operation, which scales quadratically with input sequence length, has led to renewed interest in recurrent sequence modeling approaches. Among them, Selective structured state space models (such as Mamba) and extended Long Short-Term Memory (xLSTM) are the two most promising approaches which have experienced widespread adoption. While the body of work on these two topics continues to grow, there is currently a lack of an adequate overview encompassing the intersection of these topics. In this paper, we present a comprehensive overview of the aforementioned research domains, covering masked spectrogram modeling and the previously mentioned neural sequence modeling architectures, Mamba and xLSTM. Further, we compare Transformers, Mamba and xLSTM based masked spectrogram models in a unified, reproducible framework on ten diverse downstream audio classification tasks, which will help interested readers to make informed decisions regarding suitability of the evaluated approaches to adjacent applications.

## 📝 요약

최근 자기 지도 학습은 라벨이 없는 데이터로 심층 신경 표현을 학습하는 데 큰 관심을 받고 있습니다. 그 중 하나인 마스크 스펙트로그램 모델링은 입력 오디오 스펙트로그램의 숨겨진 부분을 예측하여 의미 있는 문맥 표현을 학습하는 방법입니다. Transformer 신경망 구조를 기반으로 하는 이 방법은 범용 오디오 표현 학습의 주요 접근법으로 자리 잡았습니다. 그러나 Transformer의 Scaled Dot-product Attention 연산이 입력 시퀀스 길이에 따라 이차적으로 증가하는 문제를 해결하기 위해, 재귀적 시퀀스 모델링 접근법에 대한 관심이 다시 증가하고 있습니다. 특히, Mamba와 같은 선택적 구조적 상태 공간 모델과 확장된 LSTM(xLSTM)이 주목받고 있습니다. 본 논문에서는 이러한 연구 영역을 포괄적으로 다루고, Transformer, Mamba, xLSTM 기반의 마스크 스펙트로그램 모델을 다양한 오디오 분류 작업에서 비교하여, 독자들이 각 접근법의 적합성을 평가할 수 있도록 돕습니다.

## 🎯 주요 포인트

- 1. 자기 지도 학습은 레이블이 없는 데이터로 심층 신경 표현을 학습하는 데 주목받고 있으며, 마스킹된 스펙트로그램 모델링이 그 중 하나로 부상하고 있다.
- 2. 트랜스포머 신경망 구조를 기반으로 한 마스킹된 스펙트로그램 모델링은 일반 목적의 오디오 표현 학습에 있어 중요한 접근 방식으로 자리잡았다.
- 3. 트랜스포머 구조의 문제를 해결하기 위해 선택적 구조적 상태 공간 모델(Mamba)과 확장된 장단기 메모리(xLSTM)가 주목받고 있다.
- 4. 본 논문에서는 마스킹된 스펙트로그램 모델링과 Mamba, xLSTM 등의 신경망 시퀀스 모델링 아키텍처에 대한 포괄적인 개요를 제시한다.
- 5. 트랜스포머, Mamba, xLSTM 기반의 마스킹된 스펙트로그램 모델을 다양한 오디오 분류 작업에서 비교하여 각 접근 방식의 적합성을 평가한다.


---

*Generated on 2025-09-24 14:00:10*