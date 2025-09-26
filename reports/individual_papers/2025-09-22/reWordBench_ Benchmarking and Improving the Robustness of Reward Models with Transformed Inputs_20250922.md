---
keywords:
  - Reward Models
  - reWordBench
  - Paraphrases
  - Alignment
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2503.11751
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:42:51.239469",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reward Models",
    "reWordBench",
    "Paraphrases",
    "Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reward Models": 0.78,
    "reWordBench": 0.8,
    "Paraphrases": 0.72,
    "Alignment": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reward Models",
        "canonical": "Reward Models",
        "aliases": [
          "RM",
          "Reward Function"
        ],
        "category": "unique_technical",
        "rationale": "Reward models are central to the paper's focus on robustness and are not covered in the existing vocabulary.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "reWordBench",
        "canonical": "reWordBench",
        "aliases": [
          "Reward Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "reWordBench is a novel benchmark introduced in the paper, crucial for understanding the robustness of reward models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Paraphrases",
        "canonical": "Paraphrases",
        "aliases": [
          "Rephrasing",
          "Restatement"
        ],
        "category": "specific_connectable",
        "rationale": "Paraphrases are key to the proposed method for improving reward model robustness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Alignment",
        "canonical": "Alignment",
        "aliases": [
          "Model Alignment",
          "Output Alignment"
        ],
        "category": "broad_technical",
        "rationale": "Alignment is a critical application area for reward models, relevant to the paper's improvements.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Performance",
      "Standard Benchmarks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reward Models",
      "resolved_canonical": "Reward Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "reWordBench",
      "resolved_canonical": "reWordBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Paraphrases",
      "resolved_canonical": "Paraphrases",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Alignment",
      "resolved_canonical": "Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs

**Korean Title:** reWordBench: 변환된 입력을 통한 보상 모델의 견고성 벤치마킹 및 개선

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.11751.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2503.11751](https://arxiv.org/abs/2503.11751)

## 🔗 유사한 논문
- [[2025-09-22/BaseReward_ A Strong Baseline for Multimodal Reward Model_20250922|BaseReward: A Strong Baseline for Multimodal Reward Model]] (86.4% similar)
- [[2025-09-22/MT-RewardTree_ A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling_20250922|MT-RewardTree: A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling]] (85.7% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (84.0% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (83.9% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Alignment|Alignment]]
**🔗 Specific Connectable**: [[keywords/Paraphrases|Paraphrases]]
**⚡ Unique Technical**: [[keywords/Reward Models|Reward Models]], [[keywords/reWordBench|reWordBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.11751v2 Announce Type: replace 
Abstract: Reward models have become a staple in modern NLP, serving as not only a scalable text evaluator, but also an indispensable component in many alignment recipes and inference-time algorithms. However, while recent reward models increase performance on standard benchmarks, this may partly be due to overfitting effects, which would confound an understanding of their true capability. In this work, we scrutinize the robustness of reward models and the extent of such overfitting. We build **reWordBench**, which systematically transforms reward model inputs in meaning- or ranking-preserving ways. We show that state-of-the-art reward models suffer from substantial performance degradation even with minor input transformations, sometimes dropping to significantly below-random accuracy, suggesting brittleness. To improve reward model robustness, we propose to explicitly train them to assign similar scores to paraphrases, and find that this approach also improves robustness to other distinct kinds of transformations. For example, our robust reward model reduces such degradation by roughly half for the Chat Hard subset in RewardBench. Furthermore, when used in alignment, our robust reward models demonstrate better utility and lead to higher-quality outputs, winning in up to 59% of instances against a standardly trained RM.

## 🔍 Abstract (한글 번역)

arXiv:2503.11751v2 발표 유형: 교체  
초록: 보상 모델은 현대 자연어 처리(NLP)에서 필수적인 요소로 자리잡고 있으며, 확장 가능한 텍스트 평가자로서뿐만 아니라, 많은 정렬 방법 및 추론 시간 알고리즘에서 필수적인 구성 요소로 사용되고 있습니다. 그러나 최근의 보상 모델이 표준 벤치마크에서 성능을 향상시키고 있지만, 이는 부분적으로 과적합 효과로 인한 것일 수 있으며, 이는 이들의 실제 능력에 대한 이해를 혼란스럽게 할 수 있습니다. 본 연구에서는 보상 모델의 견고성과 그러한 과적합의 정도를 면밀히 조사합니다. 우리는 **reWordBench**를 구축하여 보상 모델 입력을 의미 또는 순위를 보존하는 방식으로 체계적으로 변환합니다. 우리는 최첨단 보상 모델이 사소한 입력 변환에도 상당한 성능 저하를 겪으며, 때로는 무작위 정확도보다 훨씬 낮은 수준으로 떨어지는 것을 보여주어 취약성을 시사합니다. 보상 모델의 견고성을 향상시키기 위해, 우리는 그들이 패러프레이즈에 유사한 점수를 할당하도록 명시적으로 훈련시키는 것을 제안하며, 이 접근 방식이 다른 다양한 종류의 변환에 대한 견고성도 향상시킨다는 것을 발견했습니다. 예를 들어, 우리의 견고한 보상 모델은 RewardBench의 Chat Hard 하위 집합에서 그러한 성능 저하를 약 절반으로 줄였습니다. 더욱이, 정렬에 사용될 때, 우리의 견고한 보상 모델은 더 나은 유용성을 보여주며, 표준적으로 훈련된 보상 모델에 비해 최대 59%의 사례에서 더 높은 품질의 출력을 생성합니다.

## 📝 요약

이 논문은 보상 모델의 강건성을 평가하고 과적합 문제를 분석합니다. 연구팀은 입력 변환을 통해 보상 모델의 성능 저하를 확인하고, 이를 개선하기 위해 유사한 의미의 문장에 대해 일관된 점수를 부여하도록 훈련하는 방법을 제안합니다. 이 접근법은 다양한 변환에 대한 강건성을 향상시켰으며, 특히 Chat Hard 데이터셋에서 성능 저하를 절반으로 줄였습니다. 또한, 개선된 보상 모델은 정렬 작업에서 더 높은 품질의 출력을 생성하며, 기존 모델 대비 최대 59%의 경우에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 최신 보상 모델은 표준 벤치마크에서 성능을 향상시키지만, 이는 부분적으로 과적합 효과 때문일 수 있습니다.
- 2. **reWordBench**를 통해 보상 모델 입력을 의미나 순위를 유지하면서 체계적으로 변환하여 모델의 취약성을 분석합니다.
- 3. 최첨단 보상 모델은 입력 변환에 대해 성능 저하를 겪으며, 이는 모델의 취약성을 시사합니다.
- 4. 보상 모델의 강건성을 향상시키기 위해 유사한 점수를 부여하도록 훈련시키는 방법을 제안하며, 이는 다양한 변환에 대한 강건성을 개선합니다.
- 5. 강건한 보상 모델은 정렬 시 더 나은 유용성을 보여주며, 표준 훈련된 모델에 비해 최대 59%의 경우에서 더 높은 품질의 출력을 생성합니다.


---

*Generated on 2025-09-23 11:42:51*