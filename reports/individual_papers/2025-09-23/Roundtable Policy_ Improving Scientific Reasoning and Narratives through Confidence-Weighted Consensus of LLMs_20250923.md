---
keywords:
  - Large Language Model
  - Roundtable Policy
  - Consensus of Multiple LLMs
  - Scientific Narratives
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16839
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:52:21.422638",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Roundtable Policy",
    "Consensus of Multiple LLMs",
    "Scientific Narratives"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Roundtable Policy": 0.85,
    "Consensus of Multiple LLMs": 0.78,
    "Scientific Narratives": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's methodology and connects to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Roundtable Policy",
        "canonical": "Roundtable Policy",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel framework introduced in the paper, enhancing reasoning through LLM consensus.",
        "novelty_score": 0.9,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Consensus of multiple LLMs",
        "canonical": "Consensus of Multiple LLMs",
        "aliases": [
          "LLM Consensus"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking multi-agent reasoning and decision-making strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Scientific narratives",
        "canonical": "Scientific Narratives",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Important for linking discussions on improving narrative quality in scientific contexts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "inference",
      "framework",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Roundtable Policy",
      "resolved_canonical": "Roundtable Policy",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Consensus of multiple LLMs",
      "resolved_canonical": "Consensus of Multiple LLMs",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Scientific narratives",
      "resolved_canonical": "Scientific Narratives",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Roundtable Policy: Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16839.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16839](https://arxiv.org/abs/2509.16839)

## 🔗 유사한 논문
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (85.9% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (85.5% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (85.5% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (85.3% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Consensus of Multiple LLMs|Consensus of Multiple LLMs]], [[keywords/Scientific Narratives|Scientific Narratives]]
**⚡ Unique Technical**: [[keywords/Roundtable Policy|Roundtable Policy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16839v1 Announce Type: new 
Abstract: Large language models (LLMs) have demonstrated remarkable capabilities not only in language generation but also in advancing scientific discovery. A growing body of work has explored ways to improve their reasoning, from self-consistency and chain-of-thought to multi-agent debate. Inspired by the dynamics of scientific committees and the "Society of Mind," we introduce Roundtable Policy, a complementary inference-time reasoning framework that performs inference through the weighted consensus of multiple LLMs. Our findings indicate that this approach significantly enhances reasoning in complex heterogeneous scientific tasks and improves scientific narratives in terms of creativity, rigor, and logical coherence, while reducing hallucinations that single models are prone to. Our approach emphasizes structured and interpretable consensus rather than opaque convergence, while requiring only black-box access and uniform procedures, making it broadly applicable to multi-LLM reasoning.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 추론 능력을 향상시키기 위해 '라운드테이블 정책'이라는 새로운 추론 프레임워크를 제안합니다. 이 방법은 여러 LLM의 가중 합의를 통해 추론을 수행하며, 과학적 위원회의 역학과 '마음의 사회' 개념에서 영감을 받았습니다. 연구 결과, 이 접근법은 복잡하고 이질적인 과학적 과제에서 추론 능력을 크게 향상시키고, 창의성, 엄밀성, 논리적 일관성을 개선하며, 단일 모델에서 발생할 수 있는 환각을 줄이는 데 효과적임을 보여줍니다. 이 방법은 구조화된 해석 가능한 합의를 강조하며, 블랙박스 접근과 일관된 절차만 필요로 하여 다중 LLM 추론에 폭넓게 적용 가능합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 언어 생성뿐만 아니라 과학적 발견을 발전시키는 데도 뛰어난 능력을 보여주고 있다.
- 2. Roundtable Policy는 여러 LLM의 가중치 합의를 통해 추론을 수행하는 보완적 추론 프레임워크로 제안되었다.
- 3. 이 접근 방식은 복잡한 이질적 과학 과제에서의 추론을 크게 향상시키고, 창의성, 엄밀성, 논리적 일관성 측면에서 과학적 서사를 개선한다.
- 4. Roundtable Policy는 단일 모델이 자주 겪는 환각을 줄이며, 구조적이고 해석 가능한 합의를 강조한다.
- 5. 이 방법은 블랙박스 접근과 균일한 절차만을 요구하여, 다중 LLM 추론에 폭넓게 적용 가능하다.


---

*Generated on 2025-09-23 22:52:21*