---
keywords:
  - Large Language Model
  - Dynamics Modelling
  - Self-Verification Sampling
  - Tool Use in Language Models
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.02918
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:39:01.793334",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Dynamics Modelling",
    "Self-Verification Sampling",
    "Tool Use in Language Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Dynamics Modelling": 0.78,
    "Self-Verification Sampling": 0.77,
    "Tool Use in Language Models": 0.72
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
        "rationale": "Central to the paper's focus on enhancing language model capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "dynamics modelling",
        "canonical": "Dynamics Modelling",
        "aliases": [
          "DyMo"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "self-verification sampling",
        "canonical": "Self-Verification Sampling",
        "aliases": [
          "SVS"
        ],
        "category": "unique_technical",
        "rationale": "Represents a unique technique proposed in the paper for improving model reliability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "tool use",
        "canonical": "Tool Use in Language Models",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Highlights the application focus of the paper, connecting to broader research on LLM applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "stateful environments",
      "test-time compute strategies",
      "future states"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "dynamics modelling",
      "resolved_canonical": "Dynamics Modelling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "self-verification sampling",
      "resolved_canonical": "Self-Verification Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "tool use",
      "resolved_canonical": "Tool Use in Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# World Modelling Improves Language Model Agents

**Korean Title:** 세계 모델링이 언어 모델 에이전트를 개선한다

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.02918.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.02918](https://arxiv.org/abs/2506.02918)

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (85.6% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.4% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (84.9% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (84.8% similar)
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models: A Survey]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Dynamics Modelling|Dynamics Modelling]], [[keywords/Self-Verification Sampling|Self-Verification Sampling]]
**🚀 Evolved Concepts**: [[keywords/Tool Use in Language Models|Tool Use in Language Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02918v2 Announce Type: replace 
Abstract: Tool use in stateful environments presents unique challenges for large language models (LLMs), where existing test-time compute strategies relying on repeated trials in the environment are impractical. We propose dynamics modelling (DyMo), a method that augments LLMs with a state prediction capability alongside function calling during post-training. This enables LLMs to predict the future states of their actions through an internal environment model. On the Berkeley Function Calling Leaderboard V2, DyMo improves success rates and significantly reduces hallucinations. We further integrate the internal environment model into self-verification sampling (SVS), and show that this substantially improves pass^k over number of trials k, and allows the model to refuse unreliable outputs. Together, DyMo and SVS greatly enhance the effectiveness and reliability of LLMs for tool use. We believe this work charts a path towards scalable planning RL methods for LLM inference without repeatedly querying the oracle environment.

## 🔍 Abstract (한글 번역)

arXiv:2506.02918v2 발표 유형: 교체  
초록: 상태 기반 환경에서의 도구 사용은 대형 언어 모델(LLMs)에게 독특한 도전을 제시하며, 환경에서 반복적인 시험에 의존하는 기존의 테스트 시점 계산 전략은 비현실적입니다. 우리는 후훈련 동안 함수 호출과 함께 상태 예측 기능을 LLM에 추가하는 방법인 동적 모델링(DyMo)을 제안합니다. 이를 통해 LLM은 내부 환경 모델을 통해 자신의 행동의 미래 상태를 예측할 수 있습니다. Berkeley Function Calling Leaderboard V2에서 DyMo는 성공률을 향상시키고 환각을 크게 줄입니다. 우리는 또한 내부 환경 모델을 자기 검증 샘플링(SVS)에 통합하여, 이것이 시험 횟수 k에 대한 pass^k를 상당히 향상시키고 모델이 신뢰할 수 없는 출력을 거부할 수 있게 함을 보여줍니다. DyMo와 SVS는 도구 사용을 위한 LLM의 효과성과 신뢰성을 크게 향상시킵니다. 우리는 이 연구가 오라클 환경을 반복적으로 쿼리하지 않고 LLM 추론을 위한 확장 가능한 계획 강화 학습(RL) 방법으로 나아가는 길을 제시한다고 믿습니다.

## 📝 요약

이 논문은 상태가 변하는 환경에서 도구를 사용하는 대형 언어 모델(LLM)의 문제를 해결하기 위해 DyMo라는 방법론을 제안합니다. DyMo는 훈련 후 상태 예측 기능을 추가하여 LLM이 내부 환경 모델을 통해 미래 상태를 예측할 수 있도록 합니다. 이를 통해 Berkeley Function Calling Leaderboard V2에서 성공률을 높이고 환각 현상을 줄였습니다. 또한, 내부 환경 모델을 자체 검증 샘플링(SVS)과 통합하여 신뢰할 수 없는 출력을 거부하고 여러 시도에서 성능을 개선했습니다. 이 연구는 LLM 추론을 위한 확장 가능한 계획 강화 학습(RL) 방법의 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. DyMo는 LLMs에 상태 예측 기능을 추가하여 도구 사용 시 미래 상태를 예측할 수 있게 합니다.
- 2. Berkeley Function Calling Leaderboard V2에서 DyMo는 성공률을 높이고 환각 현상을 크게 줄입니다.
- 3. DyMo와 SVS의 통합은 신뢰할 수 없는 출력을 거부할 수 있게 하여 LLMs의 신뢰성을 향상시킵니다.
- 4. 본 연구는 반복적인 환경 쿼리 없이 LLM 추론을 위한 확장 가능한 계획 RL 방법의 가능성을 제시합니다.


---

*Generated on 2025-09-23 09:39:01*