<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:05:28.261704",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Advantage Calibration",
    "Asymmetric Clipping",
    "Mathematical Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Advantage Calibration": 0.78,
    "Asymmetric Clipping": 0.77,
    "Mathematical Reasoning": 0.8
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
        "rationale": "Large Language Models are central to the paper's discussion on reasoning capabilities, linking to broader AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Advantage Calibration",
        "canonical": "Advantage Calibration",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel mechanism introduced in the paper, crucial for converting homogeneous errors into learning signals.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Asymmetric Clipping",
        "canonical": "Asymmetric Clipping",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique technique proposed to stabilize exploration pressure, enhancing the learning process.",
        "novelty_score": 0.7,
        "connectivity_score": 0.58,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "Mathematical Reasoning",
        "canonical": "Mathematical Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The paper's focus on improving mathematical reasoning links it to specific AI tasks and benchmarks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
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
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Advantage Calibration",
      "resolved_canonical": "Advantage Calibration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Asymmetric Clipping",
      "resolved_canonical": "Asymmetric Clipping",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.58,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Mathematical Reasoning",
      "resolved_canonical": "Mathematical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# NGRPO: Negative-enhanced Group Relative Policy Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18851.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18851](https://arxiv.org/abs/2509.18851)

## 🔗 유사한 논문
- [[2025-09-23/GRPO-LEAD_ A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models_20250923|GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models]] (87.9% similar)
- [[2025-09-24/MAPO_ Mixed Advantage Policy Optimization_20250924|MAPO: Mixed Advantage Policy Optimization]] (87.4% similar)
- [[2025-09-23/GRPOformer_ Advancing Hyperparameter Optimization via Group Relative Policy Optimization_20250923|GRPOformer: Advancing Hyperparameter Optimization via Group Relative Policy Optimization]] (85.9% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (85.6% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Mathematical Reasoning|Mathematical Reasoning]]
**⚡ Unique Technical**: [[keywords/Advantage Calibration|Advantage Calibration]], [[keywords/Asymmetric Clipping|Asymmetric Clipping]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18851v1 Announce Type: cross 
Abstract: RLVR has enhanced the reasoning capabilities of Large Language Models (LLMs) across various tasks. However, GRPO, a representative RLVR algorithm, suffers from a critical limitation: when all responses within a group are either entirely correct or entirely incorrect, the model fails to learn from these homogeneous responses. This is particularly problematic for homogeneously incorrect groups, where GRPO's advantage function yields a value of zero, leading to null gradients and the loss of valuable learning signals. To overcome this issue, we propose NGRPO (Negative-enhanced Group Relative Policy Optimization), an algorithm designed to convert homogeneous errors into robust learning signals. First, NGRPO introduces Advantage Calibration. This mechanism hypothesizes the existence of a virtual maximum-reward sample during advantage calculation, thereby altering the mean and variance of rewards within a group and ensuring that the advantages for homogeneously incorrect samples are no longer zero. Second, NGRPO employs Asymmetric Clipping, which relaxes the update magnitude for positive samples while imposing stricter constraints on that of negative samples. This serves to stabilize the exploration pressure introduced by the advantage calibration. Our experiments on Qwen2.5-Math-7B demonstrate that NGRPO significantly outperforms baselines such as PPO, GRPO, DAPO, and PSR-NSR on mathematical benchmarks including MATH500, AMC23, and AIME2025. These results validate NGRPO's ability to learn from homogeneous errors, leading to stable and substantial improvements in mathematical reasoning. Our code is available at https://github.com/nangongrui-ngr/NGRPO.

## 📝 요약

RLVR는 대형 언어 모델(LLM)의 추론 능력을 향상시키지만, 대표적인 RLVR 알고리즘인 GRPO는 모든 응답이 전부 맞거나 틀린 경우 학습이 어려운 한계를 가집니다. 특히, 모두 틀린 그룹에서는 학습 신호가 사라지는 문제가 발생합니다. 이를 해결하기 위해, 우리는 NGRPO(Negative-enhanced Group Relative Policy Optimization)를 제안합니다. NGRPO는 Advantage Calibration을 도입하여 가상의 최대 보상 샘플을 가정함으로써, 틀린 샘플의 이점이 0이 되지 않도록 합니다. 또한, Asymmetric Clipping을 통해 긍정적 샘플의 업데이트를 완화하고 부정적 샘플에는 더 엄격한 제한을 가하여 안정성을 높입니다. Qwen2.5-Math-7B 실험 결과, NGRPO는 MATH500, AMC23, AIME2025 등의 수학적 벤치마크에서 기존 알고리즘보다 뛰어난 성능을 보였습니다. 이는 NGRPO가 동질적 오류로부터 효과적으로 학습할 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. GRPO 알고리즘은 모든 응답이 완전히 맞거나 틀린 경우 학습 신호를 잃는 한계가 있습니다.
- 2. NGRPO는 동질적인 오류를 강력한 학습 신호로 전환하기 위해 설계된 알고리즘입니다.
- 3. Advantage Calibration을 통해 동질적으로 틀린 샘플의 이점이 0이 되지 않도록 보장합니다.
- 4. Asymmetric Clipping을 사용하여 긍정적 샘플의 업데이트 크기를 완화하고 부정적 샘플에는 더 엄격한 제약을 가합니다.
- 5. NGRPO는 수학적 벤치마크에서 기존 알고리즘보다 우수한 성능을 보이며, 동질적 오류로부터 학습할 수 있는 능력을 입증했습니다.


---

*Generated on 2025-09-24 14:05:28*