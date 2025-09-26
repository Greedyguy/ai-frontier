---
keywords:
  - Large Language Model
  - Multi-Agent Systems
  - Rule-Based System
  - Semantic Adversarial Generation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2411.13932
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:24:10.379199",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Agent Systems",
    "Rule-Based System",
    "Semantic Adversarial Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multi-Agent Systems": 0.8,
    "Rule-Based System": 0.78,
    "Semantic Adversarial Generation": 0.7
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
        "rationale": "Large Language Models are central to the paper's discussion and connect well with existing research in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Agent Systems",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "MAS",
          "Multi-Agent System"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on multi-agent cooperation, which is a key concept for linking with other works in AI.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Rule-Based System",
        "canonical": "Rule-Based System",
        "aliases": [
          "Rule-Based Systems",
          "IF-THEN System"
        ],
        "category": "specific_connectable",
        "rationale": "Rule-based systems are crucial for the interpretability aspect of the framework, providing strong linkage to expert systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semantic Adversarial Generation",
        "canonical": "Semantic Adversarial Generation",
        "aliases": [
          "Adversarial Generation"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper, enhancing understanding of adversarial techniques in AI.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "evaluation",
      "performance"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-Agent Systems",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Rule-Based System",
      "resolved_canonical": "Rule-Based System",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semantic Adversarial Generation",
      "resolved_canonical": "Semantic Adversarial Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2411.13932.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2411.13932](https://arxiv.org/abs/2411.13932)

## 🔗 유사한 논문
- [[2025-09-23/The STAR-XAI Protocol_ An Interactive Framework for Inducing Second-Order Agency in AI Agents_20250923|The STAR-XAI Protocol: An Interactive Framework for Inducing Second-Order Agency in AI Agents]] (86.4% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (84.7% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (84.6% similar)
- [[2025-09-22/Watson_ A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents_20250922|Watson: A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents]] (84.2% similar)
- [[2025-09-18/Co-Investigator AI_ The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives_20250918|Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]], [[keywords/Rule-Based System|Rule-Based System]]
**⚡ Unique Technical**: [[keywords/Semantic Adversarial Generation|Semantic Adversarial Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.13932v2 Announce Type: replace 
Abstract: Extracting implicit knowledge and logical reasoning abilities from large language models (LLMs) has consistently been a significant challenge. The advancement of multi-agent systems has further en-hanced the capabilities of LLMs. Inspired by the structure of multi-polar neurons (MNs), we propose the XAgents framework, an in-terpretable multi-agent cooperative framework based on the IF-THEN rule-based system. The IF-Parts of the rules are responsible for logical reasoning and domain membership calculation, while the THEN-Parts are comprised of domain expert agents that generate domain-specific contents. Following the calculation of the member-ship, XAgetns transmits the task to the disparate domain rules, which subsequently generate the various responses. These re-sponses are analogous to the answers provided by different experts to the same question. The final response is reached at by eliminat-ing the hallucinations and erroneous knowledge of the LLM through membership computation and semantic adversarial genera-tion of the various domain rules. The incorporation of rule-based interpretability serves to bolster user confidence in the XAgents framework. We evaluate the efficacy of XAgents through a com-parative analysis with the latest AutoAgents, in which XAgents demonstrated superior performance across three distinct datasets. We perform post-hoc interpretable studies with SHAP algorithm and case studies, proving the interpretability of XAgent in terms of input-output feature correlation and rule-based semantics.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서 암묵적 지식 추출과 논리적 추론 능력을 향상시키기 위해 XAgents라는 해석 가능한 다중 에이전트 협력 프레임워크를 제안합니다. XAgents는 IF-THEN 규칙 기반 시스템을 활용하여 논리적 추론과 도메인 전문가 에이전트의 협력을 통해 다양한 도메인별 응답을 생성합니다. 이를 통해 LLM의 오류와 환각을 줄이고, 사용자 신뢰를 높입니다. XAgents는 최신 AutoAgents와의 비교 분석에서 세 가지 데이터셋에서 우수한 성능을 보였으며, SHAP 알고리즘과 사례 연구를 통해 해석 가능성을 입증했습니다.

## 🎯 주요 포인트

- 1. XAgents 프레임워크는 IF-THEN 규칙 기반 시스템을 활용하여 다중 에이전트 협력 구조를 제안합니다.
- 2. IF-파트는 논리적 추론과 도메인 멤버십 계산을 담당하며, THEN-파트는 도메인 전문가 에이전트가 도메인별 콘텐츠를 생성합니다.
- 3. XAgents는 멤버십 계산과 의미론적 적대 생성 과정을 통해 LLM의 오류와 환각을 제거하여 최종 응답을 도출합니다.
- 4. 규칙 기반 해석 가능성을 통해 사용자 신뢰를 강화하며, SHAP 알고리즘과 사례 연구를 통해 XAgents의 해석 가능성을 입증합니다.
- 5. 최신 AutoAgents와의 비교 분석에서 XAgents는 세 가지 서로 다른 데이터셋에서 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 00:24:10*