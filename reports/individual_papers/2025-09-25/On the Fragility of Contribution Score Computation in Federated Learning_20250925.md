---
keywords:
  - Federated Learning
  - Contribution Score
  - Model Aggregation
  - Poisoning Attacks
  - Flower Framework
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19921
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:42:17.863178",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Contribution Score",
    "Model Aggregation",
    "Poisoning Attacks",
    "Flower Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.78,
    "Contribution Score": 0.75,
    "Model Aggregation": 0.72,
    "Poisoning Attacks": 0.77,
    "Flower Framework": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a core concept of the paper, linking it to broader discussions on distributed machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contribution Score",
        "canonical": "Contribution Score",
        "aliases": [
          "Contribution Evaluation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's argument, it provides a unique angle on fairness in federated systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Model Aggregation Methods",
        "canonical": "Model Aggregation",
        "aliases": [
          "Aggregation Techniques"
        ],
        "category": "specific_connectable",
        "rationale": "Key to understanding the architectural sensitivity discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Poisoning Attacks",
        "canonical": "Poisoning Attacks",
        "aliases": [
          "Data Poisoning"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights security vulnerabilities in federated learning, crucial for linking to cybersecurity discussions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Flower Framework",
        "canonical": "Flower Framework",
        "aliases": [
          "Flower"
        ],
        "category": "unique_technical",
        "rationale": "Specific implementation context that may connect to other works using the same framework.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "fairness",
      "experiments",
      "datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contribution Score",
      "resolved_canonical": "Contribution Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Model Aggregation Methods",
      "resolved_canonical": "Model Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Poisoning Attacks",
      "resolved_canonical": "Poisoning Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Flower Framework",
      "resolved_canonical": "Flower Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# On the Fragility of Contribution Score Computation in Federated Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19921.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19921](https://arxiv.org/abs/2509.19921)

## 🔗 유사한 논문
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (79.0% similar)
- [[2025-09-23/Robust Reinforcement Learning with Dynamic Distortion Risk Measures_20250923|Robust Reinforcement Learning with Dynamic Distortion Risk Measures]] (78.9% similar)
- [[2025-09-25/What Does Your Benchmark Really Measure? A Framework for Robust Inference of AI Capabilities_20250925|What Does Your Benchmark Really Measure? A Framework for Robust Inference of AI Capabilities]] (78.8% similar)
- [[2025-09-24/A Validation Strategy for Deep Learning Models_ Evaluating and Enhancing Robustness_20250924|A Validation Strategy for Deep Learning Models: Evaluating and Enhancing Robustness]] (78.6% similar)
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Model Aggregation|Model Aggregation]], [[keywords/Poisoning Attacks|Poisoning Attacks]]
**⚡ Unique Technical**: [[keywords/Contribution Score|Contribution Score]], [[keywords/Flower Framework|Flower Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19921v1 Announce Type: new 
Abstract: This paper investigates the fragility of contribution evaluation in federated learning, a critical mechanism for ensuring fairness and incentivizing participation. We argue that contribution scores are susceptible to significant distortions from two fundamental perspectives: architectural sensitivity and intentional manipulation. First, we explore how different model aggregation methods impact these scores. While most research assumes a basic averaging approach, we demonstrate that advanced techniques, including those designed to handle unreliable or diverse clients, can unintentionally yet significantly alter the final scores. Second, we explore vulnerabilities posed by poisoning attacks, where malicious participants strategically manipulate their model updates to inflate their own contribution scores or reduce the importance of other participants. Through extensive experiments across diverse datasets and model architectures, implemented within the Flower framework, we rigorously show that both the choice of aggregation method and the presence of attackers are potent vectors for distorting contribution scores, highlighting a critical need for more robust evaluation schemes.

## 📝 요약

이 논문은 연합 학습에서 기여도 평가의 취약성을 조사합니다. 기여도 점수는 모델 집계 방법에 따라 크게 왜곡될 수 있으며, 악의적인 공격자에 의해 조작될 가능성이 있습니다. 다양한 데이터셋과 모델 아키텍처를 사용한 실험을 통해, 집계 방법의 선택과 공격자의 존재가 기여도 점수 왜곡의 주요 원인임을 보여주었습니다. 이러한 결과는 보다 견고한 평가 체계의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 페더레이티드 러닝에서 기여도 평가의 취약성을 조사하며, 이는 공정성과 참여 유도를 위한 중요한 메커니즘이다.
- 2. 기여도 점수는 모델 집계 방법의 변화에 민감하며, 고급 기법들이 의도치 않게 점수를 왜곡할 수 있음을 보여준다.
- 3. 악의적인 참가자가 자신의 기여도 점수를 부풀리거나 다른 참가자의 중요성을 감소시키기 위해 모델 업데이트를 조작할 수 있는 취약성을 탐구한다.
- 4. 다양한 데이터셋과 모델 아키텍처를 통해 실험한 결과, 집계 방법의 선택과 공격자의 존재가 기여도 점수를 왜곡할 수 있는 강력한 요인임을 입증한다.
- 5. 이러한 왜곡 문제를 해결하기 위해 더 견고한 평가 체계의 필요성을 강조한다.


---

*Generated on 2025-09-25 16:42:17*