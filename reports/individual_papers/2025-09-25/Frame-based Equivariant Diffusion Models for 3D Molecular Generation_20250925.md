---
keywords:
  - Transformer
  - Equivariance
  - Frame-based Diffusion
  - Molecular Generation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19506
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:36:43.250321",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Equivariance",
    "Frame-based Diffusion",
    "Molecular Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Equivariance": 0.78,
    "Frame-based Diffusion": 0.8,
    "Molecular Generation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformer",
        "canonical": "Transformer",
        "aliases": [
          "EdgeDiT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in machine learning, and linking to them can enhance understanding of the diffusion model's architecture.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "E(3)-equivariance",
        "canonical": "Equivariance",
        "aliases": [
          "E(3) symmetry"
        ],
        "category": "unique_technical",
        "rationale": "E(3)-equivariance is a specific type of symmetry important in molecular generation, providing a unique technical aspect to link.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Global Frame Diffusion",
        "canonical": "Frame-based Diffusion",
        "aliases": [
          "GFD",
          "Local Frame Diffusion",
          "Invariant Frame Diffusion"
        ],
        "category": "unique_technical",
        "rationale": "Frame-based diffusion is central to the paper's methodology, offering a unique approach to molecular generation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Molecular Generation",
        "canonical": "Molecular Generation",
        "aliases": [
          "3D Molecular Generation"
        ],
        "category": "specific_connectable",
        "rationale": "Molecular generation is a specific application area that connects to broader research in computational chemistry and drug discovery.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
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
      "candidate_surface": "Diffusion Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "E(3)-equivariance",
      "resolved_canonical": "Equivariance",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Global Frame Diffusion",
      "resolved_canonical": "Frame-based Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Molecular Generation",
      "resolved_canonical": "Molecular Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Frame-based Equivariant Diffusion Models for 3D Molecular Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19506.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19506](https://arxiv.org/abs/2509.19506)

## 🔗 유사한 논문
- [[2025-09-22/Space Group Equivariant Crystal Diffusion_20250922|Space Group Equivariant Crystal Diffusion]] (82.9% similar)
- [[2025-09-23/Extract and Diffuse_ Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement_20250923|Extract and Diffuse: Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement]] (81.9% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (81.7% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (81.0% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Molecular Generation|Molecular Generation]]
**⚡ Unique Technical**: [[keywords/Equivariance|Equivariance]], [[keywords/Frame-based Diffusion|Frame-based Diffusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19506v1 Announce Type: new 
Abstract: Recent methods for molecular generation face a trade-off: they either enforce strict equivariance with costly architectures or relax it to gain scalability and flexibility. We propose a frame-based diffusion paradigm that achieves deterministic E(3)-equivariance while decoupling symmetry handling from the backbone. Building on this paradigm, we investigate three variants: Global Frame Diffusion (GFD), which assigns a shared molecular frame; Local Frame Diffusion (LFD), which constructs node-specific frames and benefits from additional alignment constraints; and Invariant Frame Diffusion (IFD), which relies on pre-canonicalized invariant representations. To enhance expressivity, we further utilize EdgeDiT, a Diffusion Transformer with edge-aware attention.
  On the QM9 dataset, GFD with EdgeDiT achieves state-of-the-art performance, with a test NLL of -137.97 at standard scale and -141.85 at double scale, alongside atom stability of 98.98%, and molecular stability of 90.51%. These results surpass all equivariant baselines while maintaining high validity and uniqueness and nearly 2x faster sampling compared to EDM. Altogether, our study establishes frame-based diffusion as a scalable, flexible, and physically grounded paradigm for molecular generation, highlighting the critical role of global structure preservation.

## 📝 요약

최근 분자 생성 방법은 엄격한 등변성을 유지하는 대신 확장성과 유연성을 얻기 위해 이를 완화하는 경향이 있습니다. 우리는 대칭 처리를 백본과 분리하여 결정론적 E(3)-등변성을 달성하는 프레임 기반 확산 패러다임을 제안합니다. 이를 바탕으로 세 가지 변형을 연구했습니다: 공유 분자 프레임을 할당하는 Global Frame Diffusion(GFD), 노드별 프레임을 구성하는 Local Frame Diffusion(LFD), 그리고 사전 표준화된 불변 표현을 사용하는 Invariant Frame Diffusion(IFD)입니다. 또한, EdgeDiT라는 엣지 인식 주의 메커니즘을 갖춘 Diffusion Transformer를 활용하여 표현력을 높였습니다. QM9 데이터셋에서 GFD와 EdgeDiT는 최첨단 성능을 기록했으며, 이는 모든 등변성 기준을 초과하며, EDM 대비 거의 2배 빠른 샘플링 속도를 보여줍니다. 이 연구는 프레임 기반 확산이 분자 생성에 있어 확장 가능하고 유연하며 물리적으로 근거 있는 패러다임임을 입증하며, 전역 구조 보존의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. 분자 생성 방법에서 엄격한 등변성을 유지하면서도 확장성과 유연성을 확보할 수 있는 프레임 기반 확산 패러다임을 제안했습니다.
- 2. 제안된 패러다임은 E(3)-등변성을 달성하면서 대칭 처리를 백본과 분리합니다.
- 3. 세 가지 변형(GFD, LFD, IFD)을 조사했으며, GFD는 EdgeDiT와 결합하여 QM9 데이터셋에서 최첨단 성능을 달성했습니다.
- 4. GFD는 테스트 NLL -137.97(표준 스케일) 및 -141.85(더블 스케일)를 기록했으며, 원자 안정성 98.98%, 분자 안정성 90.51%를 달성했습니다.
- 5. 연구 결과는 프레임 기반 확산이 분자 생성에 있어 확장 가능하고 유연하며 물리적으로 근거 있는 패러다임임을 입증했습니다.


---

*Generated on 2025-09-25 16:36:43*