---
keywords:
  - Large Language Model
  - Formal Verification
  - Smart Contract
  - GPT-5
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19153
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:21:09.956400",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Formal Verification",
    "Smart Contract",
    "GPT-5"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Formal Verification": 0.78,
    "Smart Contract": 0.8,
    "GPT-5": 0.75
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
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's exploration of verification oracles, linking AI with smart contract security.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Formal Verification",
        "canonical": "Formal Verification",
        "aliases": [
          "Formal Methods",
          "Verification Tools"
        ],
        "category": "specific_connectable",
        "rationale": "Connects the use of LLMs with established methods for ensuring smart contract correctness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Smart Contracts",
        "canonical": "Smart Contract",
        "aliases": [
          "Blockchain Contracts",
          "Crypto Contracts"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's context, linking blockchain technology with AI verification methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.84,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "GPT-5",
        "canonical": "GPT-5",
        "aliases": [
          "Generative Pre-trained Transformer 5"
        ],
        "category": "unique_technical",
        "rationale": "A specific LLM evaluated in the study, crucial for understanding the paper's experimental setup.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "verification oracles",
      "security-related tasks",
      "real-world auditing scenarios"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Formal Verification",
      "resolved_canonical": "Formal Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Smart Contracts",
      "resolved_canonical": "Smart Contract",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.84,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "GPT-5",
      "resolved_canonical": "GPT-5",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# LLMs as verification oracles for Solidity

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19153.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19153](https://arxiv.org/abs/2509.19153)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (82.9% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (82.9% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (82.2% similar)
- [[2025-09-24/G\"odel Test_ Can Large Language Models Solve Easy Conjectures?_20250924|G\"odel Test: Can Large Language Models Solve Easy Conjectures?]] (82.0% similar)
- [[2025-09-23/Advanced Financial Reasoning at Scale_ A Comprehensive Evaluation of Large Language Models on CFA Level III_20250923|Advanced Financial Reasoning at Scale: A Comprehensive Evaluation of Large Language Models on CFA Level III]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Formal Verification|Formal Verification]], [[keywords/Smart Contract|Smart Contract]]
**⚡ Unique Technical**: [[keywords/GPT-5|GPT-5]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19153v1 Announce Type: cross 
Abstract: Ensuring the correctness of smart contracts is critical, as even subtle flaws can lead to severe financial losses. While bug detection tools able to spot common vulnerability patterns can serve as a first line of defense, most real-world exploits and losses stem from errors in the contract business logic. Formal verification tools such as SolCMC and the Certora Prover address this challenge, but their impact remains limited by steep learning curves and restricted specification languages. Recent works have begun to explore the use of large language models (LLMs) for security-related tasks such as vulnerability detection and test generation. Yet, a fundamental question remains open: can LLMs serve as verification oracles, capable of reasoning about arbitrary contract-specific properties? In this paper, we provide the first systematic evaluation of GPT-5, a state-of-the-art reasoning LLM, in this role. We benchmark its performance on a large dataset of verification tasks, compare its outputs against those of established formal verification tools, and assess its practical effectiveness in real-world auditing scenarios. Our study combines quantitative metrics with qualitative analysis, and shows that recent reasoning-oriented LLMs can be surprisingly effective as verification oracles, suggesting a new frontier in the convergence of AI and formal methods for secure smart contract development and auditing.

## 📝 요약

스마트 계약의 정확성 보장은 중요하며, 작은 결함도 큰 재정적 손실을 초래할 수 있습니다. 기존의 버그 탐지 도구는 일반적인 취약점 패턴을 찾아내는 데 유용하지만, 실제 문제는 계약 비즈니스 로직의 오류에서 발생합니다. SolCMC와 Certora Prover 같은 형식 검증 도구가 이러한 문제를 해결하려 하지만, 학습 곡선이 가파르고 명세 언어가 제한적이라는 한계가 있습니다. 최근 대형 언어 모델(LLM)을 보안 작업에 활용하려는 연구가 진행 중이며, 이 논문에서는 최첨단 추론 LLM인 GPT-5를 검증 오라클로서 평가했습니다. 대규모 검증 작업 데이터셋을 통해 성능을 벤치마크하고, 기존 형식 검증 도구와 비교했으며, 실제 감사 시나리오에서의 실용성을 평가했습니다. 연구 결과, 최근의 추론 지향 LLM이 검증 오라클로서 효과적일 수 있음을 보여주어, AI와 형식 방법의 융합을 통한 스마트 계약 개발 및 감사의 새로운 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 스마트 계약의 비즈니스 로직 오류는 실제 세계에서의 손실과 악용의 주요 원인입니다.
- 2. 기존의 형식 검증 도구는 학습 곡선이 가파르고 명세 언어가 제한적이라는 한계가 있습니다.
- 3. 대형 언어 모델(LLM)은 취약성 탐지 및 테스트 생성과 같은 보안 관련 작업에 사용되고 있습니다.
- 4. 본 연구는 GPT-5를 검증 오라클로 활용하여 스마트 계약의 임의 속성을 추론할 수 있는지를 평가합니다.
- 5. 연구 결과, 최신 추론 지향 LLM은 검증 오라클로서 효과적일 수 있으며, AI와 형식 방법의 융합 가능성을 제시합니다.


---

*Generated on 2025-09-25 15:21:09*