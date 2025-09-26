---
keywords:
  - Mixture of Experts
  - Synthetic Image Detection
  - Generative Models
  - Discriminative Expert Array
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15741
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:07:40.982193",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture of Experts",
    "Synthetic Image Detection",
    "Generative Models",
    "Discriminative Expert Array"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture of Experts": 0.85,
    "Synthetic Image Detection": 0.8,
    "Generative Models": 0.75,
    "Discriminative Expert Array": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixture of Discriminative Experts",
        "canonical": "Mixture of Experts",
        "aliases": [
          "MoE",
          "Mixture of Experts"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's approach and connects to broader discussions on expert models in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Synthetic Image Detection",
        "canonical": "Synthetic Image Detection",
        "aliases": [
          "Fake Image Detection",
          "Generative Image Detection"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel approach in this specific domain, making it a unique technical contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Generative Models",
        "canonical": "Generative Models",
        "aliases": [
          "Generative Networks",
          "Generative Algorithms"
        ],
        "category": "broad_technical",
        "rationale": "Generative models are a foundational concept in the paper, linking to a wide range of machine learning discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Discriminative Expert Array",
        "canonical": "Discriminative Expert Array",
        "aliases": [
          "DEA"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel component introduced in the paper, contributing to its unique approach.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
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
      "candidate_surface": "Mixture of Discriminative Experts",
      "resolved_canonical": "Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Synthetic Image Detection",
      "resolved_canonical": "Synthetic Image Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Generative Models",
      "resolved_canonical": "Generative Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Discriminative Expert Array",
      "resolved_canonical": "Discriminative Expert Array",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection

**Korean Title:** TrueMoE: 차별적 전문가의 이중 라우팅 혼합을 통한 합성 이미지 탐지

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15741.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15741](https://arxiv.org/abs/2509.15741)

## 🔗 유사한 논문
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (86.5% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (84.2% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (84.2% similar)
- [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (83.4% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative Models|Generative Models]]
**🔗 Specific Connectable**: [[keywords/Mixture of Experts|Mixture of Experts]]
**⚡ Unique Technical**: [[keywords/Synthetic Image Detection|Synthetic Image Detection]], [[keywords/Discriminative Expert Array|Discriminative Expert Array]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15741v1 Announce Type: new 
Abstract: The rapid progress of generative models has made synthetic image detection an increasingly critical task. Most existing approaches attempt to construct a single, universal discriminative space to separate real from fake content. However, such unified spaces tend to be complex and brittle, often struggling to generalize to unseen generative patterns. In this work, we propose TrueMoE, a novel dual-routing Mixture-of-Discriminative-Experts framework that reformulates the detection task as a collaborative inference across multiple specialized and lightweight discriminative subspaces. At the core of TrueMoE is a Discriminative Expert Array (DEA) organized along complementary axes of manifold structure and perceptual granularity, enabling diverse forgery cues to be captured across subspaces. A dual-routing mechanism, comprising a granularity-aware sparse router and a manifold-aware dense router, adaptively assigns input images to the most relevant experts. Extensive experiments across a wide spectrum of generative models demonstrate that TrueMoE achieves superior generalization and robustness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15741v1 발표 유형: 신규  
초록: 생성 모델의 급속한 발전은 합성 이미지 검출을 점점 더 중요한 과제로 만들고 있습니다. 대부분의 기존 접근 방식은 진짜와 가짜 콘텐츠를 구분하기 위한 단일의 보편적인 판별 공간을 구축하려고 시도합니다. 그러나 이러한 통합된 공간은 복잡하고 취약한 경향이 있어 보지 못한 생성 패턴에 일반화하는 데 어려움을 겪습니다. 본 연구에서는 TrueMoE라는 새로운 이중 라우팅 판별 전문가 혼합(Mixture-of-Discriminative-Experts) 프레임워크를 제안하여, 검출 과제를 여러 전문화되고 경량화된 판별 하위 공간 간의 협력적 추론으로 재구성합니다. TrueMoE의 핵심은 다양하고 위조된 단서를 하위 공간에서 포착할 수 있도록 다양체 구조와 지각적 세분성의 보완적인 축을 따라 조직된 판별 전문가 배열(Discriminative Expert Array, DEA)입니다. 세분성 인식 희소 라우터와 다양체 인식 밀집 라우터로 구성된 이중 라우팅 메커니즘은 입력 이미지를 가장 관련성 높은 전문가에게 적응적으로 할당합니다. 다양한 생성 모델에 걸친 광범위한 실험을 통해 TrueMoE가 뛰어난 일반화와 견고성을 달성함을 입증합니다.

## 📝 요약

TrueMoE는 합성 이미지 탐지를 위한 새로운 접근법으로, 여러 전문화된 경량 판별 하위 공간을 활용하여 탐지 작업을 협력적 추론으로 재구성합니다. 기존 방법들이 단일 판별 공간을 구축하는 데 비해, TrueMoE는 다양하고 복잡한 위조 패턴을 효과적으로 포착할 수 있습니다. 이 프레임워크의 핵심은 다양한 위조 단서를 포착할 수 있는 판별 전문가 배열(DEA)이며, 이는 다중 구조와 지각적 세분성 축을 따라 조직됩니다. 또한, 이중 라우팅 메커니즘을 통해 입력 이미지를 관련 전문가에게 적응적으로 할당합니다. 다양한 생성 모델에 대한 실험 결과, TrueMoE는 뛰어난 일반화 능력과 강인성을 보여줍니다.

## 🎯 주요 포인트

- 1. TrueMoE는 합성 이미지 탐지를 위한 새로운 Mixture-of-Discriminative-Experts 프레임워크로, 여러 전문화된 경량 서브스페이스를 활용하여 탐지 작업을 수행합니다.
- 2. TrueMoE의 핵심은 다양하고 상호 보완적인 축을 따라 구성된 Discriminative Expert Array (DEA)로, 다양한 위조 단서를 포착할 수 있습니다.
- 3. 이중 라우팅 메커니즘은 입력 이미지를 가장 관련성이 높은 전문가에게 할당하여 적응적으로 처리합니다.
- 4. TrueMoE는 다양한 생성 모델에 대한 실험에서 뛰어난 일반화 능력과 견고성을 입증했습니다.


---

*Generated on 2025-09-23 12:07:40*