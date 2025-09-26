<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:48:01.726120",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Transformer",
    "Attention Mechanism",
    "More Attention To Audio",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Transformer": 0.8,
    "Attention Mechanism": 0.85,
    "More Attention To Audio": 0.9,
    "Multimodal Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Audio-Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LALMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing research on large models, bridging audio and language processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer architecture",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational model architecture relevant to many multi-modal systems.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the paper's method, linking to broader attention-based model research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "MATA",
        "canonical": "More Attention To Audio",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel method proposed by the paper, crucial for understanding its contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Multimodal fusion layers",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key to understanding the integration of audio and text in models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "audio-textual attention imbalance",
      "acoustic cues",
      "open-source model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Audio-Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer architecture",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "MATA",
      "resolved_canonical": "More Attention To Audio",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Multimodal fusion layers",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Pay More Attention To Audio: Mitigating Imbalance of Cross-Modal Attention in Large Audio Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18816.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18816](https://arxiv.org/abs/2509.18816)

## 🔗 유사한 논문
- [[2025-09-23/Does Audio Matter for Modern Video-LLMs and Their Benchmarks?_20250923|Does Audio Matter for Modern Video-LLMs and Their Benchmarks?]] (86.2% similar)
- [[2025-09-24/An overview of neural architectures for self-supervised audio representation learning from masked spectrograms_20250924|An overview of neural architectures for self-supervised audio representation learning from masked spectrograms]] (85.0% similar)
- [[2025-09-23/Audio-Reasoner_ Improving Reasoning Capability in Large Audio Language Models_20250923|Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models]] (84.8% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (84.3% similar)
- [[2025-09-22/Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding_20250922|Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/More Attention To Audio|More Attention To Audio]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18816v1 Announce Type: cross 
Abstract: Large Audio-Language Models (LALMs) often suffer from audio-textual attention imbalance, prioritizing text over acoustic information, particularly in the multi-modal fusion layers of the Transformer architecture. This bias hinders their ability to fully utilize acoustic cues, causing suboptimal performance on audio reasoning tasks. To mitigate this, we propose \textbf{MATA}, a novel training-free method that dynamically pushes LALMs to pay \textbf{M}ore \textbf{A}ttention \textbf{T}o \textbf{A}udio tokens within the self-attention mechanism. Specifically, MATA intervenes post raw attention scoring, targeting only the last token in intermediate layers without introducing additional parameters or computational overhead. Experiments on the MMAU and MMAR benchmarks confirm MATA's effectiveness, with consistent performance gains. Notably, on MMAR, MATA enables an open-source model to surpass the proprietary Gemini 2.0 Flash for the first time. Our work provides an efficient solution to mitigate attention bias and opens a new research direction for enhancing the audio-processing capabilities of multi-modal models.

## 📝 요약

이 논문은 대규모 오디오-언어 모델(LALMs)이 텍스트에 비해 오디오 정보에 대한 주의가 부족한 문제를 해결하기 위해 MATA라는 새로운 방법을 제안합니다. MATA는 추가적인 매개변수나 계산 부담 없이, 셀프 어텐션 메커니즘에서 오디오 토큰에 더 많은 주의를 기울이도록 모델을 유도합니다. 실험 결과, MATA는 MMAU와 MMAR 벤치마크에서 성능 향상을 보였으며, 특히 MMAR에서 오픈소스 모델이 Gemini 2.0 Flash를 능가하는 성과를 달성했습니다. 이 연구는 멀티모달 모델의 오디오 처리 능력을 향상시키는 새로운 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 오디오-언어 모델(LALMs)은 오디오-텍스트 주의력 불균형으로 인해 음향 정보를 충분히 활용하지 못하는 문제가 있다.
- 2. MATA는 LALMs가 오디오 토큰에 더 많은 주의를 기울이도록 유도하는 새로운 훈련 없는 방법이다.
- 3. MATA는 중간 레이어의 마지막 토큰에만 개입하여 추가적인 매개변수나 계산 부담 없이 주의력 편향을 완화한다.
- 4. MMAU 및 MMAR 벤치마크 실험에서 MATA의 효과가 입증되었으며, 특히 MMAR에서 오픈 소스 모델이 Gemini 2.0 Flash를 처음으로 능가했다.
- 5. 이 연구는 멀티모달 모델의 오디오 처리 능력을 향상시키기 위한 새로운 연구 방향을 제시한다.


---

*Generated on 2025-09-24 15:48:01*