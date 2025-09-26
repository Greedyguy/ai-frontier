---
keywords:
  - Large Language Model
  - Radiology Report Generation
  - Multimodal Learning
  - Multi-Agent Reinforcement Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17353
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:58:48.738598",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Radiology Report Generation",
    "Multimodal Learning",
    "Multi-Agent Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Radiology Report Generation": 0.78,
    "Multimodal Learning": 0.8,
    "Multi-Agent Reinforcement Learning": 0.82
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
        "rationale": "Large Language Models are central to the framework and align with existing technical vocabularies, facilitating connections to related AI concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Radiology Report Generation",
        "canonical": "Radiology Report Generation",
        "aliases": [
          "Radiology Reporting",
          "Medical Report Generation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area of AI in healthcare, providing a unique link to medical AI research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multimodal Clinical Reasoning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Reasoning",
          "Multimodal AI"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Clinical Reasoning integrates multiple data types, which is crucial for comprehensive AI systems in healthcare.",
        "novelty_score": 0.67,
        "connectivity_score": 0.84,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-Agent Reinforcement Learning",
        "canonical": "Multi-Agent Reinforcement Learning",
        "aliases": [
          "MARL",
          "Multi-Agent RL"
        ],
        "category": "specific_connectable",
        "rationale": "This approach is key to the paper's framework, linking to advanced AI methodologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.79,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "evaluation protocols",
      "modular architecture",
      "public radiology datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Radiology Report Generation",
      "resolved_canonical": "Radiology Report Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multimodal Clinical Reasoning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.84,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-Agent Reinforcement Learning",
      "resolved_canonical": "Multi-Agent Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.79,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17353.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17353](https://arxiv.org/abs/2509.17353)

## 🔗 유사한 논문
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (85.7% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (85.3% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (84.7% similar)
- [[2025-09-23/Can Agents Judge Systematic Reviews Like Humans? Evaluating SLRs with LLM-based Multi-Agent System_20250923|Can Agents Judge Systematic Reviews Like Humans? Evaluating SLRs with LLM-based Multi-Agent System]] (84.6% similar)
- [[2025-09-17/Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models_20250917|Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Multi-Agent Reinforcement Learning|Multi-Agent Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Radiology Report Generation|Radiology Report Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17353v1 Announce Type: new 
Abstract: Automating radiology report generation poses a dual challenge: building clinically reliable systems and designing rigorous evaluation protocols. We introduce a multi-agent reinforcement learning framework that serves as both a benchmark and evaluation environment for multimodal clinical reasoning in the radiology ecosystem. The proposed framework integrates large language models (LLMs) and large vision models (LVMs) within a modular architecture composed of ten specialized agents responsible for image analysis, feature extraction, report generation, review, and evaluation. This design enables fine-grained assessment at both the agent level (e.g., detection and segmentation accuracy) and the consensus level (e.g., report quality and clinical relevance). We demonstrate an implementation using chatGPT-4o on public radiology datasets, where LLMs act as evaluators alongside medical radiologist feedback. By aligning evaluation protocols with the LLM development lifecycle, including pretraining, finetuning, alignment, and deployment, the proposed benchmark establishes a path toward trustworthy deviance-based radiology report generation.

## 📝 요약

이 논문은 방사선 보고서 자동 생성의 임상적 신뢰성과 평가 프로토콜 설계의 이중 과제를 다루고 있습니다. 저자들은 방사선 생태계에서 다중 모드 임상 추론을 위한 벤치마크 및 평가 환경으로 작용하는 다중 에이전트 강화 학습 프레임워크를 제안합니다. 이 프레임워크는 대규모 언어 모델(LLMs)과 대규모 비전 모델(LVMs)을 통합하여 이미지 분석, 특징 추출, 보고서 생성, 검토 및 평가를 담당하는 10개의 전문 에이전트로 구성된 모듈식 아키텍처를 제공합니다. 이를 통해 에이전트 수준(예: 탐지 및 세분화 정확도)과 합의 수준(예: 보고서 품질 및 임상 관련성)에서 세밀한 평가가 가능합니다. 공공 방사선 데이터셋을 사용한 구현을 통해 LLMs가 의료 방사선 전문의의 피드백과 함께 평가자로 작동하는 방식을 보여줍니다. 제안된 벤치마크는 LLM 개발 주기와 평가 프로토콜을 정렬하여 신뢰할 수 있는 방사선 보고서 생성을 위한 경로를 제시합니다.

## 🎯 주요 포인트

- 1. 방사선 보고서 생성을 자동화하기 위한 다중 에이전트 강화 학습 프레임워크를 제안합니다.
- 2. 제안된 프레임워크는 이미지 분석, 특징 추출, 보고서 생성, 검토 및 평가를 담당하는 10개의 전문 에이전트로 구성된 모듈형 아키텍처를 통합합니다.
- 3. 에이전트 수준(예: 탐지 및 세분화 정확도)과 합의 수준(예: 보고서 품질 및 임상 관련성)에서 세밀한 평가가 가능합니다.
- 4. 공공 방사선학 데이터셋에서 chatGPT-4o를 사용하여 구현을 시연하며, LLM이 의학 방사선 전문의의 피드백과 함께 평가자로 작동합니다.
- 5. 평가 프로토콜을 LLM 개발 주기와 정렬하여 신뢰할 수 있는 편차 기반 방사선 보고서 생성을 위한 경로를 설정합니다.


---

*Generated on 2025-09-23 22:58:48*