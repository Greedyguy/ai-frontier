<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:29:31.384261",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Multimodal Learning",
    "THFlow",
    "Peptide-Protein Binding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.78,
    "Multimodal Learning": 0.82,
    "THFlow": 0.89,
    "Peptide-Protein Binding": 0.84
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Generative Models",
        "canonical": "Deep Learning",
        "aliases": [
          "Generative Models",
          "Deep Models"
        ],
        "category": "broad_technical",
        "rationale": "Deep generative models are a subset of deep learning, which is a foundational concept in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multimodal Temporal Inconsistency",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Temporal Inconsistency",
          "Multimodal Inconsistency"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's problem statement and links to broader multimodal learning discussions.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.83,
        "link_intent_score": 0.82
      },
      {
        "surface": "THFlow",
        "canonical": "THFlow",
        "aliases": [
          "Temporally Hierarchical Flow"
        ],
        "category": "unique_technical",
        "rationale": "THFlow is the novel framework proposed in the paper, crucial for understanding the specific solution presented.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.92,
        "link_intent_score": 0.89
      },
      {
        "surface": "Peptide-Protein Binding",
        "canonical": "Peptide-Protein Binding",
        "aliases": [
          "Protein Binding",
          "Peptide Binding"
        ],
        "category": "unique_technical",
        "rationale": "This is a key biological process discussed in the paper, relevant for linking to biochemical and therapeutic contexts.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.84
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
      "candidate_surface": "Deep Generative Models",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.67,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multimodal Temporal Inconsistency",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.83,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "THFlow",
      "resolved_canonical": "THFlow",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.92,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Peptide-Protein Binding",
      "resolved_canonical": "Peptide-Protein Binding",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.84
      }
    }
  ]
}
-->

# THFlow: A Temporally Hierarchical Flow Matching Framework for 3D Peptide Design

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.15855.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2502.15855](https://arxiv.org/abs/2502.15855)

## 🔗 유사한 논문
- [[2025-09-24/Flow marching for a generative PDE foundation model_20250924|Flow marching for a generative PDE foundation model]] (82.6% similar)
- [[2025-09-23/TempFlow-GRPO_ When Timing Matters for GRPO in Flow Models_20250923|TempFlow-GRPO: When Timing Matters for GRPO in Flow Models]] (81.6% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (80.3% similar)
- [[2025-09-22/ChannelFlow-Tools_ A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows_20250922|ChannelFlow-Tools: A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows]] (79.5% similar)
- [[2025-09-23/Emergent 3D Correspondence from Neural Shape Representation_20250923|Emergent 3D Correspondence from Neural Shape Representation]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/THFlow|THFlow]], [[keywords/Peptide-Protein Binding|Peptide-Protein Binding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.15855v2 Announce Type: replace-cross 
Abstract: Deep generative models provide a promising approach to de novo 3D peptide design. Most of them jointly model the distributions of peptide's position, orientation, and conformation, attempting to simultaneously converge to the target pocket. However, in the early stage of docking, optimizing conformation-only modalities such as rotation and torsion can be physically meaningless, as the peptide is initialized far from the protein pocket and no interaction field is present. We define this problem as the multimodal temporal inconsistency problem and claim it is a key factor contributing to low binding affinity in generated peptides. To address this challenge, we propose THFlow, a novel flow matching-based multimodal generative model that explicitly models the temporal hierarchy between peptide position and conformation. It employs a polynomial based conditional flow to accelerate positional convergence early on, and later aligns it with rotation and torsion for coordinated conformation refinement under the emerging interaction field. Additionally, we incorporate interaction-related features, such as polarity, to further enhance the model's understanding of peptide-protein binding. Extensive experiments demonstrate that THFlow outperforms existing methods in generating peptides with superior stability, affinity, and diversity, offering an effective and accurate solution for advancing peptide-based therapeutic development.

## 📝 요약

이 논문은 새로운 3D 펩타이드 설계를 위한 딥 생성 모델의 문제점을 해결하기 위해 THFlow라는 모델을 제안합니다. 기존 모델들은 펩타이드의 위치, 방향, 형태를 동시에 모델링하지만, 초기 도킹 단계에서 이는 비효율적입니다. THFlow는 위치와 형태 간의 시간적 계층을 명시적으로 모델링하여, 초기에는 위치 수렴을 가속화하고 이후 회전과 비틀림을 조정하여 결합 친화성을 높입니다. 또한, 극성 등 상호작용 관련 특징을 포함하여 펩타이드-단백질 결합 이해를 강화합니다. 실험 결과, THFlow는 안정성, 친화성, 다양성 면에서 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 딥 생성 모델은 새로운 3D 펩타이드 설계에 유망한 접근 방식을 제공하며, 대부분은 펩타이드의 위치, 방향, 형태의 분포를 공동으로 모델링합니다.
- 2. 초기 도킹 단계에서는 회전 및 비틀림과 같은 형태 전용 모달리티 최적화가 물리적으로 무의미할 수 있으며, 이를 다중 모달 시간 불일치 문제로 정의합니다.
- 3. THFlow는 펩타이드 위치와 형태 간의 시간적 계층 구조를 명시적으로 모델링하는 새로운 흐름 매칭 기반 다중 모달 생성 모델입니다.
- 4. THFlow는 초기 위치 수렴을 가속화하고, 나중에 회전 및 비틀림과 정렬하여 상호작용 필드 하에서 형태 정제를 조정합니다.
- 5. THFlow는 펩타이드-단백질 결합의 이해를 향상시키기 위해 극성 등 상호작용 관련 특징을 통합하며, 실험 결과 기존 방법보다 우수한 안정성, 친화성, 다양성을 가진 펩타이드를 생성합니다.


---

*Generated on 2025-09-24 14:29:31*