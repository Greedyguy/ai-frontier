---
keywords:
  - Large Language Model
  - Chain-of-Thought Prompting
  - Structured Reasoning Templates
  - Function Calling
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18076
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:05:20.658349",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Prompting",
    "Structured Reasoning Templates",
    "Function Calling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought Prompting": 0.8,
    "Structured Reasoning Templates": 0.78,
    "Function Calling": 0.77
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving interaction capabilities, linking to broader AI discussions.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought prompting",
        "canonical": "Chain-of-Thought Prompting",
        "aliases": [
          "CoT prompting"
        ],
        "category": "unique_technical",
        "rationale": "A specific technique discussed for enhancing reasoning, relevant for linking to prompting strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "structured reasoning templates",
        "canonical": "Structured Reasoning Templates",
        "aliases": [
          "reasoning templates"
        ],
        "category": "unique_technical",
        "rationale": "Introduced as a novel framework in the paper, important for linking to structured reasoning methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "function calling",
        "canonical": "Function Calling",
        "aliases": [
          "function call"
        ],
        "category": "specific_connectable",
        "rationale": "Key aspect of the paper's methodology, relevant for linking to programming and AI interaction topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "tool-use errors",
      "real-world applications"
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
      "candidate_surface": "Chain-of-Thought prompting",
      "resolved_canonical": "Chain-of-Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "structured reasoning templates",
      "resolved_canonical": "Structured Reasoning Templates",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "function calling",
      "resolved_canonical": "Function Calling",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18076.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18076](https://arxiv.org/abs/2509.18076)

## 🔗 유사한 논문
- [[2025-09-17/THOR_ Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning_20250917|THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (88.1% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (88.0% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (87.9% similar)
- [[2025-09-23/Roundtable Policy_ Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs_20250923|Roundtable Policy: Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs]] (87.7% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (87.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Function Calling|Function Calling]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Prompting|Chain-of-Thought Prompting]], [[keywords/Structured Reasoning Templates|Structured Reasoning Templates]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18076v1 Announce Type: new 
Abstract: Large language models (LLMs) have demonstrated strong reasoning and tool-use capabilities, yet they often fail in real-world tool-interactions due to incorrect parameterization, poor tool selection, or misinterpretation of user intent. These issues often stem from an incomplete understanding of user goals and inadequate comprehension of tool documentation. While Chain-of-Thought (CoT) prompting has proven effective for enhancing reasoning in general contexts, our analysis reveals that free-form CoT is insufficient and sometimes counterproductive for structured function-calling tasks. To address this, we introduce a curriculum-inspired framework that leverages structured reasoning templates to guide LLMs through more deliberate step-by-step instructions for generating function callings. Experimental results show that our method reduces tool-use errors, achieving 3-12% relative improvements over strong baselines across diverse model series and approaches. Moreover, our framework enhances the robustness, interpretability, and transparency of tool-using agents, advancing the development of more reliable AI assistants for real-world applications.

## 📝 요약

대형 언어 모델(LLM)은 강력한 추론 및 도구 사용 능력을 보이지만, 실제 도구 상호작용에서는 종종 실패합니다. 이는 사용자 목표의 불완전한 이해와 도구 문서의 부적절한 해석에서 비롯됩니다. 일반적인 추론 향상에 효과적인 연쇄적 사고(Chain-of-Thought, CoT) 기법은 구조화된 함수 호출 작업에서는 충분하지 않습니다. 이를 해결하기 위해, 우리는 구조화된 추론 템플릿을 활용한 커리큘럼 기반 프레임워크를 제안합니다. 이 방법은 단계별 지침을 통해 LLM의 함수 호출 생성 오류를 줄이며, 다양한 모델에서 3-12%의 상대적 개선을 보였습니다. 또한, 이 프레임워크는 도구 사용 에이전트의 견고성, 해석 가능성, 투명성을 향상시켜 실세계 응용을 위한 보다 신뢰할 수 있는 AI 비서 개발에 기여합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 강력한 추론 및 도구 사용 능력을 보이지만, 실제 도구 상호작용에서는 종종 실패한다.
- 2. 이러한 실패는 사용자 목표의 불완전한 이해와 도구 문서의 불충분한 이해에서 비롯된다.
- 3. 일반적인 문맥에서의 추론을 향상시키기 위해 사용되는 Chain-of-Thought(COT) 프롬프트는 구조화된 함수 호출 작업에서는 충분하지 않다.
- 4. 구조화된 추론 템플릿을 활용한 커리큘럼 기반 프레임워크를 도입하여 LLM의 함수 호출 생성 과정을 단계별로 안내한다.
- 5. 제안된 방법은 도구 사용 오류를 줄이고, 다양한 모델 시리즈와 접근법에서 3-12%의 상대적 개선을 달성한다.


---

*Generated on 2025-09-23 23:05:20*