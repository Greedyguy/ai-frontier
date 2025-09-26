---
keywords:
  - Systematic Literature Review
  - Large Language Model
  - PRISMA Guideline
  - Natural Language Processing
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17240
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:57:36.031489",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Systematic Literature Review",
    "Large Language Model",
    "PRISMA Guideline",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Systematic Literature Review": 0.8,
    "Large Language Model": 0.9,
    "PRISMA Guideline": 0.7,
    "Natural Language Processing": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Systematic Literature Reviews",
        "canonical": "Systematic Literature Review",
        "aliases": [
          "SLR",
          "Systematic Review"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, offering a unique perspective on automating review processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "LLM-based Multi-Agent System",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Multi-Agent System"
        ],
        "category": "broad_technical",
        "rationale": "Combines known concepts to introduce a novel application in systematic reviews.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "PRISMA guidelines",
        "canonical": "PRISMA Guideline",
        "aliases": [
          "Preferred Reporting Items for Systematic Reviews and Meta-Analyses"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding the structured evaluation framework used in the study.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "NLP-driven systems",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "Highlights the role of NLP in automating and enhancing systematic review processes.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "protocol validation",
      "methodological assessment",
      "topic relevance checks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Systematic Literature Reviews",
      "resolved_canonical": "Systematic Literature Review",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LLM-based Multi-Agent System",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "PRISMA guidelines",
      "resolved_canonical": "PRISMA Guideline",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "NLP-driven systems",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Can Agents Judge Systematic Reviews Like Humans? Evaluating SLRs with LLM-based Multi-Agent System

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17240.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17240](https://arxiv.org/abs/2509.17240)

## 🔗 유사한 논문
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (83.3% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (82.9% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (82.8% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (82.6% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/PRISMA Guideline|PRISMA Guideline]]
**⚡ Unique Technical**: [[keywords/Systematic Literature Review|Systematic Literature Review]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17240v1 Announce Type: new 
Abstract: Systematic Literature Reviews (SLRs) are foundational to evidence-based research but remain labor-intensive and prone to inconsistency across disciplines. We present an LLM-based SLR evaluation copilot built on a Multi-Agent System (MAS) architecture to assist researchers in assessing the overall quality of the systematic literature reviews. The system automates protocol validation, methodological assessment, and topic relevance checks using a scholarly database. Unlike conventional single-agent methods, our design integrates a specialized agentic approach aligned with PRISMA guidelines to support more structured and interpretable evaluations. We conducted an initial study on five published SLRs from diverse domains, comparing system outputs to expert-annotated PRISMA scores, and observed 84% agreement. While early results are promising, this work represents a first step toward scalable and accurate NLP-driven systems for interdisciplinary workflows and reveals their capacity for rigorous, domain-agnostic knowledge aggregation to streamline the review process.

## 📝 요약

이 논문은 체계적 문헌 검토(SLR)의 품질 평가를 돕기 위한 LLM 기반의 평가 보조 시스템을 제안합니다. 이 시스템은 다중 에이전트 시스템(MAS) 아키텍처를 사용하여 프로토콜 검증, 방법론 평가, 주제 관련성 검사를 자동화합니다. PRISMA 지침에 맞춘 전문 에이전트 접근 방식을 통합하여 구조적이고 해석 가능한 평가를 지원합니다. 다양한 분야의 SLR 5건을 대상으로 한 초기 연구에서 전문가가 주석을 단 PRISMA 점수와 84%의 일치를 보였습니다. 이 연구는 NLP 기반 시스템의 확장 가능성과 정확성을 향상시키고, 분야에 구애받지 않는 지식 집계를 통해 검토 과정을 간소화할 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 체계적 문헌 검토(SLR)는 증거 기반 연구에 필수적이지만, 여전히 많은 노동이 필요하고 분야 간 일관성이 부족하다.
- 2. 우리는 다중 에이전트 시스템(MAS) 아키텍처를 기반으로 한 LLM 기반 SLR 평가 보조 시스템을 제안하여 연구자들이 문헌 검토의 전반적인 품질을 평가할 수 있도록 지원한다.
- 3. 이 시스템은 학술 데이터베이스를 활용하여 프로토콜 검증, 방법론 평가 및 주제 관련성 검사를 자동화한다.
- 4. 초기 연구에서 다양한 분야의 5개 SLR에 대해 시스템 출력과 전문가 주석 PRISMA 점수를 비교한 결과, 84%의 일치율을 보였다.
- 5. 이 연구는 학제 간 워크플로우를 위한 확장 가능하고 정확한 NLP 기반 시스템을 개발하기 위한 첫 단계로, 검토 과정을 간소화하는 데 기여할 수 있다.


---

*Generated on 2025-09-23 22:57:36*