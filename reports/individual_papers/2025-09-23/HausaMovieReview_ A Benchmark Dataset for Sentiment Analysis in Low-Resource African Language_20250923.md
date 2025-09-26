---
keywords:
  - Natural Language Processing
  - Transformer
  - Sentiment Analysis
  - Low-Resource Languages
  - Decision Tree
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16256
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:09:22.251116",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Natural Language Processing",
    "Transformer",
    "Sentiment Analysis",
    "Low-Resource Languages",
    "Decision Tree"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Natural Language Processing": 0.85,
    "Transformer": 0.8,
    "Sentiment Analysis": 0.82,
    "Low-Resource Languages": 0.78,
    "Decision Tree": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "This is a core field relevant to the study and connects to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Transformer models",
        "canonical": "Transformer",
        "aliases": [
          "BERT",
          "RoBERTa"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are pivotal in modern NLP, providing a strong link to related advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sentiment Analysis",
        "canonical": "Sentiment Analysis",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific application of NLP, crucial for understanding the dataset's purpose.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Low-Resource Languages",
        "canonical": "Low-Resource Languages",
        "aliases": [
          "under-resourced languages"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the focus on languages with limited resources, a key aspect of the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Decision Tree classifier",
        "canonical": "Decision Tree",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A classical model that outperformed others, providing a unique insight into model performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "annotated datasets",
      "classical models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Transformer models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sentiment Analysis",
      "resolved_canonical": "Sentiment Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Low-Resource Languages",
      "resolved_canonical": "Low-Resource Languages",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Decision Tree classifier",
      "resolved_canonical": "Decision Tree",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# HausaMovieReview: A Benchmark Dataset for Sentiment Analysis in Low-Resource African Language

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16256.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16256](https://arxiv.org/abs/2509.16256)

## 🔗 유사한 논문
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (75.9% similar)
- [[2025-09-19/Advancing Conversational AI with Shona Slang_ A Dataset and Hybrid Model for Digital Inclusion_20250919|Advancing Conversational AI with Shona Slang: A Dataset and Hybrid Model for Digital Inclusion]] (75.9% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (75.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Sentiment Analysis|Sentiment Analysis]], [[keywords/Decision Tree|Decision Tree]]
**⚡ Unique Technical**: [[keywords/Low-Resource Languages|Low-Resource Languages]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16256v1 Announce Type: cross 
Abstract: The development of Natural Language Processing (NLP) tools for low-resource languages is critically hindered by the scarcity of annotated datasets. This paper addresses this fundamental challenge by introducing HausaMovieReview, a novel benchmark dataset comprising 5,000 YouTube comments in Hausa and code-switched English. The dataset was meticulously annotated by three independent annotators, demonstrating a robust agreement with a Fleiss' Kappa score of 0.85 between annotators. We used this dataset to conduct a comparative analysis of classical models (Logistic Regression, Decision Tree, K-Nearest Neighbors) and fine-tuned transformer models (BERT and RoBERTa). Our results reveal a key finding: the Decision Tree classifier, with an accuracy and F1-score 89.72% and 89.60% respectively, significantly outperformed the deep learning models. Our findings also provide a robust baseline, demonstrating that effective feature engineering can enable classical models to achieve state-of-the-art performance in low-resource contexts, thereby laying a solid foundation for future research.
  Keywords: Hausa, Kannywood, Low-Resource Languages, NLP, Sentiment Analysis

## 📝 요약

이 논문은 자원이 부족한 언어의 자연어 처리 도구 개발에 있어 주석 데이터 부족 문제를 해결하기 위해, 5,000개의 하우사어 및 코드 전환된 영어 유튜브 댓글로 구성된 HausaMovieReview라는 새로운 벤치마크 데이터셋을 소개합니다. 세 명의 독립적인 주석자가 주석을 달았으며, Fleiss' Kappa 점수 0.85로 높은 일치를 보였습니다. 이 데이터셋을 활용하여 고전 모델(로지스틱 회귀, 결정 트리, K-최근접 이웃)과 미세 조정된 트랜스포머 모델(BERT, RoBERTa)을 비교 분석한 결과, 결정 트리 분류기가 89.72%의 정확도와 89.60%의 F1 점수로 심층 학습 모델을 뛰어넘는 성능을 보였습니다. 이러한 결과는 효과적인 특징 공학이 고전 모델이 자원이 부족한 환경에서도 최첨단 성능을 달성할 수 있음을 보여주며, 향후 연구의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저자들은 저


---

*Generated on 2025-09-23 23:09:22*