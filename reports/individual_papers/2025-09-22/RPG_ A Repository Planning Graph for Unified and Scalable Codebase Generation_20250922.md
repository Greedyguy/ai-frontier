---
keywords:
  - Large Language Model
  - Repository Planning Graph
  - Graph-Driven Framework
  - ZeroRepo
  - RepoCraft
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16198
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:32:06.724970",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Repository Planning Graph",
    "Graph-Driven Framework",
    "ZeroRepo",
    "RepoCraft"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Repository Planning Graph": 0.92,
    "Graph-Driven Framework": 0.82,
    "ZeroRepo": 0.88,
    "RepoCraft": 0.8
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
        "rationale": "Large Language Models are central to the paper's approach to code generation, linking it to broader AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Repository Planning Graph",
        "canonical": "Repository Planning Graph",
        "aliases": [
          "RPG"
        ],
        "category": "unique_technical",
        "rationale": "The Repository Planning Graph is a novel concept introduced in the paper, crucial for understanding the proposed methodology.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.92
      },
      {
        "surface": "Graph-Driven Framework",
        "canonical": "Graph-Driven Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This framework is a key component of the paper's methodology, linking graph theory with software engineering.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "ZeroRepo",
        "canonical": "ZeroRepo",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ZeroRepo is the specific implementation of the proposed framework, essential for understanding the practical application.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "RepoCraft",
        "canonical": "RepoCraft",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "RepoCraft serves as the benchmark for evaluating the proposed approach, linking the paper to empirical validation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "function",
      "file-level",
      "natural language"
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
      "candidate_surface": "Repository Planning Graph",
      "resolved_canonical": "Repository Planning Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Graph-Driven Framework",
      "resolved_canonical": "Graph-Driven Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "ZeroRepo",
      "resolved_canonical": "ZeroRepo",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "RepoCraft",
      "resolved_canonical": "RepoCraft",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation

**Korean Title:** RPG: 통합적이고 확장 가능한 코드베이스 생성을 위한 저장소 계획 그래프

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16198.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16198](https://arxiv.org/abs/2509.16198)

## 🔗 유사한 논문
- [[2025-09-22/CodeRAG_ Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion_20250922|CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion]] (84.1% similar)
- [[2025-09-18/KGCompass_ Knowledge Graph Enhanced Repository-Level Software Repair_20250918|KGCompass: Knowledge Graph Enhanced Repository-Level Software Repair]] (80.4% similar)
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions?_20250919|SWE-QA: Can Language Models Answer Repository-level Code Questions?]] (79.4% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (79.1% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Repository Planning Graph|Repository Planning Graph]], [[keywords/Graph-Driven Framework|Graph-Driven Framework]], [[keywords/ZeroRepo|ZeroRepo]], [[keywords/RepoCraft|RepoCraft]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16198v1 Announce Type: cross 
Abstract: Large language models excel at function- and file-level code generation, yet generating complete repositories from scratch remains a fundamental challenge. This process demands coherent and reliable planning across proposal- and implementation-level stages, while natural language, due to its ambiguity and verbosity, is ill-suited for faithfully representing complex software structures. To address this, we introduce the Repository Planning Graph (RPG), a persistent representation that unifies proposal- and implementation-level planning by encoding capabilities, file structures, data flows, and functions in one graph. RPG replaces ambiguous natural language with an explicit blueprint, enabling long-horizon planning and scalable repository generation. Building on RPG, we develop ZeroRepo, a graph-driven framework for repository generation from scratch. It operates in three stages: proposal-level planning and implementation-level refinement to construct the graph, followed by graph-guided code generation with test validation. To evaluate this setting, we construct RepoCraft, a benchmark of six real-world projects with 1,052 tasks. On RepoCraft, ZeroRepo produces repositories averaging nearly 36K LOC, roughly 3.9$\times$ the strongest baseline (Claude Code) and about 64$\times$ other baselines. It attains 81.5% functional coverage and a 69.7% pass rate, exceeding Claude Code by 27.3 and 35.8 percentage points, respectively. Further analysis shows that RPG models complex dependencies, enables progressively more sophisticated planning through near-linear scaling, and enhances LLM understanding of repositories, thereby accelerating agent localization.

## 🔍 Abstract (한글 번역)

arXiv:2509.16198v1 발표 유형: 교차  
초록: 대형 언어 모델은 함수 및 파일 수준의 코드 생성에서 뛰어난 성능을 보이지만, 처음부터 완전한 저장소를 생성하는 것은 여전히 근본적인 도전 과제입니다. 이 과정은 제안 및 구현 수준의 단계에서 일관되고 신뢰할 수 있는 계획을 요구하며, 자연어는 그 모호함과 장황함 때문에 복잡한 소프트웨어 구조를 충실히 표현하기에 적합하지 않습니다. 이를 해결하기 위해, 우리는 제안 및 구현 수준의 계획을 통합하여 기능, 파일 구조, 데이터 흐름 및 기능을 하나의 그래프로 인코딩하는 지속적인 표현인 저장소 계획 그래프(RPG)를 소개합니다. RPG는 모호한 자연어를 명확한 청사진으로 대체하여 장기 계획과 확장 가능한 저장소 생성을 가능하게 합니다. RPG를 기반으로 우리는 처음부터 저장소 생성을 위한 그래프 기반 프레임워크인 ZeroRepo를 개발합니다. 이는 그래프를 구성하기 위한 제안 수준의 계획 및 구현 수준의 정제, 그리고 테스트 검증을 통한 그래프 안내 코드 생성의 세 단계로 작동합니다. 이 설정을 평가하기 위해, 우리는 1,052개의 작업을 포함한 6개의 실제 프로젝트로 구성된 RepoCraft라는 벤치마크를 구축합니다. RepoCraft에서 ZeroRepo는 평균 약 36K LOC의 저장소를 생성하며, 이는 가장 강력한 기준선(Claude Code)의 약 3.9배, 다른 기준선의 약 64배에 해당합니다. 이는 기능적 커버리지 81.5%와 통과율 69.7%를 달성하여 각각 Claude Code를 27.3 및 35.8 퍼센트 포인트 초과합니다. 추가 분석을 통해 RPG는 복잡한 종속성을 모델링하고, 거의 선형적인 확장을 통해 점진적으로 더 정교한 계획을 가능하게 하며, 저장소에 대한 LLM의 이해를 향상시켜 에이전트 위치 파악을 가속화함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델이 코드 생성에서 뛰어난 성능을 보이지만, 전체 저장소를 처음부터 생성하는 데 어려움이 있다는 문제를 다룹니다. 이를 해결하기 위해, 제안 및 구현 수준의 계획을 통합하는 저장소 계획 그래프(RPG)를 제안합니다. RPG는 명확한 청사진을 제공하여 장기 계획과 확장 가능한 저장소 생성을 가능하게 합니다. RPG를 기반으로 제로레포(ZeroRepo)라는 프레임워크를 개발하여, 세 단계의 과정을 통해 저장소를 생성합니다. 이를 평가하기 위해 RepoCraft라는 벤치마크를 사용했으며, 제로레포는 평균 약 36K LOC의 저장소를 생성하여 기존 방법보다 훨씬 뛰어난 성능을 보였습니다. RPG는 복잡한 의존성을 모델링하고, 대규모 언어 모델의 저장소 이해를 향상시켜 에이전트의 위치 파악을 가속화합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델은 함수 및 파일 수준의 코드 생성에 뛰어나지만, 전체 저장소를 처음부터 생성하는 것은 여전히 어려운 과제입니다.
- 2. Repository Planning Graph (RPG)는 제안 및 구현 수준의 계획을 통합하여 명확한 청사진을 제공함으로써 자연어의 모호성을 해결합니다.
- 3. ZeroRepo는 RPG를 기반으로 한 저장소 생성 프레임워크로, 제안 수준의 계획, 구현 수준의 세부 조정, 그래프 기반 코드 생성 단계를 포함합니다.
- 4. RepoCraft 벤치마크에서 ZeroRepo는 평균 36K LOC의 저장소를 생성하며, 이는 기존 최강 기준보다 약 3.9배, 다른 기준보다 약 64배 더 많습니다.
- 5. RPG는 복잡한 의존성을 모델링하고, LLM의 저장소 이해도를 향상시켜 에이전트 로컬라이제이션을 가속화합니다.


---

*Generated on 2025-09-23 09:32:06*