---
keywords:
  - Large Language Model
  - Code Translation
  - Equivalence Validation
  - Multi-Agent Architecture
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16187
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:58:27.541301",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Code Translation",
    "Equivalence Validation",
    "Multi-Agent Architecture"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Code Translation": 0.78,
    "Equivalence Validation": 0.77,
    "Multi-Agent Architecture": 0.8
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
        "rationale": "Connects to the broader field of AI and machine learning, facilitating links to related technologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Code Translation",
        "canonical": "Code Translation",
        "aliases": [
          "Programming Language Translation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, enabling connections to software engineering and programming language studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Equivalence Validation",
        "canonical": "Equivalence Validation",
        "aliases": [
          "Functional Equivalence Checking"
        ],
        "category": "unique_technical",
        "rationale": "Key process in ensuring accurate code translation, linking to software verification and validation fields.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multi-Agent Architecture",
        "canonical": "Multi-Agent Architecture",
        "aliases": [
          "Agent-Based System"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the structural approach of the system, connecting to studies in distributed systems and AI.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "test agent",
      "repair agent",
      "verdict agent"
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
      "candidate_surface": "Code Translation",
      "resolved_canonical": "Code Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Equivalence Validation",
      "resolved_canonical": "Equivalence Validation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multi-Agent Architecture",
      "resolved_canonical": "Multi-Agent Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair

**Korean Title:** MatchFixAgent: 언어에 구애받지 않는 자율적 저장소 수준의 코드 번역 검증 및 수정

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16187.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16187](https://arxiv.org/abs/2509.16187)

## 🔗 유사한 논문
- [[2025-09-18/Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (86.4% similar)
- [[2025-09-19/RulER_ Automated Rule-Based Semantic Error Localization and Repair for Code Translation_20250919|RulER: Automated Rule-Based Semantic Error Localization and Repair for Code Translation]] (84.0% similar)
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub]] (81.4% similar)
- [[2025-09-19/Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect: Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (80.4% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent Architecture|Multi-Agent Architecture]]
**⚡ Unique Technical**: [[keywords/Code Translation|Code Translation]], [[keywords/Equivalence Validation|Equivalence Validation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16187v1 Announce Type: cross 
Abstract: Code translation transforms source code from one programming language (PL) to another. Validating the functional equivalence of translation and repairing, if necessary, are critical steps in code translation. Existing automated validation and repair approaches struggle to generalize to many PLs due to high engineering overhead, and they rely on existing and often inadequate test suites, which results in false claims of equivalence and ineffective translation repair. We develop MatchFixAgent, a large language model (LLM)-based, PL-agnostic framework for equivalence validation and repair of translations. MatchFixAgent features a multi-agent architecture that divides equivalence validation into several sub-tasks to ensure thorough and consistent semantic analysis of the translation. Then it feeds this analysis to test agent to write and execute tests. Upon observing a test failure, the repair agent attempts to fix the translation bug. The final (in)equivalence decision is made by the verdict agent, considering semantic analyses and test execution results.
  We compare MatchFixAgent's validation and repair results with four repository-level code translation techniques. We use 2,219 translation pairs from their artifacts, which cover 6 PL pairs, and are collected from 24 GitHub projects totaling over 900K lines of code. Our results demonstrate that MatchFixAgent produces (in)equivalence verdicts for 99.2% of translation pairs, with the same equivalence validation result as prior work on 72.8% of them. When MatchFixAgent's result disagrees with prior work, we find that 60.7% of the time MatchFixAgent's result is actually correct. In addition, we show that MatchFixAgent can repair 50.6% of inequivalent translation, compared to prior work's 18.5%. This demonstrates that MatchFixAgent is far more adaptable to many PL pairs than prior work, while producing highly accurate validation results.

## 🔍 Abstract (한글 번역)

arXiv:2509.16187v1 발표 유형: 교차  
초록: 코드 번역은 소스 코드를 한 프로그래밍 언어(PL)에서 다른 언어로 변환하는 작업입니다. 번역의 기능적 동등성을 검증하고 필요시 수정하는 것은 코드 번역에서 중요한 단계입니다. 기존의 자동화된 검증 및 수정 접근법은 높은 엔지니어링 비용 때문에 많은 PL에 일반화하는 데 어려움을 겪으며, 기존의 불충분한 테스트 스위트에 의존하여 동등성에 대한 잘못된 주장과 비효율적인 번역 수정을 초래합니다. 우리는 번역의 동등성 검증 및 수정을 위한 대형 언어 모델(LLM) 기반의 PL-독립적 프레임워크인 MatchFixAgent를 개발했습니다. MatchFixAgent는 다중 에이전트 아키텍처를 특징으로 하여 번역의 철저하고 일관된 의미 분석을 보장하기 위해 동등성 검증을 여러 하위 작업으로 나눕니다. 그런 다음 이 분석을 테스트 에이전트에 제공하여 테스트를 작성하고 실행합니다. 테스트 실패가 관찰되면 수정 에이전트가 번역 버그를 수정하려고 시도합니다. 최종 (비)동등성 결정은 의미 분석 및 테스트 실행 결과를 고려하여 판결 에이전트에 의해 이루어집니다.  
우리는 MatchFixAgent의 검증 및 수정 결과를 네 가지 저장소 수준 코드 번역 기술과 비교합니다. 우리는 6개의 PL 쌍을 다루는 2,219개의 번역 쌍을 사용하며, 이는 24개의 GitHub 프로젝트에서 수집된 총 90만 줄 이상의 코드에서 수집되었습니다. 우리의 결과는 MatchFixAgent가 번역 쌍의 99.2%에 대해 (비)동등성 판결을 내리며, 그 중 72.8%는 이전 작업과 동일한 동등성 검증 결과를 나타냅니다. MatchFixAgent의 결과가 이전 작업과 일치하지 않는 경우, 60.7%의 경우 MatchFixAgent의 결과가 실제로 올바름을 발견했습니다. 또한, MatchFixAgent가 이전 작업의 18.5%에 비해 50.6%의 비동등 번역을 수정할 수 있음을 보여줍니다. 이는 MatchFixAgent가 이전 작업보다 많은 PL 쌍에 훨씬 더 적응력이 뛰어나며, 매우 정확한 검증 결과를 생성함을 입증합니다.

## 📝 요약

MatchFixAgent는 프로그래밍 언어 간 코드 번역의 기능적 동등성을 검증하고 필요 시 수정하는 LLM 기반의 프레임워크입니다. 이 시스템은 다중 에이전트 아키텍처를 통해 번역의 의미 분석을 수행하고, 테스트 에이전트가 테스트를 작성 및 실행하며, 오류 발생 시 수리 에이전트가 번역 오류를 수정합니다. 최종 동등성 판단은 의미 분석과 테스트 결과를 바탕으로 이루어집니다. 6개의 프로그래밍 언어 쌍을 포함한 2,219개의 번역 쌍을 대상으로 한 실험에서 MatchFixAgent는 99.2%의 번역 쌍에 대해 동등성 판단을 내렸으며, 기존 방법과의 불일치 시 60.7%의 경우에 MatchFixAgent의 결과가 정확했습니다. 또한, MatchFixAgent는 기존 방법보다 50.6%의 비동등 번역을 성공적으로 수정하여 더 높은 적응성과 정확성을 입증했습니다.

## 🎯 주요 포인트

- 1. MatchFixAgent는 프로그래밍 언어에 구애받지 않는 대규모 언어 모델 기반의 코드 번역 등가성 검증 및 수정을 위한 프레임워크입니다.
- 2. MatchFixAgent는 다중 에이전트 아키텍처를 통해 번역의 철저하고 일관된 의미 분석을 수행하고, 테스트 에이전트를 통해 테스트를 작성 및 실행합니다.
- 3. MatchFixAgent는 6개의 프로그래밍 언어 쌍을 포함한 2,219개의 번역 쌍에 대해 99.2%의 등가성 판정을 내렸으며, 기존 연구와 72.8%의 일치율을 보였습니다.
- 4. MatchFixAgent는 기존 연구보다 60.7% 더 정확한 결과를 제공하며, 비등가 번역의 50.6%를 수정할 수 있습니다.
- 5. MatchFixAgent는 다양한 프로그래밍 언어 쌍에 대해 높은 적응성과 정확성을 보여줍니다.


---

*Generated on 2025-09-23 10:58:27*