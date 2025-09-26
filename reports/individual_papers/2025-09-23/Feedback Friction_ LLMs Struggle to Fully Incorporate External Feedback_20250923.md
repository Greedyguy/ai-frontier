---
keywords:
  - Large Language Model
  - Feedback Friction
  - Semantic Entropy
  - Progressive Temperature Increases
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.11930
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:05:00.570421",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Feedback Friction",
    "Semantic Entropy",
    "Progressive Temperature Increases"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Feedback Friction": 0.78,
    "Semantic Entropy": 0.72,
    "Progressive Temperature Increases": 0.7
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
        "rationale": "Central to the paper's investigation and connects to broader discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Feedback Friction",
        "canonical": "Feedback Friction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper's findings on LLMs' resistance to feedback.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semantic Entropy",
        "canonical": "Semantic Entropy",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key metric used in the paper to analyze feedback resistance, offering a unique angle for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Progressive Temperature Increases",
        "canonical": "Progressive Temperature Increases",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific strategy explored in the paper to mitigate feedback friction, relevant for technical linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "external feedback",
      "correct solutions",
      "target performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Feedback Friction",
      "resolved_canonical": "Feedback Friction",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semantic Entropy",
      "resolved_canonical": "Semantic Entropy",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Progressive Temperature Increases",
      "resolved_canonical": "Progressive Temperature Increases",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Feedback Friction: LLMs Struggle to Fully Incorporate External Feedback

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.11930.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.11930](https://arxiv.org/abs/2506.11930)

## 🔗 유사한 논문
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (86.6% similar)
- [[2025-09-23/Adaptive Distraction_ Probing LLM Contextual Robustness with Automated Tree Search_20250923|Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search]] (85.1% similar)
- [[2025-09-23/Neither Stochastic Parroting nor AGI_ LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors_20250923|Neither Stochastic Parroting nor AGI: LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors]] (84.8% similar)
- [[2025-09-23/Challenging the Evaluator_ LLM Sycophancy Under User Rebuttal_20250923|Challenging the Evaluator: LLM Sycophancy Under User Rebuttal]] (84.8% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Feedback Friction|Feedback Friction]], [[keywords/Semantic Entropy|Semantic Entropy]], [[keywords/Progressive Temperature Increases|Progressive Temperature Increases]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.11930v2 Announce Type: replace 
Abstract: Recent studies have shown LLMs possess some ability to improve their responses when given external feedback. However, it remains unclear how effectively and thoroughly these models can incorporate extrinsic feedback. In an ideal scenario, if LLMs receive near-perfect and complete feedback, we would expect them to fully integrate the feedback and reach correct solutions. In this paper, we systematically investigate LLMs' ability to incorporate feedback by designing a controlled experimental environment. For each problem, a solver model attempts a solution, then a feedback generator with access to near-complete ground-truth answers produces targeted feedback, after which the solver tries again. We evaluate this pipeline across a diverse range of tasks, including math reasoning, knowledge reasoning, scientific reasoning, and general multi-domain evaluations with state-of-the-art language models including Claude 3.7 with extended thinking. Surprisingly, even under these near-ideal conditions, solver models consistently show resistance to feedback, a limitation that we term Feedback Friction. To mitigate this limitation, we experiment with sampling-based strategies like progressive temperature increases and explicit rejection of previously attempted incorrect answers, which yield improvements but still fail to help models achieve target performance. We analyze Feedback Friction and find that models' confidence on specific questions, measured by semantic entropy, predicts feedback resistance: high-confidence predictions remain resistant to external correction. We hope that highlighting this issue in LLMs will help future research in self-improvement.

## 📝 요약

최근 연구에 따르면 대형 언어 모델(LLMs)은 외부 피드백을 통해 응답을 개선할 수 있는 능력을 일부 가지고 있지만, 이를 얼마나 효과적으로 통합할 수 있는지는 불명확합니다. 본 논문에서는 LLMs가 피드백을 통합하는 능력을 체계적으로 조사하기 위해 통제된 실험 환경을 설계했습니다. 문제 해결 모델이 솔루션을 시도하고, 피드백 생성기가 거의 완벽한 정답을 바탕으로 피드백을 제공한 후, 해결 모델이 다시 시도하는 과정을 평가했습니다. 다양한 작업에서 실험한 결과, 이상적인 조건에서도 모델들이 피드백에 저항하는 '피드백 마찰' 현상이 발견되었습니다. 이를 완화하기 위해 점진적인 온도 증가와 이전의 잘못된 답변을 명시적으로 거부하는 샘플링 기반 전략을 시도했으나, 목표 성능을 달성하는 데는 실패했습니다. 피드백 마찰은 모델의 특정 질문에 대한 자신감, 즉 의미론적 엔트로피로 측정된 피드백 저항성을 예측하며, 높은 자신감의 예측은 외부 수정에 저항합니다. 이 문제를 강조함으로써 LLMs의 자기 개선에 대한 향후 연구에 기여하고자 합니다.

## 🎯 주요 포인트

- 1. LLMs는 외부 피드백을 통해 응답을 개선할 수 있는 능력을 어느 정도 보유하고 있지만, 이를 얼마나 효과적으로 통합할 수 있는지는 불분명하다.
- 2. 연구에서는 LLMs가 피드백을 통합하는 능력을 체계적으로 조사하기 위해 제어된 실험 환경을 설계하였다.
- 3. 이상적인 조건에서도 솔버 모델은 피드백에 대한 저항성을 보이며, 이를 '피드백 마찰'로 명명하였다.
- 4. 피드백 마찰을 완화하기 위해 점진적인 온도 증가 및 이전에 시도한 잘못된 답변의 명시적 거부와 같은 샘플링 기반 전략을 실험하였으나 목표 성능 달성에는 실패하였다.
- 5. 모델의 특정 질문에 대한 자신감이 피드백 저항성을 예측하며, 높은 자신감을 가진 예측은 외부 수정에 저항한다는 것을 발견하였다.


---

*Generated on 2025-09-24 04:05:00*