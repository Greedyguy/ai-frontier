---
keywords:
  - Semantic Clustering
  - Multi-Agent System
  - Occupation Taxonomies
  - Labor Market Intelligence
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15786
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:45:25.512322",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Semantic Clustering",
    "Multi-Agent System",
    "Occupation Taxonomies",
    "Labor Market Intelligence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Semantic Clustering": 0.82,
    "Multi-Agent System": 0.79,
    "Occupation Taxonomies": 0.74,
    "Labor Market Intelligence": 0.71
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Semantic Clustering",
        "canonical": "Semantic Clustering",
        "aliases": [
          "Cluster Analysis",
          "Clustering"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic Clustering is crucial for organizing data-driven taxonomies, enhancing connectivity with clustering techniques in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-Agent System",
        "canonical": "Multi-Agent System",
        "aliases": [
          "MAS",
          "Agent-Based System"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-Agent Systems are integral to collaborative frameworks, linking to broader AI and system design concepts.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      },
      {
        "surface": "Occupation Taxonomies",
        "canonical": "Occupation Taxonomies",
        "aliases": [
          "Job Taxonomies",
          "Employment Taxonomies"
        ],
        "category": "unique_technical",
        "rationale": "Occupation Taxonomies are unique to labor market studies, providing a specialized link to employment data analysis.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.81,
        "link_intent_score": 0.74
      },
      {
        "surface": "Labor Market Intelligence",
        "canonical": "Labor Market Intelligence",
        "aliases": [
          "Labor Market Analysis",
          "Employment Intelligence"
        ],
        "category": "unique_technical",
        "rationale": "Labor Market Intelligence is specific to economic and employment research, offering unique insights into market dynamics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.79,
        "link_intent_score": 0.71
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Semantic Clustering",
      "resolved_canonical": "Semantic Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-Agent System",
      "resolved_canonical": "Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Occupation Taxonomies",
      "resolved_canonical": "Occupation Taxonomies",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.81,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Labor Market Intelligence",
      "resolved_canonical": "Labor Market Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.79,
        "link_intent": 0.71
      }
    }
  ]
}
-->

# Building Data-Driven Occupation Taxonomies: A Bottom-Up Multi-Stage Approach via Semantic Clustering and Multi-Agent Collaboration

**Korean Title:** 데이터 기반 직업 분류 체계 구축: 의미론적 클러스터링과 다중 에이전트 협력을 통한 하향식 다단계 접근법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15786.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15786](https://arxiv.org/abs/2509.15786)

## 🔗 유사한 논문
- [[2025-09-18/CrowdAgent_ Multi-Agent Managed Multi-Source Annotation System_20250918|CrowdAgent: Multi-Agent Managed Multi-Source Annotation System]] (78.6% similar)
- [[2025-09-22/LC-SLab -- An Object-based Deep Learning Framework for Large-scale Land Cover Classification from Satellite Imagery and Sparse In-situ Labels_20250922|LC-SLab -- An Object-based Deep Learning Framework for Large-scale Land Cover Classification from Satellite Imagery and Sparse In-situ Labels]] (77.5% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (77.5% similar)
- [[2025-09-22/Enhancing Interpretability in Deep Reinforcement Learning through Semantic Clustering_20250922|Enhancing Interpretability in Deep Reinforcement Learning through Semantic Clustering]] (77.1% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (76.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Clustering|Semantic Clustering]], [[keywords/Multi-Agent System|Multi-Agent System]]
**⚡ Unique Technical**: [[keywords/Occupation Taxonomies|Occupation Taxonomies]], [[keywords/Labor Market Intelligence|Labor Market Intelligence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15786v1 Announce Type: new 
Abstract: Creating robust occupation taxonomies, vital for applications ranging from job recommendation to labor market intelligence, is challenging. Manual curation is slow, while existing automated methods are either not adaptive to dynamic regional markets (top-down) or struggle to build coherent hierarchies from noisy data (bottom-up). We introduce CLIMB (CLusterIng-based Multi-agent taxonomy Builder), a framework that fully automates the creation of high-quality, data-driven taxonomies from raw job postings. CLIMB uses global semantic clustering to distill core occupations, then employs a reflection-based multi-agent system to iteratively build a coherent hierarchy. On three diverse, real-world datasets, we show that CLIMB produces taxonomies that are more coherent and scalable than existing methods and successfully capture unique regional characteristics. We release our code and datasets at https://anonymous.4open.science/r/CLIMB.

## 🔍 Abstract (한글 번역)

arXiv:2509.15786v1 발표 유형: 신규  
초록: 직업 추천에서 노동 시장 정보에 이르기까지 다양한 응용 분야에 필수적인 견고한 직업 분류 체계를 만드는 것은 도전적인 과제입니다. 수동 큐레이션은 느리고, 기존의 자동화된 방법들은 동적인 지역 시장에 적응하지 못하거나(상향식) 잡음이 많은 데이터로부터 일관된 계층 구조를 구축하는 데 어려움을 겪습니다(하향식). 우리는 원시 구인 공고로부터 고품질의 데이터 기반 분류 체계를 완전히 자동화하여 생성하는 프레임워크인 CLIMB(CLusterIng-based Multi-agent taxonomy Builder)를 소개합니다. CLIMB는 글로벌 의미 클러스터링을 사용하여 핵심 직업을 추출한 다음, 반영 기반 다중 에이전트 시스템을 활용하여 일관된 계층 구조를 반복적으로 구축합니다. 세 가지 다양한 실제 데이터셋에서 CLIMB가 기존 방법보다 더 일관되고 확장 가능한 분류 체계를 생성하며, 독특한 지역적 특성을 성공적으로 포착함을 보여줍니다. 우리는 우리의 코드와 데이터셋을 https://anonymous.4open.science/r/CLIMB에서 공개합니다.

## 📝 요약

이 논문은 직업 추천 및 노동 시장 분석에 중요한 직업 분류 체계를 자동화하는 CLIMB라는 프레임워크를 제안합니다. 기존 방법론의 한계를 극복하기 위해, CLIMB는 전 세계의 의미론적 클러스터링을 통해 핵심 직업을 추출하고, 반영 기반의 다중 에이전트 시스템을 사용하여 일관된 계층 구조를 구축합니다. 세 가지 실제 데이터셋에서 CLIMB는 기존 방법보다 더 일관되고 확장 가능한 분류 체계를 생성하며, 지역적 특성을 잘 반영하는 것을 입증했습니다. 코드와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. CLIMB는 원시 구인 공고로부터 고품질의 데이터 기반 직업 분류 체계를 자동으로 생성하는 프레임워크입니다.
- 2. 글로벌 의미 클러스터링을 사용하여 핵심 직업을 도출하고, 반영 기반의 다중 에이전트 시스템을 통해 일관된 계층 구조를 구축합니다.
- 3. 세 가지 다양한 실제 데이터셋에서 CLIMB는 기존 방법보다 더 일관되고 확장 가능한 분류 체계를 생성하며, 지역적 특성을 성공적으로 포착합니다.
- 4. CLIMB의 코드와 데이터셋은 공개되어 있어 연구 및 응용에 활용할 수 있습니다.


---

*Generated on 2025-09-23 08:45:25*