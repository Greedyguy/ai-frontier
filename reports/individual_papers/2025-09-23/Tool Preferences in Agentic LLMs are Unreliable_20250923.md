---
keywords:
  - Large Language Model
  - Model Context Protocol
  - Tool Description Optimization
  - Agentic Large Language Models
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.18135
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:26:20.156560",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Model Context Protocol",
    "Tool Description Optimization",
    "Agentic Large Language Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Model Context Protocol": 0.78,
    "Tool Description Optimization": 0.8,
    "Agentic Large Language Models": 0.77
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
        "rationale": "Central to the paper's discussion, linking to advancements in AI and NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Context Protocol",
        "canonical": "Model Context Protocol",
        "aliases": [
          "MCP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a specific protocol crucial for tool interaction in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Tool Descriptions",
        "canonical": "Tool Description Optimization",
        "aliases": [
          "Tool Descriptions"
        ],
        "category": "specific_connectable",
        "rationale": "Focuses on how tool descriptions impact LLM tool usage, a key insight for developers.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Agentic LLMs",
        "canonical": "Agentic Large Language Models",
        "aliases": [
          "Agentic LLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents a new concept in LLMs acting as autonomous agents.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "experiments",
      "usage",
      "developers"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Model Context Protocol",
      "resolved_canonical": "Model Context Protocol",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Tool Descriptions",
      "resolved_canonical": "Tool Description Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Agentic LLMs",
      "resolved_canonical": "Agentic Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Tool Preferences in Agentic LLMs are Unreliable

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18135.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.18135](https://arxiv.org/abs/2505.18135)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.9% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.2% similar)
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (83.4% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.3% similar)
- [[2025-09-22/World Modelling Improves Language Model Agents_20250922|World Modelling Improves Language Model Agents]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Tool Description Optimization|Tool Description Optimization]]
**⚡ Unique Technical**: [[keywords/Model Context Protocol|Model Context Protocol]]
**🚀 Evolved Concepts**: [[keywords/Agentic Large Language Models|Agentic Large Language Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18135v2 Announce Type: replace 
Abstract: Large language models (LLMs) can now access a wide range of external tools, thanks to the Model Context Protocol (MCP). This greatly expands their abilities as various agents. However, LLMs rely entirely on the text descriptions of tools to decide which ones to use--a process that is surprisingly fragile. In this work, we expose a vulnerability in prevalent tool/function-calling protocols by investigating a series of edits to tool descriptions, some of which can drastically increase a tool's usage from LLMs when competing with alternatives. Through controlled experiments, we show that tools with properly edited descriptions receive over 10 times more usage from GPT-4.1 and Qwen2.5-7B than tools with original descriptions. We further evaluate how various edits to tool descriptions perform when competing directly with one another and how these trends generalize or differ across a broader set of 17 different models. These phenomena, while giving developers a powerful way to promote their tools, underscore the need for a more reliable foundation for agentic LLMs to select and utilize tools and resources. Our code is publicly available at https://github.com/kazemf78/llm-unreliable-tool-preferences.

## 📝 요약

이 논문은 Model Context Protocol(MCP)을 통해 대형 언어 모델(LLM)이 외부 도구에 접근할 수 있게 되면서 발생하는 취약성을 다룹니다. LLM은 도구의 텍스트 설명에 의존하여 사용할 도구를 선택하는데, 이는 매우 불안정한 과정입니다. 연구는 도구 설명을 편집함으로써 LLM의 도구 사용 빈도가 크게 증가할 수 있음을 보여줍니다. 실험 결과, 적절히 편집된 도구 설명은 GPT-4.1과 Qwen2.5-7B에서 원래 설명보다 10배 이상의 사용 빈도를 기록했습니다. 이러한 현상은 도구 개발자에게 유용할 수 있지만, LLM이 도구를 선택하고 활용하는 데 있어 더 신뢰할 수 있는 기반이 필요함을 강조합니다. 연구의 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. Model Context Protocol (MCP)를 통해 대형 언어 모델(LLMs)이 다양한 외부 도구에 접근할 수 있게 되면서 그 기능이 크게 확장되었습니다.
- 2. LLMs는 도구의 텍스트 설명에 전적으로 의존하여 사용할 도구를 결정하는데, 이는 예상 외로 취약한 과정입니다.
- 3. 도구 설명을 적절히 편집하면 GPT-4.1과 Qwen2.5-7B에서 해당 도구의 사용 빈도가 10배 이상 증가할 수 있습니다.
- 4. 다양한 모델에서 도구 설명 편집이 어떻게 작용하는지 평가한 결과, 개발자에게 도구를 홍보할 수 있는 강력한 방법을 제공하지만, LLMs가 도구를 선택하고 활용하는 더 신뢰할 수 있는 기반이 필요함을 강조합니다.
- 5. 연구의 코드는 공개되어 있으며, 다양한 모델에서의 도구 설명 편집 효과를 일반화하거나 차별화하는 경향을 분석했습니다.


---

*Generated on 2025-09-24 00:26:20*