---
keywords:
  - Graph Neural Network
  - Attention Mechanism
  - Multi-Scale Representation
  - Uncertainty Estimation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15256
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:50:04.071999",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Attention Mechanism",
    "Multi-Scale Representation",
    "Uncertainty Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.82,
    "Attention Mechanism": 0.85,
    "Multi-Scale Representation": 0.78,
    "Uncertainty Estimation": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Process",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNP"
        ],
        "category": "specific_connectable",
        "rationale": "This concept extends Graph Neural Networks by incorporating process-based learning, enhancing connectivity with existing graph-based models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Cross-Drug Co-Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Drug Co-Attention"
        ],
        "category": "specific_connectable",
        "rationale": "This mechanism is a specialized form of attention, facilitating connections with other attention-based models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Scale Representation",
        "canonical": "Multi-Scale Representation",
        "aliases": [
          "Hierarchical Representation"
        ],
        "category": "unique_technical",
        "rationale": "Captures structural information across scales, crucial for linking to hierarchical data processing techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.78
      },
      {
        "surface": "Uncertainty Estimation",
        "canonical": "Uncertainty Estimation",
        "aliases": [
          "Prediction Confidence"
        ],
        "category": "unique_technical",
        "rationale": "Provides a mechanism for evaluating prediction reliability, linking to probabilistic modeling approaches.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "drug-drug interactions",
      "medication safety",
      "effective drug development"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Process",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Cross-Drug Co-Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-Scale Representation",
      "resolved_canonical": "Multi-Scale Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Uncertainty Estimation",
      "resolved_canonical": "Uncertainty Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction

**Korean Title:** 다중 스케일 그래프 신경 프로세스와 교차 약물 공동 주의를 활용한 약물 상호작용 예측

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15256.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15256](https://arxiv.org/abs/2509.15256)

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (83.0% similar)
- [[2025-09-22/Detail Across Scales_ Multi-Scale Enhancement for Full Spectrum Neural Representations_20250922|Detail Across Scales: Multi-Scale Enhancement for Full Spectrum Neural Representations]] (79.2% similar)
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (78.8% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (77.8% similar)
- [[2025-09-19/DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO: Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (77.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Multi-Scale Representation|Multi-Scale Representation]], [[keywords/Uncertainty Estimation|Uncertainty Estimation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15256v1 Announce Type: cross 
Abstract: Accurate prediction of drug-drug interactions (DDI) is crucial for medication safety and effective drug development. However, existing methods often struggle to capture structural information across different scales, from local functional groups to global molecular topology, and typically lack mechanisms to quantify prediction confidence. To address these limitations, we propose MPNP-DDI, a novel Multi-scale Graph Neural Process framework. The core of MPNP-DDI is a unique message-passing scheme that, by being iteratively applied, learns a hierarchy of graph representations at multiple scales. Crucially, a cross-drug co-attention mechanism then dynamically fuses these multi-scale representations to generate context-aware embeddings for interacting drug pairs, while an integrated neural process module provides principled uncertainty estimation. Extensive experiments demonstrate that MPNP-DDI significantly outperforms state-of-the-art baselines on benchmark datasets. By providing accurate, generalizable, and uncertainty-aware predictions built upon multi-scale structural features, MPNP-DDI represents a powerful computational tool for pharmacovigilance, polypharmacy risk assessment, and precision medicine.

## 🔍 Abstract (한글 번역)

arXiv:2509.15256v1 발표 유형: 교차  
초록: 약물 간 상호작용(DDI)의 정확한 예측은 약물 안전성과 효과적인 약물 개발에 필수적입니다. 그러나 기존 방법들은 종종 지역적 기능 그룹에서 전역 분자 위상에 이르기까지 다양한 규모의 구조적 정보를 포착하는 데 어려움을 겪으며, 일반적으로 예측 신뢰도를 정량화할 수 있는 메커니즘이 부족합니다. 이러한 한계를 극복하기 위해, 우리는 MPNP-DDI라는 새로운 다중 규모 그래프 신경 프로세스 프레임워크를 제안합니다. MPNP-DDI의 핵심은 반복적으로 적용되어 여러 규모에서 그래프 표현의 계층을 학습하는 독특한 메시지 전달 방식입니다. 중요한 것은, 교차 약물 공동 주의 메커니즘이 이러한 다중 규모 표현을 동적으로 융합하여 상호작용하는 약물 쌍에 대한 맥락 인식 임베딩을 생성하며, 통합된 신경 프로세스 모듈은 원칙적인 불확실성 추정을 제공합니다. 광범위한 실험 결과, MPNP-DDI가 벤치마크 데이터셋에서 최첨단 기준 모델들을 크게 능가함을 보여줍니다. 다중 규모 구조적 특징에 기반하여 정확하고 일반화 가능하며 불확실성을 인식하는 예측을 제공함으로써, MPNP-DDI는 약물 감시, 다약제 위험 평가, 정밀 의학을 위한 강력한 계산 도구를 대표합니다.

## 📝 요약

이 논문은 약물 상호작용(DDI) 예측의 정확성을 높이기 위해 MPNP-DDI라는 새로운 다중 스케일 그래프 신경 프로세스 프레임워크를 제안합니다. MPNP-DDI는 독특한 메시지 전달 방식을 통해 여러 스케일에서 그래프 표현을 학습하며, 교차 약물 주의 메커니즘을 통해 상호작용하는 약물 쌍의 문맥 인식 임베딩을 생성합니다. 또한, 통합된 신경 프로세스 모듈을 통해 예측의 불확실성을 정량화합니다. 실험 결과, MPNP-DDI는 기존 방법들보다 뛰어난 성능을 보였으며, 다중 스케일 구조적 특징을 기반으로 정확하고 일반화 가능하며 불확실성을 고려한 예측을 제공하여 약물 감시, 다약제 위험 평가, 정밀 의학에 유용한 도구로 자리잡을 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. MPNP-DDI는 다중 스케일 그래프 신경 프로세스 프레임워크로, 약물 간 상호작용 예측의 정확성을 높입니다.
- 2. 이 프레임워크는 메시지 전달 방식을 통해 여러 스케일에서 그래프 표현의 계층 구조를 학습합니다.
- 3. 교차 약물 공동 주의 메커니즘을 사용하여 다중 스케일 표현을 동적으로 융합하고, 상호작용하는 약물 쌍에 대한 문맥 인식 임베딩을 생성합니다.
- 4. 통합된 신경 프로세스 모듈은 예측의 불확실성을 정량화하는 기능을 제공합니다.
- 5. MPNP-DDI는 벤치마크 데이터셋에서 최신 기법들을 능가하며, 약물 감시, 다약제 위험 평가, 정밀 의학에 강력한 도구로 활용될 수 있습니다.


---

*Generated on 2025-09-23 08:50:04*