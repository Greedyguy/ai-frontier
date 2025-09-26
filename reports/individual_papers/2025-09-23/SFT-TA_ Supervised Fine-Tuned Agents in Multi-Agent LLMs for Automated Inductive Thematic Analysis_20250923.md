---
keywords:
  - Thematic Analysis
  - Large Language Model
  - Supervised Fine-Tuned Agents
  - Multi-Agent System
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17167
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:21:36.861491",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Thematic Analysis",
    "Large Language Model",
    "Supervised Fine-Tuned Agents",
    "Multi-Agent System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Thematic Analysis": 0.78,
    "Large Language Model": 0.82,
    "Supervised Fine-Tuned Agents": 0.77,
    "Multi-Agent System": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Thematic Analysis",
        "canonical": "Thematic Analysis",
        "aliases": [
          "TA"
        ],
        "category": "unique_technical",
        "rationale": "Thematic Analysis is central to the paper's focus on automating qualitative methods, providing a unique technical concept for linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a foundational technology in the paper, linking to broader discussions in AI and NLP.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      },
      {
        "surface": "Supervised Fine-Tuned Agents",
        "canonical": "Supervised Fine-Tuned Agents",
        "aliases": [
          "SFT Agents"
        ],
        "category": "unique_technical",
        "rationale": "These agents are a novel aspect of the proposed framework, offering a unique technical concept for thematic analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multi-Agent System",
        "canonical": "Multi-Agent System",
        "aliases": [
          "MAS"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-Agent Systems are crucial for understanding the collaborative approach in the framework, linking to broader AI strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "baseline",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Thematic Analysis",
      "resolved_canonical": "Thematic Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Supervised Fine-Tuned Agents",
      "resolved_canonical": "Supervised Fine-Tuned Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multi-Agent System",
      "resolved_canonical": "Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SFT-TA: Supervised Fine-Tuned Agents in Multi-Agent LLMs for Automated Inductive Thematic Analysis

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17167.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17167](https://arxiv.org/abs/2509.17167)

## 🔗 유사한 논문
- [[2025-09-19/Position_ Thematic Analysis of Unstructured Clinical Transcripts with Large Language Models_20250919|Position: Thematic Analysis of Unstructured Clinical Transcripts with Large Language Models]] (82.3% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (81.8% similar)
- [[2025-09-19/Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (80.5% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (80.4% similar)
- [[2025-09-19/Judging with Many Minds_ Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge_20250919|Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent System|Multi-Agent System]]
**⚡ Unique Technical**: [[keywords/Thematic Analysis|Thematic Analysis]], [[keywords/Supervised Fine-Tuned Agents|Supervised Fine-Tuned Agents]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17167v1 Announce Type: new 
Abstract: Thematic Analysis (TA) is a widely used qualitative method that provides a structured yet flexible framework for identifying and reporting patterns in clinical interview transcripts. However, manual thematic analysis is time-consuming and limits scalability. Recent advances in LLMs offer a pathway to automate thematic analysis, but alignment with human results remains limited. To address these limitations, we propose SFT-TA, an automated thematic analysis framework that embeds supervised fine-tuned (SFT) agents within a multi-agent system. Our framework outperforms existing frameworks and the gpt-4o baseline in alignment with human reference themes. We observed that SFT agents alone may underperform, but achieve better results than the baseline when embedded within a multi-agent system. Our results highlight that embedding SFT agents in specific roles within a multi-agent system is a promising pathway to improve alignment with desired outputs for thematic analysis.

## 📝 요약

이 논문은 임상 인터뷰 전사본의 주제를 식별하고 보고하는 데 사용되는 질적 방법인 주제 분석(TA)의 자동화를 다룹니다. 기존의 수작업 주제 분석은 시간이 많이 소요되고 확장성이 제한적입니다. 이를 해결하기 위해 저자들은 감독된 미세 조정(SFT) 에이전트를 다중 에이전트 시스템에 내장한 자동화된 주제 분석 프레임워크인 SFT-TA를 제안합니다. 이 프레임워크는 기존 방법과 gpt-4o 기준보다 인간 참조 주제와의 일치도가 높습니다. SFT 에이전트 단독으로는 성능이 떨어질 수 있지만, 다중 에이전트 시스템에 내장되면 기준보다 더 나은 결과를 얻을 수 있습니다. 연구 결과는 SFT 에이전트를 특정 역할에 배치하는 것이 주제 분석의 결과 정렬을 개선하는 유망한 방법임을 보여줍니다.

## 🎯 주요 포인트

- 1. 주제 분석(TA)은 임상 인터뷰 전사에서 패턴을 식별하고 보고하는 데 널리 사용되는 질적 방법이다.
- 2. 수작업으로 진행되는 주제 분석은 시간이 많이 소요되며 확장성이 제한된다.
- 3. SFT-TA는 감독된 미세 조정(SFT) 에이전트를 다중 에이전트 시스템에 내장한 자동화된 주제 분석 프레임워크로, 인간 참조 주제와의 정렬에서 기존 프레임워크와 gpt-4o 기준선을 능가한다.
- 4. SFT 에이전트는 단독으로는 성능이 떨어질 수 있지만, 다중 에이전트 시스템에 내장될 경우 기준선보다 더 나은 결과를 얻는다.
- 5. SFT 에이전트를 다중 에이전트 시스템 내 특정 역할에 내장하는 것이 주제 분석의 원하는 출력과의 정렬을 개선하는 유망한 경로임을 강조한다.


---

*Generated on 2025-09-24 03:21:36*