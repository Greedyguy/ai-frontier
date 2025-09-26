<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:47:31.126978",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Agentic AutoSurvey",
    "Large Language Model",
    "Multi-agent System",
    "Topic Mining and Clustering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Agentic AutoSurvey": 0.78,
    "Large Language Model": 0.8,
    "Multi-agent System": 0.77,
    "Topic Mining and Clustering": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Agentic AutoSurvey",
        "canonical": "Agentic AutoSurvey",
        "aliases": [
          "AutoSurvey"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel multi-agent framework for automated survey generation, crucial for linking advancements in literature synthesis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, providing a basis for understanding the framework's application in literature surveys.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-agent framework",
        "canonical": "Multi-agent System",
        "aliases": [
          "Multi-agent architecture"
        ],
        "category": "specific_connectable",
        "rationale": "Key to the system's design, enabling the orchestration of specialized agents for improved survey generation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Topic Mining & Clustering",
        "canonical": "Topic Mining and Clustering",
        "aliases": [
          "Topic Clustering"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for organizing and synthesizing literature, enhancing the framework's effectiveness.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "system",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Agentic AutoSurvey",
      "resolved_canonical": "Agentic AutoSurvey",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-agent framework",
      "resolved_canonical": "Multi-agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Topic Mining & Clustering",
      "resolved_canonical": "Topic Mining and Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Agentic AutoSurvey: Let LLMs Survey LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18661.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18661](https://arxiv.org/abs/2509.18661)

## 🔗 유사한 논문
- [[2025-09-23/Can Agents Judge Systematic Reviews Like Humans? Evaluating SLRs with LLM-based Multi-Agent System_20250923|Can Agents Judge Systematic Reviews Like Humans? Evaluating SLRs with LLM-based Multi-Agent System]] (85.6% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (83.9% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (83.6% similar)
- [[2025-09-23/Medical AI Consensus_ A Multi-Agent Framework for Radiology Report Generation and Evaluation_20250923|Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation]] (83.4% similar)
- [[2025-09-23/XAgents_ A Framework for Interpretable Rule-Based Multi-Agents Cooperation_20250923|XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-agent System|Multi-agent System]], [[keywords/Topic Mining and Clustering|Topic Mining and Clustering]]
**⚡ Unique Technical**: [[keywords/Agentic AutoSurvey|Agentic AutoSurvey]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18661v1 Announce Type: cross 
Abstract: The exponential growth of scientific literature poses unprecedented challenges for researchers attempting to synthesize knowledge across rapidly evolving fields. We present \textbf{Agentic AutoSurvey}, a multi-agent framework for automated survey generation that addresses fundamental limitations in existing approaches. Our system employs four specialized agents (Paper Search Specialist, Topic Mining \& Clustering, Academic Survey Writer, and Quality Evaluator) working in concert to generate comprehensive literature surveys with superior synthesis quality. Through experiments on six representative LLM research topics from COLM 2024 categories, we demonstrate that our multi-agent approach achieves significant improvements over existing baselines, scoring 8.18/10 compared to AutoSurvey's 4.77/10. The multi-agent architecture processes 75--443 papers per topic (847 total across six topics) while targeting high citation coverage (often $\geq$80\% on 75--100-paper sets; lower on very large sets such as RLHF) through specialized agent orchestration. Our 12-dimension evaluation captures organization, synthesis integration, and critical analysis beyond basic metrics. These findings demonstrate that multi-agent architectures represent a meaningful advancement for automated literature survey generation in rapidly evolving scientific domains.

## 📝 요약

Agentic AutoSurvey는 과학 문헌의 급속한 증가로 인한 지식 통합의 어려움을 해결하기 위해 개발된 다중 에이전트 프레임워크입니다. 이 시스템은 논문 검색, 주제 탐색 및 군집화, 학술 조사 작성, 품질 평가를 담당하는 네 가지 전문 에이전트를 활용하여 기존 방법론의 한계를 극복하고 종합적인 문헌 조사를 생성합니다. COLM 2024의 여섯 가지 대표적인 연구 주제에 대한 실험 결과, 이 시스템은 기존의 AutoSurvey보다 높은 평가 점수(8.18/10 대 4.77/10)를 기록하며, 75~443개의 논문을 처리하면서 높은 인용 커버리지를 달성했습니다. 12차원 평가를 통해 조직, 통합, 비판적 분석에서의 개선을 입증하며, 이는 급변하는 과학 분야에서 자동화된 문헌 조사 생성에 있어 의미 있는 발전을 나타냅니다.

## 🎯 주요 포인트

- 1. Agentic AutoSurvey는 자동 설문 생성에 있어 기존 접근 방식의 근본적인 한계를 해결하기 위한 다중 에이전트 프레임워크입니다.
- 2. 이 시스템은 네 가지 전문 에이전트(논문 검색 전문가, 주제 마이닝 및 클러스터링, 학술 설문 작성자, 품질 평가자)를 활용하여 종합적인 문헌 조사를 수행합니다.
- 3. COLM 2024 카테고리의 여섯 가지 대표적인 LLM 연구 주제에 대한 실험을 통해, 다중 에이전트 접근 방식이 기존 기준보다 뛰어난 성과를 보임을 입증하였습니다.
- 4. 다중 에이전트 아키텍처는 주제당 75~443편의 논문을 처리하며, 높은 인용 범위를 목표로 합니다.
- 5. 12차원 평가를 통해 조직, 통합, 비판적 분석 등 기본 지표를 넘어서는 성과를 측정하였습니다.


---

*Generated on 2025-09-24 15:47:31*