---
keywords:
  - Decision Tree
  - Predictive Equivalence
  - Rashomon Set
  - Quine-McCluskey Method
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17774
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:03:30.150660",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Decision Tree",
    "Predictive Equivalence",
    "Rashomon Set",
    "Quine-McCluskey Method"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Decision Tree": 0.85,
    "Predictive Equivalence": 0.78,
    "Rashomon Set": 0.8,
    "Quine-McCluskey Method": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Decision Trees",
        "canonical": "Decision Tree",
        "aliases": [
          "DT",
          "Decision Tree Model"
        ],
        "category": "broad_technical",
        "rationale": "Decision Trees are a fundamental concept in machine learning, providing strong connectivity to related works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Predictive Equivalence",
        "canonical": "Predictive Equivalence",
        "aliases": [
          "Equivalent Prediction",
          "Prediction Equivalence"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on decision tree redundancy and optimization.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Rashomon Set",
        "canonical": "Rashomon Set",
        "aliases": [
          "Rashomon Effect",
          "Rashomon Framework"
        ],
        "category": "unique_technical",
        "rationale": "The Rashomon Set is a unique concept that highlights the diversity of models with similar predictive performance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Quine-McCluskey Method",
        "canonical": "Quine-McCluskey Method",
        "aliases": [
          "QM Method",
          "Quine-McCluskey Algorithm"
        ],
        "category": "specific_connectable",
        "rationale": "This method is critical for understanding the computational challenges discussed in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Decision Trees",
      "resolved_canonical": "Decision Tree",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Predictive Equivalence",
      "resolved_canonical": "Predictive Equivalence",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Rashomon Set",
      "resolved_canonical": "Rashomon Set",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Quine-McCluskey Method",
      "resolved_canonical": "Quine-McCluskey Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Efficient & Correct Predictive Equivalence for Decision Trees

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17774.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17774](https://arxiv.org/abs/2509.17774)

## 🔗 유사한 논문
- [[2025-09-19/SMART_ Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction_20250919|SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction]] (77.4% similar)
- [[2025-09-22/Mental Accounts for Actions_ EWA-Inspired Attention in Decision Transformers_20250922|Mental Accounts for Actions: EWA-Inspired Attention in Decision Transformers]] (76.8% similar)
- [[2025-09-22/RMT-KD_ Random Matrix Theoretic Causal Knowledge Distillation_20250922|RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation]] (76.7% similar)
- [[2025-09-19/Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization_20250919|Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization]] (76.7% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (76.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Decision Tree|Decision Tree]]
**🔗 Specific Connectable**: [[keywords/Quine-McCluskey Method|Quine-McCluskey Method]]
**⚡ Unique Technical**: [[keywords/Predictive Equivalence|Predictive Equivalence]], [[keywords/Rashomon Set|Rashomon Set]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17774v1 Announce Type: new 
Abstract: The Rashomon set of decision trees (DTs) finds importance uses. Recent work showed that DTs computing the same classification function, i.e. predictive equivalent DTs, can represent a significant fraction of the Rashomon set. Such redundancy is undesirable. For example, feature importance based on the Rashomon set becomes inaccurate due the existence of predictive equivalent DTs, i.e. DTs with the same prediction for every possible input. In recent work, McTavish et al. proposed solutions for several computational problems related with DTs, including that of deciding predictive equivalent DTs. This approach, which this paper refers to as MBDSR, consists of applying the well-known method of Quine-McCluskey (QM) for obtaining minimum-size DNF (disjunctive normal form) representations of DTs, which are then used for comparing DTs for predictive equivalence. Furthermore, the minimum-size DNF representation was also applied to computing explanations for the predictions made by DTs, and to finding predictions in the presence of missing data. However, the problem of formula minimization is hard for the second level of the polynomial hierarchy, and the QM method may exhibit worst-case exponential running time and space. This paper first demonstrates that there exist decision trees that trigger the worst-case exponential running time and space of the QM method. Second, the paper shows that the MBDSR approach can produce incorrect results for the problem of deciding predictive equivalence. Third, the paper shows that any of the problems to which the minimum-size DNF representation has been applied to can in fact be solved in polynomial time, in the size of the DT. The experiments confirm that, for DTs for which the the worst-case of the QM method is triggered, the algorithms proposed in this paper are orders of magnitude faster than the ones proposed by McTavish et al.

## 📝 요약

이 논문은 결정 트리(DT)의 라쇼몽 집합에서 예측 등가성을 갖는 DT들이 중복 문제를 일으켜 특징 중요도 평가를 왜곡할 수 있음을 지적합니다. McTavish 등은 이러한 예측 등가 DT를 판별하기 위해 Quine-McCluskey(QM) 방법을 사용한 MBDSR 접근법을 제안했으나, 이는 최악의 경우 지수적인 시간과 공간을 소모할 수 있습니다. 본 논문은 QM 방법의 한계를 지적하고, 최소 크기 DNF 표현을 사용하는 문제들이 실제로는 다항 시간 내에 해결 가능함을 보입니다. 실험 결과, 제안된 알고리즘이 기존 방법보다 훨씬 빠름을 확인했습니다.

## 🎯 주요 포인트

- 1. Rashomon 집합의 의사결정 나무(DT)에서 예측 등가 DT의 존재는 특징 중요성을 부정확하게 만든다.
- 2. McTavish et al.의 MBDSR 접근법은 Quine-McCluskey(QM) 방법을 사용하여 최소 크기의 DNF 표현을 통해 예측 등가성을 결정한다.
- 3. QM 방법은 최악의 경우 지수적 실행 시간과 공간을 요구하며, 이는 특정 DT에서 발생할 수 있다.
- 4. MBDSR 접근법은 예측 등가성을 결정하는 문제에서 부정확한 결과를 초래할 수 있다.
- 5. 최소 크기 DNF 표현을 적용한 문제들은 실제로 DT의 크기에 대해 다항 시간 내에 해결될 수 있다.


---

*Generated on 2025-09-23 23:03:30*