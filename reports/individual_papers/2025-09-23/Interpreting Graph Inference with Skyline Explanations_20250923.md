---
keywords:
  - Graph Neural Network
  - Skyline Explanation
  - Multi-criteria Optimization
  - Onion-peeling Approach
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2505.07635
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:42:44.073847",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Skyline Explanation",
    "Multi-criteria Optimization",
    "Onion-peeling Approach"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Skyline Explanation": 0.79,
    "Multi-criteria Optimization": 0.72,
    "Onion-peeling Approach": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Neural Nets"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on interpreting inference queries, linking with existing GNN research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Skyline Explanation",
        "canonical": "Skyline Explanation",
        "aliases": [
          "Skyline Explanations"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel paradigm for interpreting GNN outputs, enhancing understanding of inference results.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Multi-criteria Optimization",
        "canonical": "Multi-criteria Optimization",
        "aliases": [
          "Multi-objective Optimization"
        ],
        "category": "broad_technical",
        "rationale": "Key to formulating the skyline explanation problem, relevant in optimization contexts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.68,
        "link_intent_score": 0.72
      },
      {
        "surface": "Onion-peeling Approach",
        "canonical": "Onion-peeling Approach",
        "aliases": [
          "Onion-peeling Method"
        ],
        "category": "unique_technical",
        "rationale": "Describes a novel algorithmic strategy for skyline explanations, potentially linking to algorithm design.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "inference queries",
      "explanatory subgraphs",
      "load-balancing strategies"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Skyline Explanation",
      "resolved_canonical": "Skyline Explanation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Multi-criteria Optimization",
      "resolved_canonical": "Multi-criteria Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.68,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Onion-peeling Approach",
      "resolved_canonical": "Onion-peeling Approach",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Interpreting Graph Inference with Skyline Explanations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.07635.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2505.07635](https://arxiv.org/abs/2505.07635)

## 🔗 유사한 논문
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (83.9% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (79.7% similar)
- [[2025-09-19/Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community: Guiding the Fairness of Graphs via New Links]] (79.2% similar)
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation]] (79.1% similar)
- [[2025-09-23/Building Transparency in Deep Learning-Powered Network Traffic Classification_ A Traffic-Explainer Framework_20250923|Building Transparency in Deep Learning-Powered Network Traffic Classification: A Traffic-Explainer Framework]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-criteria Optimization|Multi-criteria Optimization]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Skyline Explanation|Skyline Explanation]], [[keywords/Onion-peeling Approach|Onion-peeling Approach]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.07635v3 Announce Type: replace 
Abstract: Inference queries have been routinely issued to graph machine learning models such as graph neural networks (GNNs) for various network analytical tasks. Nevertheless, GNN outputs are often hard to interpret comprehensively. Existing methods typically conform to individual pre-defined explainability measures (such as fidelity), which often leads to biased, ``one-side'' interpretations. This paper introduces skyline explanation, a new paradigm that interprets GNN outputs by simultaneously optimizing multiple explainability measures of users' interests. (1) We propose skyline explanations as a Pareto set of explanatory subgraphs that dominate others over multiple explanatory measures. We formulate skyline explanation as a multi-criteria optimization problem, and establish its hardness results. (2) We design efficient algorithms with an onion-peeling approach, which strategically prioritizes nodes and removes unpromising edges to incrementally assemble skyline explanations. (3) We also develop an algorithm to diversify the skyline explanations to enrich the comprehensive interpretation. (4) We introduce efficient parallel algorithms with load-balancing strategies to scale skyline explanation for large-scale GNN-based inference. Using real-world and synthetic graphs, we experimentally verify our algorithms' effectiveness and scalability.

## 📝 요약

이 논문은 그래프 신경망(GNN)의 출력 해석을 위한 새로운 패러다임인 스카이라인 설명을 제안합니다. 스카이라인 설명은 사용자가 관심 있는 여러 설명 가능성 측정 기준을 동시에 최적화하여 GNN의 출력을 해석합니다. 주요 기여는 다음과 같습니다: (1) 여러 설명 기준에서 우수한 설명적 서브그래프의 파레토 집합으로 스카이라인 설명을 정의하고, 이를 다기준 최적화 문제로 공식화했습니다. (2) 노드를 전략적으로 우선시하고 가능성이 낮은 엣지를 제거하는 '양파 껍질 벗기기' 접근법을 사용하여 효율적인 알고리즘을 설계했습니다. (3) 스카이라인 설명을 다양화하여 해석의 포괄성을 강화하는 알고리즘을 개발했습니다. (4) 대규모 GNN 기반 추론을 위한 부하 균형 전략을 갖춘 병렬 알고리즘을 도입했습니다. 실험 결과, 제안된 알고리즘의 효과성과 확장 가능성을 검증했습니다.

## 🎯 주요 포인트

- 1. 그래프 신경망(GNN) 출력의 해석을 위해 여러 설명 가능성 측정을 동시에 최적화하는 새로운 패러다임인 스카이라인 설명을 도입합니다.
- 2. 스카이라인 설명은 여러 설명 가능성 측정에서 다른 설명을 지배하는 설명적 부분 그래프의 파레토 집합으로 정의됩니다.
- 3. 양파 껍질 벗기기 접근법을 사용하여 효율적인 알고리즘을 설계하여 노드를 전략적으로 우선시하고 유망하지 않은 엣지를 제거하여 스카이라인 설명을 점진적으로 구성합니다.
- 4. 스카이라인 설명의 다양성을 높여 포괄적인 해석을 풍부하게 하기 위한 알고리즘을 개발합니다.
- 5. 대규모 GNN 기반 추론을 위한 스카이라인 설명의 확장을 위해 부하 분산 전략을 갖춘 효율적인 병렬 알고리즘을 도입합니다.


---

*Generated on 2025-09-24 02:42:44*