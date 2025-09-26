---
keywords:
  - Neural Network
  - Adversarial Attack
  - Dynamical Low-Rank Training
  - Spectral Regularizer
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2505.08022
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:43:01.254566",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Adversarial Attack",
    "Dynamical Low-Rank Training",
    "Spectral Regularizer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Adversarial Attack": 0.78,
    "Dynamical Low-Rank Training": 0.7,
    "Spectral Regularizer": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "neural networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "neural nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the study and are a key concept in machine learning, facilitating connections across various related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "adversarial attacks",
        "canonical": "Adversarial Attack",
        "aliases": [
          "adversarial input",
          "adversarial perturbation"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial attacks are a specific challenge addressed in the paper, linking to security and robustness in neural networks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "dynamical low-rank training",
        "canonical": "Dynamical Low-Rank Training",
        "aliases": [
          "low-rank training",
          "dynamic rank training"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, offering unique insights into model compression techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "spectral regularizer",
        "canonical": "Spectral Regularizer",
        "aliases": [
          "spectral regularization"
        ],
        "category": "unique_technical",
        "rationale": "The spectral regularizer is a unique component of the proposed method, crucial for controlling model robustness.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
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
      "candidate_surface": "neural networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "adversarial attacks",
      "resolved_canonical": "Adversarial Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "dynamical low-rank training",
      "resolved_canonical": "Dynamical Low-Rank Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "spectral regularizer",
      "resolved_canonical": "Spectral Regularizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.08022.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2505.08022](https://arxiv.org/abs/2505.08022)

## 🔗 유사한 논문
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (86.1% similar)
- [[2025-09-23/Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection_20250923|Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection]] (86.0% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (85.1% similar)
- [[2025-09-23/Train to Defend_ First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks_20250923|Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks]] (83.0% similar)
- [[2025-09-22/RMT-KD_ Random Matrix Theoretic Causal Knowledge Distillation_20250922|RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Adversarial Attack|Adversarial Attack]]
**⚡ Unique Technical**: [[keywords/Dynamical Low-Rank Training|Dynamical Low-Rank Training]], [[keywords/Spectral Regularizer|Spectral Regularizer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.08022v2 Announce Type: replace 
Abstract: Deployment of neural networks on resource-constrained devices demands models that are both compact and robust to adversarial inputs. However, compression and adversarial robustness often conflict. In this work, we introduce a dynamical low-rank training scheme enhanced with a novel spectral regularizer that controls the condition number of the low-rank core in each layer. This approach mitigates the sensitivity of compressed models to adversarial perturbations without sacrificing clean accuracy. The method is model- and data-agnostic, computationally efficient, and supports rank adaptivity to automatically compress the network at hand. Extensive experiments across standard architectures, datasets, and adversarial attacks show the regularized networks can achieve over 94% compression while recovering or improving adversarial accuracy relative to uncompressed baselines.

## 📝 요약

이 연구는 자원이 제한된 장치에서 신경망을 효과적으로 배포하기 위해, 압축과 적대적 공격에 대한 강건성을 동시에 달성하는 방법을 제안합니다. 저자들은 각 층의 저랭크 핵심의 조건수를 제어하는 새로운 스펙트럼 정규화를 포함한 동적 저랭크 학습 기법을 도입했습니다. 이 방법은 압축된 모델의 적대적 교란에 대한 민감성을 줄이면서도 정확도를 유지합니다. 이 기법은 모델과 데이터에 독립적이며, 계산 효율성이 높고 자동으로 네트워크를 압축할 수 있습니다. 실험 결과, 정규화된 네트워크는 94% 이상의 압축을 달성하면서도 비압축 기준 모델과 비교해 적대적 정확도를 회복하거나 향상시켰습니다.

## 🎯 주요 포인트

- 1. 신경망의 압축과 적대적 견고성 간의 갈등을 해결하기 위해 새로운 스펙트럼 정규화 기법을 도입한 동적 저랭크 훈련 방식을 제안합니다.
- 2. 제안된 방법은 모델과 데이터에 무관하게 적용 가능하며, 계산 효율적이고 랭크 적응성을 지원하여 네트워크를 자동으로 압축합니다.
- 3. 다양한 표준 아키텍처, 데이터셋, 적대적 공격에 대한 실험 결과, 정규화된 네트워크는 94% 이상의 압축을 달성하면서도 비압축 기준보다 적대적 정확도를 회복하거나 개선할 수 있음을 보여줍니다.
- 4. 이 접근 방식은 압축된 모델의 적대적 교란에 대한 민감성을 줄이면서도 깨끗한 정확도를 희생하지 않습니다.


---

*Generated on 2025-09-24 02:43:01*