---
keywords:
  - Large Language Model
  - Multimodal Learning
  - Financial Trading Systems
  - Investment Strategy Development
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2507.20474
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:22:13.673774",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multimodal Learning",
    "Financial Trading Systems",
    "Investment Strategy Development"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multimodal Learning": 0.82,
    "Financial Trading Systems": 0.71,
    "Investment Strategy Development": 0.68
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
        "rationale": "Large Language Models are central to the system's ability to process multi-modal data, making them a key technical component.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "multi-modal data",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multi-modal",
          "multi-modal learning"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is crucial for integrating diverse data types in the system, enhancing its interpretability and adaptability.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "financial trading",
        "canonical": "Financial Trading Systems",
        "aliases": [
          "trading systems",
          "financial systems"
        ],
        "category": "unique_technical",
        "rationale": "The focus on financial trading systems highlights the unique application of the technology in a specific domain.",
        "novelty_score": 0.65,
        "connectivity_score": 0.67,
        "specificity_score": 0.78,
        "link_intent_score": 0.71
      },
      {
        "surface": "investment strategies",
        "canonical": "Investment Strategy Development",
        "aliases": [
          "investment strategies",
          "strategy development"
        ],
        "category": "unique_technical",
        "rationale": "Investment Strategy Development is a unique aspect of the system's application, focusing on actionable financial insights.",
        "novelty_score": 0.62,
        "connectivity_score": 0.73,
        "specificity_score": 0.76,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "interpretability",
      "real-time analysis"
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
      "candidate_surface": "multi-modal data",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "financial trading",
      "resolved_canonical": "Financial Trading Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.67,
        "specificity": 0.78,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "investment strategies",
      "resolved_canonical": "Investment Strategy Development",
      "decision": "linked",
      "scores": {
        "novelty": 0.62,
        "connectivity": 0.73,
        "specificity": 0.76,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# MountainLion: A Multi-Modal LLM-Based Agent System for Interpretable and Adaptive Financial Trading

**Korean Title:** 마운틴라이언: 해석 가능하고 적응적인 금융 거래를 위한 다중 모드 LLM 기반 에이전트 시스템

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.20474.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2507.20474](https://arxiv.org/abs/2507.20474)

## 🔗 유사한 논문
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA: A multi-agent framework for annotation]] (80.6% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (80.6% similar)
- [[2025-09-18/From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions: A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (80.1% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (80.0% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Financial Trading Systems|Financial Trading Systems]], [[keywords/Investment Strategy Development|Investment Strategy Development]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.20474v3 Announce Type: replace-cross 
Abstract: Cryptocurrency trading is a challenging task requiring the integration of heterogeneous data from multiple modalities. Traditional deep learning and reinforcement learning approaches typically demand large training datasets and encode diverse inputs into numerical representations, often at the cost of interpretability. Recent progress in large language model (LLM)-based agents has demonstrated the capacity to process multi-modal data and support complex investment decision-making. Building on these advances, we present \textbf{MountainLion}, a multi-modal, multi-agent system for financial trading that coordinates specialized LLM-based agents to interpret financial data and generate investment strategies. MountainLion processes textual news, candlestick charts, and trading signal charts to produce high-quality financial reports, while also enabling modification of reports and investment recommendations through data-driven user interaction and question answering. A central reflection module analyzes historical trading signals and outcomes to continuously refine decision processes, and the system is capable of real-time report analysis, summarization, and dynamic adjustment of investment strategies. Empirical results confirm that MountainLion systematically enriches technical price triggers with contextual macroeconomic and capital flow signals, providing a more interpretable, robust, and actionable investment framework that improves returns and strengthens investor confidence.

## 🔍 Abstract (한글 번역)

arXiv:2507.20474v3 발표 유형: 교차 교체  
요약: 암호화폐 거래는 여러 모달리티에서 이질적인 데이터를 통합해야 하는 도전적인 작업입니다. 전통적인 딥러닝 및 강화 학습 접근법은 일반적으로 대규모 학습 데이터셋을 요구하며, 다양한 입력을 수치 표현으로 인코딩하는 과정에서 해석 가능성을 종종 희생합니다. 최근 대형 언어 모델(LLM) 기반 에이전트의 발전은 다중 모달 데이터를 처리하고 복잡한 투자 의사 결정을 지원할 수 있는 능력을 보여주었습니다. 이러한 발전을 바탕으로, 우리는 금융 거래를 위한 다중 모달, 다중 에이전트 시스템인 \textbf{MountainLion}을 소개합니다. 이 시스템은 금융 데이터를 해석하고 투자 전략을 생성하기 위해 특화된 LLM 기반 에이전트를 조정합니다. MountainLion은 텍스트 뉴스, 캔들스틱 차트, 거래 신호 차트를 처리하여 고품질의 금융 보고서를 생성하며, 데이터 기반 사용자 상호작용 및 질문 응답을 통해 보고서 및 투자 추천을 수정할 수 있도록 합니다. 중앙 반영 모듈은 과거 거래 신호와 결과를 분석하여 의사 결정 과정을 지속적으로 개선하며, 시스템은 실시간 보고서 분석, 요약 및 투자 전략의 동적 조정이 가능합니다. 실증 결과에 따르면 MountainLion은 기술적 가격 트리거를 맥락적 거시경제 및 자본 흐름 신호로 체계적으로 풍부하게 하여, 해석 가능하고 견고하며 실행 가능한 투자 프레임워크를 제공함으로써 수익을 개선하고 투자자의 신뢰를 강화합니다.

## 📝 요약

학술 논문은 암호화폐 거래를 위한 다중 모달, 다중 에이전트 시스템인 MountainLion을 소개합니다. 이 시스템은 대형 언어 모델(LLM) 기반 에이전트를 활용하여 금융 데이터를 해석하고 투자 전략을 생성합니다. MountainLion은 텍스트 뉴스, 캔들스틱 차트, 거래 신호 차트를 처리하여 고품질의 금융 보고서를 생성하며, 사용자와의 상호작용을 통해 보고서와 투자 권고안을 수정할 수 있습니다. 중앙 반영 모듈은 과거 거래 신호와 결과를 분석하여 의사 결정 과정을 지속적으로 개선합니다. 실험 결과, MountainLion은 기술적 가격 신호를 거시경제 및 자본 흐름 신호와 결합하여 해석 가능하고 실행 가능한 투자 프레임워크를 제공하며, 투자 수익을 향상시키고 투자자의 신뢰를 강화하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. MountainLion은 LLM 기반 에이전트를 활용하여 금융 데이터를 해석하고 투자 전략을 생성하는 다중 모달, 다중 에이전트 시스템입니다.
- 2. 이 시스템은 텍스트 뉴스, 캔들스틱 차트, 거래 신호 차트를 처리하여 고품질의 금융 보고서를 생성합니다.
- 3. 중앙 반영 모듈은 과거 거래 신호와 결과를 분석하여 의사 결정 과정을 지속적으로 개선합니다.
- 4. MountainLion은 실시간 보고서 분석, 요약 및 투자 전략의 동적 조정을 지원합니다.
- 5. 실증 결과에 따르면, MountainLion은 기술적 가격 신호를 거시 경제 및 자본 흐름 신호와 결합하여 더 해석 가능하고 실행 가능한 투자 프레임워크를 제공합니다.


---

*Generated on 2025-09-23 11:22:13*