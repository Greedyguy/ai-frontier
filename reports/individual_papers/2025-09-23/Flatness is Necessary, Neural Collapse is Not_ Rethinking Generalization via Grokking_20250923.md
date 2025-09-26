---
keywords:
  - Neural Collapse
  - Flatness
  - Grokking
  - Generalization
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17738
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:56:17.626563",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Collapse",
    "Flatness",
    "Grokking",
    "Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Collapse": 0.78,
    "Flatness": 0.77,
    "Grokking": 0.75,
    "Generalization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Collapse",
        "canonical": "Neural Collapse",
        "aliases": [
          "Class-wise Clustered Representations"
        ],
        "category": "unique_technical",
        "rationale": "Neural Collapse is a unique phenomenon observed in deep networks that is crucial for understanding generalization processes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Flatness",
        "canonical": "Flatness",
        "aliases": [
          "Loss Landscape Flatness"
        ],
        "category": "unique_technical",
        "rationale": "Flatness is a key geometric property linked to generalization, offering a distinct perspective on model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Grokking",
        "canonical": "Grokking",
        "aliases": [
          "Memorization Preceding Generalization"
        ],
        "category": "unique_technical",
        "rationale": "Grokking provides a unique training regime to study the temporal separation of memorization and generalization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Generalization",
        "canonical": "Generalization",
        "aliases": [
          "Model Generalization"
        ],
        "category": "broad_technical",
        "rationale": "Generalization is a fundamental concept in machine learning, central to understanding model performance.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Training Dynamics",
      "Empirical Co-occurrence"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Collapse",
      "resolved_canonical": "Neural Collapse",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Flatness",
      "resolved_canonical": "Flatness",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Grokking",
      "resolved_canonical": "Grokking",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Generalization",
      "resolved_canonical": "Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Flatness is Necessary, Neural Collapse is Not: Rethinking Generalization via Grokking

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17738.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17738](https://arxiv.org/abs/2509.17738)

## 🔗 유사한 논문
- [[2025-09-22/Navigate Beyond Shortcuts_ Debiased Learning through the Lens of Neural Collapse_20250922|Navigate Beyond Shortcuts: Debiased Learning through the Lens of Neural Collapse]] (81.2% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (81.1% similar)
- [[2025-09-23/A Closer Look at Model Collapse_ From a Generalization-to-Memorization Perspective_20250923|A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective]] (80.1% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (78.1% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generalization|Generalization]]
**⚡ Unique Technical**: [[keywords/Neural Collapse|Neural Collapse]], [[keywords/Flatness|Flatness]], [[keywords/Grokking|Grokking]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17738v1 Announce Type: new 
Abstract: Neural collapse, i.e., the emergence of highly symmetric, class-wise clustered representations, is frequently observed in deep networks and is often assumed to reflect or enable generalization. In parallel, flatness of the loss landscape has been theoretically and empirically linked to generalization. Yet, the causal role of either phenomenon remains unclear: Are they prerequisites for generalization, or merely by-products of training dynamics? We disentangle these questions using grokking, a training regime in which memorization precedes generalization, allowing us to temporally separate generalization from training dynamics and we find that while both neural collapse and relative flatness emerge near the onset of generalization, only flatness consistently predicts it. Models encouraged to collapse or prevented from collapsing generalize equally well, whereas models regularized away from flat solutions exhibit delayed generalization. Furthermore, we show theoretically that neural collapse implies relative flatness under classical assumptions, explaining their empirical co-occurrence. Our results support the view that relative flatness is a potentially necessary and more fundamental property for generalization, and demonstrate how grokking can serve as a powerful probe for isolating its geometric underpinnings.

## 📝 요약

이 논문은 신경 붕괴와 손실 지형의 평탄함이 일반화에 미치는 영향을 분석합니다. 연구는 'grokking'이라는 훈련 체제를 사용하여 일반화와 훈련 동력을 시간적으로 분리합니다. 실험 결과, 신경 붕괴와 평탄함 모두 일반화 시작 시점에 나타나지만, 평탄함만이 일관되게 일반화를 예측합니다. 붕괴를 유도하거나 방지한 모델은 일반화에 차이가 없었으나, 평탄한 해를 피하도록 정규화된 모델은 일반화가 지연되었습니다. 이론적으로 신경 붕괴가 평탄함을 암시함을 보이며, 평탄함이 일반화에 더 근본적인 속성임을 제안합니다.

## 🎯 주요 포인트

- 1. 신경 붕괴와 손실 지형의 평탄함은 일반화와 관련이 있지만, 그 인과적 역할은 불분명하다.
- 2. grokking 훈련 체제를 통해 일반화와 훈련 역학을 시간적으로 분리하여 연구를 진행했다.
- 3. 신경 붕괴와 평탄함은 일반화 시작 시점에 나타나지만, 평탄함만이 일관되게 일반화를 예측한다.
- 4. 신경 붕괴는 상대적 평탄함을 암시하며, 이는 이들의 경험적 동시 발생을 설명한다.
- 5. 연구 결과는 상대적 평탄함이 일반화를 위한 잠재적으로 필수적이고 근본적인 속성임을 지지한다.


---

*Generated on 2025-09-24 01:56:17*