---
keywords:
  - Bayesian Optimization
  - Multimodal Gene Embeddings
  - Enrichment Analysis
  - Pathway-Level Explanations
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19988
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:59:23.655595",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bayesian Optimization",
    "Multimodal Gene Embeddings",
    "Enrichment Analysis",
    "Pathway-Level Explanations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bayesian Optimization": 0.78,
    "Multimodal Gene Embeddings": 0.74,
    "Enrichment Analysis": 0.75,
    "Pathway-Level Explanations": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian Optimization",
        "canonical": "Bayesian Optimization",
        "aliases": [
          "BO"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian Optimization is a fundamental technique in machine learning and optimization, facilitating connections across various domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multimodal Gene Embeddings",
        "canonical": "Multimodal Gene Embeddings",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept represents a novel approach in integrating multiple data types for gene analysis, enhancing biological data interpretation.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.74
      },
      {
        "surface": "Enrichment Analysis",
        "canonical": "Enrichment Analysis",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Enrichment Analysis is crucial for gene prioritization, linking experimental designs to biological pathways.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
      },
      {
        "surface": "Pathway-Level Explanations",
        "canonical": "Pathway-Level Explanations",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Provides mechanistic insights into gene perturbations, facilitating deeper biological understanding.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.81,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "genomic perturbation",
      "drug discovery",
      "therapeutic target"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian Optimization",
      "resolved_canonical": "Bayesian Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multimodal Gene Embeddings",
      "resolved_canonical": "Multimodal Gene Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Enrichment Analysis",
      "resolved_canonical": "Enrichment Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Pathway-Level Explanations",
      "resolved_canonical": "Pathway-Level Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.81,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# BioBO: Biology-informed Bayesian Optimization for Perturbation Design

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19988.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19988](https://arxiv.org/abs/2509.19988)

## 🔗 유사한 논문
- [[2025-09-23/Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs_20250923|Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs]] (84.9% similar)
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (84.7% similar)
- [[2025-09-23/An AI-powered Bayesian generative modeling approach for causal inference in observational studies_20250923|An AI-powered Bayesian generative modeling approach for causal inference in observational studies]] (82.1% similar)
- [[2025-09-24/Bayesian Calibration and Model Assessment of Cell Migration Dynamics with Surrogate Model Integration_20250924|Bayesian Calibration and Model Assessment of Cell Migration Dynamics with Surrogate Model Integration]] (81.2% similar)
- [[2025-09-23/Enhancing Performance and Calibration in Quantile Hyperparameter Optimization_20250923|Enhancing Performance and Calibration in Quantile Hyperparameter Optimization]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Optimization|Bayesian Optimization]]
**🔗 Specific Connectable**: [[keywords/Enrichment Analysis|Enrichment Analysis]]
**⚡ Unique Technical**: [[keywords/Multimodal Gene Embeddings|Multimodal Gene Embeddings]], [[keywords/Pathway-Level Explanations|Pathway-Level Explanations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19988v1 Announce Type: cross 
Abstract: Efficient design of genomic perturbation experiments is crucial for accelerating drug discovery and therapeutic target identification, yet exhaustive perturbation of the human genome remains infeasible due to the vast search space of potential genetic interactions and experimental constraints. Bayesian optimization (BO) has emerged as a powerful framework for selecting informative interventions, but existing approaches often fail to exploit domain-specific biological prior knowledge. We propose Biology-Informed Bayesian Optimization (BioBO), a method that integrates Bayesian optimization with multimodal gene embeddings and enrichment analysis, a widely used tool for gene prioritization in biology, to enhance surrogate modeling and acquisition strategies. BioBO combines biologically grounded priors with acquisition functions in a principled framework, which biases the search toward promising genes while maintaining the ability to explore uncertain regions. Through experiments on established public benchmarks and datasets, we demonstrate that BioBO improves labeling efficiency by 25-40%, and consistently outperforms conventional BO by identifying top-performing perturbations more effectively. Moreover, by incorporating enrichment analysis, BioBO yields pathway-level explanations for selected perturbations, offering mechanistic interpretability that links designs to biologically coherent regulatory circuits.

## 📝 요약

이 논문은 유전자 변형 실험의 효율적 설계를 위해 제안된 Biology-Informed Bayesian Optimization (BioBO) 방법론을 소개합니다. BioBO는 베이지안 최적화에 생물학적 사전 지식과 다중 모드 유전자 임베딩, 그리고 유전자 우선순위 결정을 위한 풍부한 분석을 통합하여 대리 모델링과 획득 전략을 향상시킵니다. 이 방법은 유망한 유전자를 탐색하면서도 불확실한 영역을 탐색할 수 있도록 설계되었습니다. 실험 결과, BioBO는 라벨링 효율성을 25-40% 향상시키고, 기존의 베이지안 최적화보다 뛰어난 성능을 보였습니다. 또한, 경로 수준의 설명을 제공하여 설계와 생물학적 규제 회로 간의 기계적 해석 가능성을 높였습니다.

## 🎯 주요 포인트

- 1. BioBO는 생물학적 사전 지식을 활용하여 유망한 유전자 탐색을 강화하는 방법입니다.
- 2. BioBO는 다중 모드 유전자 임베딩과 풍부화 분석을 통합하여 대리 모델링과 획득 전략을 개선합니다.
- 3. BioBO는 기존의 베이지안 최적화보다 25-40% 더 높은 라벨링 효율성을 보여줍니다.
- 4. BioBO는 선택된 유전자 변형에 대한 경로 수준의 설명을 제공하여 메커니즘적 해석 가능성을 높입니다.
- 5. BioBO는 공공 벤치마크와 데이터셋 실험에서 일관되게 우수한 성능을 보입니다.


---

*Generated on 2025-09-25 16:59:23*