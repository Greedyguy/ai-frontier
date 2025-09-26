---
keywords:
  - Brain Tumor Segmentation
  - Test-Time Adaptation
  - Style-Modulated Adaptation
  - Source-Free Domain Generalization
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17925
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:05:42.106906",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Brain Tumor Segmentation",
    "Test-Time Adaptation",
    "Style-Modulated Adaptation",
    "Source-Free Domain Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Brain Tumor Segmentation": 0.8,
    "Test-Time Adaptation": 0.85,
    "Style-Modulated Adaptation": 0.7,
    "Source-Free Domain Generalization": 0.9
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "brain tumor segmentation",
        "canonical": "Brain Tumor Segmentation",
        "aliases": [
          "tumor segmentation in MRI"
        ],
        "category": "unique_technical",
        "rationale": "Highly specific to the medical imaging domain and crucial for linking to neuro-oncology tools.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "test-time adaptation",
        "canonical": "Test-Time Adaptation",
        "aliases": [
          "test-time domain adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "Facilitates connections to adaptation strategies in machine learning, especially in domain shift scenarios.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "style-modulated",
        "canonical": "Style-Modulated Adaptation",
        "aliases": [
          "style-aware adaptation"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to adaptation in MRI, enhancing cross-domain generalization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "source-free cross-domain generalization",
        "canonical": "Source-Free Domain Generalization",
        "aliases": [
          "source-free adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader theme of domain generalization without source data, relevant in privacy-sensitive applications.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.9
      }
    ],
    "ban_list_suggestions": [
      "treatment planning",
      "outcome monitoring",
      "scanner variability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "brain tumor segmentation",
      "resolved_canonical": "Brain Tumor Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "test-time adaptation",
      "resolved_canonical": "Test-Time Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "style-modulated",
      "resolved_canonical": "Style-Modulated Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "source-free cross-domain generalization",
      "resolved_canonical": "Source-Free Domain Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# SmaRT: Style-Modulated Robust Test-Time Adaptation for Cross-Domain Brain Tumor Segmentation in MRI

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17925.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17925](https://arxiv.org/abs/2509.17925)

## 🔗 유사한 논문
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (83.3% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (82.9% similar)
- [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (82.2% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (81.7% similar)
- [[2025-09-23/Unified Multimodal Coherent Field_ Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation_20250923|Unified Multimodal Coherent Field: Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Test-Time Adaptation|Test-Time Adaptation]], [[keywords/Source-Free Domain Generalization|Source-Free Domain Generalization]]
**⚡ Unique Technical**: [[keywords/Brain Tumor Segmentation|Brain Tumor Segmentation]], [[keywords/Style-Modulated Adaptation|Style-Modulated Adaptation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17925v1 Announce Type: new 
Abstract: Reliable brain tumor segmentation in MRI is indispensable for treatment planning and outcome monitoring, yet models trained on curated benchmarks often fail under domain shifts arising from scanner and protocol variability as well as population heterogeneity. Such gaps are especially severe in low-resource and pediatric cohorts, where conventional test-time or source-free adaptation strategies often suffer from instability and structural inconsistency. We propose SmaRT, a style-modulated robust test-time adaptation framework that enables source-free cross-domain generalization. SmaRT integrates style-aware augmentation to mitigate appearance discrepancies, a dual-branch momentum strategy for stable pseudo-label refinement, and structural priors enforcing consistency, integrity, and connectivity. This synergy ensures both adaptation stability and anatomical fidelity under extreme domain shifts. Extensive evaluations on sub-Saharan Africa and pediatric glioma datasets show that SmaRT consistently outperforms state-of-the-art methods, with notable gains in Dice accuracy and boundary precision. Overall, SmaRT bridges the gap between algorithmic advances and equitable clinical applicability, supporting robust deployment of MRI-based neuro-oncology tools in diverse clinical environments. Our source code is available at https://github.com/baiyou1234/SmaRT.

## 📝 요약

이 논문은 MRI 기반 뇌종양 분할의 신뢰성을 높이기 위해 SmaRT라는 새로운 테스트 시간 적응 프레임워크를 제안합니다. SmaRT는 스타일 인식 증강 기법과 이중 분기 모멘텀 전략을 통해 외부 데이터셋에서도 안정적인 적응과 해부학적 일관성을 유지합니다. 특히, 저자원 및 소아 환자 그룹에서 기존 방법보다 뛰어난 성능을 보이며, Dice 정확도와 경계 정밀도에서 유의미한 향상을 달성했습니다. 이 연구는 다양한 임상 환경에서 MRI 기반 신경종양 도구의 공평한 적용을 지원합니다.

## 🎯 주요 포인트

- 1. SmaRT는 스타일-모듈화된 테스트 시간 적응 프레임워크로, 소스 없는 교차 도메인 일반화를 가능하게 합니다.
- 2. 스타일 인식 증강, 이중 분기 모멘텀 전략, 구조적 우선순위를 통합하여 적응 안정성과 해부학적 충실성을 보장합니다.
- 3. SmaRT는 극단적인 도메인 변화에서도 안정적인 적응과 해부학적 일관성을 유지합니다.
- 4. 사하라 사막 이남 아프리카 및 소아 교모세포종 데이터셋에서 SmaRT는 최첨단 방법보다 뛰어난 성능을 보여줍니다.
- 5. SmaRT는 MRI 기반 신경 종양학 도구의 다양한 임상 환경에서의 강력한 배포를 지원합니다.


---

*Generated on 2025-09-24 05:05:42*