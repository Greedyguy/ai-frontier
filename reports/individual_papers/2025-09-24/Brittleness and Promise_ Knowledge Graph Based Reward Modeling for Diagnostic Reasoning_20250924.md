<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:44:56.960576",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Knowledge Graph",
    "Unified Medical Language System",
    "Reward Model",
    "Diagnostic Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Knowledge Graph": 0.89,
    "Unified Medical Language System": 0.78,
    "Reward Model": 0.82,
    "Diagnostic Reasoning": 0.79
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
        "rationale": "Central to the paper's exploration of diagnostic reasoning and reward modeling.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Knowledge Graphs",
        "canonical": "Knowledge Graph",
        "aliases": [
          "KG",
          "Knowledge Graphs"
        ],
        "category": "specific_connectable",
        "rationale": "Key to the paper's approach of integrating structured biomedical knowledge.",
        "novelty_score": 0.58,
        "connectivity_score": 0.92,
        "specificity_score": 0.78,
        "link_intent_score": 0.89
      },
      {
        "surface": "Unified Medical Language System",
        "canonical": "Unified Medical Language System",
        "aliases": [
          "UMLS"
        ],
        "category": "unique_technical",
        "rationale": "Specific knowledge graph used for biomedical knowledge representation.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reward Model",
        "canonical": "Reward Model",
        "aliases": [
          "Reward Modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Central concept for evaluating knowledge graph reasoning paths.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "Diagnostic Reasoning",
        "canonical": "Diagnostic Reasoning",
        "aliases": [
          "Clinical Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "The primary application domain for the proposed knowledge graph-based approach.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
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
      "candidate_surface": "Knowledge Graphs",
      "resolved_canonical": "Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.92,
        "specificity": 0.78,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Unified Medical Language System",
      "resolved_canonical": "Unified Medical Language System",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reward Model",
      "resolved_canonical": "Reward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Diagnostic Reasoning",
      "resolved_canonical": "Diagnostic Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Brittleness and Promise: Knowledge Graph Based Reward Modeling for Diagnostic Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18316.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18316](https://arxiv.org/abs/2509.18316)

## 🔗 유사한 논문
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (86.4% similar)
- [[2025-09-23/Evaluation of Causal Reasoning for Large Language Models in Contextualized Clinical Scenarios of Laboratory Test Interpretation_20250923|Evaluation of Causal Reasoning for Large Language Models in Contextualized Clinical Scenarios of Laboratory Test Interpretation]] (86.1% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (86.0% similar)
- [[2025-09-23/How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark_20250923|How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark]] (85.9% similar)
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (85.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Graph|Knowledge Graph]], [[keywords/Reward Model|Reward Model]]
**⚡ Unique Technical**: [[keywords/Unified Medical Language System|Unified Medical Language System]], [[keywords/Diagnostic Reasoning|Diagnostic Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18316v1 Announce Type: cross 
Abstract: Large language models (LLMs) show promise for diagnostic reasoning but often lack reliable, knowledge grounded inference. Knowledge graphs (KGs), such as the Unified Medical Language System (UMLS), offer structured biomedical knowledge that can support trustworthy reasoning. Prior approaches typically integrate KGs via retrieval augmented generation or fine tuning, inserting KG content into prompts rather than enabling structured reasoning. We explore an alternative paradigm: treating the LLM as a reward model of KG reasoning paths, where the model learns to judge whether a candidate path leads to correct diagnosis for a given patient input. This approach is inspired by recent work that leverages reward training to enhance model reasoning abilities, and grounded in computational theory, which suggests that verifying a solution is often easier than generating one from scratch. It also parallels physicians' diagnostic assessment, where they judge which sequences of findings and intermediate conditions most plausibly support a diagnosis. We first systematically evaluate five task formulation for knowledge path judging and eight training paradigm. Second, we test whether the path judging abilities generalize to downstream diagnostic tasks, including diagnosis summarization and medical question answering. Experiments with three open source instruct-tuned LLMs reveal both promise and brittleness: while specific reward optimization and distillation lead to strong path-judging performance, the transferability to downstream tasks remain weak. Our finding provides the first systematic assessment of "reward model style" reasoning over clinical KGs, offering insights into how structured, reward-based supervision influences diagnostic reasoning in GenAI systems for healthcare.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 진단 추론 능력을 향상시키기 위해 지식 그래프(KG)를 활용하는 새로운 접근 방식을 제안합니다. 기존 방법은 KG를 단순히 정보 검색이나 미세 조정에 사용했으나, 본 연구는 LLM을 KG 추론 경로의 보상 모델로 취급하여 환자 입력에 대한 올바른 진단 경로를 판단하도록 학습시킵니다. 이는 최근 보상 학습을 통한 모델 추론 능력 향상 연구에 영감을 받았으며, 의사들이 진단을 평가하는 방식과 유사합니다. 연구는 다섯 가지 작업 형식과 여덟 가지 학습 패러다임을 평가하고, 경로 판단 능력이 진단 요약 및 의료 질문 응답과 같은 하위 작업에 일반화되는지를 테스트합니다. 실험 결과, 특정 보상 최적화와 증류는 강력한 경로 판단 성능을 보였으나, 하위 작업으로의 전이 가능성은 약했습니다. 이는 임상 KG에서의 "보상 모델 스타일" 추론에 대한 체계적인 평가를 제공하며, GenAI 시스템의 진단 추론에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 진단 추론에 유망하지만 신뢰할 수 있는 지식 기반의 추론이 부족하다.
- 2. 지식 그래프(KG)는 구조화된 생물 의학 지식을 제공하여 신뢰할 수 있는 추론을 지원할 수 있다.
- 3. LLM을 KG 추론 경로의 보상 모델로 취급하여 환자 입력에 대한 올바른 진단으로 이어지는 경로를 판단하는 방식을 탐구한다.
- 4. 보상 최적화와 증류는 경로 판단 성능을 강화하지만, 하위 진단 작업으로의 전이 가능성은 약하다.
- 5. 임상 KG에 대한 "보상 모델 스타일" 추론의 체계적인 평가를 통해 GenAI 시스템의 진단 추론에 대한 통찰을 제공한다.


---

*Generated on 2025-09-24 13:44:56*