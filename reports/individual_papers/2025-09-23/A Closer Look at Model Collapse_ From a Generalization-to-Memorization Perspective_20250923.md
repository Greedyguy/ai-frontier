---
keywords:
  - Diffusion Models
  - Model Collapse
  - Entropy-Based Data Selection
  - Generalization to Memorization Transition
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16499
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:37:45.877176",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Model Collapse",
    "Entropy-Based Data Selection",
    "Generalization to Memorization Transition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Model Collapse": 0.78,
    "Entropy-Based Data Selection": 0.77,
    "Generalization to Memorization Transition": 0.75
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
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the discussion of model collapse and are increasingly relevant in AI-generated data contexts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "model collapse",
        "canonical": "Model Collapse",
        "aliases": [
          "collapse in models"
        ],
        "category": "unique_technical",
        "rationale": "Model collapse is a unique phenomenon discussed in the paper, crucial for understanding performance degradation in recursive training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "entropy-based data selection",
        "canonical": "Entropy-Based Data Selection",
        "aliases": [
          "entropy data selection"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel strategy proposed to mitigate model collapse, providing a specific technique for improving model performance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "generalization to memorization",
        "canonical": "Generalization to Memorization Transition",
        "aliases": [
          "memorization transition"
        ],
        "category": "unique_technical",
        "rationale": "The transition from generalization to memorization is a key aspect of model collapse, offering insights into model behavior changes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance degradation",
      "synthetic data",
      "training cycle"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "model collapse",
      "resolved_canonical": "Model Collapse",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "entropy-based data selection",
      "resolved_canonical": "Entropy-Based Data Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "generalization to memorization",
      "resolved_canonical": "Generalization to Memorization Transition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16499.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16499](https://arxiv.org/abs/2509.16499)

## 🔗 유사한 논문
- [[2025-09-19/Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (83.6% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (83.6% similar)
- [[2025-09-22/Navigate Beyond Shortcuts_ Debiased Learning through the Lens of Neural Collapse_20250922|Navigate Beyond Shortcuts: Debiased Learning through the Lens of Neural Collapse]] (83.0% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (82.7% similar)
- [[2025-09-22/Autoguided Online Data Curation for Diffusion Model Training_20250922|Autoguided Online Data Curation for Diffusion Model Training]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]]
**⚡ Unique Technical**: [[keywords/Model Collapse|Model Collapse]], [[keywords/Entropy-Based Data Selection|Entropy-Based Data Selection]], [[keywords/Generalization to Memorization Transition|Generalization to Memorization Transition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16499v1 Announce Type: new 
Abstract: The widespread use of diffusion models has led to an abundance of AI-generated data, raising concerns about model collapse -- a phenomenon in which recursive iterations of training on synthetic data lead to performance degradation. Prior work primarily characterizes this collapse via variance shrinkage or distribution shift, but these perspectives miss practical manifestations of model collapse. This paper identifies a transition from generalization to memorization during model collapse in diffusion models, where models increasingly replicate training data instead of generating novel content during iterative training on synthetic samples. This transition is directly driven by the declining entropy of the synthetic training data produced in each training cycle, which serves as a clear indicator of model degradation. Motivated by this insight, we propose an entropy-based data selection strategy to mitigate the transition from generalization to memorization and alleviate model collapse. Empirical results show that our approach significantly enhances visual quality and diversity in recursive generation, effectively preventing collapse.

## 📝 요약

이 논문은 확산 모델의 반복적인 훈련 과정에서 발생하는 모델 붕괴 현상을 다룹니다. 기존 연구는 주로 분산 감소나 분포 변화로 모델 붕괴를 설명하지만, 이 논문은 일반화에서 암기로의 전환을 모델 붕괴의 핵심으로 지적합니다. 이는 반복적인 합성 데이터 훈련에서 모델이 새로운 콘텐츠를 생성하기보다 기존 데이터를 반복하는 현상으로, 합성 데이터의 엔트로피 감소가 원인입니다. 이를 해결하기 위해 엔트로피 기반 데이터 선택 전략을 제안하며, 실험 결과 이 방법이 시각적 품질과 다양성을 향상시켜 모델 붕괴를 효과적으로 방지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 확산 모델의 반복적인 합성 데이터 학습은 모델 붕괴를 초래하며, 이는 일반화에서 암기로의 전환을 포함합니다.
- 2. 모델 붕괴는 합성 데이터의 엔트로피 감소에 의해 직접적으로 유발되며, 이는 모델 성능 저하의 명확한 지표로 작용합니다.
- 3. 엔트로피 기반 데이터 선택 전략을 통해 일반화에서 암기로의 전환을 완화하고 모델 붕괴를 방지할 수 있습니다.
- 4. 제안된 접근법은 반복 생성 과정에서 시각적 품질과 다양성을 크게 향상시켜 모델 붕괴를 효과적으로 방지합니다.


---

*Generated on 2025-09-24 01:37:45*