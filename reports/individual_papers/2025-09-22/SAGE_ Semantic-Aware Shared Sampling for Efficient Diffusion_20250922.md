---
keywords:
  - Diffusion Models
  - Semantic-Aware Shared Sampling
  - Fréchet Inception Distance
  - Contrastive Language–Image Pretraining
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15865
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:37:41.665105",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Semantic-Aware Shared Sampling",
    "Fréchet Inception Distance",
    "Contrastive Language–Image Pretraining"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "Semantic-Aware Shared Sampling": 0.82,
    "Fréchet Inception Distance": 0.8,
    "Contrastive Language–Image Pretraining": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion",
          "Diffusion Process"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are central to the paper's methodology and have broad applicability across domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semantic-aware shared sampling",
        "canonical": "Semantic-Aware Shared Sampling",
        "aliases": [
          "SAGE",
          "Shared Sampling"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, essential for understanding the proposed efficiency improvements.",
        "novelty_score": 0.92,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "FID",
        "canonical": "Fréchet Inception Distance",
        "aliases": [
          "FID Score"
        ],
        "category": "specific_connectable",
        "rationale": "FID is a standard metric for evaluating the quality of generated images, relevant for linking to evaluation methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "CLIP",
        "canonical": "Contrastive Language–Image Pretraining",
        "aliases": [
          "CLIP Model"
        ],
        "category": "specific_connectable",
        "rationale": "CLIP is a well-known model for vision-language tasks, relevant for linking to multimodal learning discussions.",
        "novelty_score": 0.35,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "sampling cost",
      "generation quality",
      "efficiency gains"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semantic-aware shared sampling",
      "resolved_canonical": "Semantic-Aware Shared Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "FID",
      "resolved_canonical": "Fréchet Inception Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "CLIP",
      "resolved_canonical": "Contrastive Language–Image Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion

**Korean Title:** SAGE: 효율적인 확산을 위한 의미 인식 공유 샘플링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15865.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15865](https://arxiv.org/abs/2509.15865)

## 🔗 유사한 논문
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (83.5% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff: Accelerating Diffusion Model Inference with Self-Speculation]] (81.9% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (80.5% similar)
- [[2025-09-22/SCoT_ Straight Consistent Trajectory for Pre-Trained Diffusion Model Distillations_20250922|SCoT: Straight Consistent Trajectory for Pre-Trained Diffusion Model Distillations]] (80.5% similar)
- [[2025-09-22/Autoguided Online Data Curation for Diffusion Model Training_20250922|Autoguided Online Data Curation for Diffusion Model Training]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Fréchet Inception Distance|Fréchet Inception Distance]], [[keywords/Contrastive Language–Image Pretraining|Contrastive Language–Image Pretraining]]
**⚡ Unique Technical**: [[keywords/Semantic-Aware Shared Sampling|Semantic-Aware Shared Sampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15865v1 Announce Type: new 
Abstract: Diffusion models manifest evident benefits across diverse domains, yet their high sampling cost, requiring dozens of sequential model evaluations, remains a major limitation. Prior efforts mainly accelerate sampling via optimized solvers or distillation, which treat each query independently. In contrast, we reduce total number of steps by sharing early-stage sampling across semantically similar queries. To enable such efficiency gains without sacrificing quality, we propose SAGE, a semantic-aware shared sampling framework that integrates a shared sampling scheme for efficiency and a tailored training strategy for quality preservation. Extensive experiments show that SAGE reduces sampling cost by 25.5%, while improving generation quality with 5.0% lower FID, 5.4% higher CLIP, and 160% higher diversity over baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15865v1 발표 유형: 신규  
초록: 확산 모델은 다양한 분야에서 명백한 이점을 보여주지만, 수십 번의 순차적인 모델 평가가 필요한 높은 샘플링 비용은 여전히 주요 제한 사항으로 남아 있습니다. 이전의 노력들은 주로 최적화된 해법이나 증류를 통해 샘플링을 가속화했으며, 이는 각 쿼리를 독립적으로 처리했습니다. 반면에, 우리는 의미적으로 유사한 쿼리 간에 초기 단계 샘플링을 공유함으로써 총 단계 수를 줄입니다. 이러한 효율성 향상을 품질을 희생하지 않고 달성하기 위해, 우리는 효율성을 위한 공유 샘플링 체계와 품질 보존을 위한 맞춤형 훈련 전략을 통합한 의미 인식 공유 샘플링 프레임워크인 SAGE를 제안합니다. 광범위한 실험 결과, SAGE는 샘플링 비용을 25.5% 줄이면서, 기준선 대비 5.0% 낮은 FID, 5.4% 높은 CLIP, 160% 높은 다양성으로 생성 품질을 향상시킵니다.

## 📝 요약

이 논문은 확산 모델의 높은 샘플링 비용 문제를 해결하기 위해 SAGE라는 새로운 프레임워크를 제안합니다. 기존 방법들이 각 쿼리를 독립적으로 처리하는 것과 달리, SAGE는 의미적으로 유사한 쿼리 간에 초기 샘플링을 공유하여 전체 단계 수를 줄입니다. 이를 통해 효율성을 높이면서도 품질을 유지하기 위한 맞춤형 학습 전략을 통합합니다. 실험 결과, SAGE는 샘플링 비용을 25.5% 절감하고, 생성 품질을 개선하여 FID는 5.0% 낮추고, CLIP 점수는 5.4% 높이며, 다양성은 160% 증가시켰습니다.

## 🎯 주요 포인트

- 1. 확산 모델의 높은 샘플링 비용 문제를 해결하기 위해 SAGE라는 프레임워크를 제안합니다.
- 2. SAGE는 의미적으로 유사한 쿼리 간의 초기 샘플링을 공유하여 총 샘플링 단계를 줄입니다.
- 3. SAGE는 효율성을 위한 공유 샘플링 스킴과 품질 유지를 위한 맞춤형 훈련 전략을 통합합니다.
- 4. 실험 결과, SAGE는 샘플링 비용을 25.5% 절감하면서, FID 5.0% 감소, CLIP 5.4% 증가, 다양성 160% 증가를 달성했습니다.


---

*Generated on 2025-09-23 10:37:41*