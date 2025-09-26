---
keywords:
  - Large Language Model
  - State-Update Dialogue Strategy
  - Multi-hop Question Answering
  - HotpotQA
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17766
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:08:42.188793",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "State-Update Dialogue Strategy",
    "Multi-hop Question Answering",
    "HotpotQA"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "State-Update Dialogue Strategy": 0.8,
    "Multi-hop Question Answering": 0.82,
    "HotpotQA": 0.88
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
        "rationale": "Connects to existing discussions on the challenges and advancements in language models.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "State-Update Multi-turn Dialogue Strategy",
        "canonical": "State-Update Dialogue Strategy",
        "aliases": [
          "State Reconstruction",
          "History Remind"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to multi-turn dialogue management.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-hop QA datasets",
        "canonical": "Multi-hop Question Answering",
        "aliases": [
          "Multi-hop QA"
        ],
        "category": "specific_connectable",
        "rationale": "Links to datasets and methodologies in question answering research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "HotpotQA dataset",
        "canonical": "HotpotQA",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A well-known dataset that provides context for evaluating the proposed strategy.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "State-Update Multi-turn Dialogue Strategy",
      "resolved_canonical": "State-Update Dialogue Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-hop QA datasets",
      "resolved_canonical": "Multi-hop Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "HotpotQA dataset",
      "resolved_canonical": "HotpotQA",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17766.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17766](https://arxiv.org/abs/2509.17766)

## 🔗 유사한 논문
- [[2025-09-19/Single- vs. Dual-Prompt Dialogue Generation with LLMs for Job Interviews in Human Resources_20250919|Single- vs. Dual-Prompt Dialogue Generation with LLMs for Job Interviews in Human Resources]] (86.5% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.5% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (85.4% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.1% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-hop Question Answering|Multi-hop Question Answering]], [[keywords/HotpotQA|HotpotQA]]
**⚡ Unique Technical**: [[keywords/State-Update Dialogue Strategy|State-Update Dialogue Strategy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17766v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) struggle with information forgetting and inefficiency in long-horizon, multi-turn dialogues. To address this, we propose a training-free prompt engineering method, the State-Update Multi-turn Dialogue Strategy. It utilizes "State Reconstruction" and "History Remind" mechanisms to effectively manage dialogue history. Our strategy shows strong performance across multiple multi-hop QA datasets. For instance, on the HotpotQA dataset, it improves the core information filtering score by 32.6%, leading to a 14.1% increase in the downstream QA score, while also reducing inference time by 73.1% and token consumption by 59.4%. Ablation studies confirm the pivotal roles of both components. Our work offers an effective solution for optimizing LLMs in long-range interactions, providing new insights for developing more robust Agents.

## 📝 요약

대형 언어 모델(LLM)은 긴 대화에서 정보 망각과 비효율성 문제를 겪습니다. 이를 해결하기 위해 우리는 훈련이 필요 없는 프롬프트 엔지니어링 방법인 '상태 업데이트 다중 턴 대화 전략'을 제안합니다. 이 전략은 '상태 재구성'과 '역사 상기' 메커니즘을 활용하여 대화 기록을 효과적으로 관리합니다. 우리의 전략은 여러 다중 홉 질의응답(QA) 데이터셋에서 뛰어난 성능을 보였으며, 특히 HotpotQA 데이터셋에서 핵심 정보 필터링 점수를 32.6% 향상시키고, QA 점수를 14.1% 증가시켰으며, 추론 시간을 73.1%, 토큰 소비를 59.4% 줄였습니다. 이 연구는 LLM의 장기 상호작용 최적화에 효과적인 해결책을 제공하며, 더 강력한 에이전트 개발에 새로운 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 장기 다중 턴 대화에서 정보 망각과 비효율성 문제를 겪는다.
- 2. 이를 해결하기 위해, 우리는 훈련이 필요 없는 프롬프트 엔지니어링 방법인 상태 업데이트 다중 턴 대화 전략을 제안한다.
- 3. 이 전략은 "상태 재구성"과 "역사 상기" 메커니즘을 활용하여 대화 기록을 효과적으로 관리한다.
- 4. HotpotQA 데이터셋에서 핵심 정보 필터링 점수를 32.6% 향상시키고, 다운스트림 QA 점수를 14.1% 증가시켰으며, 추론 시간은 73.1%, 토큰 소비는 59.4% 감소시켰다.
- 5. 연구 결과는 LLM의 장거리 상호작용 최적화를 위한 효과적인 솔루션을 제공하며, 더 견고한 에이전트 개발에 대한 새로운 통찰을 제시한다.


---

*Generated on 2025-09-24 00:08:42*