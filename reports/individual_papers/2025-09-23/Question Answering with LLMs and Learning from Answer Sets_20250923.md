---
keywords:
  - Large Language Model
  - Learning from Answer Sets
  - Answer Set Programming
  - Symbolic Reasoning Systems
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16590
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:50:44.063261",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Learning from Answer Sets",
    "Answer Set Programming",
    "Symbolic Reasoning Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Learning from Answer Sets": 0.78,
    "Answer Set Programming": 0.82,
    "Symbolic Reasoning Systems": 0.8
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
        "rationale": "Large Language Models are central to the paper's approach, providing a direct link to existing research in natural language processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Learning from Answer Sets",
        "canonical": "Learning from Answer Sets",
        "aliases": [
          "LAS"
        ],
        "category": "unique_technical",
        "rationale": "This is a core component of the proposed system, crucial for understanding the paper's novel approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Answer Set Programming",
        "canonical": "Answer Set Programming",
        "aliases": [
          "ASP"
        ],
        "category": "specific_connectable",
        "rationale": "ASP is a key reasoning framework used in the paper, linking it to formal logic and reasoning research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "symbolic reasoning systems",
        "canonical": "Symbolic Reasoning Systems",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Symbolic reasoning systems are integral to the hybrid approach discussed, connecting to broader AI methodologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Learning from Answer Sets",
      "resolved_canonical": "Learning from Answer Sets",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Answer Set Programming",
      "resolved_canonical": "Answer Set Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "symbolic reasoning systems",
      "resolved_canonical": "Symbolic Reasoning Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Question Answering with LLMs and Learning from Answer Sets

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16590.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16590](https://arxiv.org/abs/2509.16590)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (87.4% similar)
- [[2025-09-23/On LLM-Based Scientific Inductive Reasoning Beyond Equations_20250923|On LLM-Based Scientific Inductive Reasoning Beyond Equations]] (87.1% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (87.1% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (86.8% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (86.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Answer Set Programming|Answer Set Programming]], [[keywords/Symbolic Reasoning Systems|Symbolic Reasoning Systems]]
**⚡ Unique Technical**: [[keywords/Learning from Answer Sets|Learning from Answer Sets]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16590v1 Announce Type: new 
Abstract: Large Language Models (LLMs) excel at understanding natural language but struggle with explicit commonsense reasoning. A recent trend of research suggests that the combination of LLM with robust symbolic reasoning systems can overcome this problem on story-based question answering tasks. In this setting, existing approaches typically depend on human expertise to manually craft the symbolic component. We argue, however, that this component can also be automatically learned from examples. In this work, we introduce LLM2LAS, a hybrid system that effectively combines the natural language understanding capabilities of LLMs, the rule induction power of the Learning from Answer Sets (LAS) system ILASP, and the formal reasoning strengths of Answer Set Programming (ASP). LLMs are used to extract semantic structures from text, which ILASP then transforms into interpretable logic rules. These rules allow an ASP solver to perform precise and consistent reasoning, enabling correct answers to previously unseen questions. Empirical results outline the strengths and weaknesses of our automatic approach for learning and reasoning in a story-based question answering benchmark.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 자연어 이해에 뛰어나지만 명시적인 상식 추론에는 한계가 있음을 지적하며, 이를 극복하기 위해 LLM과 강력한 상징적 추론 시스템을 결합하는 방법을 제안합니다. 기존 방법은 인간 전문가가 상징적 요소를 수작업으로 설계하는 데 의존하지만, 본 연구는 이 요소를 예시로부터 자동으로 학습할 수 있음을 주장합니다. 제안된 LLM2LAS 시스템은 LLM의 자연어 이해 능력, ILASP의 규칙 유도 능력, ASP의 형식적 추론 능력을 결합하여 새로운 질문에 대한 정확한 답변을 제공합니다. 실험 결과는 스토리 기반 질문 응답 벤치마크에서 자동 학습 및 추론 접근법의 장단점을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 자연어 이해에 뛰어나지만 명시적인 상식 추론에는 어려움을 겪는다.
- 2. LLM과 강력한 상징적 추론 시스템의 결합이 이야기 기반 질문 답변 작업에서 문제를 해결할 수 있다는 연구가 증가하고 있다.
- 3. 기존 접근 방식은 상징적 구성 요소를 수동으로 제작하는 데 인간의 전문성에 의존하지만, 본 연구는 예시로부터 자동으로 학습할 수 있음을 주장한다.
- 4. LLM2LAS는 LLM의 자연어 이해, ILASP의 규칙 유도, ASP의 형식적 추론을 결합한 하이브리드 시스템이다.
- 5. 실험 결과는 이야기 기반 질문 답변 벤치마크에서 자동 학습 및 추론 접근 방식의 장단점을 보여준다.


---

*Generated on 2025-09-23 22:50:44*