---
keywords:
  - Attention Mechanism
  - Speech-to-Text Models
  - Saliency Maps
  - Transformer
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18010
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:16:57.998224",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Speech-to-Text Models",
    "Saliency Maps",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Speech-to-Text Models": 0.78,
    "Saliency Maps": 0.82,
    "Transformer": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cross-attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Cross Attention",
          "Cross-Attention Mechanism"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-attention is a specific type of attention mechanism, crucial for linking to broader discussions on attention in neural networks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Speech-to-Text Models",
        "canonical": "Speech-to-Text Models",
        "aliases": [
          "S2T Models",
          "Speech Recognition Models"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper and connects to specific discussions on speech processing technologies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Saliency Maps",
        "canonical": "Saliency Maps",
        "aliases": [
          "Input Saliency Maps",
          "Feature Attribution Maps"
        ],
        "category": "unique_technical",
        "rationale": "Saliency maps are key to understanding model interpretability, which is a focal point of the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "Encoder-Decoder Architectures",
        "canonical": "Transformer",
        "aliases": [
          "Encoder-Decoder Models"
        ],
        "category": "broad_technical",
        "rationale": "Encoder-decoder architectures are foundational to many neural network models, including Transformers.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "downstream applications",
      "input relevance",
      "explanatory proxy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cross-attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Speech-to-Text Models",
      "resolved_canonical": "Speech-to-Text Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Saliency Maps",
      "resolved_canonical": "Saliency Maps",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Encoder-Decoder Architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Cross-Attention is Half Explanation in Speech-to-Text Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18010.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18010](https://arxiv.org/abs/2509.18010)

## 🔗 유사한 논문
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation]] (79.7% similar)
- [[2025-09-23/Interpreting Attention Heads for Image-to-Text Information Flow in Large Vision-Language Models_20250923|Interpreting Attention Heads for Image-to-Text Information Flow in Large Vision-Language Models]] (79.4% similar)
- [[2025-09-22/Pruning the Paradox_ How CLIP's Most Informative Heads Enhance Performance While Amplifying Bias_20250922|Pruning the Paradox: How CLIP's Most Informative Heads Enhance Performance While Amplifying Bias]] (79.4% similar)
- [[2025-09-18/Stochastic Clock Attention for Aligning Continuous and Ordered Sequences_20250918|Stochastic Clock Attention for Aligning Continuous and Ordered Sequences]] (79.2% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (78.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Speech-to-Text Models|Speech-to-Text Models]], [[keywords/Saliency Maps|Saliency Maps]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18010v1 Announce Type: cross 
Abstract: Cross-attention is a core mechanism in encoder-decoder architectures, widespread in many fields, including speech-to-text (S2T) processing. Its scores have been repurposed for various downstream applications--such as timestamp estimation and audio-text alignment--under the assumption that they reflect the dependencies between input speech representation and the generated text. While the explanatory nature of attention mechanisms has been widely debated in the broader NLP literature, this assumption remains largely unexplored within the speech domain. To address this gap, we assess the explanatory power of cross-attention in S2T models by comparing its scores to input saliency maps derived from feature attribution. Our analysis spans monolingual and multilingual, single-task and multi-task models at multiple scales, and shows that attention scores moderately to strongly align with saliency-based explanations, particularly when aggregated across heads and layers. However, it also shows that cross-attention captures only about 50% of the input relevance and, in the best case, only partially reflects how the decoder attends to the encoder's representations--accounting for just 52-75% of the saliency. These findings uncover fundamental limitations in interpreting cross-attention as an explanatory proxy, suggesting that it offers an informative yet incomplete view of the factors driving predictions in S2T models.

## 📝 요약

이 논문은 음성-텍스트(S2T) 모델에서의 교차 주의 메커니즘의 설명력을 평가합니다. 교차 주의 점수가 입력 음성 표현과 생성된 텍스트 간의 의존성을 반영한다고 가정하여 다양한 응용에 사용되어 왔지만, 음성 분야에서는 이 가정이 충분히 탐구되지 않았습니다. 저자들은 교차 주의 점수와 입력 중요도 맵을 비교하여 이 가정을 검토하였습니다. 분석 결과, 주의 점수는 중요도 기반 설명과 중간에서 강한 상관관계를 보였으나, 입력 관련성을 약 50%만 포착하며, 디코더가 인코더 표현에 주의를 기울이는 방식을 부분적으로만 반영했습니다. 이는 S2T 모델의 예측 요인을 설명하는 데 있어 교차 주의가 불완전한 정보를 제공함을 시사합니다.

## 🎯 주요 포인트

- 1. Cross-attention 메커니즘은 음성-텍스트(S2T) 처리 분야에서 핵심적인 역할을 하며, 다양한 하위 응용 프로그램에 활용되고 있습니다.
- 2. S2T 모델에서의 cross-attention 점수는 입력 음성 표현과 생성된 텍스트 간의 의존성을 반영한다고 가정되지만, 이 가정은 음성 분야에서 충분히 탐구되지 않았습니다.
- 3. 연구 결과, cross-attention 점수는 saliency 기반 설명과 중간에서 강한 수준으로 일치하지만, 입력 관련성을 약 50%만 포착합니다.
- 4. Cross-attention은 디코더가 인코더의 표현에 주의를 기울이는 방식을 부분적으로만 반영하며, saliency의 52-75%만 설명합니다.
- 5. 이러한 결과는 cross-attention을 설명적 프록시로 해석하는 데 근본적인 한계가 있음을 드러내며, S2T 모델의 예측을 주도하는 요인들에 대한 불완전한 시각을 제공합니다.


---

*Generated on 2025-09-24 00:16:57*