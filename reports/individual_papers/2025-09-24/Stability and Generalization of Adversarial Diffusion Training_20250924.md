<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:02:40.287236",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Adversarial Training",
    "Algorithmic Stability",
    "Generalization Gap",
    "Decentralized Networks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Adversarial Training": 0.82,
    "Algorithmic Stability": 0.78,
    "Generalization Gap": 0.8,
    "Decentralized Networks": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Adversarial Training",
        "canonical": "Adversarial Training",
        "aliases": [
          "Robust Training"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial Training is a key concept in enhancing model robustness and is central to the paper's analysis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Algorithmic Stability",
        "canonical": "Algorithmic Stability",
        "aliases": [
          "Stability Analysis"
        ],
        "category": "unique_technical",
        "rationale": "Algorithmic Stability is crucial for understanding generalization in adversarial contexts, providing a novel perspective in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Generalization Gap",
        "canonical": "Generalization Gap",
        "aliases": [
          "Generalization Error"
        ],
        "category": "specific_connectable",
        "rationale": "The Generalization Gap is a significant challenge in adversarial training, linking to broader discussions on model performance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Decentralized Networks",
        "canonical": "Decentralized Networks",
        "aliases": [
          "Distributed Networks"
        ],
        "category": "unique_technical",
        "rationale": "Decentralized Networks are a novel setting for adversarial training, expanding the scope of traditional analyses.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Convergence",
      "Training Steps"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Adversarial Training",
      "resolved_canonical": "Adversarial Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Algorithmic Stability",
      "resolved_canonical": "Algorithmic Stability",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Generalization Gap",
      "resolved_canonical": "Generalization Gap",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Decentralized Networks",
      "resolved_canonical": "Decentralized Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Stability and Generalization of Adversarial Diffusion Training

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19234.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19234](https://arxiv.org/abs/2509.19234)

## 🔗 유사한 논문
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (85.0% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (82.5% similar)
- [[2025-09-24/Algorithms for Adversarially Robust Deep Learning_20250924|Algorithms for Adversarially Robust Deep Learning]] (81.3% similar)
- [[2025-09-24/A Weighted Gradient Tracking Privacy-Preserving Method for Distributed Optimization_20250924|A Weighted Gradient Tracking Privacy-Preserving Method for Distributed Optimization]] (80.8% similar)
- [[2025-09-24/Latent Danger Zone_ Distilling Unified Attention for Cross-Architecture Black-box Attacks_20250924|Latent Danger Zone: Distilling Unified Attention for Cross-Architecture Black-box Attacks]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Adversarial Training|Adversarial Training]], [[keywords/Generalization Gap|Generalization Gap]]
**⚡ Unique Technical**: [[keywords/Algorithmic Stability|Algorithmic Stability]], [[keywords/Decentralized Networks|Decentralized Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19234v1 Announce Type: new 
Abstract: Algorithmic stability is an established tool for analyzing generalization. While adversarial training enhances model robustness, it often suffers from robust overfitting and an enlarged generalization gap. Although recent work has established the convergence of adversarial training in decentralized networks, its generalization properties remain unexplored. This work presents a stability-based generalization analysis of adversarial training under the diffusion strategy for convex losses. We derive a bound showing that the generalization error grows with both the adversarial perturbation strength and the number of training steps, a finding consistent with single-agent case but novel for decentralized settings. Numerical experiments on logistic regression validate these theoretical predictions.

## 📝 요약

이 논문은 분산 네트워크에서의 적대적 훈련의 일반화 특성을 안정성 기반으로 분석합니다. 특히, 볼록 손실 함수에 대한 확산 전략을 사용하여 일반화 오류가 적대적 교란 강도와 훈련 단계 수에 따라 증가한다는 경계를 도출했습니다. 이는 단일 에이전트 경우와 일치하면서도 분산 환경에서는 새로운 발견입니다. 로지스틱 회귀에 대한 수치 실험을 통해 이론적 예측을 검증했습니다. 주요 기여는 분산 네트워크에서의 적대적 훈련의 일반화 특성을 처음으로 규명한 것입니다.

## 🎯 주요 포인트

- 1. 알고리즘 안정성은 일반화 분석에 유용한 도구로 자리 잡고 있다.
- 2. 적대적 훈련은 모델의 강건성을 향상시키지만, 강건 과적합 및 일반화 간격 확대 문제를 겪는다.
- 3. 본 연구는 분산 네트워크에서 적대적 훈련의 수렴성을 확립한 최근 연구와 달리, 일반화 특성을 탐구한다.
- 4. 확산 전략 하에서 볼록 손실에 대한 적대적 훈련의 안정성 기반 일반화 분석을 제시한다.
- 5. 일반화 오류가 적대적 교란 강도와 훈련 단계 수에 따라 증가한다는 경계를 도출하였으며, 이는 단일 에이전트 경우와 일치하지만 분산 설정에서는 새로운 발견이다.


---

*Generated on 2025-09-24 15:02:40*