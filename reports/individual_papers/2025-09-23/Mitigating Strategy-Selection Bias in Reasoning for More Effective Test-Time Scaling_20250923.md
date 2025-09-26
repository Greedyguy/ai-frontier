---
keywords:
  - Test-time Scaling
  - Large Language Model
  - Reasoning Strategies
  - Selection Bias
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17905
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:03:40.073910",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Test-time Scaling",
    "Large Language Model",
    "Reasoning Strategies",
    "Selection Bias"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Test-time Scaling": 0.78,
    "Large Language Model": 0.7,
    "Reasoning Strategies": 0.8,
    "Selection Bias": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Test-time scaling",
        "canonical": "Test-time Scaling",
        "aliases": [
          "TTS"
        ],
        "category": "unique_technical",
        "rationale": "Test-time scaling is a novel approach specific to the paper, enhancing the performance of LLMs by exploring diverse reasoning paths.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on improving reasoning strategy selection.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reasoning strategies",
        "canonical": "Reasoning Strategies",
        "aliases": [
          "Reasoning Paths"
        ],
        "category": "specific_connectable",
        "rationale": "Reasoning strategies are crucial for understanding the selection bias and its impact on model performance.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Selection bias",
        "canonical": "Selection Bias",
        "aliases": [
          "Bias in Strategy Selection"
        ],
        "category": "specific_connectable",
        "rationale": "Selection bias is a key issue addressed in the paper, affecting the effectiveness of test-time scaling.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.68,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Test-time scaling",
      "resolved_canonical": "Test-time Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reasoning strategies",
      "resolved_canonical": "Reasoning Strategies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Selection bias",
      "resolved_canonical": "Selection Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.68,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17905.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17905](https://arxiv.org/abs/2509.17905)

## 🔗 유사한 논문
- [[2025-09-17/Slim-SC_ Thought Pruning for Efficient Scaling with Self-Consistency_20250917|Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency]] (87.7% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (83.6% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (82.9% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech]] (82.9% similar)
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reasoning Strategies|Reasoning Strategies]], [[keywords/Selection Bias|Selection Bias]]
**⚡ Unique Technical**: [[keywords/Test-time Scaling|Test-time Scaling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17905v1 Announce Type: new 
Abstract: Test-time scaling (TTS) has been shown to improve the performance of large language models (LLMs) by sampling and aggregating diverse reasoning paths. However, existing research has overlooked a critical issue: selection bias of reasoning strategies during scaling. Specifically, when generating reasoning processes, LLMs tend to follow certain strategies (e.g., algebraic solutions for math problems) while neglecting other valid alternatives (e.g., geometric solutions), resulting in insufficient exploration of the solution space. To further understand the impact of this bias, we present a theoretical analysis that reveals when it undermines the effectiveness of test-time scaling. Motivated by this theoretical insight, we introduce TTS-Uniform, a framework designed to mitigate the selection bias of reasoning strategies. It (i) identifies potential strategies, (ii) uniformly allocates the sampling budget across them, and (iii) filters out unstable strategies prior to aggregation. Experimental results show that TTS-Uniform significantly enhances scaling effectiveness across multiple mainstream LLMs and benchmark datasets.

## 📝 요약

이 논문은 테스트 시 확장(TTS)이 대형 언어 모델(LLM)의 성능을 향상시킬 수 있음을 보여주지만, 기존 연구에서는 확장 과정에서의 추론 전략 선택 편향을 간과했다고 지적합니다. LLM은 특정 전략(예: 수학 문제에서 대수적 해결책)을 따르는 경향이 있어 해결 공간의 충분한 탐색이 이루어지지 않습니다. 이 편향이 확장 효과에 미치는 영향을 이론적으로 분석하고, 이를 기반으로 TTS-Uniform이라는 프레임워크를 제안합니다. TTS-Uniform은 잠재적 전략을 식별하고, 샘플링 예산을 균등하게 할당하며, 불안정한 전략을 제거합니다. 실험 결과, TTS-Uniform은 여러 LLM과 벤치마크 데이터셋에서 확장 효과를 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. 테스트 시간 스케일링(TTS)은 다양한 추론 경로를 샘플링하고 집계하여 대형 언어 모델(LLM)의 성능을 향상시킨다.
- 2. 기존 연구는 스케일링 중 추론 전략의 선택 편향 문제를 간과했다.
- 3. LLM은 특정 전략을 선호하여 해결 공간을 충분히 탐색하지 못하는 경향이 있다.
- 4. TTS-Uniform은 이러한 선택 편향을 완화하기 위해 설계된 프레임워크로, 잠재적 전략을 식별하고 균등하게 샘플링 예산을 할당하며 불안정한 전략을 필터링한다.
- 5. 실험 결과, TTS-Uniform은 여러 주류 LLM과 벤치마크 데이터셋에서 스케일링 효과를 크게 향상시켰다.


---

*Generated on 2025-09-23 23:03:40*