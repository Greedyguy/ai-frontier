---
keywords:
  - Large Language Model
  - Zero-Shot Learning
  - RankNet
  - Comparative Essay Scoring
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.08498
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:57:29.524717",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Zero-Shot Learning",
    "RankNet",
    "Comparative Essay Scoring"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Zero-Shot Learning": 0.78,
    "RankNet": 0.7,
    "Comparative Essay Scoring": 0.72
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
        "rationale": "Essential for understanding the underlying technology used in zero-shot AES.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-shot Automated Essay Scoring",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot AES"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the application of zero-shot learning in essay scoring, connecting to broader zero-shot techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "RankNet",
        "canonical": "RankNet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific algorithm used for scalability in the proposed method, linking to machine learning ranking techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Comparative Essay Scoring",
        "canonical": "Comparative Essay Scoring",
        "aliases": [
          "LCES"
        ],
        "category": "unique_technical",
        "rationale": "Unique approach proposed in the paper, highlighting a novel application of pairwise comparisons in AES.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "essay scoring",
      "manual grading",
      "human evaluations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-shot Automated Essay Scoring",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "RankNet",
      "resolved_canonical": "RankNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Comparative Essay Scoring",
      "resolved_canonical": "Comparative Essay Scoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# LCES: Zero-shot Automated Essay Scoring via Pairwise Comparisons Using Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.08498.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.08498](https://arxiv.org/abs/2505.08498)

## 🔗 유사한 논문
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (88.1% similar)
- [[2025-09-22/Beyond the Score_ Uncertainty-Calibrated LLMs for Automated Essay Assessment_20250922|Beyond the Score: Uncertainty-Calibrated LLMs for Automated Essay Assessment]] (87.4% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (83.1% similar)
- [[2025-09-22/Beyond Pointwise Scores_ Decomposed Criteria-Based Evaluation of LLM Responses_20250922|Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses]] (82.4% similar)
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/RankNet|RankNet]], [[keywords/Comparative Essay Scoring|Comparative Essay Scoring]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.08498v2 Announce Type: replace-cross 
Abstract: Recent advances in large language models (LLMs) have enabled zero-shot automated essay scoring (AES), providing a promising way to reduce the cost and effort of essay scoring in comparison with manual grading. However, most existing zero-shot approaches rely on LLMs to directly generate absolute scores, which often diverge from human evaluations owing to model biases and inconsistent scoring. To address these limitations, we propose LLM-based Comparative Essay Scoring (LCES), a method that formulates AES as a pairwise comparison task. Specifically, we instruct LLMs to judge which of two essays is better, collect many such comparisons, and convert them into continuous scores. Considering that the number of possible comparisons grows quadratically with the number of essays, we improve scalability by employing RankNet to efficiently transform LLM preferences into scalar scores. Experiments using AES benchmark datasets show that LCES outperforms conventional zero-shot methods in accuracy while maintaining computational efficiency. Moreover, LCES is robust across different LLM backbones, highlighting its applicability to real-world zero-shot AES.

## 📝 요약

최근 대형 언어 모델(LLM)의 발전으로 인해 자동 에세이 채점(AES)이 가능해졌습니다. 하지만 기존의 제로샷 접근법은 모델 편향과 일관성 문제로 인해 인간 평가와 차이가 발생합니다. 이를 해결하기 위해, 우리는 LLM 기반의 비교 에세이 채점(LCES)을 제안합니다. LCES는 에세이를 쌍으로 비교하여 더 나은 에세이를 판단하고, 이를 연속적인 점수로 변환합니다. RankNet을 활용하여 비교 수를 효율적으로 처리함으로써 확장성을 개선하였습니다. 실험 결과, LCES는 기존 제로샷 방법보다 정확도가 높고, 다양한 LLM에서도 강건성을 보여 실제 제로샷 AES에 적용 가능성이 높습니다.

## 🎯 주요 포인트

- 1. 최근 대형 언어 모델(LLM)의 발전으로 인해 제로샷 자동 에세이 채점(AES)이 가능해졌으며, 이는 수작업 채점에 비해 비용과 노력을 줄일 수 있는 유망한 방법을 제공합니다.
- 2. 기존 제로샷 접근법은 LLM이 절대 점수를 직접 생성하는 데 의존하지만, 이는 모델 편향과 일관성 없는 채점으로 인해 인간 평가와 종종 다르게 나타납니다.
- 3. LLM 기반 비교 에세이 채점(LCES)은 AES를 쌍별 비교 작업으로 공식화하여 이러한 한계를 극복하고, RankNet을 사용해 LLM의 선호도를 효율적으로 스칼라 점수로 변환하여 확장성을 개선합니다.
- 4. AES 벤치마크 데이터셋을 사용한 실험에서 LCES는 정확도 면에서 기존 제로샷 방법을 능가하면서도 계산 효율성을 유지합니다.
- 5. LCES는 다양한 LLM 백본에서도 강력한 성능을 보여주며, 실제 제로샷 AES에 적용 가능성이 높습니다.


---

*Generated on 2025-09-24 00:57:29*