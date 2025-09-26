---
keywords:
  - Large Language Model
  - Zero-Shot Learning
  - Idea Originality Scoring
  - Frequency-Based Originality
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2505.16232
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:46:09.954176",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Zero-Shot Learning",
    "Idea Originality Scoring",
    "Frequency-Based Originality"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Zero-Shot Learning": 0.82,
    "Idea Originality Scoring": 0.78,
    "Frequency-Based Originality": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the system's operation, facilitating the originality scoring process.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Prompts",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot capabilities are crucial for the system's ability to categorize ideas without prior examples.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Idea Originality Scoring",
        "canonical": "Idea Originality Scoring",
        "aliases": [
          "Originality Scoring"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the paper and central to its contribution, linking creativity and computational methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Frequency-Based Originality",
        "canonical": "Frequency-Based Originality",
        "aliases": [
          "Originality Frequency"
        ],
        "category": "unique_technical",
        "rationale": "This method is a novel approach to measuring originality, distinct from traditional methods.",
        "novelty_score": 0.72,
        "connectivity_score": 0.63,
        "specificity_score": 0.81,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "process",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Zero-Shot Prompts",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Idea Originality Scoring",
      "resolved_canonical": "Idea Originality Scoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Frequency-Based Originality",
      "resolved_canonical": "Frequency-Based Originality",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.63,
        "specificity": 0.81,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MuseScorer: Idea Originality Scoring At Scale

**Korean Title:** MuseScorer: 대규모 아이디어 독창성 점수화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.16232.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2505.16232](https://arxiv.org/abs/2505.16232)

## 🔗 유사한 논문
- [[2025-09-22/Creative Preference Optimization_20250922|Creative Preference Optimization]] (82.6% similar)
- [[2025-09-18/AssoCiAm_ A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity_20250918|AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity]] (80.0% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (79.9% similar)
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (79.5% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Idea Originality Scoring|Idea Originality Scoring]], [[keywords/Frequency-Based Originality|Frequency-Based Originality]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.16232v2 Announce Type: replace 
Abstract: An objective, face-valid method for scoring idea originality is to measure each idea's statistical infrequency within a population -- an approach long used in creativity research. Yet, computing these frequencies requires manually bucketing idea rephrasings, a process that is subjective, labor-intensive, error-prone, and brittle at scale. We introduce MuseScorer, a fully automated, psychometrically validated system for frequency-based originality scoring. MuseScorer integrates a Large Language Model (LLM) with externally orchestrated retrieval: given a new idea, it retrieves semantically similar prior idea-buckets and zero-shot prompts the LLM to judge whether the idea fits an existing bucket or forms a new one. These buckets enable frequency-based originality scoring without human annotation. Across five datasets N_{participants}=1143, n_{ideas}=16,294), MuseScorer matches human annotators in idea clustering structure (AMI = 0.59) and participant-level scoring (r = 0.89), while demonstrating strong convergent and external validity. The system enables scalable, intent-sensitive, and human-aligned originality assessment for creativity research.

## 🔍 Abstract (한글 번역)

arXiv:2505.16232v2 발표 유형: 교체  
초록: 아이디어 독창성을 평가하는 객관적이고 신뢰성 있는 방법은 인구 내에서 각 아이디어의 통계적 희소성을 측정하는 것입니다. 이 접근법은 창의성 연구에서 오랫동안 사용되어 왔습니다. 그러나 이러한 빈도를 계산하려면 아이디어의 재구성을 수동으로 분류해야 하며, 이 과정은 주관적이고, 노동 집약적이며, 오류가 발생하기 쉽고, 대규모로는 취약합니다. 우리는 빈도 기반 독창성 점수를 위한 완전 자동화되고 심리측정학적으로 검증된 시스템인 MuseScorer를 소개합니다. MuseScorer는 대형 언어 모델(LLM)과 외부에서 조정된 검색을 통합합니다: 새로운 아이디어가 주어지면, 의미적으로 유사한 이전 아이디어 버킷을 검색하고, LLM을 제로샷으로 유도하여 아이디어가 기존 버킷에 적합한지 또는 새로운 버킷을 형성하는지를 판단합니다. 이러한 버킷은 인간의 주석 없이 빈도 기반 독창성 점수를 가능하게 합니다. 다섯 개의 데이터셋(N_{participants}=1143, n_{ideas}=16,294)에서 MuseScorer는 아이디어 클러스터링 구조(AMI = 0.59)와 참가자 수준 점수(r = 0.89)에서 인간 주석자와 일치하며, 강력한 수렴 및 외부 타당성을 입증합니다. 이 시스템은 창의성 연구를 위한 확장 가능하고, 의도에 민감하며, 인간과 조화된 독창성 평가를 가능하게 합니다.

## 📝 요약

이 논문은 아이디어의 독창성을 평가하기 위해 통계적 희소성을 측정하는 방법을 자동화한 MuseScorer 시스템을 소개합니다. MuseScorer는 대형 언어 모델(LLM)과 외부 검색 기능을 통합하여 새로운 아이디어가 기존의 아이디어 버킷에 속하는지 또는 새로운 버킷을 형성하는지를 판단합니다. 이를 통해 인간의 주관적 개입 없이 독창성을 평가할 수 있습니다. 1,143명의 참가자와 16,294개의 아이디어를 대상으로 한 실험에서 MuseScorer는 인간 평가자와 유사한 아이디어 클러스터링 구조(AMI = 0.59)와 참가자 수준의 점수(r = 0.89)를 보였으며, 높은 수렴 및 외부 타당성을 입증했습니다. 이 시스템은 창의성 연구에서 대규모로 의도에 민감하고 인간과 일치하는 독창성 평가를 가능하게 합니다.

## 🎯 주요 포인트

- 1. MuseScorer는 아이디어의 빈도 기반 독창성 점수를 자동으로 평가하는 시스템으로, 대규모 언어 모델(LLM)과 외부 조정 검색을 통합하여 작동합니다.
- 2. 새로운 아이디어가 주어지면 MuseScorer는 유사한 이전 아이디어 버킷을 검색하고, LLM을 통해 해당 아이디어가 기존 버킷에 적합한지 또는 새로운 버킷을 형성하는지를 판단합니다.
- 3. MuseScorer는 인간 주석자와 유사한 아이디어 클러스터링 구조(AMI = 0.59)와 참가자 수준의 점수(r = 0.89)를 보여주며, 강력한 수렴 및 외부 타당성을 입증합니다.
- 4. 이 시스템은 창의성 연구를 위한 확장 가능하고 의도에 민감하며 인간과 일치하는 독창성 평가를 가능하게 합니다.


---

*Generated on 2025-09-23 11:46:09*