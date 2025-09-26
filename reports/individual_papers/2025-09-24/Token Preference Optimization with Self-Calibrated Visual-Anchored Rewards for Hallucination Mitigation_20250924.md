<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:27:12.358144",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Token Preference Optimization",
    "Visual-Anchored Reward",
    "Hallucination Mitigation",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Token Preference Optimization": 0.78,
    "Visual-Anchored Reward": 0.77,
    "Hallucination Mitigation": 0.75,
    "Vision-Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Token Preference Optimization",
        "canonical": "Token Preference Optimization",
        "aliases": [
          "TPO"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, crucial for linking discussions on optimization techniques in vision-language models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Visual-Anchored Reward",
        "canonical": "Visual-Anchored Reward",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution, focusing on token-level optimization linked to visual data.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Hallucination Mitigation",
        "canonical": "Hallucination Mitigation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a key problem addressed by the paper, relevant for linking to broader discussions on improving model outputs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLM"
        ],
        "category": "evolved_concepts",
        "rationale": "The paper builds on this concept, which is crucial for linking multimodal learning discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Direct Preference Optimization",
      "self-calibrated rewards"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Token Preference Optimization",
      "resolved_canonical": "Token Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Visual-Anchored Reward",
      "resolved_canonical": "Visual-Anchored Reward",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Hallucination Mitigation",
      "resolved_canonical": "Hallucination Mitigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2412.14487.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2412.14487](https://arxiv.org/abs/2412.14487)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization_20250923|Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization]] (86.1% similar)
- [[2025-09-23/Preference Distillation via Value based Reinforcement Learning_20250923|Preference Distillation via Value based Reinforcement Learning]] (85.6% similar)
- [[2025-09-23/From Uniform to Heterogeneous_ Tailoring Policy Optimization to Every Token's Nature_20250923|From Uniform to Heterogeneous: Tailoring Policy Optimization to Every Token's Nature]] (84.8% similar)
- [[2025-09-22/OSPO_ Object-centric Self-improving Preference Optimization for Text-to-Image Generation_20250922|OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation]] (84.0% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Hallucination Mitigation|Hallucination Mitigation]]
**⚡ Unique Technical**: [[keywords/Token Preference Optimization|Token Preference Optimization]], [[keywords/Visual-Anchored Reward|Visual-Anchored Reward]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.14487v4 Announce Type: replace 
Abstract: Direct Preference Optimization (DPO) has been demonstrated to be highly effective in mitigating hallucinations in Large Vision Language Models (LVLMs) by aligning their outputs more closely with human preferences. Despite the recent progress, existing methods suffer from two drawbacks: 1) Lack of scalable token-level rewards; and 2) Neglect of visual-anchored tokens. To this end, we propose a novel Token Preference Optimization model with self-calibrated rewards (dubbed as TPO), which adaptively attends to visual-correlated tokens without fine-grained annotations. Specifically, we introduce a token-level \emph{visual-anchored} \emph{reward} as the difference of the logistic distributions of generated tokens conditioned on the raw image and the corrupted one. In addition, to highlight the informative visual-anchored tokens, a visual-aware training objective is proposed to enhance more accurate token-level optimization. Extensive experimental results have manifested the state-of-the-art performance of the proposed TPO. For example, by building on top of LLAVA-1.5-7B, our TPO boosts the performance absolute improvement for hallucination benchmarks.

## 📝 요약

Direct Preference Optimization(DPO)는 대규모 비전 언어 모델(LVLM)에서 인간의 선호에 맞춰 출력을 조정하여 환각 현상을 줄이는 데 효과적입니다. 그러나 기존 방법은 확장 가능한 토큰 수준 보상의 부족과 시각적으로 고정된 토큰을 간과하는 문제를 가지고 있습니다. 이를 해결하기 위해, 우리는 시각적으로 연관된 토큰에 적응적으로 주목하는 새로운 토큰 선호 최적화 모델(TPO)을 제안합니다. 이 모델은 세밀한 주석 없이도 작동하며, 원본 이미지와 손상된 이미지에 기반한 생성 토큰의 로지스틱 분포 차이를 통해 시각적으로 고정된 보상을 도입합니다. 또한, 정보가 풍부한 시각적으로 고정된 토큰을 강조하기 위해 시각 인식 학습 목표를 제안하여 더 정확한 토큰 수준 최적화를 강화합니다. 실험 결과, 제안된 TPO가 최첨단 성능을 보이며, LLAVA-1.5-7B 기반에서 환각 벤치마크 성능을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. Direct Preference Optimization (DPO)는 대규모 비전 언어 모델(LVLMs)에서 인간의 선호도에 맞춰 출력을 조정하여 환각 현상을 완화하는 데 효과적입니다.
- 2. 기존 방법들은 확장 가능한 토큰 수준의 보상 부족과 시각적 앵커 토큰을 간과하는 두 가지 단점을 가지고 있습니다.
- 3. 제안된 Token Preference Optimization (TPO) 모델은 세밀한 주석 없이 시각적으로 연관된 토큰에 적응적으로 주목하며, 자기 보정 보상을 통해 이를 최적화합니다.
- 4. TPO는 원본 이미지와 손상된 이미지에 조건화된 생성 토큰의 로지스틱 분포 차이를 사용하여 토큰 수준의 시각 앵커 보상을 도입합니다.
- 5. 실험 결과, TPO는 환각 벤치마크에서 성능을 크게 향상시키며, 최첨단 성능을 입증했습니다.


---

*Generated on 2025-09-24 16:27:12*