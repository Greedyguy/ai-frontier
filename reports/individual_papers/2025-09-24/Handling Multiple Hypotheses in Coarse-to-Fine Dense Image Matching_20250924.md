<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:33:12.669895",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dense Image Matching",
    "Coarse-to-Fine Mechanism",
    "Attention Mechanism",
    "BEAMER Architecture"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dense Image Matching": 0.78,
    "Coarse-to-Fine Mechanism": 0.72,
    "Attention Mechanism": 0.8,
    "BEAMER Architecture": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dense Image Matching",
        "canonical": "Dense Image Matching",
        "aliases": [
          "Dense Matching",
          "Pixel Correspondence"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper, offering unique insights into image processing tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Coarse-to-Fine Mechanism",
        "canonical": "Coarse-to-Fine Mechanism",
        "aliases": [
          "Hierarchical Matching",
          "Multi-Scale Approach"
        ],
        "category": "unique_technical",
        "rationale": "This technique is crucial for understanding the hierarchical processing approach in image matching.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Cross-Attention Layers",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Cross Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing concepts in neural network architectures, enhancing understanding of attention mechanisms.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "BEAMER",
        "canonical": "BEAMER Architecture",
        "aliases": [
          "BEAMER Model"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel architecture that may become a reference point for future research in dense matching.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "hypothesis",
      "scale"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dense Image Matching",
      "resolved_canonical": "Dense Image Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Coarse-to-Fine Mechanism",
      "resolved_canonical": "Coarse-to-Fine Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Cross-Attention Layers",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "BEAMER",
      "resolved_canonical": "BEAMER Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Handling Multiple Hypotheses in Coarse-to-Fine Dense Image Matching

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08805.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.08805](https://arxiv.org/abs/2509.08805)

## 🔗 유사한 논문
- [[2025-09-23/Efficient Beam Search for Large Language Models Using Trie-Based Decoding_20250923|Efficient Beam Search for Large Language Models Using Trie-Based Decoding]] (81.1% similar)
- [[2025-09-22/DistillMatch_ Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching_20250922|DistillMatch: Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching]] (81.0% similar)
- [[2025-09-23/CoBEVMoE_ Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception_20250923|CoBEVMoE: Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception]] (80.7% similar)
- [[2025-09-24/Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable_20250924|Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable]] (80.2% similar)
- [[2025-09-24/Do It Yourself_ Learning Semantic Correspondence from Pseudo-Labels_20250924|Do It Yourself: Learning Semantic Correspondence from Pseudo-Labels]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Dense Image Matching|Dense Image Matching]], [[keywords/Coarse-to-Fine Mechanism|Coarse-to-Fine Mechanism]], [[keywords/BEAMER Architecture|BEAMER Architecture]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08805v2 Announce Type: replace 
Abstract: Dense image matching aims to find a correspondent for every pixel of a source image in a partially overlapping target image. State-of-the-art methods typically rely on a coarse-to-fine mechanism where a single correspondent hypothesis is produced per source location at each scale. In challenging cases -- such as at depth discontinuities or when the target image is a strong zoom-in of the source image -- the correspondents of neighboring source locations are often widely spread and predicting a single correspondent hypothesis per source location at each scale may lead to erroneous matches. In this paper, we investigate the idea of predicting multiple correspondent hypotheses per source location at each scale instead. We consider a beam search strategy to propagat multiple hypotheses at each scale and propose integrating these multiple hypotheses into cross-attention layers, resulting in a novel dense matching architecture called BEAMER. BEAMER learns to preserve and propagate multiple hypotheses across scales, making it significantly more robust than state-of-the-art methods, especially at depth discontinuities or when the target image is a strong zoom-in of the source image.

## 📝 요약

이 논문은 밀집 이미지 매칭 문제를 다루며, 기존 방법들이 각 스케일에서 단일 대응 가설을 생성하는 것과 달리, 각 스케일에서 여러 대응 가설을 예측하는 방식을 제안합니다. 이를 위해 빔 서치 전략을 사용하여 여러 가설을 전파하고, 이를 교차 주의 레이어에 통합하여 새로운 밀집 매칭 아키텍처인 BEAMER를 개발했습니다. BEAMER는 깊이 불연속성이나 타겟 이미지가 소스 이미지의 강한 줌인인 경우에도 보다 강력한 성능을 발휘합니다.

## 🎯 주요 포인트

- 1. 밀집 이미지 매칭은 소스 이미지의 각 픽셀에 대해 부분적으로 겹치는 타겟 이미지에서 대응점을 찾는 것을 목표로 한다.
- 2. 기존 방법들은 각 스케일에서 소스 위치당 단일 대응 가설을 생성하는 조밀-대-조밀 메커니즘에 의존한다.
- 3. 본 논문에서는 각 스케일에서 소스 위치당 다중 대응 가설을 예측하는 아이디어를 탐구한다.
- 4. BEAMER라는 새로운 밀집 매칭 아키텍처를 제안하며, 이는 다중 가설을 보존하고 스케일 간에 전파하는 학습을 통해 깊이 불연속성이나 타겟 이미지가 소스 이미지의 강한 줌인일 때 더 강력한 성능을 발휘한다.
- 5. BEAMER는 다중 가설을 크로스-어텐션 레이어에 통합하여 기존 방법보다 더 강력한 성능을 보여준다.


---

*Generated on 2025-09-24 16:33:12*