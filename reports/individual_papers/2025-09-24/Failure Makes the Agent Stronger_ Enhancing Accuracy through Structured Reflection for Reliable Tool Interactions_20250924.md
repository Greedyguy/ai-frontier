<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:04:56.816726",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Structured Reflection",
    "Tool-Reflection-Bench",
    "Error Recovery"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Structured Reflection": 0.72,
    "Tool-Reflection-Bench": 0.7,
    "Error Recovery": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Tool-augmented large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "Tool-augmented LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Links to existing knowledge on large language models, which are central to the paper's methodology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Structured Reflection",
        "canonical": "Structured Reflection",
        "aliases": [
          "Reflection Strategy"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to error diagnosis and repair in tool interactions, enhancing agent reliability.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Tool-Reflection-Bench",
        "canonical": "Tool-Reflection-Bench",
        "aliases": [
          "TRB"
        ],
        "category": "unique_technical",
        "rationale": "Represents a new benchmark for evaluating structured reflection, crucial for reproducibility and validation.",
        "novelty_score": 0.81,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Error Recovery",
        "canonical": "Error Recovery",
        "aliases": [
          "Failure Recovery"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on improving multi-turn tool-call success through structured reflection.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
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
      "candidate_surface": "Tool-augmented large language models",
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
      "candidate_surface": "Structured Reflection",
      "resolved_canonical": "Structured Reflection",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Tool-Reflection-Bench",
      "resolved_canonical": "Tool-Reflection-Bench",
      "decision": "linked",
      "scores": {
        "novelty": 0.81,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Error Recovery",
      "resolved_canonical": "Error Recovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18847.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18847](https://arxiv.org/abs/2509.18847)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (87.9% similar)
- [[2025-09-23/Retrieval Enhanced Feedback via In-context Neural Error-book_20250923|Retrieval Enhanced Feedback via In-context Neural Error-book]] (85.4% similar)
- [[2025-09-23/Tool Preferences in Agentic LLMs are Unreliable_20250923|Tool Preferences in Agentic LLMs are Unreliable]] (85.3% similar)
- [[2025-09-22/World Modelling Improves Language Model Agents_20250922|World Modelling Improves Language Model Agents]] (84.5% similar)
- [[2025-09-24/COLT_ Enhancing Video Large Language Models with Continual Tool Usage_20250924|COLT: Enhancing Video Large Language Models with Continual Tool Usage]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Error Recovery|Error Recovery]]
**⚡ Unique Technical**: [[keywords/Structured Reflection|Structured Reflection]], [[keywords/Tool-Reflection-Bench|Tool-Reflection-Bench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18847v1 Announce Type: cross 
Abstract: Tool-augmented large language models (LLMs) are usually trained with supervised imitation or coarse-grained reinforcement learning that optimizes single tool calls. Current self-reflection practices rely on heuristic prompts or one-way reasoning: the model is urged to 'think more' instead of learning error diagnosis and repair. This is fragile in multi-turn interactions; after a failure the model often repeats the same mistake. We propose structured reflection, which turns the path from error to repair into an explicit, controllable, and trainable action. The agent produces a short yet precise reflection: it diagnoses the failure using evidence from the previous step and then proposes a correct, executable follow-up call. For training we combine DAPO and GSPO objectives with a reward scheme tailored to tool use, optimizing the stepwise strategy Reflect, then Call, then Final. To evaluate, we introduce Tool-Reflection-Bench, a lightweight benchmark that programmatically checks structural validity, executability, parameter correctness, and result consistency. Tasks are built as mini trajectories of erroneous call, reflection, and corrected call, with disjoint train and test splits. Experiments on BFCL v3 and Tool-Reflection-Bench show large gains in multi-turn tool-call success and error recovery, and a reduction of redundant calls. These results indicate that making reflection explicit and optimizing it directly improves the reliability of tool interaction and offers a reproducible path for agents to learn from failure.

## 📝 요약

이 논문은 도구를 활용한 대형 언어 모델(LLM)의 성능 향상을 위해 구조화된 반성 메커니즘을 제안합니다. 기존의 모델들은 주로 단일 도구 호출을 최적화하는 지도 학습이나 강화 학습을 사용하며, 오류 진단과 수정을 학습하지 못해 다중 회차 상호작용에서 같은 실수를 반복하는 문제가 있습니다. 제안된 구조화된 반성은 오류에서 수정을 위한 명확하고 훈련 가능한 행동 경로를 제공합니다. 에이전트는 이전 단계의 증거를 사용해 오류를 진단하고, 올바른 후속 호출을 제안합니다. DAPO와 GSPO 목표를 결합한 보상 체계로 Reflect, Call, Final 전략을 최적화합니다. 평가를 위해 Tool-Reflection-Bench라는 벤치마크를 도입하여 구조적 유효성, 실행 가능성, 매개변수 정확성, 결과 일관성을 검사합니다. 실험 결과, 다중 회차 도구 호출 성공률과 오류 회복이 크게 향상되었으며, 불필요한 호출이 줄어들었습니다. 이는 반성을 명시적으로 하고 최적화함으로써 도구 상호작용의 신뢰성을 높이고, 실패로부터 학습할 수 있는 재현 가능한 경로를 제공함을 보여줍니다.

## 🎯 주요 포인트

- 1. 도구를 활용한 대형 언어 모델(LLM)은 현재 단일 도구 호출을 최적화하는 감독 모방 학습이나 대략적인 강화 학습으로 훈련된다.
- 2. 기존의 자기 반성 방식은 모델이 오류 진단과 수정을 배우기보다는 '더 깊이 생각하라'는 식의 일방적인 추론에 의존한다.
- 3. 구조화된 반성을 제안하여 오류에서 수리로 가는 경로를 명시적이고 통제 가능하며 훈련 가능한 행동으로 전환한다.
- 4. Tool-Reflection-Bench라는 경량 벤치마크를 도입하여 구조적 유효성, 실행 가능성, 매개변수 정확성 및 결과 일관성을 프로그램적으로 검사한다.
- 5. BFCL v3와 Tool-Reflection-Bench 실험에서 다중 턴 도구 호출 성공과 오류 회복에서 큰 향상을 보였으며, 중복 호출이 감소했다.


---

*Generated on 2025-09-24 14:04:56*