---
keywords:
  - Transformer
  - Emotion-Aware Talking Head Generation
  - Large Language Model
  - Interactive Talking Tree Structure
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2508.18337
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:34:00.120426",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Emotion-Aware Talking Head Generation",
    "Large Language Model",
    "Interactive Talking Tree Structure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Emotion-Aware Talking Head Generation": 0.88,
    "Large Language Model": 0.87,
    "Interactive Talking Tree Structure": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based head mask generator",
        "canonical": "Transformer",
        "aliases": [
          "Transformer model"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model architecture in deep learning, crucial for linking advancements in AI-driven generation tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "emotion-aware talking head generation",
        "canonical": "Emotion-Aware Talking Head Generation",
        "aliases": [
          "emotion-adaptive talking heads"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel integration of emotion recognition in AI-generated avatars, offering unique insights into interactive AI development.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs",
          "GPT-4"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are pivotal in enabling advanced dialogue generation, linking to broader AI communication research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.89,
        "specificity_score": 0.7,
        "link_intent_score": 0.87
      },
      {
        "surface": "interactive talking tree structure",
        "canonical": "Interactive Talking Tree Structure",
        "aliases": [
          "dialogue state tree"
        ],
        "category": "unique_technical",
        "rationale": "This structure is a unique method for managing dialogue states, enhancing understanding of conversational AI frameworks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based head mask generator",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "emotion-aware talking head generation",
      "resolved_canonical": "Emotion-Aware Talking Head Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.89,
        "specificity": 0.7,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "interactive talking tree structure",
      "resolved_canonical": "Interactive Talking Tree Structure",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# EAI-Avatar: Emotion-Aware Interactive Talking Head Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.18337.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2508.18337](https://arxiv.org/abs/2508.18337)

## 🔗 유사한 논문
- [[2025-09-23/Beat on Gaze_ Learning Stylized Generation of Gaze and Head Dynamics_20250923|Beat on Gaze: Learning Stylized Generation of Gaze and Head Dynamics]] (83.2% similar)
- [[2025-09-24/Audio-Driven Universal Gaussian Head Avatars_20250924|Audio-Driven Universal Gaussian Head Avatars]] (82.7% similar)
- [[2025-09-22/Emotion-Aware Speech Generation with Character-Specific Voices for Comics_20250922|Emotion-Aware Speech Generation with Character-Specific Voices for Comics]] (82.2% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (81.2% similar)
- [[2025-09-19/Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Emotion-Aware Talking Head Generation|Emotion-Aware Talking Head Generation]], [[keywords/Interactive Talking Tree Structure|Interactive Talking Tree Structure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.18337v2 Announce Type: replace-cross 
Abstract: Generative models have advanced rapidly, enabling impressive talking head generation that brings AI to life. However, most existing methods focus solely on one-way portrait animation. Even the few that support bidirectional conversational interactions lack precise emotion-adaptive capabilities, significantly limiting their practical applicability. In this paper, we propose EAI-Avatar, a novel emotion-aware talking head generation framework for dyadic interactions. Leveraging the dialogue generation capability of large language models (LLMs, e.g., GPT-4), our method produces temporally consistent virtual avatars with rich emotional variations that seamlessly transition between speaking and listening states. Specifically, we design a Transformer-based head mask generator that learns temporally consistent motion features in a latent mask space, capable of generating arbitrary-length, temporally consistent mask sequences to constrain head motions. Furthermore, we introduce an interactive talking tree structure to represent dialogue state transitions, where each tree node contains information such as child/parent/sibling nodes and the current character's emotional state. By performing reverse-level traversal, we extract rich historical emotional cues from the current node to guide expression synthesis. Extensive experiments demonstrate the superior performance and effectiveness of our method.

## 📝 요약

이 논문에서는 감정 인식이 가능한 새로운 대화형 아바타 생성 프레임워크인 EAI-Avatar를 제안합니다. 기존의 대부분의 생성 모델이 단방향 초상화 애니메이션에 집중하는 반면, EAI-Avatar는 양방향 대화에서 감정에 적응하는 기능을 제공합니다. 이 방법은 대형 언어 모델(예: GPT-4)의 대화 생성 능력을 활용하여, 말하기와 듣기 상태 간의 자연스러운 전환과 풍부한 감정 변화를 가진 가상 아바타를 생성합니다. 특히, Transformer 기반의 헤드 마스크 생성기를 설계하여 일관된 움직임 특징을 학습하고, 대화 상태 전환을 표현하는 대화 트리 구조를 도입하여 감정적 단서를 활용한 표현 합성을 가능하게 합니다. 실험 결과, 제안된 방법의 우수한 성능과 효과를 입증하였습니다.

## 🎯 주요 포인트

- 1. EAI-Avatar는 감정 인식 기능을 갖춘 새로운 양방향 대화형 아바타 생성 프레임워크입니다.
- 2. 대형 언어 모델의 대화 생성 능력을 활용하여 감정 변화를 반영한 가상 아바타를 생성합니다.
- 3. Transformer 기반의 헤드 마스크 생성기를 설계하여 시간적으로 일관된 모션 특징을 학습합니다.
- 4. 대화 상태 전환을 표현하기 위해 상호작용 가능한 대화 트리 구조를 도입합니다.
- 5. 실험 결과, 제안된 방법의 성능과 효과가 우수함을 입증하였습니다.


---

*Generated on 2025-09-25 16:34:00*