<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:39:50.835527",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Graph Inference",
    "Code Generation",
    "Heterophilic Graphs",
    "Node Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Graph Inference": 0.82,
    "Code Generation": 0.79,
    "Heterophilic Graphs": 0.77,
    "Node Classification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to broader discussions on LLM capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Inference",
        "canonical": "Graph Inference",
        "aliases": [
          "Graph Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Focus of the study, exploring LLM applications in graph-based tasks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Code Generation",
        "canonical": "Code Generation",
        "aliases": [
          "LLM Code Generation"
        ],
        "category": "specific_connectable",
        "rationale": "Identified as a key method for enhancing LLM performance on graph data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Heterophilic Graphs",
        "canonical": "Heterophilic Graphs",
        "aliases": [
          "Low Homophily Graphs"
        ],
        "category": "specific_connectable",
        "rationale": "Challenges assumptions about LLM performance, relevant for graph studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Node Classification",
        "canonical": "Node Classification",
        "aliases": [
          "Graph Node Classification"
        ],
        "category": "specific_connectable",
        "rationale": "A primary application area for LLMs in graph machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Inference",
      "resolved_canonical": "Graph Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Code Generation",
      "resolved_canonical": "Code Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Heterophilic Graphs",
      "resolved_canonical": "Heterophilic Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Node Classification",
      "resolved_canonical": "Node Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Actions Speak Louder than Prompts: A Large-Scale Study of LLMs for Graph Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18487.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18487](https://arxiv.org/abs/2509.18487)

## 🔗 유사한 논문
- [[2025-09-22/A Survey of Large Language Models for Data Challenges in Graphs_20250922|A Survey of Large Language Models for Data Challenges in Graphs]] (89.3% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (88.7% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (86.7% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (86.7% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (86.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Code Generation|Code Generation]], [[keywords/Heterophilic Graphs|Heterophilic Graphs]], [[keywords/Node Classification|Node Classification]]
**⚡ Unique Technical**: [[keywords/Graph Inference|Graph Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18487v1 Announce Type: new 
Abstract: Large language models (LLMs) are increasingly used for text-rich graph machine learning tasks such as node classification in high-impact domains like fraud detection and recommendation systems. Yet, despite a surge of interest, the field lacks a principled understanding of the capabilities of LLMs in their interaction with graph data. In this work, we conduct a large-scale, controlled evaluation across several key axes of variability to systematically assess the strengths and weaknesses of LLM-based graph reasoning methods in text-based applications. The axes include the LLM-graph interaction mode, comparing prompting, tool-use, and code generation; dataset domains, spanning citation, web-link, e-commerce, and social networks; structural regimes contrasting homophilic and heterophilic graphs; feature characteristics involving both short- and long-text node attributes; and model configurations with varying LLM sizes and reasoning capabilities. We further analyze dependencies by methodically truncating features, deleting edges, and removing labels to quantify reliance on input types. Our findings provide practical and actionable guidance. (1) LLMs as code generators achieve the strongest overall performance on graph data, with especially large gains on long-text or high-degree graphs where prompting quickly exceeds the token budget. (2) All interaction strategies remain effective on heterophilic graphs, challenging the assumption that LLM-based methods collapse under low homophily. (3) Code generation is able to flexibly adapt its reliance between structure, features, or labels to leverage the most informative input type. Together, these findings provide a comprehensive view of the strengths and limitations of current LLM-graph interaction modes and highlight key design principles for future approaches.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 그래프 데이터와 상호작용하는 방식에 대한 체계적인 평가를 통해 LLM 기반 그래프 추론 방법의 강점과 약점을 분석합니다. 주요 기여는 LLM-그래프 상호작용 모드(프롬프트, 도구 사용, 코드 생성), 데이터셋 도메인(인용, 웹 링크, 전자상거래, 소셜 네트워크), 구조적 특성(동질적 및 이질적 그래프), 특징(짧은 및 긴 텍스트 노드 속성), 모델 구성(다양한 LLM 크기 및 추론 능력)을 포함한 여러 변수를 고려한 평가입니다. 연구 결과, 코드 생성 방식이 긴 텍스트 또는 높은 차수의 그래프에서 가장 우수한 성능을 보였으며, 이질적 그래프에서도 모든 상호작용 전략이 효과적임을 확인했습니다. 또한, 코드 생성은 구조, 특징, 레이블 간의 의존성을 유연하게 조정하여 가장 유익한 입력 유형을 활용할 수 있습니다. 이러한 결과는 LLM-그래프 상호작용 모드의 강점과 한계를 종합적으로 보여주며, 향후 접근 방식에 대한 설계 원칙을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 코드 생성 방식에서 그래프 데이터에 대해 가장 강력한 성능을 발휘하며, 특히 긴 텍스트나 높은 차수의 그래프에서 큰 이점을 보인다.
- 2. 모든 상호작용 전략은 이질적인 그래프에서도 효과적이며, LLM 기반 방법이 낮은 동질성에서 무너질 것이라는 가정을 도전한다.
- 3. 코드 생성은 구조, 특징, 또는 레이블 간의 의존성을 유연하게 조정하여 가장 정보가 많은 입력 유형을 활용할 수 있다.
- 4. LLM과 그래프 데이터의 상호작용 모드에 대한 체계적인 평가를 통해 LLM 기반 그래프 추론 방법의 강점과 약점을 분석하였다.
- 5. 연구 결과는 실용적이고 실행 가능한 지침을 제공하며, 향후 접근 방식에 대한 주요 설계 원칙을 강조한다.


---

*Generated on 2025-09-24 15:39:50*