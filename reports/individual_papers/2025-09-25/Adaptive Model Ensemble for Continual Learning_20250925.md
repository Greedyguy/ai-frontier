---
keywords:
  - Model Ensemble
  - Continual Learning
  - Catastrophic Forgetting
  - Meta-learning
  - Meta-weight-ensembler
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19819
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:07:37.342319",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Model Ensemble",
    "Continual Learning",
    "Catastrophic Forgetting",
    "Meta-learning",
    "Meta-weight-ensembler"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Model Ensemble": 0.81,
    "Continual Learning": 0.88,
    "Catastrophic Forgetting": 0.84,
    "Meta-learning": 0.8,
    "Meta-weight-ensembler": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Model Ensemble",
        "canonical": "Model Ensemble",
        "aliases": [
          "Ensemble Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Model ensemble is a key technique in continual learning, facilitating knowledge fusion and mitigating catastrophic forgetting.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.81
      },
      {
        "surface": "Continual Learning",
        "canonical": "Continual Learning",
        "aliases": [
          "Lifelong Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Continual learning is a central theme of the paper, addressing the challenge of learning across tasks without forgetting.",
        "novelty_score": 0.48,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Catastrophic Forgetting",
        "canonical": "Catastrophic Forgetting",
        "aliases": [
          "Forgetting in Neural Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Catastrophic forgetting is a critical issue in continual learning that the proposed method aims to alleviate.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.77,
        "link_intent_score": 0.84
      },
      {
        "surface": "Meta-learning",
        "canonical": "Meta-learning",
        "aliases": [
          "Learning to Learn"
        ],
        "category": "specific_connectable",
        "rationale": "Meta-learning is used to train the mixing coefficient generator, making it integral to the proposed solution.",
        "novelty_score": 0.52,
        "connectivity_score": 0.79,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Meta-weight-ensembler",
        "canonical": "Meta-weight-ensembler",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is the novel method proposed in the paper, specifically designed to address knowledge conflicts in model ensembles.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "knowledge fusion",
      "mixing coefficient"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Model Ensemble",
      "resolved_canonical": "Model Ensemble",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Continual Learning",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Catastrophic Forgetting",
      "resolved_canonical": "Catastrophic Forgetting",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.77,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "Meta-learning",
      "resolved_canonical": "Meta-learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.79,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Meta-weight-ensembler",
      "resolved_canonical": "Meta-weight-ensembler",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Adaptive Model Ensemble for Continual Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19819.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19819](https://arxiv.org/abs/2509.19819)

## 🔗 유사한 논문
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (82.7% similar)
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (82.4% similar)
- [[2025-09-23/Learning to Learn with Contrastive Meta-Objective_20250923|Learning to Learn with Contrastive Meta-Objective]] (80.6% similar)
- [[2025-09-24/Statistical Insight into Meta-Learning via Predictor Subspace Characterization and Quantification of Task Diversity_20250924|Statistical Insight into Meta-Learning via Predictor Subspace Characterization and Quantification of Task Diversity]] (80.6% similar)
- [[2025-09-24/Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning_20250924|Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Model Ensemble|Model Ensemble]], [[keywords/Continual Learning|Continual Learning]], [[keywords/Catastrophic Forgetting|Catastrophic Forgetting]], [[keywords/Meta-learning|Meta-learning]]
**⚡ Unique Technical**: [[keywords/Meta-weight-ensembler|Meta-weight-ensembler]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19819v1 Announce Type: new 
Abstract: Model ensemble is an effective strategy in continual learning, which alleviates catastrophic forgetting by interpolating model parameters, achieving knowledge fusion learned from different tasks. However, existing model ensemble methods usually encounter the knowledge conflict issue at task and layer levels, causing compromised learning performance in both old and new tasks. To solve this issue, we propose meta-weight-ensembler that adaptively fuses knowledge of different tasks for continual learning. Concretely, we employ a mixing coefficient generator trained via meta-learning to generate appropriate mixing coefficients for model ensemble to address the task-level knowledge conflict. The mixing coefficient is individually generated for each layer to address the layer-level knowledge conflict. In this way, we learn the prior knowledge about adaptively accumulating knowledge of different tasks in a fused model, achieving efficient learning in both old and new tasks. Meta-weight-ensembler can be flexibly combined with existing continual learning methods to boost their ability of alleviating catastrophic forgetting. Experiments on multiple continual learning datasets show that meta-weight-ensembler effectively alleviates catastrophic forgetting and achieves state-of-the-art performance.

## 📝 요약

이 논문은 연속 학습에서 발생하는 지식 충돌 문제를 해결하기 위해 메타-웨이트-엔셈블러(meta-weight-ensembler)를 제안합니다. 기존 모델 앙상블 방법은 과거와 새로운 작업 간의 학습 성능 저하를 초래하는 지식 충돌 문제를 겪습니다. 이를 해결하기 위해, 메타-웨이트-엔셈블러는 메타러닝을 통해 훈련된 혼합 계수 생성기를 사용하여 작업 수준과 층 수준에서 적절한 혼합 계수를 생성합니다. 이를 통해 다양한 작업의 지식을 적응적으로 융합하여 과거와 새로운 작업 모두에서 효율적인 학습을 달성합니다. 제안된 방법은 기존 연속 학습 방법과 유연하게 결합할 수 있으며, 실험 결과는 이 방법이 망각 현상을 효과적으로 완화하고 최첨단 성능을 달성함을 보여줍니다.

## 🎯 주요 포인트

- 1. 모델 앙상블은 연속 학습에서 모델 파라미터를 보간하여 서로 다른 작업에서 학습한 지식을 융합함으로써 망각을 완화하는 효과적인 전략입니다.
- 2. 기존 모델 앙상블 방법은 작업 및 레이어 수준에서 지식 충돌 문제를 겪어 학습 성능이 저하됩니다.
- 3. 메타-웨이트-앙상블러는 메타 러닝을 통해 학습된 혼합 계수 생성기를 사용하여 작업 수준 및 레이어 수준의 지식 충돌을 해결합니다.
- 4. 메타-웨이트-앙상블러는 기존 연속 학습 방법과 유연하게 결합하여 망각을 완화하는 능력을 향상시킬 수 있습니다.
- 5. 여러 연속 학습 데이터셋에 대한 실험 결과, 메타-웨이트-앙상블러는 망각을 효과적으로 완화하고 최첨단 성능을 달성합니다.


---

*Generated on 2025-09-26 09:07:37*