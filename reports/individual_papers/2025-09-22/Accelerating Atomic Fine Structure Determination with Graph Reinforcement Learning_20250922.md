---
keywords:
  - Graph Reinforcement Learning
  - Markov Decision Process
  - Atomic Fine Structure
  - Plasma Diagnostics
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16184
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:30:57.234495",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Reinforcement Learning",
    "Markov Decision Process",
    "Atomic Fine Structure",
    "Plasma Diagnostics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Reinforcement Learning": 0.78,
    "Markov Decision Process": 0.82,
    "Atomic Fine Structure": 0.75,
    "Plasma Diagnostics": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Reinforcement Learning",
        "canonical": "Graph Reinforcement Learning",
        "aliases": [
          "GRL"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's methodology and connects to the broader field of reinforcement learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Markov Decision Process",
        "canonical": "Markov Decision Process",
        "aliases": [
          "MDP"
        ],
        "category": "specific_connectable",
        "rationale": "This is a foundational concept in decision-making algorithms, linking to various reinforcement learning frameworks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Atomic Fine Structure",
        "canonical": "Atomic Fine Structure",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific application area of the study, linking to atomic physics and spectroscopy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "Plasma Diagnostics",
        "canonical": "Plasma Diagnostics",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This term connects the study to practical applications in plasma physics and fusion research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "automation",
      "efficiency",
      "analysis procedure"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Reinforcement Learning",
      "resolved_canonical": "Graph Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Markov Decision Process",
      "resolved_canonical": "Markov Decision Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Atomic Fine Structure",
      "resolved_canonical": "Atomic Fine Structure",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Plasma Diagnostics",
      "resolved_canonical": "Plasma Diagnostics",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Accelerating Atomic Fine Structure Determination with Graph Reinforcement Learning

**Korean Title:** 원자 미세 구조 결정의 가속화를 위한 그래프 강화 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16184.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16184](https://arxiv.org/abs/2509.16184)

## 🔗 유사한 논문
- [[2025-09-22/CCrepairBench_ A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair_20250922|CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair]] (77.2% similar)
- [[2025-09-22/DeepMech_ A Machine Learning Framework for Chemical Reaction Mechanism Prediction_20250922|DeepMech: A Machine Learning Framework for Chemical Reaction Mechanism Prediction]] (77.2% similar)
- [[2025-09-19/DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO: Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (77.2% similar)
- [[2025-09-18/LLM Agents for Interactive Workflow Provenance_ Reference Architecture and Evaluation Methodology_20250918|LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology]] (76.9% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (76.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Markov Decision Process|Markov Decision Process]]
**⚡ Unique Technical**: [[keywords/Graph Reinforcement Learning|Graph Reinforcement Learning]], [[keywords/Atomic Fine Structure|Atomic Fine Structure]], [[keywords/Plasma Diagnostics|Plasma Diagnostics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16184v1 Announce Type: cross 
Abstract: Atomic data determined by analysis of observed atomic spectra are essential for plasma diagnostics. For each low-ionisation open d- and f-subshell atomic species, around $10^3$ fine structure level energies can be determined through years of analysis of $10^4$ observable spectral lines. We propose the automation of this task by casting the analysis procedure as a Markov decision process and solving it by graph reinforcement learning using reward functions learned on historical human decisions. In our evaluations on existing spectral line lists and theoretical calculations for Co II and Nd II-III, hundreds of level energies were computed within hours, agreeing with published values in 95% of cases for Co II and 54-87% for Nd II-III. As the current efficiency in atomic fine structure determination struggles to meet growing atomic data demands from astronomy and fusion science, our new artificial intelligence approach sets the stage for closing this gap.

## 🔍 Abstract (한글 번역)

arXiv:2509.16184v1 발표 유형: 교차  
초록: 관측된 원자 스펙트럼의 분석을 통해 결정된 원자 데이터는 플라즈마 진단에 필수적입니다. 낮은 이온화 상태의 열린 d- 및 f-준위 원자 종마다, 약 $10^3$개의 미세 구조 준위 에너지가 $10^4$개의 관측 가능한 스펙트럼 선을 수년간 분석하여 결정될 수 있습니다. 우리는 이 작업을 자동화하기 위해 분석 절차를 마르코프 결정 과정으로 변환하고, 과거 인간의 결정을 학습한 보상 함수를 사용하여 그래프 강화 학습으로 이를 해결할 것을 제안합니다. Co II와 Nd II-III에 대한 기존 스펙트럼 선 목록 및 이론적 계산에 대한 평가에서, 수백 개의 준위 에너지가 몇 시간 내에 계산되었으며, Co II의 경우 95%, Nd II-III의 경우 54-87%의 사례에서 발표된 값과 일치했습니다. 천문학과 핵융합 과학에서 증가하는 원자 데이터 수요를 충족하기 위해 원자 미세 구조 결정의 현재 효율성이 어려움을 겪고 있는 상황에서, 우리의 새로운 인공지능 접근 방식은 이 격차를 해소하는 데 중요한 발판을 마련합니다.

## 📝 요약

이 논문은 원자 스펙트럼 분석을 자동화하여 플라즈마 진단에 필요한 원자 데이터를 효율적으로 제공하는 방법을 제안합니다. 저자들은 마르코프 결정 과정을 그래프 강화 학습으로 해결하여, 과거 인간의 결정을 학습한 보상 함수를 사용합니다. Co II와 Nd II-III의 스펙트럼 라인 목록과 이론적 계산을 통해 평가한 결과, 수백 개의 에너지 레벨이 몇 시간 내에 계산되었으며, Co II의 경우 95%, Nd II-III의 경우 54-87%의 정확도로 기존 값과 일치했습니다. 이 연구는 천문학과 핵융합 과학에서의 원자 데이터 수요 증가에 대응하기 위한 인공지능 기반의 새로운 접근법을 제시합니다.

## 🎯 주요 포인트

- 1. 원자 스펙트럼 분석을 통한 원자 데이터는 플라즈마 진단에 필수적입니다.
- 2. 저이온화된 열린 d- 및 f-서브셸 원자 종의 미세 구조 수준 에너지를 자동화하여 분석하는 방법을 제안합니다.
- 3. 마르코프 결정 과정을 그래프 강화 학습으로 해결하여 분석 절차를 자동화합니다.
- 4. Co II와 Nd II-III에 대한 평가에서 수백 개의 수준 에너지를 몇 시간 내에 계산하여 높은 정확도를 보였습니다.
- 5. 인공지능 접근 방식은 천문학과 융합 과학의 원자 데이터 수요 증가에 대응하는 데 기여할 수 있습니다.


---

*Generated on 2025-09-23 09:30:57*