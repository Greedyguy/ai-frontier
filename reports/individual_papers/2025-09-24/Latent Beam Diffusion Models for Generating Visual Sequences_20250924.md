<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:27:59.362288",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Beam Search",
    "Latent Space Exploration",
    "Attention Mechanism",
    "Visual Consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "Beam Search": 0.81,
    "Latent Space Exploration": 0.79,
    "Attention Mechanism": 0.82,
    "Visual Consistency": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion model"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are central to the paper's methodology and connect to broader machine learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "beam search strategy",
        "canonical": "Beam Search",
        "aliases": [
          "beam search"
        ],
        "category": "specific_connectable",
        "rationale": "Beam search is a key technique for generating coherent sequences, linking to search and optimization methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.81
      },
      {
        "surface": "latent space exploration",
        "canonical": "Latent Space Exploration",
        "aliases": [
          "exploration of latent space"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the paper's approach, focusing on exploring latent spaces for sequence generation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "cross-attention mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "cross-attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for aligning textual prompts with visual content, enhancing connectivity.",
        "novelty_score": 0.52,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "visual consistency",
        "canonical": "Visual Consistency",
        "aliases": [
          "consistency in visuals"
        ],
        "category": "unique_technical",
        "rationale": "Ensuring visual consistency is a unique challenge addressed by the paper, relevant for narrative coherence.",
        "novelty_score": 0.66,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "beam search strategy",
      "resolved_canonical": "Beam Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "latent space exploration",
      "resolved_canonical": "Latent Space Exploration",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "cross-attention mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "visual consistency",
      "resolved_canonical": "Visual Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Latent Beam Diffusion Models for Generating Visual Sequences

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.20429.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2503.20429](https://arxiv.org/abs/2503.20429)

## 🔗 유사한 논문
- [[2025-09-24/DS-Diffusion_ Data Style-Guided Diffusion Model for Time-Series Generation_20250924|DS-Diffusion: Data Style-Guided Diffusion Model for Time-Series Generation]] (84.0% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (83.9% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (83.7% similar)
- [[2025-09-24/Foresight_ Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation_20250924|Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation]] (83.2% similar)
- [[2025-09-23/Image-to-Brain Signal Generation for Visual Prosthesis with CLIP Guided Multimodal Diffusion Models_20250923|Image-to-Brain Signal Generation for Visual Prosthesis with CLIP Guided Multimodal Diffusion Models]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Beam Search|Beam Search]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Latent Space Exploration|Latent Space Exploration]], [[keywords/Visual Consistency|Visual Consistency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.20429v3 Announce Type: replace 
Abstract: While diffusion models excel at generating high-quality images from text prompts, they struggle with visual consistency when generating image sequences. Existing methods generate each image independently, leading to disjointed narratives - a challenge further exacerbated in non-linear storytelling, where scenes must connect beyond adjacent images. We introduce a novel beam search strategy for latent space exploration, enabling conditional generation of full image sequences with beam search decoding. In contrast to earlier methods that rely on fixed latent priors, our method dynamically samples past latents to search for an optimal sequence of latent representations, ensuring coherent visual transitions. As the latent denoising space is explored, the beam search graph is pruned with a cross-attention mechanism that efficiently scores search paths, prioritizing alignment with both textual prompts and visual context. Human and automatic evaluations confirm that BeamDiffusion outperforms other baseline methods, producing full sequences with superior coherence, visual continuity, and textual alignment.

## 📝 요약

이 논문은 텍스트 프롬프트로부터 이미지 시퀀스를 생성할 때 시각적 일관성 문제를 해결하기 위한 새로운 방법을 제안합니다. 기존 방법들은 각 이미지를 독립적으로 생성하여 연결성이 부족한 서사를 만들지만, 이 연구는 잠재 공간 탐색을 위한 빔 서치 전략을 도입하여 전체 이미지 시퀀스를 조건부로 생성합니다. 고정된 잠재 프라이어에 의존하지 않고, 과거의 잠재를 동적으로 샘플링하여 최적의 잠재 표현 시퀀스를 찾아내어 시각적 전환의 일관성을 보장합니다. 또한, 크로스 어텐션 메커니즘을 사용하여 탐색 경로를 효율적으로 평가하고 텍스트 프롬프트와 시각적 컨텍스트에 맞춰 정렬을 우선시합니다. 인간 및 자동 평가 결과, BeamDiffusion은 다른 기준 방법보다 우수한 시퀀스 일관성, 시각적 연속성 및 텍스트 정렬을 보여줍니다.

## 🎯 주요 포인트

- 1. 확산 모델은 텍스트 프롬프트로부터 고품질 이미지를 생성하는 데 뛰어나지만, 이미지 시퀀스를 생성할 때 시각적 일관성 문제를 겪습니다.
- 2. 기존 방법은 각 이미지를 독립적으로 생성하여 비선형 스토리텔링에서 장면 간 연결성을 유지하기 어렵습니다.
- 3. 새로운 빔 서치 전략을 도입하여 잠재 공간 탐색을 통해 전체 이미지 시퀀스를 조건부로 생성할 수 있습니다.
- 4. 제안된 방법은 고정된 잠재 사전 대신 과거 잠재 샘플링을 통해 최적의 잠재 표현 시퀀스를 탐색하여 일관된 시각적 전환을 보장합니다.
- 5. BeamDiffusion은 인간 및 자동 평가에서 다른 기준 방법보다 우수한 시퀀스 일관성, 시각적 연속성 및 텍스트 정렬을 보여줍니다.


---

*Generated on 2025-09-24 16:27:59*