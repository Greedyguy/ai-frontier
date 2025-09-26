---
keywords:
  - Unsupervised Domain Generalization
  - Self-supervised Learning
  - Minimal Sufficient Semantic Representation
  - InfoNCE Objective
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15791
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:11:05.289565",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Unsupervised Domain Generalization",
    "Self-supervised Learning",
    "Minimal Sufficient Semantic Representation",
    "InfoNCE Objective"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Unsupervised Domain Generalization": 0.78,
    "Self-supervised Learning": 0.82,
    "Minimal Sufficient Semantic Representation": 0.77,
    "InfoNCE Objective": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Unsupervised Domain Generalization",
        "canonical": "Unsupervised Domain Generalization",
        "aliases": [
          "UDG"
        ],
        "category": "unique_technical",
        "rationale": "It represents a specialized task in machine learning focusing on generalization without supervision, crucial for connecting related research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Self-Supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "A prevalent technique in unsupervised learning, linking it to broader machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Minimal Sufficient Semantic Representation",
        "canonical": "Minimal Sufficient Semantic Representation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and provides a unique perspective on semantic representation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      },
      {
        "surface": "InfoNCE-based objective",
        "canonical": "InfoNCE Objective",
        "aliases": [
          "InfoNCE"
        ],
        "category": "specific_connectable",
        "rationale": "A key component in optimizing representations, linking to information theory and learning objectives.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "generalization",
      "task",
      "model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Unsupervised Domain Generalization",
      "resolved_canonical": "Unsupervised Domain Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Self-Supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Minimal Sufficient Semantic Representation",
      "resolved_canonical": "Minimal Sufficient Semantic Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "InfoNCE-based objective",
      "resolved_canonical": "InfoNCE Objective",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Minimal Semantic Sufficiency Meets Unsupervised Domain Generalization

**Korean Title:** 최소 의미적 충분성과 비지도 도메인 일반화의 만남

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15791.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15791](https://arxiv.org/abs/2509.15791)

## 🔗 유사한 논문
- [[2025-09-17/Class-invariant Test-Time Augmentation for Domain Generalization_20250917|Class-invariant Test-Time Augmentation for Domain Generalization]] (81.1% similar)
- [[2025-09-18/BEVUDA++_ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection_20250918|BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (81.0% similar)
- [[2025-09-22/CoDoL_ Conditional Domain Prompt Learning for Out-of-Distribution Generalization_20250922|CoDoL: Conditional Domain Prompt Learning for Out-of-Distribution Generalization]] (80.3% similar)
- [[2025-09-22/Two Facets of the Same Optimization Coin_ Model Degradation and Representation Collapse in Graph Foundation Models_20250922|Two Facets of the Same Optimization Coin: Model Degradation and Representation Collapse in Graph Foundation Models]] (80.2% similar)
- [[2025-09-18/Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/InfoNCE Objective|InfoNCE Objective]]
**⚡ Unique Technical**: [[keywords/Unsupervised Domain Generalization|Unsupervised Domain Generalization]], [[keywords/Minimal Sufficient Semantic Representation|Minimal Sufficient Semantic Representation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15791v1 Announce Type: new 
Abstract: The generalization ability of deep learning has been extensively studied in supervised settings, yet it remains less explored in unsupervised scenarios. Recently, the Unsupervised Domain Generalization (UDG) task has been proposed to enhance the generalization of models trained with prevalent unsupervised learning techniques, such as Self-Supervised Learning (SSL). UDG confronts the challenge of distinguishing semantics from variations without category labels. Although some recent methods have employed domain labels to tackle this issue, such domain labels are often unavailable in real-world contexts. In this paper, we address these limitations by formalizing UDG as the task of learning a Minimal Sufficient Semantic Representation: a representation that (i) preserves all semantic information shared across augmented views (sufficiency), and (ii) maximally removes information irrelevant to semantics (minimality). We theoretically ground these objectives from the perspective of information theory, demonstrating that optimizing representations to achieve sufficiency and minimality directly reduces out-of-distribution risk. Practically, we implement this optimization through Minimal-Sufficient UDG (MS-UDG), a learnable model by integrating (a) an InfoNCE-based objective to achieve sufficiency; (b) two complementary components to promote minimality: a novel semantic-variation disentanglement loss and a reconstruction-based mechanism for capturing adequate variation. Empirically, MS-UDG sets a new state-of-the-art on popular unsupervised domain-generalization benchmarks, consistently outperforming existing SSL and UDG methods, without category or domain labels during representation learning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15791v1 발표 유형: 신규  
초록: 심층 학습의 일반화 능력은 지도 학습 환경에서 광범위하게 연구되었지만, 비지도 학습 환경에서는 덜 탐구되었습니다. 최근에 비지도 도메인 일반화(Unsupervised Domain Generalization, UDG) 과제가 제안되어, 자가 지도 학습(Self-Supervised Learning, SSL)과 같은 널리 사용되는 비지도 학습 기법으로 훈련된 모델의 일반화를 향상시키고자 합니다. UDG는 범주 레이블 없이 의미와 변형을 구별하는 문제에 직면합니다. 최근의 일부 방법은 이 문제를 해결하기 위해 도메인 레이블을 사용했지만, 실제 환경에서는 이러한 도메인 레이블이 종종 제공되지 않습니다. 본 논문에서는 UDG를 최소 충분 의미 표현(Minimal Sufficient Semantic Representation)을 학습하는 과제로 공식화하여 이러한 제한을 해결합니다. 이는 (i) 증강된 뷰 간에 공유되는 모든 의미 정보를 보존하고(충분성), (ii) 의미와 관련 없는 정보를 최대한 제거하는(최소성) 표현입니다. 우리는 정보 이론의 관점에서 이러한 목표를 이론적으로 뒷받침하며, 충분성과 최소성을 달성하기 위한 표현 최적화가 직접적으로 분포 외 위험을 줄인다는 것을 입증합니다. 실질적으로, 우리는 최소-충분 UDG(Minimal-Sufficient UDG, MS-UDG)를 통해 이 최적화를 구현하며, 이는 (a) 충분성을 달성하기 위한 InfoNCE 기반의 목표와 (b) 최소성을 촉진하기 위한 두 가지 보완적 구성 요소: 새로운 의미-변형 분리 손실과 적절한 변형을 포착하기 위한 재구성 기반 메커니즘을 통합한 학습 가능한 모델입니다. 실험적으로, MS-UDG는 인기 있는 비지도 도메인 일반화 벤치마크에서 새로운 최첨단 성능을 기록하며, 표현 학습 중 범주나 도메인 레이블 없이 기존의 SSL 및 UDG 방법을 지속적으로 능가합니다.

## 📝 요약

이 논문은 비지도 학습의 일반화 능력을 향상시키기 위한 새로운 접근법인 비지도 도메인 일반화(UDG)를 제안합니다. 기존의 방법들이 도메인 레이블을 필요로 하는 반면, 이 연구는 정보 이론을 기반으로 최소 충분 의미 표현을 학습하는 방법을 제시합니다. 이는 의미 있는 정보를 보존하고 불필요한 정보를 제거하는 것을 목표로 합니다. 이를 위해 InfoNCE 기반의 목표와 의미-변이 분리 손실, 재구성 기반 메커니즘을 통합한 MS-UDG 모델을 개발했습니다. 실험 결과, MS-UDG는 기존의 비지도 학습 및 UDG 방법을 뛰어넘는 성능을 보여주었습니다.

## 🎯 주요 포인트

- 1. 비지도 학습 시나리오에서의 일반화 능력 향상을 위해 비지도 도메인 일반화(UDG) 과제가 제안되었습니다.
- 2. UDG는 범주 레이블 없이 의미와 변화를 구분하는 문제를 해결하려고 합니다.
- 3. 이 논문은 UDG를 최소 충분 의미 표현을 학습하는 과제로 공식화하여 정보 이론 관점에서 이론적으로 뒷받침합니다.
- 4. MS-UDG 모델은 InfoNCE 기반 목표와 새로운 의미-변화 분리 손실 및 재구성 기반 메커니즘을 통합하여 구현됩니다.
- 5. MS-UDG는 기존의 SSL 및 UDG 방법을 능가하며, 범주 또는 도메인 레이블 없이도 비지도 도메인 일반화 벤치마크에서 새로운 최첨단 성능을 달성합니다.


---

*Generated on 2025-09-23 12:11:05*