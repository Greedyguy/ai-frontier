---
keywords:
  - Vision-Language Model
  - Magic Evaluation Framework
  - Magic-Bench-377
  - Multivariate Logistic Regression
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17907
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:03:53.934766",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Magic Evaluation Framework",
    "Magic-Bench-377",
    "Multivariate Logistic Regression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Magic Evaluation Framework": 0.72,
    "Magic-Bench-377": 0.7,
    "Multivariate Logistic Regression": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Text-to-Image",
        "canonical": "Vision-Language Model",
        "aliases": [
          "T2I",
          "Text-to-Image Generation"
        ],
        "category": "evolved_concepts",
        "rationale": "Links advancements in multimodal AI, connecting text and image processing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Magic Evaluation Framework",
        "canonical": "Magic Evaluation Framework",
        "aliases": [
          "MEF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework specifically for evaluating T2I models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Magic-Bench-377",
        "canonical": "Magic-Bench-377",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a new benchmark dataset for evaluating T2I models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multivariate Logistic Regression",
        "canonical": "Multivariate Logistic Regression",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Commonly used statistical method for analysis, linking statistical evaluation techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "framework",
      "model",
      "benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Text-to-Image",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Magic Evaluation Framework",
      "resolved_canonical": "Magic Evaluation Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Magic-Bench-377",
      "resolved_canonical": "Magic-Bench-377",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multivariate Logistic Regression",
      "resolved_canonical": "Multivariate Logistic Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# MEF: A Systematic Evaluation Framework for Text-to-Image Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17907.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17907](https://arxiv.org/abs/2509.17907)

## 🔗 유사한 논문
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (84.8% similar)
- [[2025-09-22/BBScoreV2_ Learning Time-Evolution and Latent Alignment from Stochastic Representation_20250922|BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation]] (82.2% similar)
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (81.9% similar)
- [[2025-09-22/CIDER_ A Causal Cure for Brand-Obsessed Text-to-Image Models_20250922|CIDER: A Causal Cure for Brand-Obsessed Text-to-Image Models]] (81.4% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multivariate Logistic Regression|Multivariate Logistic Regression]]
**⚡ Unique Technical**: [[keywords/Magic Evaluation Framework|Magic Evaluation Framework]], [[keywords/Magic-Bench-377|Magic-Bench-377]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17907v1 Announce Type: new 
Abstract: Rapid advances in text-to-image (T2I) generation have raised higher requirements for evaluation methodologies. Existing benchmarks center on objective capabilities and dimensions, but lack an application-scenario perspective, limiting external validity. Moreover, current evaluations typically rely on either ELO for overall ranking or MOS for dimension-specific scoring, yet both methods have inherent shortcomings and limited interpretability. Therefore, we introduce the Magic Evaluation Framework (MEF), a systematic and practical approach for evaluating T2I models. First, we propose a structured taxonomy encompassing user scenarios, elements, element compositions, and text expression forms to construct the Magic-Bench-377, which supports label-level assessment and ensures a balanced coverage of both user scenarios and capabilities. On this basis, we combine ELO and dimension-specific MOS to generate model rankings and fine-grained assessments respectively. This joint evaluation method further enables us to quantitatively analyze the contribution of each dimension to user satisfaction using multivariate logistic regression. By applying MEF to current T2I models, we obtain a leaderboard and key characteristics of the leading models. We release our evaluation framework and make Magic-Bench-377 fully open-source to advance research in the evaluation of visual generative models.

## 📝 요약

이 논문은 텍스트-이미지(T2I) 생성 모델의 평가를 위한 새로운 방법론인 Magic Evaluation Framework (MEF)를 제안합니다. 기존 평가 방식의 한계를 극복하기 위해 사용자 시나리오, 요소, 요소 구성, 텍스트 표현 형태를 포함한 구조적 분류 체계를 통해 Magic-Bench-377을 구축하였습니다. 이를 통해 사용자 시나리오와 모델의 능력을 균형 있게 평가할 수 있습니다. 또한, ELO와 차원별 MOS를 결합하여 모델 순위와 세부 평가를 수행하고, 다변량 로지스틱 회귀를 통해 사용자 만족도에 기여하는 각 차원의 영향을 분석합니다. MEF를 활용하여 현재 T2I 모델을 평가하고, 주요 모델의 특성을 분석하여 공개합니다. Magic-Bench-377은 오픈 소스로 제공되어 시각적 생성 모델 평가 연구를 촉진합니다.

## 🎯 주요 포인트

- 1. 텍스트-이미지 생성(T2I) 모델 평가를 위한 Magic Evaluation Framework(MEF)를 제안합니다.
- 2. MEF는 사용자 시나리오, 요소, 요소 구성 및 텍스트 표현 형태를 포함하는 구조적 분류 체계를 제공합니다.
- 3. ELO와 차원별 MOS를 결합하여 모델 순위와 세부 평가를 생성하는 평가 방법을 도입합니다.
- 4. 다변량 로지스틱 회귀를 사용하여 사용자 만족도에 대한 각 차원의 기여도를 정량적으로 분석합니다.
- 5. 평가 프레임워크와 Magic-Bench-377을 오픈 소스로 공개하여 시각적 생성 모델 평가 연구를 촉진합니다.


---

*Generated on 2025-09-23 23:03:53*