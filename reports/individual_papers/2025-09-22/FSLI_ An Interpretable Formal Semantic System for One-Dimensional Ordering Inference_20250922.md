---
keywords:
  - Formal Semantic Logic Inferer
  - Natural Language Processing
  - Constraint Logic Programming
  - Logical Deduction
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2502.08415
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:40:56.683794",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Formal Semantic Logic Inferer",
    "Natural Language Processing",
    "Constraint Logic Programming",
    "Logical Deduction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Formal Semantic Logic Inferer": 0.8,
    "Natural Language Processing": 0.7,
    "Constraint Logic Programming": 0.75,
    "Logical Deduction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Formal Semantic Logic Inferer",
        "canonical": "Formal Semantic Logic Inferer",
        "aliases": [
          "FSLI"
        ],
        "category": "unique_technical",
        "rationale": "FSLI is a novel system introduced in the paper, providing a unique approach to logical deduction in NLP.",
        "novelty_score": 0.9,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "NLP is a foundational field relevant to the paper's focus on logical deduction from natural language.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Constraint Logic Programming",
        "canonical": "Constraint Logic Programming",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for executing logical forms in the system, linking to broader logic programming concepts.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Logical Deduction",
        "canonical": "Logical Deduction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Logical deduction is the core task addressed by the system, connecting to broader logical reasoning frameworks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Formal Semantic Logic Inferer",
      "resolved_canonical": "Formal Semantic Logic Inferer",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Constraint Logic Programming",
      "resolved_canonical": "Constraint Logic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Logical Deduction",
      "resolved_canonical": "Logical Deduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# FSLI: An Interpretable Formal Semantic System for One-Dimensional Ordering Inference

**Korean Title:** FSLI: 일차원적 순서 추론을 위한 해석 가능한 형식적 의미 체계

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.08415.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2502.08415](https://arxiv.org/abs/2502.08415)

## 🔗 유사한 논문
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (83.4% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (82.9% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (82.9% similar)
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE: Faithful Logic-Aided Reasoning and Exploration]] (82.5% similar)
- [[2025-09-18/Implementing a Logical Inference System for Japanese Comparatives_20250918|Implementing a Logical Inference System for Japanese Comparatives]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Constraint Logic Programming|Constraint Logic Programming]], [[keywords/Logical Deduction|Logical Deduction]]
**⚡ Unique Technical**: [[keywords/Formal Semantic Logic Inferer|Formal Semantic Logic Inferer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.08415v2 Announce Type: replace 
Abstract: We develop a system for solving logical deduction one-dimensional ordering problems by transforming natural language premises and candidate statements into first-order logic. Building on Heim and Kratzer's syntax-based compositional semantic rules which utilizes lambda calculus, we develop a semantic parsing algorithm with abstract types, templated rules, and a dynamic component for interpreting entities within a context constructed from the input. The resulting logical forms are executed via constraint logic programming to determine which candidate statements can be logically deduced from the premises.
  The symbolic system, the Formal Semantic Logic Inferer (FSLI), provides a formally grounded, linguistically driven system for natural language logical deduction. We evaluate it on both synthetic and derived logical deduction problems. FSLI achieves 100% accuracy on BIG-bench's logical deduction task and 88% on a syntactically simplified subset of AR-LSAT outperforming an LLM baseline, o1-preview.
  While current research in natural language reasoning emphasizes neural language models, FSLI highlights the potential of principled, interpretable systems for symbolic logical deduction in NLP.

## 🔍 Abstract (한글 번역)

arXiv:2502.08415v2 발표 유형: 교체  
초록: 우리는 자연어 전제와 후보 명제를 일차 논리로 변환하여 논리적 추론 일차원 순서 문제를 해결하는 시스템을 개발합니다. 람다 계산을 활용한 Heim과 Kratzer의 구문 기반 구성 의미론 규칙을 기반으로 하여, 우리는 입력으로부터 구성된 맥락 내에서 개체를 해석하기 위한 추상 유형, 템플릿 규칙 및 동적 구성 요소를 갖춘 의미론적 구문 분석 알고리즘을 개발합니다. 결과로 생성된 논리 형식은 제약 논리 프로그래밍을 통해 실행되어 전제로부터 논리적으로 추론할 수 있는 후보 명제를 결정합니다.  
상징적 시스템인 Formal Semantic Logic Inferer (FSLI)은 자연어 논리적 추론을 위한 형식적으로 근거가 있는, 언어학적으로 주도된 시스템을 제공합니다. 우리는 이를 합성 및 파생된 논리적 추론 문제에서 평가합니다. FSLI는 BIG-bench의 논리적 추론 과제에서 100%의 정확도를 달성하고, AR-LSAT의 구문적으로 단순화된 하위 집합에서 LLM 기준선인 o1-preview를 능가하여 88%의 정확도를 달성합니다.  
현재 자연어 추론 연구가 신경 언어 모델에 중점을 두고 있는 반면, FSLI는 NLP에서 상징적 논리적 추론을 위한 원칙적이고 해석 가능한 시스템의 잠재력을 강조합니다.

## 📝 요약

이 논문은 자연어 전제를 일차 논리로 변환하여 논리적 추론 문제를 해결하는 시스템을 개발합니다. Heim과 Kratzer의 구문 기반 의미론 규칙을 바탕으로, 람다 계산을 활용한 의미 구문 분석 알고리즘을 제안합니다. 이 알고리즘은 추상 타입, 템플릿 규칙, 동적 구성 요소를 사용하여 입력으로부터 맥락을 구성하고, 제약 논리 프로그래밍을 통해 후보 문장을 논리적으로 추론할 수 있는지를 판단합니다. 개발된 시스템인 FSLI는 BIG-bench의 논리 추론 과제에서 100%의 정확도를 달성하고, AR-LSAT의 단순화된 부분 집합에서 88%의 정확도를 기록하며, LLM 기반의 o1-preview를 능가합니다. 이 연구는 자연어 처리에서 상징적 논리 추론의 가능성을 강조합니다.

## 🎯 주요 포인트

- 1. 자연어 전제를 일차 논리로 변환하여 논리적 추론 문제를 해결하는 시스템을 개발했습니다.
- 2. 람다 계산을 활용한 Heim과 Kratzer의 구문 기반 의미론 규칙을 기반으로 의미론적 구문 분석 알고리즘을 개발했습니다.
- 3. 제약 논리 프로그래밍을 통해 후보 문장이 전제로부터 논리적으로 추론될 수 있는지를 판단합니다.
- 4. 개발된 시스템인 Formal Semantic Logic Inferer (FSLI)는 BIG-bench의 논리적 추론 과제에서 100%의 정확도를 달성했습니다.
- 5. FSLI는 신경망 언어 모델에 비해 해석 가능한 상징적 논리 추론 시스템의 잠재력을 강조합니다.


---

*Generated on 2025-09-23 11:40:56*