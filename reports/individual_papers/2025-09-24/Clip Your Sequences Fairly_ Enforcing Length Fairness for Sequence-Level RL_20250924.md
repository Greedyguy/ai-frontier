<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:41:07.876551",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fair Sequence Policy Optimization",
    "Large Language Model",
    "Length Fairness",
    "Importance Sampling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fair Sequence Policy Optimization": 0.8,
    "Large Language Model": 0.85,
    "Length Fairness": 0.78,
    "Importance Sampling": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FSPO",
        "canonical": "Fair Sequence Policy Optimization",
        "aliases": [
          "FSPO"
        ],
        "category": "unique_technical",
        "rationale": "FSPO is a novel method introduced in the paper, providing a unique approach to sequence-level reinforcement learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on sequence-level reinforcement learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Length Fairness",
        "canonical": "Length Fairness",
        "aliases": [
          "Length Reweighting"
        ],
        "category": "unique_technical",
        "rationale": "Length Fairness is a key concept introduced to address optimization issues in sequence-level reinforcement learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Importance Sampling",
        "canonical": "Importance Sampling",
        "aliases": [
          "IS"
        ],
        "category": "specific_connectable",
        "rationale": "Importance Sampling is a fundamental technique used in the proposed FSPO method, crucial for understanding its implementation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
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
      "candidate_surface": "FSPO",
      "resolved_canonical": "Fair Sequence Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Length Fairness",
      "resolved_canonical": "Length Fairness",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Importance Sampling",
      "resolved_canonical": "Importance Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Clip Your Sequences Fairly: Enforcing Length Fairness for Sequence-Level RL

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.09177.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.09177](https://arxiv.org/abs/2509.09177)

## 🔗 유사한 논문
- [[2025-09-23/From Uniform to Heterogeneous_ Tailoring Policy Optimization to Every Token's Nature_20250923|From Uniform to Heterogeneous: Tailoring Policy Optimization to Every Token's Nature]] (81.8% similar)
- [[2025-09-19/FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL: Matching Reward Distributions for LLM Reasoning]] (81.4% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (80.1% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (80.0% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Importance Sampling|Importance Sampling]]
**⚡ Unique Technical**: [[keywords/Fair Sequence Policy Optimization|Fair Sequence Policy Optimization]], [[keywords/Length Fairness|Length Fairness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09177v2 Announce Type: replace-cross 
Abstract: We propose FSPO (Fair Sequence Policy Optimization), a sequence-level reinforcement learning method for LLMs that enforces length-fair clipping on the importance-sampling (IS) weight. We study RL methods with sequence-level IS and identify a mismatch when PPO/GRPO-style clipping is transplanted to sequences: a fixed clip range systematically reweights short vs.\ long responses, distorting the optimization direction. FSPO introduces a simple remedy: we clip the sequence log-IS ratio with a band that scales as $\sqrt{L}$. Theoretically, we formalize length fairness via a Length Reweighting Error (LRE) and prove that small LRE yields a cosine directional guarantee between the clipped and true updates. Empirically, FSPO flattens clip rates across length bins, stabilizes training, and outperforms all baselines across multiple evaluation datasets on Qwen3-8B-Base model.

## 📝 요약

FSPO(Fair Sequence Policy Optimization)는 LLM을 위한 시퀀스 수준의 강화 학습 방법으로, 중요도 샘플링(IS) 가중치에 길이 공정성을 부여합니다. 기존 PPO/GRPO 스타일의 클리핑을 시퀀스에 적용할 때 발생하는 불일치를 해결하기 위해, FSPO는 시퀀스 로그-IS 비율을 $\sqrt{L}$로 스케일링된 밴드로 클리핑합니다. 이론적으로, 길이 재가중치 오류(LRE)를 통해 길이 공정성을 공식화하고, 작은 LRE가 클리핑된 업데이트와 실제 업데이트 간의 코사인 방향성을 보장함을 증명합니다. 실험적으로, FSPO는 길이별 클립 비율을 평탄화하고, 훈련을 안정화하며, Qwen3-8B-Base 모델의 여러 평가 데이터셋에서 모든 기준선을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. FSPO는 LLM을 위한 시퀀스 수준의 강화 학습 방법으로, 중요도 샘플링(IS) 가중치에 길이 공정 클리핑을 적용합니다.
- 2. PPO/GRPO 스타일의 클리핑을 시퀀스에 적용할 때 발생하는 불일치를 해결하기 위해, FSPO는 시퀀스 로그-IS 비율을 $\sqrt{L}$로 스케일링된 밴드로 클리핑합니다.
- 3. 이론적으로, FSPO는 길이 재가중치 오류(LRE)를 통해 길이 공정을 형식화하고, 작은 LRE가 클리핑된 업데이트와 실제 업데이트 간의 코사인 방향 보장을 제공함을 증명합니다.
- 4. 실험적으로, FSPO는 길이 구간 전반에 걸쳐 클립 비율을 평탄화하고, 훈련을 안정화하며, Qwen3-8B-Base 모델의 여러 평가 데이터셋에서 모든 기준선을 능가합니다.


---

*Generated on 2025-09-24 14:41:07*