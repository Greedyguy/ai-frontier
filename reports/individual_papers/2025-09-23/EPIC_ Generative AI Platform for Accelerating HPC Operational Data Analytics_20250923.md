---
keywords:
  - Large Language Model
  - Multimodal Learning
  - Hierarchical Multi-Agent System
  - Predictive Analytics
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16212
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:06:19.195754",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multimodal Learning",
    "Hierarchical Multi-Agent System",
    "Predictive Analytics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multimodal Learning": 0.78,
    "Hierarchical Multi-Agent System": 0.7,
    "Predictive Analytics": 0.77
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
        "rationale": "Central to the platform's architecture, facilitating query processing and reasoning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multimodal Data",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Analytics"
        ],
        "category": "specific_connectable",
        "rationale": "Key to EPIC's capability to handle diverse data types, enhancing its analytical scope.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hierarchical Multi-Agent Architecture",
        "canonical": "Hierarchical Multi-Agent System",
        "aliases": [
          "Multi-Agent Architecture"
        ],
        "category": "unique_technical",
        "rationale": "Describes the novel structural approach of EPIC, enabling dynamic task orchestration.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Predictive Analytics",
        "canonical": "Predictive Analytics",
        "aliases": [
          "Predictive Modelling"
        ],
        "category": "specific_connectable",
        "rationale": "One of the specialized agents in EPIC, crucial for forecasting and decision-making.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "operational data analytics",
      "extensive evaluations",
      "static methods"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multimodal Data",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hierarchical Multi-Agent Architecture",
      "resolved_canonical": "Hierarchical Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Predictive Analytics",
      "resolved_canonical": "Predictive Analytics",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# EPIC: Generative AI Platform for Accelerating HPC Operational Data Analytics

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16212.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16212](https://arxiv.org/abs/2509.16212)

## 🔗 유사한 논문
- [[2025-09-23/LIMI_ Less is More for Agency_20250923|LIMI: Less is More for Agency]] (80.2% similar)
- [[2025-09-23/MCTS-EP_ Empowering Embodied Planning with Online Preference Optimization_20250923|MCTS-EP: Empowering Embodied Planning with Online Preference Optimization]] (79.9% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (79.9% similar)
- [[2025-09-18/DAVIS_ Planning Agent with Knowledge Graph-Powered Inner Monologue_20250918|DAVIS: Planning Agent with Knowledge Graph-Powered Inner Monologue]] (79.5% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Predictive Analytics|Predictive Analytics]]
**⚡ Unique Technical**: [[keywords/Hierarchical Multi-Agent System|Hierarchical Multi-Agent System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16212v1 Announce Type: cross 
Abstract: We present EPIC, an AI-driven platform designed to augment operational data analytics. EPIC employs a hierarchical multi-agent architecture where a top-level large language model provides query processing, reasoning and synthesis capabilities. These capabilities orchestrate three specialized low-level agents for information retrieval, descriptive analytics, and predictive analytics. This architecture enables EPIC to perform HPC operational analytics on multi-modal data, including text, images, and tabular formats, dynamically and iteratively. EPIC addresses the limitations of existing HPC operational analytics approaches, which rely on static methods that struggle to adapt to evolving analytics tasks and stakeholder demands.
  Through extensive evaluations on the Frontier HPC system, we demonstrate that EPIC effectively handles complex queries. Using descriptive analytics as a use case, fine-tuned smaller models outperform large state-of-the-art foundation models, achieving up to 26% higher accuracy. Additionally, we achieved 19x savings in LLM operational costs compared to proprietary solutions by employing a hybrid approach that combines large foundational models with fine-tuned local open-weight models.

## 📝 요약

EPIC은 AI 기반 플랫폼으로, 운영 데이터 분석을 강화하는 데 중점을 둡니다. 이 플랫폼은 계층적 다중 에이전트 구조를 사용하여, 상위 수준의 대형 언어 모델이 쿼리 처리, 추론 및 통합 기능을 제공합니다. 이 기능은 정보 검색, 기술 분석 및 예측 분석을 담당하는 세 가지 전문 하위 에이전트를 조율합니다. EPIC은 텍스트, 이미지, 표 형식의 다중 모달 데이터를 동적으로 분석하며, 기존의 정적 방법론의 한계를 극복합니다. Frontier HPC 시스템에서의 평가를 통해 EPIC이 복잡한 쿼리를 효과적으로 처리함을 입증했으며, 기술 분석 사례에서 소형 모델이 대형 모델보다 최대 26% 높은 정확도를 보였습니다. 또한, 대형 모델과 세밀하게 조정된 로컬 모델을 결합한 하이브리드 접근법으로 운영 비용을 19배 절감했습니다.

## 🎯 주요 포인트

- 1. EPIC는 AI 기반 플랫폼으로, 계층적 다중 에이전트 아키텍처를 통해 운영 데이터 분석을 향상시킵니다.
- 2. 상위 수준의 대형 언어 모델이 쿼리 처리, 추론 및 종합 기능을 제공하여 세 가지 전문 하위 에이전트를 조율합니다.
- 3. EPIC는 텍스트, 이미지, 표 형식의 다중 모달 데이터를 동적으로 분석하여 기존의 정적 방법의 한계를 극복합니다.
- 4. Frontier HPC 시스템에서의 평가를 통해 EPIC가 복잡한 쿼리를 효과적으로 처리함을 입증했습니다.
- 5. 하이브리드 접근 방식을 통해 LLM 운영 비용을 19배 절감하면서도 높은 정확도를 달성했습니다.


---

*Generated on 2025-09-23 23:06:19*