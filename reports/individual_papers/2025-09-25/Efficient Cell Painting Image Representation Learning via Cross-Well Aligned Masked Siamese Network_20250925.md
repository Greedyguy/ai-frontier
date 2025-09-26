---
keywords:
  - Cross-Well Aligned Masked Siamese Network
  - Self-supervised Learning
  - Cell Painting
  - Contrastive Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19896
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:09:13.568862",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cross-Well Aligned Masked Siamese Network",
    "Self-supervised Learning",
    "Cell Painting",
    "Contrastive Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cross-Well Aligned Masked Siamese Network": 0.8,
    "Self-supervised Learning": 0.85,
    "Cell Painting": 0.78,
    "Contrastive Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cross-Well Aligned Masked Siamese Network",
        "canonical": "Cross-Well Aligned Masked Siamese Network",
        "aliases": [
          "CWA-MSN"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel representation learning framework specific to the paper, offering unique insights into phenotype modeling.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a key method used in the paper, linking it to a broader context of machine learning techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cell Painting",
        "canonical": "Cell Painting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific assay technique central to the study, providing a unique context for biological image representation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Contrastive Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This method is compared against in the paper, offering a point of connection to other studies using similar techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "computational models",
      "batch effects"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cross-Well Aligned Masked Siamese Network",
      "resolved_canonical": "Cross-Well Aligned Masked Siamese Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cell Painting",
      "resolved_canonical": "Cell Painting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Efficient Cell Painting Image Representation Learning via Cross-Well Aligned Masked Siamese Network

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19896.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19896](https://arxiv.org/abs/2509.19896)

## 🔗 유사한 논문
- [[2025-09-25/CellCLIP -- Learning Perturbation Effects in Cell Painting via Text-Guided Contrastive Learning_20250925|CellCLIP -- Learning Perturbation Effects in Cell Painting via Text-Guided Contrastive Learning]] (85.4% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (82.2% similar)
- [[2025-09-23/SynergyNet_ Fusing Generative Priors and State-Space Models for Facial Beauty Prediction_20250923|SynergyNet: Fusing Generative Priors and State-Space Models for Facial Beauty Prediction]] (82.2% similar)
- [[2025-09-23/SISMA_ Semantic Face Image Synthesis with Mamba_20250923|SISMA: Semantic Face Image Synthesis with Mamba]] (82.1% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Contrastive Learning|Contrastive Learning]]
**⚡ Unique Technical**: [[keywords/Cross-Well Aligned Masked Siamese Network|Cross-Well Aligned Masked Siamese Network]], [[keywords/Cell Painting|Cell Painting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19896v1 Announce Type: new 
Abstract: Computational models that predict cellular phenotypic responses to chemical and genetic perturbations can accelerate drug discovery by prioritizing therapeutic hypotheses and reducing costly wet-lab iteration. However, extracting biologically meaningful and batch-robust cell painting representations remains challenging. Conventional self-supervised and contrastive learning approaches often require a large-scale model and/or a huge amount of carefully curated data, still struggling with batch effects. We present Cross-Well Aligned Masked Siamese Network (CWA-MSN), a novel representation learning framework that aligns embeddings of cells subjected to the same perturbation across different wells, enforcing semantic consistency despite batch effects. Integrated into a masked siamese architecture, this alignment yields features that capture fine-grained morphology while remaining data- and parameter-efficient. For instance, in a gene-gene relationship retrieval benchmark, CWA-MSN outperforms the state-of-the-art publicly available self-supervised (OpenPhenom) and contrastive learning (CellCLIP) methods, improving the benchmark scores by +29\% and +9\%, respectively, while training on substantially fewer data (e.g., 0.2M images for CWA-MSN vs. 2.2M images for OpenPhenom) or smaller model size (e.g., 22M parameters for CWA-MSN vs. 1.48B parameters for CellCLIP). Extensive experiments demonstrate that CWA-MSN is a simple and effective way to learn cell image representation, enabling efficient phenotype modeling even under limited data and parameter budgets.

## 📝 요약

이 논문은 세포의 표현을 학습하는 새로운 프레임워크인 Cross-Well Aligned Masked Siamese Network (CWA-MSN)을 제안합니다. CWA-MSN은 배치 효과에도 불구하고 동일한 처리 조건을 받은 세포의 임베딩을 정렬하여 의미론적 일관성을 유지합니다. 이 방법은 데이터와 파라미터 효율성을 높이면서 세포의 세밀한 형태를 포착하는 특징을 제공합니다. CWA-MSN은 유전자 관계 검색 벤치마크에서 기존의 자가 지도 학습(OpenPhenom) 및 대조 학습(CellCLIP) 방법보다 우수한 성능을 보이며, 적은 데이터와 작은 모델 크기로도 높은 성능을 달성합니다. 이 연구는 제한된 데이터와 파라미터 환경에서도 효율적인 표현 학습이 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. CWA-MSN은 배치 효과에도 불구하고 동일한 처리에 대한 세포의 임베딩을 정렬하여 의미론적 일관성을 강화하는 새로운 표현 학습 프레임워크입니다.
- 2. CWA-MSN은 마스크드 시암 네트워크 아키텍처에 통합되어 세밀한 형태학을 포착하는 동시에 데이터 및 파라미터 효율성을 유지합니다.
- 3. CWA-MSN은 제한된 데이터와 파라미터 예산 하에서도 효율적인 표현 학습을 가능하게 하여, OpenPhenom 및 CellCLIP 대비 우수한 성능을 보입니다.
- 4. CWA-MSN은 기존의 셀프 슈퍼바이즈드 및 대조 학습 방법보다 적은 데이터와 작은 모델 크기로도 뛰어난 성능을 발휘합니다.
- 5. CWA-MSN은 유전자-유전자 관계 검색 벤치마크에서 OpenPhenom과 CellCLIP을 각각 +29% 및 +9% 개선된 점수로 능가합니다.


---

*Generated on 2025-09-26 09:09:13*