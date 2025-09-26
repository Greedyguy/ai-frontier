---
keywords:
  - Conformal Prediction
  - Learning to Defer
  - Expert Deferral
  - Human-AI Collaboration
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.12573
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:52:42.871661",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Conformal Prediction",
    "Learning to Defer",
    "Expert Deferral",
    "Human-AI Collaboration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Conformal Prediction": 0.78,
    "Learning to Defer": 0.8,
    "Expert Deferral": 0.77,
    "Human-AI Collaboration": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Conformal Prediction",
        "canonical": "Conformal Prediction",
        "aliases": [
          "Conformal Predictor"
        ],
        "category": "unique_technical",
        "rationale": "Conformal Prediction is central to the proposed framework, offering a novel approach to expert deferral.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Learning to Defer",
        "canonical": "Learning to Defer",
        "aliases": [
          "L2D"
        ],
        "category": "specific_connectable",
        "rationale": "Learning to Defer is a key concept in hybrid human-AI decision-making, relevant for linking with related decision-making frameworks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Expert Deferral",
        "canonical": "Expert Deferral",
        "aliases": [
          "Deferral Framework"
        ],
        "category": "unique_technical",
        "rationale": "Expert Deferral is a unique aspect of the framework, highlighting its training-free and expert-agnostic nature.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Human-AI Collaboration",
        "canonical": "Human-AI Collaboration",
        "aliases": [
          "Hybrid Decision-Making"
        ],
        "category": "broad_technical",
        "rationale": "Human-AI Collaboration is a broad technical area that connects various decision-making and AI integration strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
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
      "candidate_surface": "Conformal Prediction",
      "resolved_canonical": "Conformal Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Learning to Defer",
      "resolved_canonical": "Learning to Defer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Expert Deferral",
      "resolved_canonical": "Expert Deferral",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Human-AI Collaboration",
      "resolved_canonical": "Human-AI Collaboration",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# No Need for Learning to Defer? A Training Free Deferral Framework to Multiple Experts through Conformal Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12573.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.12573](https://arxiv.org/abs/2509.12573)

## 🔗 유사한 논문
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (81.6% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (80.3% similar)
- [[2025-09-19/Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision_ An Information-Theoretic Impossibility_20250919|Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility]] (80.1% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (79.7% similar)
- [[2025-09-19/Predicting Multi-Agent Specialization via Task Parallelizability_20250919|Predicting Multi-Agent Specialization via Task Parallelizability]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Human-AI Collaboration|Human-AI Collaboration]]
**🔗 Specific Connectable**: [[keywords/Learning to Defer|Learning to Defer]]
**⚡ Unique Technical**: [[keywords/Conformal Prediction|Conformal Prediction]], [[keywords/Expert Deferral|Expert Deferral]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12573v2 Announce Type: replace 
Abstract: AI systems often fail to deliver reliable predictions across all inputs, prompting the need for hybrid human-AI decision-making. Existing Learning to Defer (L2D) approaches address this by training deferral models, but these are sensitive to changes in expert composition and require significant retraining if experts change. We propose a training-free, model- and expert-agnostic framework for expert deferral based on conformal prediction. Our method uses the prediction set generated by a conformal predictor to identify label-specific uncertainty and selects the most discriminative expert using a segregativity criterion, measuring how well an expert distinguishes between the remaining plausible labels. Experiments on CIFAR10-H and ImageNet16-H show that our method consistently outperforms both the standalone model and the strongest expert, with accuracies attaining $99.57\pm0.10\%$ and $99.40\pm0.52\%$, while reducing expert workload by up to a factor of $11$. The method remains robust under degraded expert performance and shows a gradual performance drop in low-information settings. These results suggest a scalable, retraining-free alternative to L2D for real-world human-AI collaboration.

## 📝 요약

이 논문은 AI 시스템의 예측 신뢰성 문제를 해결하기 위해 인간과 AI의 하이브리드 의사결정 방식을 제안합니다. 기존의 Learning to Defer(L2D) 접근법은 전문가 구성이 변할 때 재훈련이 필요하지만, 본 연구는 훈련이 필요 없는 전문가 위임 프레임워크를 제안합니다. 이 방법은 적합 예측을 사용하여 라벨별 불확실성을 식별하고, 가장 구별력 있는 전문가를 선택합니다. CIFAR10-H와 ImageNet16-H 실험 결과, 제안된 방법이 독립 모델과 가장 강력한 전문가보다 높은 정확도(각각 99.57%와 99.40%)를 보이며, 전문가의 작업량을 최대 11배 줄였습니다. 이 방법은 전문가 성능이 저하된 상황에서도 강건함을 유지하며, 정보가 적은 환경에서도 점진적인 성능 저하를 보입니다. 이는 L2D의 대안으로서 실용적인 인간-AI 협업을 위한 확장 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. AI 시스템의 예측 신뢰성 문제를 해결하기 위해 인간과 AI의 하이브리드 의사결정이 필요합니다.
- 2. 기존의 L2D 접근 방식은 전문가 구성이 변경될 때 민감하여 재훈련이 필요합니다.
- 3. 제안된 방법은 훈련이 필요 없는 전문가 위임 프레임워크로, 적합 예측을 기반으로 합니다.
- 4. CIFAR10-H 및 ImageNet16-H 실험에서 제안된 방법은 독립 모델과 가장 강력한 전문가보다 높은 정확도를 보였습니다.
- 5. 제안된 방법은 전문가의 작업량을 최대 11배 줄이고, 성능 저하 상황에서도 강건함을 유지합니다.


---

*Generated on 2025-09-24 02:52:42*