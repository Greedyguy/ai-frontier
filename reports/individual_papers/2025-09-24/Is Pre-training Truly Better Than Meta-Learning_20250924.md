<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:23:21.948764",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Pre-Trained Model",
    "Meta-Learning",
    "Formal Diversity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.9,
    "Pre-Trained Model": 0.85,
    "Meta-Learning": 0.88,
    "Formal Diversity": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "few-shot learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "few-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is a key focus of the paper, providing a direct link to current trends and discussions in the field.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "pre-trained model",
        "canonical": "Pre-Trained Model",
        "aliases": [
          "PT model"
        ],
        "category": "unique_technical",
        "rationale": "The comparison between pre-trained models and meta-learning is central to the paper's argument.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "meta-learning",
        "canonical": "Meta-Learning",
        "aliases": [
          "MAML",
          "Model Agnostic Meta-Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Meta-Learning is a core concept compared against pre-training, crucial for understanding the paper's findings.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "formal diversity",
        "canonical": "Formal Diversity",
        "aliases": [
          "diversity coefficient"
        ],
        "category": "unique_technical",
        "rationale": "Formal diversity is a novel metric used in the paper to evaluate dataset characteristics, offering a unique perspective.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "effect size",
      "classical statistical thresholds"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "few-shot learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "pre-trained model",
      "resolved_canonical": "Pre-Trained Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "meta-learning",
      "resolved_canonical": "Meta-Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "formal diversity",
      "resolved_canonical": "Formal Diversity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Is Pre-training Truly Better Than Meta-Learning?

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2306.13841.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2306.13841](https://arxiv.org/abs/2306.13841)

## 🔗 유사한 논문
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (85.0% similar)
- [[2025-09-23/Language Modeling with Learned Meta-Tokens_20250923|Language Modeling with Learned Meta-Tokens]] (83.0% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (82.1% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (81.4% similar)
- [[2025-09-23/Scaling, Simplification, and Adaptation_ Lessons from Pretraining on Machine-Translated Text_20250923|Scaling, Simplification, and Adaptation: Lessons from Pretraining on Machine-Translated Text]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]], [[keywords/Meta-Learning|Meta-Learning]]
**⚡ Unique Technical**: [[keywords/Pre-Trained Model|Pre-Trained Model]], [[keywords/Formal Diversity|Formal Diversity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2306.13841v2 Announce Type: replace-cross 
Abstract: In the context of few-shot learning, it is currently believed that a fixed pre-trained (PT) model, along with fine-tuning the final layer during evaluation, outperforms standard meta-learning algorithms. We re-evaluate these claims under an in-depth empirical examination of an extensive set of formally diverse datasets and compare PT to Model Agnostic Meta-Learning (MAML). Unlike previous work, we emphasize a fair comparison by using: the same architecture, the same optimizer, and all models trained to convergence. Crucially, we use a more rigorous statistical tool -- the effect size (Cohen's d) -- to determine the practical significance of the difference between a model trained with PT vs. a MAML. We then use a previously proposed metric -- the diversity coefficient -- to compute the average formal diversity of a dataset. Using this analysis, we demonstrate the following: 1. when the formal diversity of a data set is low, PT beats MAML on average and 2. when the formal diversity is high, MAML beats PT on average. The caveat is that the magnitude of the average difference between a PT vs. MAML using the effect size is low (according to classical statistical thresholds) -- less than 0.2. Nevertheless, this observation is contrary to the currently held belief that a pre-trained model is always better than a meta-learning model. Our extensive experiments consider 21 few-shot learning benchmarks, including the large-scale few-shot learning dataset Meta-Data set. We also show no significant difference between a MAML model vs. a PT model with GPT-2 on Openwebtext. We, therefore, conclude that a pre-trained model does not always beat a meta-learned model and that the formal diversity of a dataset is a driving factor.

## 📝 요약

이 논문은 소수 샷 학습에서 고정된 사전 학습 모델(PT)이 최종 레이어를 미세 조정하는 것이 표준 메타 학습 알고리즘보다 우수하다는 기존의 믿음을 재평가합니다. 다양한 데이터셋을 사용하여 PT와 모델 무관 메타 학습(MAML)을 비교하며, 동일한 아키텍처와 옵티마이저를 사용하여 공정한 비교를 강조합니다. 효과 크기(Cohen's d)를 통해 PT와 MAML 간의 실질적 차이를 평가하고, 데이터셋의 형식적 다양성을 측정하는 다양성 계수를 사용하여 분석합니다. 연구 결과, 데이터셋의 형식적 다양성이 낮을 때는 PT가 MAML을 평균적으로 능가하고, 다양성이 높을 때는 MAML이 PT를 능가한다는 것을 보여줍니다. 그러나 두 모델 간의 평균 차이는 작으며, 사전 학습 모델이 항상 메타 학습 모델보다 우수하다는 기존 믿음에 반하는 결과를 제시합니다. 21개의 소수 샷 학습 벤치마크 실험을 통해 데이터셋의 형식적 다양성이 중요한 요인임을 결론지었습니다.

## 🎯 주요 포인트

- 1. 사전 학습된 모델(PT)은 데이터셋의 형식적 다양성이 낮을 때 MAML보다 평균적으로 우수하다.
- 2. 데이터셋의 형식적 다양성이 높을 때는 MAML이 PT보다 평균적으로 우수하다.
- 3. PT와 MAML 간의 평균 차이는 효과 크기 기준으로 낮으며, 이는 사전 학습된 모델이 항상 메타 학습 모델보다 우수하다는 기존 믿음과 반대된다.
- 4. 21개의 소수 샷 학습 벤치마크 실험 결과, 사전 학습된 모델이 항상 메타 학습 모델보다 우수하지 않음을 확인했다.
- 5. 데이터셋의 형식적 다양성이 모델 성능에 중요한 영향을 미친다.


---

*Generated on 2025-09-24 14:23:21*