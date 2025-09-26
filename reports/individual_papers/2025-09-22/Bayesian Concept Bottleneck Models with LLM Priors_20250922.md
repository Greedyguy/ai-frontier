---
keywords:
  - Concept Bottleneck Models
  - Large Language Model
  - Bayesian Framework
  - Interpretability-Accuracy Tradeoff
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2410.15555
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:47:56.801622",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Concept Bottleneck Models",
    "Large Language Model",
    "Bayesian Framework",
    "Interpretability-Accuracy Tradeoff"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Concept Bottleneck Models": 0.78,
    "Large Language Model": 0.82,
    "Bayesian Framework": 0.79,
    "Interpretability-Accuracy Tradeoff": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Concept Bottleneck Models",
        "canonical": "Concept Bottleneck Models",
        "aliases": [
          "CBM",
          "Concept Bottleneck"
        ],
        "category": "unique_technical",
        "rationale": "This is a central concept in the paper, representing a specific model architecture that balances interpretability and accuracy.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are used as a concept extraction mechanism and prior, crucial for understanding the paper's methodology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bayesian Framework",
        "canonical": "Bayesian Framework",
        "aliases": [
          "Bayesian Approach",
          "Bayesian Method"
        ],
        "category": "specific_connectable",
        "rationale": "The Bayesian framework is key to the novel approach proposed, enabling rigorous statistical inference.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Interpretability-Accuracy Tradeoff",
        "canonical": "Interpretability-Accuracy Tradeoff",
        "aliases": [
          "Interpretability Tradeoff"
        ],
        "category": "unique_technical",
        "rationale": "This tradeoff is a critical issue addressed by the proposed model, relevant for linking discussions on model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
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
      "candidate_surface": "Concept Bottleneck Models",
      "resolved_canonical": "Concept Bottleneck Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bayesian Framework",
      "resolved_canonical": "Bayesian Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Interpretability-Accuracy Tradeoff",
      "resolved_canonical": "Interpretability-Accuracy Tradeoff",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Bayesian Concept Bottleneck Models with LLM Priors

**Korean Title:** 베이지안 개념 병목 모델과 대형 언어 모델 사전 분포

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.15555.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2410.15555](https://arxiv.org/abs/2410.15555)

## 🔗 유사한 논문
- [[2025-09-19/EnCoBo_ Energy-Guided Concept Bottlenecks for Interpretable Generation_20250919|EnCoBo: Energy-Guided Concept Bottlenecks for Interpretable Generation]] (83.7% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (81.9% similar)
- [[2025-09-22/Capturing Polysemanticity with PRISM_ A Multi-Concept Feature Description Framework_20250922|Capturing Polysemanticity with PRISM: A Multi-Concept Feature Description Framework]] (81.0% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (81.0% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Bayesian Framework|Bayesian Framework]]
**⚡ Unique Technical**: [[keywords/Concept Bottleneck Models|Concept Bottleneck Models]], [[keywords/Interpretability-Accuracy Tradeoff|Interpretability-Accuracy Tradeoff]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.15555v2 Announce Type: replace-cross 
Abstract: Concept Bottleneck Models (CBMs) have been proposed as a compromise between white-box and black-box models, aiming to achieve interpretability without sacrificing accuracy. The standard training procedure for CBMs is to predefine a candidate set of human-interpretable concepts, extract their values from the training data, and identify a sparse subset as inputs to a transparent prediction model. However, such approaches are often hampered by the tradeoff between exploring a sufficiently large set of concepts versus controlling the cost of obtaining concept extractions, resulting in a large interpretability-accuracy tradeoff. This work investigates a novel approach that sidesteps these challenges: BC-LLM iteratively searches over a potentially infinite set of concepts within a Bayesian framework, in which Large Language Models (LLMs) serve as both a concept extraction mechanism and prior. Even though LLMs can be miscalibrated and hallucinate, we prove that BC-LLM can provide rigorous statistical inference and uncertainty quantification. Across image, text, and tabular datasets, BC-LLM outperforms interpretable baselines and even black-box models in certain settings, converges more rapidly towards relevant concepts, and is more robust to out-of-distribution samples.

## 🔍 Abstract (한글 번역)

arXiv:2410.15555v2 발표 유형: 교체-교차  
초록: 개념 병목 모델(CBMs)은 해석 가능성과 정확성 간의 절충을 목표로 하는 화이트박스와 블랙박스 모델 간의 타협안으로 제안되었습니다. CBM의 표준 훈련 절차는 인간이 해석할 수 있는 개념의 후보 집합을 미리 정의하고, 훈련 데이터에서 그 값을 추출한 후, 투명한 예측 모델의 입력으로 사용할 희소한 부분 집합을 식별하는 것입니다. 그러나 이러한 접근 방식은 충분히 큰 개념 집합을 탐색하는 것과 개념 추출 비용을 제어하는 것 사이의 균형을 맞추는 데 어려움을 겪어, 해석 가능성과 정확성 간의 큰 절충을 초래합니다. 이 연구는 이러한 문제를 피하는 새로운 접근 방식을 조사합니다: BC-LLM은 잠재적으로 무한한 개념 집합을 베이지안 프레임워크 내에서 반복적으로 탐색하며, 대형 언어 모델(LLMs)이 개념 추출 메커니즘과 사전으로 작용합니다. LLM이 잘못 조정되거나 환상을 일으킬 수 있음에도 불구하고, 우리는 BC-LLM이 엄격한 통계적 추론과 불확실성 정량화를 제공할 수 있음을 증명합니다. 이미지, 텍스트 및 표 형식 데이터셋 전반에 걸쳐, BC-LLM은 해석 가능한 기준선을 능가하고 특정 설정에서는 블랙박스 모델보다도 뛰어난 성능을 보이며, 관련 개념으로 더 빠르게 수렴하고, 분포 외 샘플에 대해 더 강건합니다.

## 📝 요약

이 논문은 해석 가능성과 정확성의 균형을 이루기 위한 개념 병목 모델(CBM)의 한계를 극복하기 위해 BC-LLM이라는 새로운 접근 방식을 제안합니다. BC-LLM은 베이지안 프레임워크 내에서 대형 언어 모델(LLM)을 활용하여 무한한 개념 집합을 탐색하며, LLM을 개념 추출 메커니즘 및 사전 정보로 사용합니다. LLM의 오차와 환각 가능성에도 불구하고, BC-LLM은 통계적 추론과 불확실성 정량화를 제공합니다. 이미지, 텍스트, 표 형식 데이터에서 BC-LLM은 해석 가능한 기준 모델과 특정 상황의 블랙박스 모델보다 우수한 성능을 보이며, 관련 개념에 더 빠르게 수렴하고 분포 외 샘플에 대해 더 강건함을 입증했습니다.

## 🎯 주요 포인트

- 1. Concept Bottleneck Models(CBMs)는 해석 가능성과 정확성의 균형을 맞추기 위한 모델로 제안되었습니다.
- 2. 기존 CBMs는 인간이 해석 가능한 개념을 미리 정의하고, 이를 투명한 예측 모델의 입력으로 사용하는 방식입니다.
- 3. BC-LLM은 잠재적으로 무한한 개념 집합을 탐색하는 새로운 접근법으로, 대형 언어 모델(LLMs)을 개념 추출 메커니즘으로 활용합니다.
- 4. BC-LLM은 이미지, 텍스트, 표 형식 데이터셋에서 해석 가능한 기준 모델과 블랙박스 모델을 능가하는 성능을 보입니다.
- 5. BC-LLM은 관련 개념으로 더 빠르게 수렴하고, 분포 외 샘플에 대해 더 강건한 특성을 보입니다.


---

*Generated on 2025-09-23 09:47:56*