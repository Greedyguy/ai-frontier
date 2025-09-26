---
keywords:
  - Transformer
  - Large Language Model
  - Context Engineering
  - Multi-step Reasoning
  - Progressive Multi-task Training
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18091
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:20:48.476585",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Large Language Model",
    "Context Engineering",
    "Multi-step Reasoning",
    "Progressive Multi-task Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Large Language Model": 0.8,
    "Context Engineering": 0.78,
    "Multi-step Reasoning": 0.77,
    "Progressive Multi-task Training": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are foundational to the proposed framework and connect with existing knowledge on neural architectures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's theme and link to broader discussions on model architectures.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Context Engineering",
        "canonical": "Context Engineering",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel mechanism proposed in the paper, crucial for understanding the framework's innovation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-step Reasoning",
        "canonical": "Multi-step Reasoning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is pivotal to the paper's methodology, offering a new approach to model refinement.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Progressive Multi-task Training",
        "canonical": "Progressive Multi-task Training",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduced as a key innovation, it enhances model training and supervision, linking to advanced training techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Context Engineering",
      "resolved_canonical": "Context Engineering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-step Reasoning",
      "resolved_canonical": "Multi-step Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Progressive Multi-task Training",
      "resolved_canonical": "Progressive Multi-task Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# OnePiece: Bringing Context Engineering and Reasoning to Industrial Cascade Ranking System

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18091.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18091](https://arxiv.org/abs/2509.18091)

## 🔗 유사한 논문
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (81.3% similar)
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (80.5% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (80.2% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (80.2% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Context Engineering|Context Engineering]], [[keywords/Multi-step Reasoning|Multi-step Reasoning]], [[keywords/Progressive Multi-task Training|Progressive Multi-task Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18091v1 Announce Type: cross 
Abstract: Despite the growing interest in replicating the scaled success of large language models (LLMs) in industrial search and recommender systems, most existing industrial efforts remain limited to transplanting Transformer architectures, which bring only incremental improvements over strong Deep Learning Recommendation Models (DLRMs). From a first principle perspective, the breakthroughs of LLMs stem not only from their architectures but also from two complementary mechanisms: context engineering, which enriches raw input queries with contextual cues to better elicit model capabilities, and multi-step reasoning, which iteratively refines model outputs through intermediate reasoning paths. However, these two mechanisms and their potential to unlock substantial improvements remain largely underexplored in industrial ranking systems.
  In this paper, we propose OnePiece, a unified framework that seamlessly integrates LLM-style context engineering and reasoning into both retrieval and ranking models of industrial cascaded pipelines. OnePiece is built on a pure Transformer backbone and further introduces three key innovations: (1) structured context engineering, which augments interaction history with preference and scenario signals and unifies them into a structured tokenized input sequence for both retrieval and ranking; (2) block-wise latent reasoning, which equips the model with multi-step refinement of representations and scales reasoning bandwidth via block size; (3) progressive multi-task training, which leverages user feedback chains to effectively supervise reasoning steps during training. OnePiece has been deployed in the main personalized search scenario of Shopee and achieves consistent online gains across different key business metrics, including over $+2\%$ GMV/UU and a $+2.90\%$ increase in advertising revenue.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 성공을 산업 검색 및 추천 시스템에 적용하려는 시도에서 기존의 한계를 극복하기 위해 제안된 OnePiece라는 통합 프레임워크를 소개합니다. 주요 기여는 LLM 스타일의 문맥 엔지니어링과 다단계 추론을 산업용 랭킹 시스템에 통합하는 것입니다. OnePiece는 Transformer 기반 구조를 사용하며, 세 가지 혁신을 도입합니다: (1) 구조화된 문맥 엔지니어링으로 상호작용 이력을 선호도 및 시나리오 신호와 함께 구조화된 입력 시퀀스로 통합, (2) 블록 단위의 잠재 추론으로 표현의 다단계 정제를 가능하게 하고 추론 대역폭을 확장, (3) 점진적 다중 과제 학습으로 사용자 피드백을 활용해 훈련 중 추론 단계를 효과적으로 감독합니다. 이 프레임워크는 Shopee의 개인화된 검색 시나리오에 적용되어 주요 비즈니스 지표에서 일관된 성과 향상을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 성공을 산업 검색 및 추천 시스템에 적용하려는 시도가 증가하고 있으나, 대부분의 기존 산업적 노력은 Transformer 아키텍처의 이식에 국한되어 있다.
- 2. LLM의 혁신은 아키텍처뿐만 아니라 맥락 엔지니어링과 다단계 추론이라는 두 가지 보완 메커니즘에서 비롯된다.
- 3. OnePiece는 LLM 스타일의 맥락 엔지니어링과 추론을 산업적 순위 시스템의 검색 및 순위 모델에 통합하는 통합 프레임워크를 제안한다.
- 4. OnePiece는 구조화된 맥락 엔지니어링, 블록 단위 잠재 추론, 점진적 다중 작업 훈련이라는 세 가지 주요 혁신을 도입한다.
- 5. OnePiece는 Shopee의 개인화된 검색 시나리오에 배치되어 다양한 주요 비즈니스 지표에서 일관된 온라인 성과 향상을 달성했다.


---

*Generated on 2025-09-24 00:20:48*