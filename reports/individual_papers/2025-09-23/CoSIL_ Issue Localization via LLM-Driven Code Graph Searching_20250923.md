---
keywords:
  - Large Language Model
  - Code Graph Search
  - Module Call Graph
  - Function Call Graph
  - Reflection Mechanism
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2503.22424
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:52:03.137861",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Code Graph Search",
    "Module Call Graph",
    "Function Call Graph",
    "Reflection Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Code Graph Search": 0.79,
    "Module Call Graph": 0.75,
    "Function Call Graph": 0.73,
    "Reflection Mechanism": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-driven",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the method described and connect to existing research on LLM applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "code graph search",
        "canonical": "Code Graph Search",
        "aliases": [
          "graph search in code"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach described in the paper, highlighting a novel method for issue localization.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "module call graph",
        "canonical": "Module Call Graph",
        "aliases": [
          "module-level call graph"
        ],
        "category": "specific_connectable",
        "rationale": "Module call graphs are a specific technique used in the paper, relevant for linking to graph-based code analysis.",
        "novelty_score": 0.56,
        "connectivity_score": 0.74,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "function call graph",
        "canonical": "Function Call Graph",
        "aliases": [
          "function-level call graph"
        ],
        "category": "specific_connectable",
        "rationale": "Function call graphs are crucial for understanding the detailed analysis phase in the paper's method.",
        "novelty_score": 0.54,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.73
      },
      {
        "surface": "reflection mechanism",
        "canonical": "Reflection Mechanism",
        "aliases": [
          "reflection strategy"
        ],
        "category": "unique_technical",
        "rationale": "The reflection mechanism is a unique feature of the method, enhancing the precision of issue localization.",
        "novelty_score": 0.67,
        "connectivity_score": 0.68,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "issue solving",
      "search space",
      "context"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-driven",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "code graph search",
      "resolved_canonical": "Code Graph Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "module call graph",
      "resolved_canonical": "Module Call Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.56,
        "connectivity": 0.74,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "function call graph",
      "resolved_canonical": "Function Call Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.54,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.73
      }
    },
    {
      "candidate_surface": "reflection mechanism",
      "resolved_canonical": "Reflection Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.68,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# CoSIL: Issue Localization via LLM-Driven Code Graph Searching

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.22424.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2503.22424](https://arxiv.org/abs/2503.22424)

## 🔗 유사한 논문
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (80.8% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (80.6% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (80.2% similar)
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT: An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (79.7% similar)
- [[2025-09-22/CCrepairBench_ A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair_20250922|CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Module Call Graph|Module Call Graph]], [[keywords/Function Call Graph|Function Call Graph]]
**⚡ Unique Technical**: [[keywords/Code Graph Search|Code Graph Search]], [[keywords/Reflection Mechanism|Reflection Mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.22424v2 Announce Type: replace-cross 
Abstract: Issue solving aims to generate patches to fix reported issues in real-world code repositories according to issue descriptions. Issue localization forms the basis for accurate issue solving. Recently, LLM-based issue localization methods have demonstrated state-of-the-art performance. However, these methods either search from files mentioned in issue descriptions or in the whole repository and struggle to balance the breadth and depth of the search space to converge on the target efficiently. Moreover, they allow LLM to explore whole repositories freely, making it challenging to control the search direction to prevent the LLM from searching for incorrect targets. This paper introduces CoSIL, an LLM-driven, powerful function-level issue localization method without training or indexing. CoSIL employs a two-phase code graph search strategy. It first conducts broad exploration at the file level using dynamically constructed module call graphs, and then performs in-depth analysis at the function level by expanding the module call graph into a function call graph and executing iterative searches. To precisely control the search direction, CoSIL designs a pruner to filter unrelated directions and irrelevant contexts. To avoid incorrect interaction formats in long contexts, CoSIL introduces a reflection mechanism that uses additional independent queries in short contexts to enhance formatted abilities. Experiment results demonstrate that CoSIL achieves a Top-1 localization accuracy of 43.3\% and 44.6\% on SWE-bench Lite and SWE-bench Verified, respectively, with Qwen2.5-Coder-32B, average outperforming the state-of-the-art methods by 96.04\%. When CoSIL is integrated into an issue-solving method, Agentless, the issue resolution rate improves by 2.98\%--30.5\%.

## 📝 요약

이 논문은 CoSIL이라는 새로운 LLM 기반 함수 수준 이슈 로컬라이제이션 방법을 제안합니다. CoSIL은 훈련이나 인덱싱 없이 모듈 호출 그래프를 활용하여 파일 수준에서 넓은 탐색을 수행한 후, 함수 호출 그래프로 확장하여 깊이 있는 분석을 진행합니다. 탐색 방향을 정확히 제어하기 위해 불필요한 방향과 문맥을 걸러내는 프루너를 설계하고, 긴 문맥에서의 오류를 피하기 위해 반사 메커니즘을 도입합니다. 실험 결과, CoSIL은 SWE-bench Lite와 SWE-bench Verified에서 각각 43.3%와 44.6%의 Top-1 로컬라이제이션 정확도를 기록하며, 기존 방법들보다 평균 96.04% 더 우수한 성능을 보였습니다. 또한, CoSIL을 이슈 해결 방법인 Agentless에 통합하면 이슈 해결률이 2.98%에서 30.5%까지 향상됩니다.

## 🎯 주요 포인트

- 1. CoSIL은 LLM 기반의 강력한 함수 수준 이슈 로컬라이제이션 방법으로, 훈련이나 인덱싱 없이 작동합니다.
- 2. CoSIL은 모듈 호출 그래프를 사용하여 파일 수준에서 광범위한 탐색을 수행한 후, 함수 호출 그래프로 확장하여 함수 수준에서 심층 분석을 수행합니다.
- 3. CoSIL은 검색 방향을 정확히 제어하기 위해 불필요한 방향과 관련 없는 컨텍스트를 필터링하는 프루너를 설계했습니다.
- 4. 긴 컨텍스트에서 잘못된 상호작용 형식을 피하기 위해 CoSIL은 짧은 컨텍스트에서 독립적인 쿼리를 사용하는 반영 메커니즘을 도입했습니다.
- 5. 실험 결과, CoSIL은 SWE-bench Lite와 SWE-bench Verified에서 각각 43.3%와 44.6%의 Top-1 로컬라이제이션 정확도를 달성했으며, 기존 최첨단 방법보다 평균 96.04% 더 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 00:52:03*