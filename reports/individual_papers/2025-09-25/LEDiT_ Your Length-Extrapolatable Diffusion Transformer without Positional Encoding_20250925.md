---
keywords:
  - Transformer
  - Attention Mechanism
  - LEDiT
  - Locality Enhancement Module
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2503.04344
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:23:38.338940",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Attention Mechanism",
    "LEDiT",
    "Locality Enhancement Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Attention Mechanism": 0.9,
    "LEDiT": 0.8,
    "Locality Enhancement Module": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformer",
        "canonical": "Transformer",
        "aliases": [
          "DiT",
          "Diffusion Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, and linking to them provides a broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "causal attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "causal attention mechanism"
        ],
        "category": "specific_connectable",
        "rationale": "Causal attention is a specific type of attention mechanism, crucial for understanding the paper's approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Length-Extrapolatable Diffusion Transformer",
        "canonical": "LEDiT",
        "aliases": [
          "Length-Extrapolatable DiT"
        ],
        "category": "unique_technical",
        "rationale": "LEDiT is a novel concept introduced in the paper, representing a significant technical innovation.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.95,
        "link_intent_score": 0.8
      },
      {
        "surface": "locality enhancement module",
        "canonical": "Locality Enhancement Module",
        "aliases": [
          "locality module"
        ],
        "category": "unique_technical",
        "rationale": "This module is a unique component of the proposed model, enhancing its technical specificity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "positional encoding",
      "resolution scaling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "causal attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Length-Extrapolatable Diffusion Transformer",
      "resolved_canonical": "LEDiT",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.95,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "locality enhancement module",
      "resolved_canonical": "Locality Enhancement Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# LEDiT: Your Length-Extrapolatable Diffusion Transformer without Positional Encoding

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.04344.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2503.04344](https://arxiv.org/abs/2503.04344)

## 🔗 유사한 논문
- [[2025-09-23/In-Context Edit_ Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer_20250923|In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer]] (83.0% similar)
- [[2025-09-23/LRQ-DiT_ Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation_20250923|LRQ-DiT: Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation]] (82.6% similar)
- [[2025-09-23/Context-aware Biases for Length Extrapolation_20250923|Context-aware Biases for Length Extrapolation]] (82.5% similar)
- [[2025-09-24/Foresight_ Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation_20250924|Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation]] (82.1% similar)
- [[2025-09-24/SparseDiT_ Token Sparsification for Efficient Diffusion Transformer_20250924|SparseDiT: Token Sparsification for Efficient Diffusion Transformer]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/LEDiT|LEDiT]], [[keywords/Locality Enhancement Module|Locality Enhancement Module]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04344v3 Announce Type: replace 
Abstract: Diffusion transformers (DiTs) struggle to generate images at resolutions higher than their training resolutions. The primary obstacle is that the explicit positional encodings(PE), such as RoPE, need extrapolating to unseen positions which degrades performance when the inference resolution differs from training. In this paper, We propose a Length-Extrapolatable Diffusion Transformer~(LEDiT) to overcome this limitation. LEDiT needs no explicit PEs, thereby avoiding PE extrapolation. The key innovation of LEDiT lies in the use of causal attention. We demonstrate that causal attention can implicitly encode global positional information and show that such information facilitates extrapolation. We further introduce a locality enhancement module, which captures fine-grained local information to complement the global coarse-grained position information encoded by causal attention. Experimental results on both conditional and text-to-image generation tasks demonstrate that LEDiT supports up to 4x resolution scaling (e.g., from 256x256 to 512x512), achieving better image quality compared to the state-of-the-art length extrapolation methods. We believe that LEDiT marks a departure from the standard RoPE-based methods and offers a promising insight into length extrapolation. Project page: https://shenzhang2145.github.io/ledit/

## 📝 요약

이 논문에서는 고해상도 이미지 생성을 위한 Length-Extrapolatable Diffusion Transformer(LEDiT)을 제안합니다. 기존의 Diffusion Transformers는 명시적 위치 인코딩(PE) 문제로 인해 훈련 해상도를 초과하는 이미지 생성에 어려움을 겪습니다. LEDiT는 명시적 PE를 사용하지 않고 인과적 주의를 통해 전역 위치 정보를 암묵적으로 인코딩하여 이 문제를 해결합니다. 또한, 세밀한 지역 정보를 포착하는 locality enhancement 모듈을 도입하여 인과적 주의로 인코딩된 전역 정보를 보완합니다. 실험 결과, LEDiT는 최대 4배 해상도 확장을 지원하며, 기존 방법보다 우수한 이미지 품질을 제공합니다. 이는 RoPE 기반 방법에서 벗어나 새로운 길을 제시하는 중요한 기여입니다.

## 🎯 주요 포인트

- 1. Diffusion transformers는 훈련 해상도보다 높은 해상도의 이미지를 생성하는 데 어려움을 겪습니다.
- 2. LEDiT는 명시적 위치 인코딩 없이도 작동하여 위치 인코딩의 외삽 문제를 피합니다.
- 3. LEDiT의 핵심 혁신은 인과적 주의(attention)를 사용하여 전역 위치 정보를 암묵적으로 인코딩하는 것입니다.
- 4. 실험 결과, LEDiT는 최대 4배 해상도 확장을 지원하며, 기존의 길이 외삽 방법들보다 더 나은 이미지 품질을 보여줍니다.
- 5. LEDiT는 RoPE 기반 방법에서 벗어나 길이 외삽에 대한 새로운 통찰을 제공합니다.


---

*Generated on 2025-09-26 09:23:38*