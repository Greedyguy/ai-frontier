---
keywords:
  - Large Language Model
  - LLM as Formalizer
  - LLM as Solver
  - Few-Shot Learning
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2505.13252
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:45:05.072146",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "LLM as Formalizer",
    "LLM as Solver",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "LLM as Formalizer": 0.78,
    "LLM as Solver": 0.77,
    "Few-Shot Learning": 0.8
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
          "large language models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion, linking LLMs provides context within the broader field of AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "LLM-as-formalizer",
        "canonical": "LLM as Formalizer",
        "aliases": [
          "formalizer LLM",
          "LLM formalization"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific application of LLMs that is central to the paper's argument.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "LLM-as-solver",
        "canonical": "LLM as Solver",
        "aliases": [
          "solver LLM",
          "LLM solving"
        ],
        "category": "unique_technical",
        "rationale": "Contrasts with LLM-as-formalizer, highlighting different roles of LLMs in problem-solving.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Few-shot settings",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "few-shot",
          "few shot"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant to the evaluation context of LLMs, connecting to broader discussions on learning paradigms.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "solution",
      "performance gain",
      "real-life constraint satisfaction problems"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "LLM-as-formalizer",
      "resolved_canonical": "LLM as Formalizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LLM-as-solver",
      "resolved_canonical": "LLM as Solver",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Few-shot settings",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Are LLMs Better Formalizers than Solvers on Complex Problems?

**Korean Title:** LLM은 복잡한 문제에 대해 해결자보다 형식화자로서 더 뛰어난가?

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.13252.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2505.13252](https://arxiv.org/abs/2505.13252)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (86.9% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (86.7% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (86.5% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (86.2% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (86.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/LLM as Formalizer|LLM as Formalizer]], [[keywords/LLM as Solver|LLM as Solver]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.13252v2 Announce Type: replace 
Abstract: A trending line of recent work advocates for using large language models (LLMs) as formalizers instead of as end-to-end solvers for logical reasoning problems. Instead of generating the solution, the LLM generates a formal program that derives a solution via an external solver. While performance gain of the seemingly scalable LLM-as-formalizer over the seemingly unscalable LLM-as-solver has been widely reported, we show that this superiority does not hold on real-life constraint satisfaction problems. On 4 domains, we systematically evaluate 6 LLMs including 4 large reasoning models with inference-time scaling, paired with 5 pipelines including 2 types of formalism. We show that in few-shot settings, LLM-as-formalizer underperforms LLM-as-solver. While LLM-as-formalizer promises accuracy, robustness, faithfulness, and efficiency, we observe that the present LLMs do not yet deliver any of those, as their limited ability to generate formal programs leads to failure to scale with complexity, hard-coded solutions, and excessive reasoning tokens. We present our detailed analysis and actionable remedies to drive future research that improves LLM-as-formalizer.

## 🔍 Abstract (한글 번역)

arXiv:2505.13252v2 발표 유형: 교체  
초록: 최근의 연구 동향은 논리적 추론 문제에 대해 종단 간 해결책으로서가 아니라 형식화 도구로서 대형 언어 모델(LLM)을 사용하는 것을 지지하고 있습니다. 해결책을 생성하는 대신, LLM은 외부 해결 도구를 통해 해결책을 도출하는 형식 프로그램을 생성합니다. 확장 가능해 보이는 형식화 도구로서의 LLM이 확장 불가능해 보이는 해결 도구로서의 LLM보다 성능이 우수하다는 보고가 널리 퍼져 있지만, 우리는 이러한 우월성이 실제 제약 만족 문제에서는 성립하지 않는다는 것을 보여줍니다. 4개의 도메인에서, 우리는 추론 시간 확장 기능을 갖춘 4개의 대형 추론 모델을 포함한 6개의 LLM과 2가지 형식 유형을 포함한 5개의 파이프라인을 체계적으로 평가합니다. 우리는 몇 가지 예시 설정에서, 형식화 도구로서의 LLM이 해결 도구로서의 LLM보다 성능이 떨어진다는 것을 보여줍니다. 형식화 도구로서의 LLM은 정확성, 견고성, 충실성, 효율성을 약속하지만, 현재의 LLM은 형식 프로그램을 생성하는 능력이 제한되어 복잡성에 따라 확장하지 못하고, 하드코딩된 해결책과 과도한 추론 토큰을 초래하여 이러한 약속을 아직 이행하지 못하고 있음을 관찰합니다. 우리는 형식화 도구로서의 LLM을 개선하는 미래 연구를 추진하기 위한 상세한 분석과 실행 가능한 해결책을 제시합니다.

## 📝 요약

최근 연구에서는 대형 언어 모델(LLM)을 논리적 추론 문제의 종단 간 해결사가 아닌 형식화 도구로 사용하는 것을 제안하고 있습니다. LLM이 직접 해답을 생성하는 대신 외부 해결사를 통해 해답을 도출하는 형식 프로그램을 생성하는 방식입니다. 그러나 실제 제약 만족 문제에서는 LLM-as-formalizer의 우월성이 보장되지 않는다는 것을 보여줍니다. 4개의 도메인에서 6개의 LLM을 평가한 결과, LLM-as-formalizer는 소수의 샘플로 학습할 때 LLM-as-solver보다 성능이 떨어졌습니다. 현재 LLM은 형식 프로그램 생성 능력이 제한되어 있어 복잡성에 따른 확장성 부족, 하드코딩된 솔루션, 과도한 추론 토큰 문제를 야기합니다. 본 연구는 이러한 문제를 해결하기 위한 분석과 개선 방안을 제시합니다.

## 🎯 주요 포인트

- 1. 최근 연구에서는 대형 언어 모델(LLM)을 논리적 추론 문제의 종단 간 해결자가 아닌 형식화 도구로 사용하는 것을 권장하고 있습니다.
- 2. LLM을 형식화 도구로 사용하는 접근 방식이 성능 향상을 보인다는 보고가 많지만, 실제 제약 만족 문제에서는 이러한 우월성이 나타나지 않았습니다.
- 3. 4개의 도메인에서 6개의 LLM을 평가한 결과, 소수의 예시로 학습하는 설정에서는 LLM-as-formalizer가 LLM-as-solver보다 성능이 떨어졌습니다.
- 4. LLM-as-formalizer는 정확성, 견고성, 신뢰성, 효율성을 약속하지만, 현재 LLM은 복잡성에 따른 확장성 부족과 과도한 추론 토큰 문제를 드러냈습니다.
- 5. 본 연구는 LLM-as-formalizer의 성능 개선을 위한 상세한 분석과 실질적인 해결책을 제시합니다.


---

*Generated on 2025-09-23 11:45:05*