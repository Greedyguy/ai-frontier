---
keywords:
  - Diffusion Models
  - Attention Mechanism
  - Cross Identity Supervision
  - Portrait Animation
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17476
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:53:03.851229",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Attention Mechanism",
    "Cross Identity Supervision",
    "Portrait Animation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.85,
    "Attention Mechanism": 0.82,
    "Cross Identity Supervision": 0.8,
    "Portrait Animation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion-based models"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion models are central to the proposed framework, offering a unique approach to portrait animation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "spatial temporal attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "spatial-temporal attention"
        ],
        "category": "specific_connectable",
        "rationale": "This mechanism is crucial for capturing subtle motions, linking to broader attention mechanism concepts.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "cross identity supervision",
        "canonical": "Cross Identity Supervision",
        "aliases": [
          "cross-identity training"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel training strategy enhancing model generalization, relevant for identity-related tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "portrait animation",
        "canonical": "Portrait Animation",
        "aliases": [
          "photo-realistic animation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, this term defines the specific application of the proposed methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "framework",
      "training"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "spatial temporal attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "cross identity supervision",
      "resolved_canonical": "Cross Identity Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "portrait animation",
      "resolved_canonical": "Portrait Animation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Stable Video-Driven Portraits

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17476.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17476](https://arxiv.org/abs/2509.17476)

## 🔗 유사한 논문
- [[2025-09-23/Follow-Your-Emoji-Faster_ Towards Efficient, Fine-Controllable, and Expressive Freestyle Portrait Animation_20250923|Follow-Your-Emoji-Faster: Towards Efficient, Fine-Controllable, and Expressive Freestyle Portrait Animation]] (87.3% similar)
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (85.1% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (84.1% similar)
- [[2025-09-23/Penalizing Boundary Activation for Object Completeness in Diffusion Models_20250923|Penalizing Boundary Activation for Object Completeness in Diffusion Models]] (82.7% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Cross Identity Supervision|Cross Identity Supervision]], [[keywords/Portrait Animation|Portrait Animation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17476v1 Announce Type: new 
Abstract: Portrait animation aims to generate photo-realistic videos from a single source image by reenacting the expression and pose from a driving video. While early methods relied on 3D morphable models or feature warping techniques, they often suffered from limited expressivity, temporal inconsistency, and poor generalization to unseen identities or large pose variations. Recent advances using diffusion models have demonstrated improved quality but remain constrained by weak control signals and architectural limitations. In this work, we propose a novel diffusion based framework that leverages masked facial regions specifically the eyes, nose, and mouth from the driving video as strong motion control cues. To enable robust training without appearance leakage, we adopt cross identity supervision. To leverage the strong prior from the pretrained diffusion model, our novel architecture introduces minimal new parameters that converge faster and help in better generalization. We introduce spatial temporal attention mechanisms that allow inter frame and intra frame interactions, effectively capturing subtle motions and reducing temporal artifacts. Our model uses history frames to ensure continuity across segments. At inference, we propose a novel signal fusion strategy that balances motion fidelity with identity preservation. Our approach achieves superior temporal consistency and accurate expression control, enabling high-quality, controllable portrait animation suitable for real-world applications.

## 📝 요약

이 논문은 단일 이미지에서 사진과 같은 영상을 생성하는 초상화 애니메이션 기술을 제안합니다. 기존 방법들은 3D 모델이나 특징 왜곡 기술에 의존했으나, 표현력 부족과 시간적 일관성 문제를 겪었습니다. 본 연구는 확산 모델을 활용하여 눈, 코, 입 등 얼굴의 특정 부위를 강력한 움직임 제어 신호로 사용합니다. 외관 누출 없이 강력한 학습을 위해 교차 신원 감독을 채택하고, 사전 학습된 확산 모델의 강력한 사전 지식을 활용하여 최소한의 새로운 매개변수를 도입했습니다. 공간-시간 주의 메커니즘을 통해 프레임 간 상호작용을 촉진하여 미세한 움직임을 포착하고 시간적 왜곡을 줄였습니다. 추론 시에는 움직임 충실도와 신원 보존을 균형 있게 유지하는 신호 융합 전략을 제안합니다. 이 접근법은 시간적 일관성과 정확한 표현 제어를 달성하여 실제 응용에 적합한 고품질의 초상화 애니메이션을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 단일 소스 이미지에서 주행 비디오의 표정과 자세를 재현하여 사진 실감 비디오를 생성하는 초상화 애니메이션을 목표로 한다.
- 2. 기존 방법의 한계를 극복하기 위해, 주행 비디오에서 눈, 코, 입 등 마스크된 얼굴 부위를 강력한 모션 제어 신호로 활용하는 새로운 확산 기반 프레임워크를 제안한다.
- 3. 교차 정체성 감독을 채택하여 외모 누출 없이 강력한 훈련을 가능하게 하고, 사전 학습된 확산 모델의 강력한 사전 지식을 활용하기 위해 최소한의 새로운 매개변수를 도입한다.
- 4. 공간적 시간적 주의 메커니즘을 도입하여 프레임 간 및 프레임 내 상호작용을 허용하고, 미세한 움직임을 효과적으로 포착하며 시간적 아티팩트를 줄인다.
- 5. 제안된 모델은 모션 충실도와 정체성 보존을 균형 있게 유지하는 새로운 신호 융합 전략을 통해 높은 품질의 제어 가능한 초상화 애니메이션을 실현한다.


---

*Generated on 2025-09-24 04:53:03*