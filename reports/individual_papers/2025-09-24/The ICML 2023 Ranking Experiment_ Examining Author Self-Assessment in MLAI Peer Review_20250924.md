<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:30:11.913025",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Isotonic Mechanism",
    "Peer Review Process",
    "Author Self-Assessment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Isotonic Mechanism": 0.78,
    "Peer Review Process": 0.82,
    "Author Self-Assessment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a foundational field relevant to the paper's context and connects to various related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Isotonic Mechanism",
        "canonical": "Isotonic Mechanism",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Isotonic Mechanism is a specific method discussed in the paper, offering a unique perspective on peer review calibration.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Peer Review",
        "canonical": "Peer Review Process",
        "aliases": [
          "Review Process"
        ],
        "category": "specific_connectable",
        "rationale": "Peer Review is central to the paper's analysis and connects to broader discussions on academic evaluation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Author Self-Assessment",
        "canonical": "Author Self-Assessment",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Author Self-Assessment is a novel concept explored in the paper, relevant for understanding biases in peer review.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "experiment",
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Isotonic Mechanism",
      "resolved_canonical": "Isotonic Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Peer Review",
      "resolved_canonical": "Peer Review Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Author Self-Assessment",
      "resolved_canonical": "Author Self-Assessment",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# The ICML 2023 Ranking Experiment: Examining Author Self-Assessment in ML/AI Peer Review

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2408.13430.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2408.13430](https://arxiv.org/abs/2408.13430)

## 🔗 유사한 논문
- [[2025-09-23/The Good, the Bad and the Constructive_ Automatically Measuring Peer Review's Utility for Authors_20250923|The Good, the Bad and the Constructive: Automatically Measuring Peer Review's Utility for Authors]] (81.9% similar)
- [[2025-09-22/The Great AI Witch Hunt_ Reviewers Perception and (Mis)Conception of Generative AI in Research Writing_20250922|The Great AI Witch Hunt: Reviewers Perception and (Mis)Conception of Generative AI in Research Writing]] (79.4% similar)
- [[2025-09-18/Calibrated Generative AI as Meta-Reviewer_ A Systemic Functional Linguistics Discourse Analysis of Reviews of Peer Reviews_20250918|Calibrated Generative AI as Meta-Reviewer: A Systemic Functional Linguistics Discourse Analysis of Reviews of Peer Reviews]] (79.4% similar)
- [[2025-09-23/Justice in Judgment_ Unveiling (Hidden) Bias in LLM-assisted Peer Reviews_20250923|Justice in Judgment: Unveiling (Hidden) Bias in LLM-assisted Peer Reviews]] (78.9% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Peer Review Process|Peer Review Process]]
**⚡ Unique Technical**: [[keywords/Isotonic Mechanism|Isotonic Mechanism]], [[keywords/Author Self-Assessment|Author Self-Assessment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.13430v3 Announce Type: replace-cross 
Abstract: We conducted an experiment during the review process of the 2023 International Conference on Machine Learning (ICML), asking authors with multiple submissions to rank their papers based on perceived quality. In total, we received 1,342 rankings, each from a different author, covering 2,592 submissions. In this paper, we present an empirical analysis of how author-provided rankings could be leveraged to improve peer review processes at machine learning conferences. We focus on the Isotonic Mechanism, which calibrates raw review scores using the author-provided rankings. Our analysis shows that these ranking-calibrated scores outperform the raw review scores in estimating the ground truth ``expected review scores'' in terms of both squared and absolute error metrics. Furthermore, we propose several cautious, low-risk applications of the Isotonic Mechanism and author-provided rankings in peer review, including supporting senior area chairs in overseeing area chairs' recommendations, assisting in the selection of paper awards, and guiding the recruitment of emergency reviewers.

## 📝 요약

이 논문은 2023 국제 기계 학습 학회(ICML)에서 저자들에게 자신이 제출한 여러 논문의 질을 스스로 평가하도록 요청한 실험을 바탕으로, 저자 제공 순위가 기계 학습 학회의 피어 리뷰 프로세스를 개선하는 데 어떻게 활용될 수 있는지를 분석합니다. 총 1,342명의 저자가 2,592개의 제출물에 대해 순위를 매겼습니다. 연구는 저자 제공 순위를 활용해 리뷰 점수를 보정하는 Isotonic Mechanism을 중심으로 진행되었으며, 이 보정된 점수가 원래의 리뷰 점수보다 실제 기대 리뷰 점수를 더 정확하게 예측함을 보여주었습니다. 또한, Isotonic Mechanism과 저자 제공 순위를 활용하여 시니어 에어리어 체어가 에어리어 체어의 추천을 감독하거나, 논문 상 수상작을 선정하거나, 긴급 리뷰어를 모집하는 등의 신중하고 저위험적인 적용 방안을 제안합니다.

## 🎯 주요 포인트

- 1. 2023년 국제 기계 학습 회의(ICML)에서 다수의 논문을 제출한 저자들에게 논문의 질을 평가하도록 요청하는 실험을 수행했습니다.
- 2. 총 1,342명의 저자로부터 2,592개의 제출물에 대한 순위를 받았습니다.
- 3. 저자 제공 순위를 활용하여 기계 학습 회의의 피어 리뷰 프로세스를 개선할 수 있는 방법을 실증적으로 분석했습니다.
- 4. Isotonic Mechanism을 사용하여 저자 제공 순위를 통해 원시 리뷰 점수를 보정하고, 이를 통해 예상 리뷰 점수를 더 정확하게 추정할 수 있음을 보였습니다.
- 5. Isotonic Mechanism과 저자 제공 순위를 피어 리뷰에 신중하고 낮은 위험으로 적용하는 여러 방법을 제안했습니다.


---

*Generated on 2025-09-24 15:30:11*