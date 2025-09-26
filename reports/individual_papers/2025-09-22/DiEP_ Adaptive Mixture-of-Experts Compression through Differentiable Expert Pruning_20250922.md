---
keywords:
  - Mixture-of-Experts
  - Differentiable Expert Pruning
  - Natural Language Processing
  - Adaptive Gradient-based Pruning
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.16105
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:35:39.305060",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts",
    "Differentiable Expert Pruning",
    "Natural Language Processing",
    "Adaptive Gradient-based Pruning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts": 0.78,
    "Differentiable Expert Pruning": 0.8,
    "Natural Language Processing": 0.85,
    "Adaptive Gradient-based Pruning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "unique_technical",
        "rationale": "Mixture-of-Experts is central to the paper's methodology and offers a unique approach to model compression.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Differentiable Expert Pruning",
        "canonical": "Differentiable Expert Pruning",
        "aliases": [
          "DiEP"
        ],
        "category": "unique_technical",
        "rationale": "This is the core technique introduced in the paper, offering a novel pruning strategy.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "The paper's experiments are conducted within the NLP domain, providing context for application.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "adaptive gradient-based pruning",
        "canonical": "Adaptive Gradient-based Pruning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for understanding the adaptive mechanisms in the proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Differentiable Expert Pruning",
      "resolved_canonical": "Differentiable Expert Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "adaptive gradient-based pruning",
      "resolved_canonical": "Adaptive Gradient-based Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning

**Korean Title:** DiEP: 미분 가능한 전문가 가지치기를 통한 적응형 전문가 혼합 압축

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16105.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.16105](https://arxiv.org/abs/2509.16105)

## 🔗 유사한 논문
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (85.0% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (84.6% similar)
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (84.2% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.7% similar)
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Adaptive Gradient-based Pruning|Adaptive Gradient-based Pruning]]
**⚡ Unique Technical**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]], [[keywords/Differentiable Expert Pruning|Differentiable Expert Pruning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16105v1 Announce Type: new 
Abstract: Despite the significant breakthrough of Mixture-of-Experts (MoE), the increasing scale of these MoE models presents huge memory and storage challenges. Existing MoE pruning methods, which involve reducing parameter size with a uniform sparsity across all layers, often lead to suboptimal outcomes and performance degradation due to varying expert redundancy in different MoE layers. To address this, we propose a non-uniform pruning strategy, dubbed \textbf{Di}fferentiable \textbf{E}xpert \textbf{P}runing (\textbf{DiEP}), which adaptively adjusts pruning rates at the layer level while jointly learning inter-layer importance, effectively capturing the varying redundancy across different MoE layers. By transforming the global discrete search space into a continuous one, our method handles exponentially growing non-uniform expert combinations, enabling adaptive gradient-based pruning. Extensive experiments on five advanced MoE models demonstrate the efficacy of our method across various NLP tasks. Notably, \textbf{DiEP} retains around 92\% of original performance on Mixtral 8$\times$7B with only half the experts, outperforming other pruning methods by up to 7.1\% on the challenging MMLU dataset.

## 🔍 Abstract (한글 번역)

arXiv:2509.16105v1 발표 유형: 신규  
초록: Mixture-of-Experts (MoE)의 상당한 발전에도 불구하고, 이러한 MoE 모델의 규모가 커지면서 메모리와 저장 공간에 큰 도전 과제가 생기고 있습니다. 모든 층에 걸쳐 균일한 희소성을 적용하여 매개변수 크기를 줄이는 기존의 MoE 가지치기 방법은 서로 다른 MoE 층에서 전문가 중복성이 다르기 때문에 최적이 아닌 결과와 성능 저하를 초래하는 경우가 많습니다. 이를 해결하기 위해, 우리는 \textbf{Di}fferentiable \textbf{E}xpert \textbf{P}runing (\textbf{DiEP})이라는 비균일 가지치기 전략을 제안합니다. 이는 층 수준에서 가지치기 비율을 적응적으로 조정하면서 층 간 중요성을 공동으로 학습하여, 서로 다른 MoE 층에서의 중복성을 효과적으로 포착합니다. 전역 이산 탐색 공간을 연속적인 공간으로 변환함으로써, 우리의 방법은 기하급수적으로 증가하는 비균일 전문가 조합을 처리하고, 적응형 그래디언트 기반 가지치기를 가능하게 합니다. 다섯 개의 고급 MoE 모델에 대한 광범위한 실험은 다양한 NLP 작업에서 우리의 방법의 효능을 입증합니다. 특히, \textbf{DiEP}는 Mixtral 8$\times$7B에서 전문가의 절반만으로도 원래 성능의 약 92\%를 유지하며, 도전적인 MMLU 데이터셋에서 다른 가지치기 방법보다 최대 7.1\% 더 우수한 성능을 보입니다.

## 📝 요약

이 논문은 Mixture-of-Experts (MoE) 모델의 메모리 및 저장 문제를 해결하기 위해 비균일한 가지치기 전략인 DiEP(Differentiable Expert Pruning)을 제안합니다. 기존의 균일한 가지치기 방법은 각 층의 전문가 중복도가 다름에도 불구하고 모든 층에 동일한 희소성을 적용하여 성능 저하를 초래했습니다. DiEP는 층별 중요도를 학습하며 가지치기 비율을 조정하여 이러한 문제를 해결합니다. 이 방법은 전역 이산 탐색 공간을 연속적으로 변환하여 적응형 그래디언트 기반 가지치기를 가능하게 합니다. 실험 결과, DiEP는 다양한 NLP 작업에서 우수한 성능을 보였으며, 특히 Mixtral 8×7B 모델에서 절반의 전문가만 사용하면서도 원래 성능의 약 92%를 유지하며, MMLU 데이터셋에서 다른 방법보다 최대 7.1% 높은 성능을 기록했습니다.

## 🎯 주요 포인트

- 1. Mixture-of-Experts(MoE) 모델의 확장으로 인한 메모리 및 저장 문제를 해결하기 위해 비균일한 가지치기 전략인 DiEP를 제안합니다.
- 2. DiEP는 레이어별 중요도를 학습하여 각 MoE 레이어의 중복성을 효과적으로 포착하고, 레이어 수준에서 가지치기 비율을 조정합니다.
- 3. 글로벌 이산 탐색 공간을 연속적인 공간으로 변환하여 적응형 그래디언트 기반 가지치기를 가능하게 합니다.
- 4. DiEP는 Mixtral 8×7B 모델에서 절반의 전문가만으로도 원래 성능의 약 92%를 유지하며, 다른 가지치기 방법보다 MMLU 데이터셋에서 최대 7.1% 더 우수한 성능을 보입니다.
- 5. 제안된 방법은 다양한 NLP 작업에서 5개의 고급 MoE 모델에 대한 실험을 통해 그 효능을 입증했습니다.


---

*Generated on 2025-09-23 11:35:39*