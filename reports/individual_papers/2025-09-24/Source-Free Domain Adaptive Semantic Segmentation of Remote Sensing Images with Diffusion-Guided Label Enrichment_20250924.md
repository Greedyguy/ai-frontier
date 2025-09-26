<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:01:16.069658",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Source-Free Domain Adaptation",
    "Diffusion-Guided Label Enrichment",
    "Pseudo-Label Optimization",
    "Remote Sensing Images"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Source-Free Domain Adaptation": 0.78,
    "Diffusion-Guided Label Enrichment": 0.85,
    "Pseudo-Label Optimization": 0.72,
    "Remote Sensing Images": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Source-Free Domain Adaptation",
        "canonical": "Source-Free Domain Adaptation",
        "aliases": [
          "SFDA"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and represents a specific challenge in domain adaptation without source data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Diffusion-Guided Label Enrichment",
        "canonical": "Diffusion-Guided Label Enrichment",
        "aliases": [
          "DGLE"
        ],
        "category": "unique_technical",
        "rationale": "The proposed framework is novel and specific to the paper, enhancing pseudo-label quality in domain adaptation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Pseudo-Label Optimization",
        "canonical": "Pseudo-Label Optimization",
        "aliases": [
          "Pseudo-Labeling"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for improving model performance in the target domain and is widely applicable in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Remote Sensing Images",
        "canonical": "Remote Sensing Images",
        "aliases": [
          "RSI"
        ],
        "category": "broad_technical",
        "rationale": "The paper focuses on semantic segmentation within this specific type of imagery, linking it to broader computer vision applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
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
      "candidate_surface": "Source-Free Domain Adaptation",
      "resolved_canonical": "Source-Free Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Diffusion-Guided Label Enrichment",
      "resolved_canonical": "Diffusion-Guided Label Enrichment",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Pseudo-Label Optimization",
      "resolved_canonical": "Pseudo-Label Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Remote Sensing Images",
      "resolved_canonical": "Remote Sensing Images",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Source-Free Domain Adaptive Semantic Segmentation of Remote Sensing Images with Diffusion-Guided Label Enrichment

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18502.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18502](https://arxiv.org/abs/2509.18502)

## 🔗 유사한 논문
- [[2025-09-23/Prototype-Based Pseudo-Label Denoising for Source-Free Domain Adaptation in Remote Sensing Semantic Segmentation_20250923|Prototype-Based Pseudo-Label Denoising for Source-Free Domain Adaptation in Remote Sensing Semantic Segmentation]] (89.6% similar)
- [[2025-09-23/Training-Free Label Space Alignment for Universal Domain Adaptation_20250923|Training-Free Label Space Alignment for Universal Domain Adaptation]] (84.7% similar)
- [[2025-09-22/Minimal Semantic Sufficiency Meets Unsupervised Domain Generalization_20250922|Minimal Semantic Sufficiency Meets Unsupervised Domain Generalization]] (82.7% similar)
- [[2025-09-24/Improving Low-Resource Sequence Labeling with Knowledge Fusion and Contextual Label Explanations_20250924|Improving Low-Resource Sequence Labeling with Knowledge Fusion and Contextual Label Explanations]] (82.1% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Remote Sensing Images|Remote Sensing Images]]
**🔗 Specific Connectable**: [[keywords/Pseudo-Label Optimization|Pseudo-Label Optimization]]
**⚡ Unique Technical**: [[keywords/Source-Free Domain Adaptation|Source-Free Domain Adaptation]], [[keywords/Diffusion-Guided Label Enrichment|Diffusion-Guided Label Enrichment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18502v1 Announce Type: new 
Abstract: Research on unsupervised domain adaptation (UDA) for semantic segmentation of remote sensing images has been extensively conducted. However, research on how to achieve domain adaptation in practical scenarios where source domain data is inaccessible namely, source-free domain adaptation (SFDA) remains limited. Self-training has been widely used in SFDA, which requires obtaining as many high-quality pseudo-labels as possible to train models on target domain data. Most existing methods optimize the entire pseudo-label set to obtain more supervisory information. However, as pseudo-label sets often contain substantial noise, simultaneously optimizing all labels is challenging. This limitation undermines the effectiveness of optimization approaches and thus restricts the performance of self-training. To address this, we propose a novel pseudo-label optimization framework called Diffusion-Guided Label Enrichment (DGLE), which starts from a few easily obtained high-quality pseudo-labels and propagates them to a complete set of pseudo-labels while ensuring the quality of newly generated labels. Firstly, a pseudo-label fusion method based on confidence filtering and super-resolution enhancement is proposed, which utilizes cross-validation of details and contextual information to obtain a small number of high-quality pseudo-labels as initial seeds. Then, we leverage the diffusion model to propagate incomplete seed pseudo-labels with irregular distributions due to its strong denoising capability for randomly distributed noise and powerful modeling capacity for complex distributions, thereby generating complete and high-quality pseudo-labels. This method effectively avoids the difficulty of directly optimizing the complete set of pseudo-labels, significantly improves the quality of pseudo-labels, and thus enhances the model's performance in the target domain.

## 📝 요약

이 논문은 원천 도메인 데이터가 접근 불가능한 상황에서의 도메인 적응, 즉 소스 프리 도메인 적응(SFDA)을 위한 새로운 방법론을 제안합니다. 기존의 자기 학습 방식은 많은 고품질의 가짜 레이블을 필요로 하지만, 가짜 레이블 세트에 포함된 잡음 때문에 최적화가 어렵습니다. 이를 해결하기 위해, 저자들은 확산 유도 레이블 강화(DGLE)라는 새로운 가짜 레이블 최적화 프레임워크를 제안합니다. 이 방법은 신뢰도 필터링과 초해상도 향상 기법을 통해 소수의 고품질 가짜 레이블을 초기 시드로 사용하고, 확산 모델을 활용해 불완전한 시드 가짜 레이블을 완전하고 고품질의 레이블로 확장합니다. 이 접근법은 가짜 레이블의 품질을 크게 향상시켜 목표 도메인에서 모델 성능을 개선합니다.

## 🎯 주요 포인트

- 1. 원격 감지 이미지의 의미론적 분할을 위한 비지도 도메인 적응 연구가 활발히 진행되고 있지만, 소스 도메인 데이터에 접근할 수 없는 실용적인 시나리오에서의 도메인 적응 연구는 제한적이다.
- 2. 기존의 자기 학습 방법은 전체 가짜 레이블 세트를 최적화하려 하지만, 이는 상당한 노이즈를 포함하고 있어 동시에 최적화하는 것이 어렵다.
- 3. 제안된 Diffusion-Guided Label Enrichment (DGLE) 프레임워크는 소수의 고품질 가짜 레이블에서 시작하여 이를 전체 가짜 레이블로 확산시키며, 새로운 레이블의 품질을 보장한다.
- 4. 신뢰도 필터링과 초해상도 향상을 기반으로 한 가짜 레이블 융합 방법을 통해 초기 시드로 사용할 소수의 고품질 가짜 레이블을 얻는다.
- 5. 확산 모델을 활용하여 불완전한 시드 가짜 레이블을 확산시켜 완전하고 고품질의 가짜 레이블을 생성함으로써, 모델의 타겟 도메인 성능을 향상시킨다.


---

*Generated on 2025-09-24 16:01:16*