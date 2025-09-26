---
keywords:
  - RevUtil Dataset
  - Peer Review
  - Automated Support Systems
  - Fine-Tuned Models
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.04484
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:25:57.504537",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "RevUtil Dataset",
    "Peer Review",
    "Automated Support Systems",
    "Fine-Tuned Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "RevUtil Dataset": 0.8,
    "Peer Review": 0.75,
    "Automated Support Systems": 0.77,
    "Fine-Tuned Models": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RevUtil dataset",
        "canonical": "RevUtil Dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The RevUtil dataset is a unique contribution of the paper, providing a specialized resource for evaluating review comments.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "peer review",
        "canonical": "Peer Review",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Peer review is a fundamental process in academic publishing, and linking to it helps contextualize the paper's focus on improving review quality.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "automated support systems",
        "canonical": "Automated Support Systems",
        "aliases": [
          "Automated Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Automated support systems are crucial for enhancing the efficiency and quality of peer reviews, making them a key concept for linking.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "fine-tuned models",
        "canonical": "Fine-Tuned Models",
        "aliases": [
          "Fine-Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Fine-tuned models are central to the paper's methodology, highlighting their importance in assessing review comments.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "review comments",
      "feedback",
      "experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "RevUtil dataset",
      "resolved_canonical": "RevUtil Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "peer review",
      "resolved_canonical": "Peer Review",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "automated support systems",
      "resolved_canonical": "Automated Support Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "fine-tuned models",
      "resolved_canonical": "Fine-Tuned Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# The Good, the Bad and the Constructive: Automatically Measuring Peer Review's Utility for Authors

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.04484.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.04484](https://arxiv.org/abs/2509.04484)

## 🔗 유사한 논문
- [[2025-09-18/Calibrated Generative AI as Meta-Reviewer_ A Systemic Functional Linguistics Discourse Analysis of Reviews of Peer Reviews_20250918|Calibrated Generative AI as Meta-Reviewer: A Systemic Functional Linguistics Discourse Analysis of Reviews of Peer Reviews]] (84.0% similar)
- [[2025-09-23/Breaking the Reviewer_ Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks_20250923|Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks]] (83.7% similar)
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (82.8% similar)
- [[2025-09-23/R3_ Robust Rubric-Agnostic Reward Models_20250923|R3: Robust Rubric-Agnostic Reward Models]] (82.5% similar)
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Peer Review|Peer Review]]
**🔗 Specific Connectable**: [[keywords/Automated Support Systems|Automated Support Systems]], [[keywords/Fine-Tuned Models|Fine-Tuned Models]]
**⚡ Unique Technical**: [[keywords/RevUtil Dataset|RevUtil Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.04484v3 Announce Type: replace-cross 
Abstract: Providing constructive feedback to paper authors is a core component of peer review. With reviewers increasingly having less time to perform reviews, automated support systems are required to ensure high reviewing quality, thus making the feedback in reviews useful for authors. To this end, we identify four key aspects of review comments (individual points in weakness sections of reviews) that drive the utility for authors: Actionability, Grounding & Specificity, Verifiability, and Helpfulness. To enable evaluation and development of models assessing review comments, we introduce the RevUtil dataset. We collect 1,430 human-labeled review comments and scale our data with 10k synthetically labeled comments for training purposes. The synthetic data additionally contains rationales, i.e., explanations for the aspect score of a review comment. Employing the RevUtil dataset, we benchmark fine-tuned models for assessing review comments on these aspects and generating rationales. Our experiments demonstrate that these fine-tuned models achieve agreement levels with humans comparable to, and in some cases exceeding, those of powerful closed models like GPT-4o. Our analysis further reveals that machine-generated reviews generally underperform human reviews on our four aspects.

## 📝 요약

이 논문은 논문 저자에게 유용한 피드백을 제공하기 위한 자동화 지원 시스템 개발을 다룹니다. 저자에게 유용한 피드백을 위한 네 가지 핵심 요소로 실행 가능성, 근거 및 구체성, 검증 가능성, 유용성을 식별합니다. 이를 평가하고 모델 개발을 지원하기 위해 RevUtil 데이터셋을 소개하며, 1,430개의 인간이 라벨링한 리뷰와 10,000개의 합성 라벨링 리뷰를 수집했습니다. 실험 결과, 미세 조정된 모델이 인간과 유사하거나 더 나은 수준의 합의에 도달했으며, 기계 생성 리뷰가 인간 리뷰보다 전반적으로 성능이 떨어짐을 발견했습니다.

## 🎯 주요 포인트

- 1. 논문 저자에게 유용한 피드백을 제공하기 위해 리뷰 코멘트의 핵심 측면으로 실행 가능성, 근거 및 구체성, 검증 가능성, 그리고 유용성을 식별했습니다.
- 2. 리뷰 코멘트를 평가하고 모델을 개발하기 위해 RevUtil 데이터셋을 소개하며, 1,430개의 인간 라벨링된 리뷰 코멘트와 10,000개의 합성 라벨링된 코멘트를 수집했습니다.
- 3. 합성 데이터는 리뷰 코멘트의 측면 점수에 대한 설명인 근거를 추가로 포함합니다.
- 4. RevUtil 데이터셋을 활용하여 리뷰 코멘트를 평가하고 근거를 생성하는 모델을 벤치마크한 결과, 인간과 유사하거나 더 나은 수준의 합의 수준을 달성했습니다.
- 5. 기계 생성 리뷰는 일반적으로 네 가지 측면에서 인간 리뷰보다 성능이 떨어지는 것으로 나타났습니다.


---

*Generated on 2025-09-24 01:25:57*