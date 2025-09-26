<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:47:03.370050",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Rank-Induced PL Mirror Descent",
    "Rank-Faithful Algorithm",
    "Variance-Adaptive Algorithm",
    "Sleeping Experts Problem"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Rank-Induced PL Mirror Descent": 0.8,
    "Rank-Faithful Algorithm": 0.7,
    "Variance-Adaptive Algorithm": 0.7,
    "Sleeping Experts Problem": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Rank-Induced Plackett--Luce Mirror Descent",
        "canonical": "Rank-Induced PL Mirror Descent",
        "aliases": [
          "RIPLM"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel algorithm introduced in the paper, crucial for understanding the specific advancements discussed.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "rank-faithful",
        "canonical": "Rank-Faithful Algorithm",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution, emphasizing the algorithm's fidelity to rank benchmarks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "variance-adaptive",
        "canonical": "Variance-Adaptive Algorithm",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This describes a key feature of the algorithm, relevant for linking to discussions on adaptability in algorithms.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "sleeping experts",
        "canonical": "Sleeping Experts Problem",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a well-known problem in machine learning, providing context for the algorithm's application.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "benchmark",
      "distribution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Rank-Induced Plackett--Luce Mirror Descent",
      "resolved_canonical": "Rank-Induced PL Mirror Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "rank-faithful",
      "resolved_canonical": "Rank-Faithful Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "variance-adaptive",
      "resolved_canonical": "Variance-Adaptive Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "sleeping experts",
      "resolved_canonical": "Sleeping Experts Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Rank-Induced PL Mirror Descent: A Rank-Faithful Second-Order Algorithm for Sleeping Experts

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18138.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18138](https://arxiv.org/abs/2509.18138)

## 🔗 유사한 논문
- [[2025-09-22/Top-$k$ Feature Importance Ranking_20250922|Top-$k$ Feature Importance Ranking]] (78.6% similar)
- [[2025-09-23/RALLM-POI_ Retrieval-Augmented LLM for Zero-shot Next POI Recommendation with Geographical Reranking_20250923|RALLM-POI: Retrieval-Augmented LLM for Zero-shot Next POI Recommendation with Geographical Reranking]] (77.9% similar)
- [[2025-09-24/NGRPO_ Negative-enhanced Group Relative Policy Optimization_20250924|NGRPO: Negative-enhanced Group Relative Policy Optimization]] (77.9% similar)
- [[2025-09-23/Synthetic POMDPs to Challenge Memory-Augmented RL_ Memory Demand Structure Modeling_20250923|Synthetic POMDPs to Challenge Memory-Augmented RL: Memory Demand Structure Modeling]] (77.5% similar)
- [[2025-09-23/On the Limits of Tabular Hardness Metrics for Deep RL_ A Study with the Pharos Benchmark_20250923|On the Limits of Tabular Hardness Metrics for Deep RL: A Study with the Pharos Benchmark]] (77.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sleeping Experts Problem|Sleeping Experts Problem]]
**⚡ Unique Technical**: [[keywords/Rank-Induced PL Mirror Descent|Rank-Induced PL Mirror Descent]], [[keywords/Rank-Faithful Algorithm|Rank-Faithful Algorithm]], [[keywords/Variance-Adaptive Algorithm|Variance-Adaptive Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18138v1 Announce Type: new 
Abstract: We introduce a new algorithm, \emph{Rank-Induced Plackett--Luce Mirror Descent (RIPLM)}, which leverages the structural equivalence between the \emph{rank benchmark} and the \emph{distributional benchmark} established in \citet{BergamOzcanHsu2022}. Unlike prior approaches that operate on expert identities, RIPLM updates directly in the \emph{rank-induced Plackett--Luce (PL)} parameterization. This ensures that the algorithm's played distributions remain within the class of rank-induced distributions at every round, preserving the equivalence with the rank benchmark. To our knowledge, RIPLM is the first algorithm that is both (i) \emph{rank-faithful} and (ii) \emph{variance-adaptive} in the sleeping experts setting.

## 📝 요약

이 논문에서는 새로운 알고리즘인 RIPLM(Rank-Induced Plackett--Luce Mirror Descent)을 소개합니다. 이 알고리즘은 \emph{rank benchmark}와 \emph{distributional benchmark} 간의 구조적 동등성을 활용하여, 기존의 전문가 정체성을 기반으로 한 접근 방식과 달리 \emph{rank-induced Plackett--Luce} 매개변수화를 직접 업데이트합니다. 이를 통해 알고리즘이 각 라운드에서 순위 유도 분포 내에 머물도록 하여, 순위 벤치마크와의 동등성을 유지합니다. RIPLM은 \emph{rank-faithful}하고 \emph{variance-adaptive}한 특성을 가진 최초의 알고리즘으로, 수면 전문가 설정에서 이러한 특성을 갖춘 알고리즘은 처음입니다.

## 🎯 주요 포인트

- 1. 새로운 알고리즘인 Rank-Induced Plackett--Luce Mirror Descent (RIPLM)을 소개합니다.
- 2. RIPLM은 \emph{rank benchmark}와 \emph{distributional benchmark} 간의 구조적 동등성을 활용합니다.
- 3. 이 알고리즘은 전문가의 정체성 대신 \emph{rank-induced Plackett--Luce (PL)} 매개변수화를 직접 업데이트합니다.
- 4. RIPLM은 \emph{rank-faithful}하며 \emph{variance-adaptive}한 특성을 가진 최초의 알고리즘입니다.
- 5. 알고리즘은 매 라운드에서 순위 유도 분포 클래스 내에 있는 분포를 유지합니다.


---

*Generated on 2025-09-24 14:47:03*