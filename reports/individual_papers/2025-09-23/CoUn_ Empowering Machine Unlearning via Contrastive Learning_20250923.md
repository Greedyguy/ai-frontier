---
keywords:
  - Machine Unlearning
  - Contrastive Learning
  - Semantic Similarity
  - Supervised Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16391
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:17:41.289773",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Unlearning",
    "Contrastive Learning",
    "Semantic Similarity",
    "Supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Unlearning": 0.88,
    "Contrastive Learning": 0.8,
    "Semantic Similarity": 0.77,
    "Supervised Learning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Unlearning",
        "canonical": "Machine Unlearning",
        "aliases": [
          "MU"
        ],
        "category": "unique_technical",
        "rationale": "Machine Unlearning is a novel concept central to the paper, enhancing connectivity with discussions on data privacy and model adaptation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Contrastive Learning",
        "aliases": [
          "CL"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive Learning is a key technique used in the paper, linking it to broader discussions on representation learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.84,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Semantic Similarity",
        "canonical": "Semantic Similarity",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Semantic Similarity is crucial for understanding how the model differentiates between 'retain' and 'forget' data.",
        "novelty_score": 0.6,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Supervised Learning",
        "canonical": "Supervised Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Supervised Learning is a fundamental technique applied to retain data, connecting to a wide range of machine learning discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "model weight perturbations",
      "label manipulation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Unlearning",
      "resolved_canonical": "Machine Unlearning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.84,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Semantic Similarity",
      "resolved_canonical": "Semantic Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Supervised Learning",
      "resolved_canonical": "Supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CoUn: Empowering Machine Unlearning via Contrastive Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16391.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16391](https://arxiv.org/abs/2509.16391)

## 🔗 유사한 논문
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG: Curriculum Unlearning Guided by the Forgetting Gradient]] (86.2% similar)
- [[2025-09-22/Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets_20250922|Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets]] (85.6% similar)
- [[2025-09-22/ToFU_ Transforming How Federated Learning Systems Forget User Data_20250922|ToFU: Transforming How Federated Learning Systems Forget User Data]] (83.7% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (83.5% similar)
- [[2025-09-22/Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models_20250922|Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Supervised Learning|Supervised Learning]]
**🔗 Specific Connectable**: [[keywords/Contrastive Learning|Contrastive Learning]], [[keywords/Semantic Similarity|Semantic Similarity]]
**⚡ Unique Technical**: [[keywords/Machine Unlearning|Machine Unlearning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16391v1 Announce Type: cross 
Abstract: Machine unlearning (MU) aims to remove the influence of specific "forget" data from a trained model while preserving its knowledge of the remaining "retain" data. Existing MU methods based on label manipulation or model weight perturbations often achieve limited unlearning effectiveness. To address this, we introduce CoUn, a novel MU framework inspired by the observation that a model retrained from scratch using only retain data classifies forget data based on their semantic similarity to the retain data. CoUn emulates this behavior by adjusting learned data representations through contrastive learning (CL) and supervised learning, applied exclusively to retain data. Specifically, CoUn (1) leverages semantic similarity between data samples to indirectly adjust forget representations using CL, and (2) maintains retain representations within their respective clusters through supervised learning. Extensive experiments across various datasets and model architectures show that CoUn consistently outperforms state-of-the-art MU baselines in unlearning effectiveness. Additionally, integrating our CL module into existing baselines empowers their unlearning effectiveness.

## 📝 요약

이 논문은 기계 학습 모델에서 특정 데이터를 잊게 하는 '기계 언러닝(MU)'의 효과를 개선하기 위해 새로운 프레임워크 CoUn을 제안합니다. 기존의 MU 방법들은 레이블 조작이나 모델 가중치 변화를 사용하지만, 효과가 제한적입니다. CoUn은 남겨야 할 데이터만으로 모델을 재훈련했을 때, 잊어야 할 데이터를 남겨야 할 데이터와의 의미적 유사성에 따라 분류한다는 점에 착안했습니다. CoUn은 대조 학습과 지도 학습을 통해 남겨야 할 데이터의 표현을 조정하여 이를 모방합니다. 실험 결과, CoUn은 다양한 데이터셋과 모델 구조에서 기존의 최첨단 MU 방법들보다 일관되게 뛰어난 성능을 보였으며, 기존 방법에 CL 모듈을 통합하면 언러닝 효과가 향상됨을 확인했습니다.

## 🎯 주요 포인트

- 1. CoUn은 특정 "잊어야 할" 데이터의 영향을 제거하면서 "유지할" 데이터의 지식을 보존하는 새로운 기계 학습 프레임워크입니다.
- 2. CoUn은 대조 학습과 지도 학습을 통해 학습된 데이터 표현을 조정하여 잊어야 할 데이터의 표현을 간접적으로 조정합니다.
- 3. CoUn은 다양한 데이터셋과 모델 아키텍처에서 기존의 최첨단 기계 학습 방법보다 일관되게 더 높은 잊기 효과를 보여줍니다.
- 4. CoUn의 대조 학습 모듈을 기존의 기계 학습 방법에 통합하면 잊기 효과가 향상됩니다.


---

*Generated on 2025-09-23 23:17:41*