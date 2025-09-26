---
keywords:
  - Autoguidance
  - Diffusion Models
  - Data Curation
  - Joint Example Selection Technique
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15267
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:51:12.658061",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Autoguidance",
    "Diffusion Models",
    "Data Curation",
    "Joint Example Selection Technique"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Autoguidance": 0.78,
    "Diffusion Models": 0.82,
    "Data Curation": 0.75,
    "Joint Example Selection Technique": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "autoguidance",
        "canonical": "Autoguidance",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Autoguidance is a novel method highlighted for improving sample quality and diversity in diffusion model training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "generative diffusion models"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are a specific type of generative model, relevant to discussions on generative AI and model efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "data curation",
        "canonical": "Data Curation",
        "aliases": [
          "online data selection"
        ],
        "category": "broad_technical",
        "rationale": "Data curation is a critical process in optimizing model training efficiency, linking to broader discussions on data management.",
        "novelty_score": 0.45,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "JEST",
        "canonical": "Joint Example Selection Technique",
        "aliases": [
          "JEST"
        ],
        "category": "unique_technical",
        "rationale": "JEST is a specific technique integrated into the study's framework, relevant for discussions on data selection methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "autoguidance",
      "resolved_canonical": "Autoguidance",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "data curation",
      "resolved_canonical": "Data Curation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "JEST",
      "resolved_canonical": "Joint Example Selection Technique",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Autoguided Online Data Curation for Diffusion Model Training

**Korean Title:** 자동 안내 온라인 데이터 큐레이션을 통한 확산 모델 훈련

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15267.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15267](https://arxiv.org/abs/2509.15267)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (82.2% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (80.4% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (80.3% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (79.9% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Data Curation|Data Curation]]
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]]
**⚡ Unique Technical**: [[keywords/Autoguidance|Autoguidance]], [[keywords/Joint Example Selection Technique|Joint Example Selection Technique]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15267v1 Announce Type: cross 
Abstract: The costs of generative model compute rekindled promises and hopes for efficient data curation. In this work, we investigate whether recently developed autoguidance and online data selection methods can improve the time and sample efficiency of training generative diffusion models. We integrate joint example selection (JEST) and autoguidance into a unified code base for fast ablation and benchmarking. We evaluate combinations of data curation on a controlled 2-D synthetic data generation task as well as (3x64x64)-D image generation. Our comparisons are made at equal wall-clock time and equal number of samples, explicitly accounting for the overhead of selection. Across experiments, autoguidance consistently improves sample quality and diversity. Early AJEST (applying selection only at the beginning of training) can match or modestly exceed autoguidance alone in data efficiency on both tasks. However, its time overhead and added complexity make autoguidance or uniform random data selection preferable in most situations. These findings suggest that while targeted online selection can yield efficiency gains in early training, robust sample quality improvements are primarily driven by autoguidance. We discuss limitations and scope, and outline when data selection may be beneficial.

## 🔍 Abstract (한글 번역)

arXiv:2509.15267v1 발표 유형: 교차  
초록: 생성 모델 계산의 비용은 효율적인 데이터 큐레이션에 대한 약속과 희망을 다시 불러일으켰습니다. 본 연구에서는 최근 개발된 자동 유도 및 온라인 데이터 선택 방법이 생성 확산 모델의 학습 시간과 샘플 효율성을 향상시킬 수 있는지 조사합니다. 우리는 빠른 소거 및 벤치마킹을 위해 공동 예제 선택(JEST)과 자동 유도를 통합하여 통합된 코드 베이스를 구축했습니다. 우리는 제어된 2차원 합성 데이터 생성 작업과 (3x64x64)-D 이미지 생성에서 데이터 큐레이션의 조합을 평가합니다. 우리의 비교는 선택의 오버헤드를 명시적으로 고려하여 동일한 월드 클록 시간과 동일한 샘플 수에서 이루어집니다. 실험 전반에 걸쳐 자동 유도는 샘플 품질과 다양성을 일관되게 향상시킵니다. 초기 AJEST(훈련 시작 시에만 선택 적용)는 두 작업 모두에서 데이터 효율성 면에서 자동 유도 단독과 맞먹거나 약간 초과할 수 있습니다. 그러나 시간 오버헤드와 추가 복잡성으로 인해 대부분의 상황에서는 자동 유도 또는 균일한 무작위 데이터 선택이 더 바람직합니다. 이러한 결과는 초기 훈련에서 목표 지향적 온라인 선택이 효율성을 높일 수 있지만, 견고한 샘플 품질 개선은 주로 자동 유도에 의해 주도된다는 것을 시사합니다. 우리는 제한 사항과 범위를 논의하고 데이터 선택이 유익할 수 있는 시기를 설명합니다.

## 📝 요약

이 연구는 생성 모델의 계산 비용을 줄이기 위한 데이터 큐레이션 방법의 효율성을 조사합니다. 최근 개발된 자동 안내 및 온라인 데이터 선택 방법이 생성 확산 모델의 학습 효율성을 향상시킬 수 있는지를 평가했습니다. JEST와 자동 안내를 통합하여 빠른 실험과 벤치마킹을 수행했으며, 2차원 합성 데이터 생성 및 (3x64x64)-차원 이미지 생성 작업에서 데이터 큐레이션의 조합을 평가했습니다. 실험 결과, 자동 안내는 샘플의 품질과 다양성을 일관되게 향상시켰으며, 초기 AJEST는 데이터 효율성에서 자동 안내와 비슷하거나 약간 더 나은 성능을 보였으나, 시간적 오버헤드와 복잡성으로 인해 대부분의 상황에서는 자동 안내나 무작위 데이터 선택이 더 선호되었습니다. 연구는 초기 훈련에서의 온라인 선택이 효율성을 높일 수 있지만, 견고한 샘플 품질 개선은 주로 자동 안내에 의해 이루어진다는 것을 시사합니다. 데이터 선택의 한계와 유용한 상황을 논의합니다.

## 🎯 주요 포인트

- 1. 생성 모델의 컴퓨팅 비용 문제를 해결하기 위해 데이터 큐레이션의 효율성을 조사했습니다.
- 2. JEST와 오토가이던스를 통합하여 빠른 실험과 벤치마킹을 위한 코드 베이스를 구축했습니다.
- 3. 오토가이던스는 샘플의 품질과 다양성을 일관되게 향상시켰습니다.
- 4. 초기 AJEST는 데이터 효율성에서 오토가이던스와 비슷하거나 약간 더 나은 성능을 보였지만, 시간 소요와 복잡성 때문에 오토가이던스가 더 선호됩니다.
- 5. 데이터 선택은 초기 훈련 단계에서 효율성을 높일 수 있지만, 샘플 품질 개선은 주로 오토가이던스에 의해 이루어집니다.


---

*Generated on 2025-09-23 08:51:12*