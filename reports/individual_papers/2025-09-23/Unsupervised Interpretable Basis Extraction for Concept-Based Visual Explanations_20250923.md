---
keywords:
  - Convolutional Neural Network
  - Interpretable Basis
  - Unsupervised Learning
  - Concept-Based Explanations
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2303.10523
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:36:09.279744",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Convolutional Neural Network",
    "Interpretable Basis",
    "Unsupervised Learning",
    "Concept-Based Explanations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Convolutional Neural Network": 0.85,
    "Interpretable Basis": 0.78,
    "Unsupervised Learning": 0.82,
    "Concept-Based Explanations": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CNN image classifier",
        "canonical": "Convolutional Neural Network",
        "aliases": [
          "CNN",
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "Convolutional Neural Networks are foundational in computer vision and link well with other neural network concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "interpretable feature space basis",
        "canonical": "Interpretable Basis",
        "aliases": [
          "interpretable directions",
          "feature space basis"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and offers a unique perspective on feature interpretability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "unsupervised basis extraction",
        "canonical": "Unsupervised Learning",
        "aliases": [
          "unsupervised method",
          "unsupervised approach"
        ],
        "category": "specific_connectable",
        "rationale": "Unsupervised learning is a key method in machine learning, providing a strong link to broader unsupervised techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "concept-based visual explanations",
        "canonical": "Concept-Based Explanations",
        "aliases": [
          "visual explanations",
          "concept explanations"
        ],
        "category": "unique_technical",
        "rationale": "This term captures the paper's focus on making neural network outputs more interpretable through concepts.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
      "candidate_surface": "CNN image classifier",
      "resolved_canonical": "Convolutional Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "interpretable feature space basis",
      "resolved_canonical": "Interpretable Basis",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "unsupervised basis extraction",
      "resolved_canonical": "Unsupervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "concept-based visual explanations",
      "resolved_canonical": "Concept-Based Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Unsupervised Interpretable Basis Extraction for Concept-Based Visual Explanations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2303.10523.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2303.10523](https://arxiv.org/abs/2303.10523)

## 🔗 유사한 논문
- [[2025-09-22/Generating Part-Based Global Explanations Via Correspondence_20250922|Generating Part-Based Global Explanations Via Correspondence]] (80.0% similar)
- [[2025-09-22/Incorporating Visual Cortical Lateral Connection Properties into CNN_ Recurrent Activation and Excitatory-Inhibitory Separation_20250922|Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation]] (79.9% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (79.4% similar)
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation]] (79.3% similar)
- [[2025-09-23/Interpreting vision transformers via residual replacement model_20250923|Interpreting vision transformers via residual replacement model]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Convolutional Neural Network|Convolutional Neural Network]]
**🔗 Specific Connectable**: [[keywords/Unsupervised Learning|Unsupervised Learning]]
**⚡ Unique Technical**: [[keywords/Interpretable Basis|Interpretable Basis]], [[keywords/Concept-Based Explanations|Concept-Based Explanations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2303.10523v3 Announce Type: replace-cross 
Abstract: An important line of research attempts to explain CNN image classifier predictions and intermediate layer representations in terms of human-understandable concepts. Previous work supports that deep representations are linearly separable with respect to their concept label, implying that the feature space has directions where intermediate representations may be projected onto, to become more understandable. These directions are called interpretable, and when considered as a set, they may form an interpretable feature space basis. Compared to previous top-down probing approaches which use concept annotations to identify the interpretable directions one at a time, in this work, we take a bottom-up approach, identifying the directions from the structure of the feature space, collectively, without relying on supervision from concept labels. Instead, we learn the directions by optimizing for a sparsity property that holds for any interpretable basis. We experiment with existing popular CNNs and demonstrate the effectiveness of our method in extracting an interpretable basis across network architectures and training datasets. We make extensions to existing basis interpretability metrics and show that intermediate layer representations become more interpretable when transformed with the extracted bases. Finally, we compare the bases extracted with our method with the bases derived with supervision and find that, in one aspect, unsupervised basis extraction has a strength that constitutes a limitation of learning the basis with supervision, and we provide potential directions for future research.

## 📝 요약

이 논문은 CNN 이미지 분류기의 예측과 중간 계층 표현을 인간이 이해할 수 있는 개념으로 설명하는 연구에 기여합니다. 기존 연구는 딥러닝 표현이 개념 레이블에 대해 선형적으로 분리 가능하다고 제안했으나, 이 연구는 개념 레이블 없이도 해석 가능한 방향을 찾는 하향식 접근법 대신 상향식 접근법을 사용합니다. 이 방법은 해석 가능한 기저의 희소성 특성을 최적화하여 방향을 학습하며, 다양한 CNN 아키텍처와 데이터셋에서 실험을 통해 그 효과를 입증했습니다. 또한 기존의 해석 가능성 지표를 확장하여 중간 계층 표현의 해석 가능성을 향상시켰음을 보여주고, 비지도 학습 방식이 지도 학습 방식의 한계를 보완할 수 있음을 제안합니다.

## 🎯 주요 포인트

- 1. CNN 이미지 분류기의 예측과 중간 계층 표현을 인간이 이해할 수 있는 개념으로 설명하려는 연구가 진행되고 있다.
- 2. 기존 연구는 심층 표현이 개념 레이블에 대해 선형적으로 분리 가능하다고 주장하며, 이는 해석 가능한 방향으로 중간 표현을 투영할 수 있음을 시사한다.
- 3. 본 연구에서는 개념 레이블에 의존하지 않고, 특징 공간의 구조에서 해석 가능한 방향을 집합적으로 식별하는 하향식 접근 방식을 제안한다.
- 4. 제안된 방법은 기존 CNN 아키텍처와 학습 데이터셋에서 해석 가능한 기저를 효과적으로 추출할 수 있음을 실험적으로 입증하였다.
- 5. 비지도 학습을 통해 추출한 기저가 감독 학습을 통해 얻은 기저와 비교했을 때, 특정 측면에서 더 강점을 보이며, 이는 향후 연구 방향을 제시한다.


---

*Generated on 2025-09-24 00:36:09*