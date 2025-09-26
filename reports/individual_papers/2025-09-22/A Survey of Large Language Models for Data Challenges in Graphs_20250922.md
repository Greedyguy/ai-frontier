---
keywords:
  - Large Language Model
  - Graph Neural Network
  - Cross-domain Heterogeneity
  - Dynamic Instability
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2505.18475
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:58:46.607131",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Graph Neural Network",
    "Cross-domain Heterogeneity",
    "Dynamic Instability"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Graph Neural Network": 0.78,
    "Cross-domain Heterogeneity": 0.65,
    "Dynamic Instability": 0.62
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on addressing graph data challenges.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Learning",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph Learning",
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Learning is closely related to Graph Neural Networks, which are pivotal in the context of the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cross-domain Heterogeneity",
        "canonical": "Cross-domain Heterogeneity",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This term captures a specific challenge in graph data that is addressed in the paper.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      },
      {
        "surface": "Dynamic Instability",
        "canonical": "Dynamic Instability",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Dynamic Instability is a unique challenge in graph data evolution discussed in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.8,
        "link_intent_score": 0.62
      }
    ],
    "ban_list_suggestions": [
      "Incompleteness",
      "Imbalance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Learning",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cross-domain Heterogeneity",
      "resolved_canonical": "Cross-domain Heterogeneity",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Dynamic Instability",
      "resolved_canonical": "Dynamic Instability",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.8,
        "link_intent": 0.62
      }
    }
  ]
}
-->

# A Survey of Large Language Models for Data Challenges in Graphs

**Korean Title:** 그래프에서 데이터 문제를 위한 대형 언어 모델에 대한 조사

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18475.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2505.18475](https://arxiv.org/abs/2505.18475)

## 🔗 유사한 논문
- [[2025-09-22/Modeling Transformers as complex networks to analyze learning dynamics_20250922|Modeling Transformers as complex networks to analyze learning dynamics]] (84.6% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (84.5% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (84.4% similar)
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (84.3% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Cross-domain Heterogeneity|Cross-domain Heterogeneity]], [[keywords/Dynamic Instability|Dynamic Instability]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18475v2 Announce Type: replace-cross 
Abstract: Graphs are a widely used paradigm for representing non-Euclidean data, with applications ranging from social network analysis to biomolecular prediction. While graph learning has achieved remarkable progress, real-world graph data presents a number of challenges that significantly hinder the learning process. In this survey, we focus on four fundamental data-centric challenges: (1) Incompleteness, real-world graphs have missing nodes, edges, or attributes; (2) Imbalance, the distribution of the labels of nodes or edges and their structures for real-world graphs are highly skewed; (3) Cross-domain Heterogeneity, graphs from different domains exhibit incompatible feature spaces or structural patterns; and (4) Dynamic Instability, graphs evolve over time in unpredictable ways. Recently, Large Language Models (LLMs) offer the potential to tackle these challenges by leveraging rich semantic reasoning and external knowledge. This survey focuses on how LLMs can address four fundamental data-centric challenges in graph-structured data, thereby improving the effectiveness of graph learning. For each challenge, we review both traditional solutions and modern LLM-driven approaches, highlighting how LLMs contribute unique advantages. Finally, we discuss open research questions and promising future directions in this emerging interdisciplinary field. To support further exploration, we have curated a repository of recent advances on graph learning challenges: https://github.com/limengran98/Awesome-Literature-Graph-Learning-Challenges.

## 🔍 Abstract (한글 번역)

arXiv:2505.18475v2 발표 유형: 교차 교체  
초록: 그래프는 비유클리드 데이터를 표현하기 위한 널리 사용되는 패러다임으로, 소셜 네트워크 분석에서부터 생체분자 예측에 이르기까지 다양한 응용 분야에 활용됩니다. 그래프 학습은 주목할 만한 발전을 이루었지만, 실제 세계의 그래프 데이터는 학습 과정을 크게 방해하는 여러 도전 과제를 제시합니다. 이 조사에서는 네 가지 기본적인 데이터 중심의 도전 과제에 초점을 맞춥니다: (1) 불완전성, 실제 세계의 그래프에는 누락된 노드, 엣지 또는 속성이 존재합니다; (2) 불균형, 실제 세계 그래프의 노드 또는 엣지의 레이블 분포와 그 구조가 매우 편향되어 있습니다; (3) 도메인 간 이질성, 서로 다른 도메인에서의 그래프는 호환되지 않는 특징 공간이나 구조적 패턴을 나타냅니다; (4) 동적 불안정성, 그래프는 예측할 수 없는 방식으로 시간이 지남에 따라 진화합니다. 최근 대형 언어 모델(LLM)은 풍부한 의미론적 추론과 외부 지식을 활용하여 이러한 도전 과제를 해결할 가능성을 제공합니다. 이 조사는 LLM이 그래프 구조 데이터에서 네 가지 기본적인 데이터 중심의 도전 과제를 어떻게 해결할 수 있는지에 중점을 두어 그래프 학습의 효과를 향상시키는 방법을 탐구합니다. 각 도전 과제에 대해 전통적인 해결책과 현대적인 LLM 기반 접근 방식을 검토하며, LLM이 제공하는 독특한 이점을 강조합니다. 마지막으로, 이 새로운 학제 간 분야에서의 미해결 연구 질문과 유망한 미래 방향을 논의합니다. 추가 탐색을 지원하기 위해, 우리는 그래프 학습 도전 과제에 대한 최근 발전을 모아놓은 저장소를 큐레이션했습니다: https://github.com/limengran98/Awesome-Literature-Graph-Learning-Challenges.

## 📝 요약

이 논문은 그래프 학습의 주요 데이터 중심 문제를 다루며, 특히 대형 언어 모델(LLM)이 이러한 문제를 해결하는 방법을 탐구합니다. 주요 기여는 그래프 데이터의 불완전성, 불균형, 도메인 간 이질성, 동적 불안정성이라는 네 가지 문제를 식별하고, LLM이 제공하는 의미적 추론과 외부 지식을 활용하여 이를 해결하는 방안을 제시하는 것입니다. 전통적인 해결책과 LLM 기반 접근법을 비교하며, LLM의 독특한 장점을 강조합니다. 또한, 이 분야의 개방형 연구 질문과 미래 연구 방향을 논의하고, 관련 연구 자료를 제공하여 추가 탐구를 지원합니다.

## 🎯 주요 포인트

- 1. 그래프는 비유클리드 데이터를 표현하는 데 널리 사용되며, 사회 네트워크 분석부터 생체 분자 예측까지 다양한 분야에 응용된다.
- 2. 실제 그래프 데이터는 불완전성, 불균형, 도메인 간 이질성, 동적 불안정성 같은 여러 도전 과제를 안고 있다.
- 3. 대형 언어 모델(LLMs)은 풍부한 의미론적 추론과 외부 지식을 활용하여 그래프 학습의 주요 도전 과제를 해결할 잠재력을 제공한다.
- 4. 이 설문 조사에서는 LLMs가 그래프 구조 데이터의 네 가지 주요 도전 과제를 해결하는 방법에 중점을 두고, 전통적인 솔루션과 현대적인 LLM 기반 접근 방식을 검토한다.
- 5. 그래프 학습 도전 과제에 대한 최근 발전을 지원하기 위해 관련 자료를 모아 저장소를 구축하였다.


---

*Generated on 2025-09-23 09:58:46*