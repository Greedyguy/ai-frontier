---
keywords:
  - Physics-Informed Neural Networks
  - Inverse Problems
  - Partial Differential Equations
  - Finite Element Method
  - Fluid Mechanics Problems
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20191
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:02:16.550678",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Physics-Informed Neural Networks",
    "Inverse Problems",
    "Partial Differential Equations",
    "Finite Element Method",
    "Fluid Mechanics Problems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Physics-Informed Neural Networks": 0.78,
    "Inverse Problems": 0.72,
    "Partial Differential Equations": 0.7,
    "Finite Element Method": 0.75,
    "Fluid Mechanics Problems": 0.71
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Physics-Informed Neural Networks",
        "canonical": "Physics-Informed Neural Networks",
        "aliases": [
          "PINNs"
        ],
        "category": "unique_technical",
        "rationale": "Physics-Informed Neural Networks are a novel approach in machine learning for solving PDEs, providing a unique link to discussions on integrating physics with neural networks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Inverse Problems",
        "canonical": "Inverse Problems",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Inverse Problems are a key application area for PINNs, offering strong connectivity to topics in computational mathematics and engineering.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.76,
        "link_intent_score": 0.72
      },
      {
        "surface": "Partial Differential Equations",
        "canonical": "Partial Differential Equations",
        "aliases": [
          "PDEs"
        ],
        "category": "broad_technical",
        "rationale": "Partial Differential Equations are fundamental in the study of dynamical systems, providing a broad technical link to various scientific and engineering fields.",
        "novelty_score": 0.45,
        "connectivity_score": 0.83,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Finite Element Method",
        "canonical": "Finite Element Method",
        "aliases": [
          "FEM"
        ],
        "category": "specific_connectable",
        "rationale": "The Finite Element Method is a traditional approach for solving PDEs, offering a direct comparison point for evaluating PINNs.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Fluid Mechanics Problems",
        "canonical": "Fluid Mechanics Problems",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Fluid Mechanics Problems are specific test cases for evaluating the robustness of PINNs, linking to specialized applications in engineering.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.71
      }
    ],
    "ban_list_suggestions": [
      "noise",
      "training",
      "data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Physics-Informed Neural Networks",
      "resolved_canonical": "Physics-Informed Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Inverse Problems",
      "resolved_canonical": "Inverse Problems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.76,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Partial Differential Equations",
      "resolved_canonical": "Partial Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.83,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Finite Element Method",
      "resolved_canonical": "Finite Element Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Fluid Mechanics Problems",
      "resolved_canonical": "Fluid Mechanics Problems",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.71
      }
    }
  ]
}
-->

# Examining the robustness of Physics-Informed Neural Networks to noise for Inverse Problems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20191.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20191](https://arxiv.org/abs/2509.20191)

## 🔗 유사한 논문
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (87.7% similar)
- [[2025-09-25/THINNs_ Thermodynamically Informed Neural Networks_20250925|THINNs: Thermodynamically Informed Neural Networks]] (87.2% similar)
- [[2025-09-23/PACMANN_ Point Adaptive Collocation Method for Artificial Neural Networks_20250923|PACMANN: Point Adaptive Collocation Method for Artificial Neural Networks]] (87.1% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (85.7% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Partial Differential Equations|Partial Differential Equations]]
**🔗 Specific Connectable**: [[keywords/Inverse Problems|Inverse Problems]], [[keywords/Finite Element Method|Finite Element Method]]
**⚡ Unique Technical**: [[keywords/Physics-Informed Neural Networks|Physics-Informed Neural Networks]], [[keywords/Fluid Mechanics Problems|Fluid Mechanics Problems]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20191v1 Announce Type: cross 
Abstract: Approximating solutions to partial differential equations (PDEs) is fundamental for the modeling of dynamical systems in science and engineering. Physics-informed neural networks (PINNs) are a recent machine learning-based approach, for which many properties and limitations remain unknown. PINNs are widely accepted as inferior to traditional methods for solving PDEs, such as the finite element method, both with regard to computation time and accuracy. However, PINNs are commonly claimed to show promise in solving inverse problems and handling noisy or incomplete data. We compare the performance of PINNs in solving inverse problems with that of a traditional approach using the finite element method combined with a numerical optimizer. The models are tested on a series of increasingly difficult fluid mechanics problems, with and without noise. We find that while PINNs may require less human effort and specialized knowledge, they are outperformed by the traditional approach. However, the difference appears to decrease with higher dimensions and more data. We identify common failures during training to be addressed if the performance of PINNs on noisy inverse problems is to become more competitive.

## 📝 요약

이 논문은 부분 미분 방정식(PDE) 해를 근사하는 방법으로 최근 주목받고 있는 물리 기반 신경망(PINNs)의 성능을 전통적인 유한 요소법과 비교합니다. PINNs는 계산 시간과 정확도 면에서 전통적인 방법보다 열등하다고 평가되지만, 역문제 해결 및 불완전한 데이터 처리에 유망하다는 주장이 있습니다. 연구는 점점 더 복잡해지는 유체 역학 문제에 대해 PINNs와 유한 요소법을 결합한 전통적 접근법의 성능을 비교했습니다. 결과적으로, PINNs는 더 적은 인력과 전문 지식을 요구하지만, 전통적 방법에 비해 성능이 떨어졌습니다. 하지만, 고차원 문제와 데이터가 많아질수록 그 차이는 줄어드는 경향을 보였습니다. 또한, PINNs의 훈련 중 일반적인 실패 원인을 파악하여, 노이즈가 있는 역문제에서의 경쟁력을 높일 필요가 있음을 제안합니다.

## 🎯 주요 포인트

- 1. 물리 정보 신경망(PINNs)은 부분 미분 방정식(PDEs) 해결에 있어 전통적인 방법보다 계산 시간과 정확성에서 열등하다고 평가받고 있습니다.
- 2. PINNs는 역문제 해결 및 노이즈가 있거나 불완전한 데이터 처리에서 유망한 가능성을 보인다고 주장됩니다.
- 3. PINNs는 인간의 노력과 전문 지식이 덜 필요하지만, 전통적인 유한 요소법과 수치 최적화기를 결합한 방법에 비해 성능이 떨어집니다.
- 4. 고차원 및 더 많은 데이터가 있을 경우, PINNs와 전통적인 방법 간의 성능 차이가 줄어드는 경향이 있습니다.
- 5. 노이즈가 있는 역문제에서 PINNs의 성능을 개선하기 위해 해결해야 할 공통적인 훈련 실패 사례가 식별되었습니다.


---

*Generated on 2025-09-25 17:02:16*