---
keywords:
  - Neural Network
  - DimINO
  - Partial Differential Equations
  - Dimensional Analysis
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2410.05894
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:35:29.584008",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "DimINO",
    "Partial Differential Equations",
    "Dimensional Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "DimINO": 0.82,
    "Partial Differential Equations": 0.85,
    "Dimensional Analysis": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Operator",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Operators"
        ],
        "category": "broad_technical",
        "rationale": "Neural Operators are a subset of Neural Networks, which helps in connecting with broader machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "DimINO",
        "canonical": "DimINO",
        "aliases": [
          "Dimension-Informed Neural Operators"
        ],
        "category": "unique_technical",
        "rationale": "DimINO is a novel framework introduced in the paper, providing a unique link to the specific methodology discussed.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Partial Differential Equations",
        "canonical": "Partial Differential Equations",
        "aliases": [
          "PDEs"
        ],
        "category": "specific_connectable",
        "rationale": "PDEs are central to the paper's focus and connect to a wide range of computational physics literature.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dimensional Analysis",
        "canonical": "Dimensional Analysis",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Dimensional Analysis is a key component of the proposed framework, linking to mathematical and physical modeling techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Operator",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "DimINO",
      "resolved_canonical": "DimINO",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Partial Differential Equations",
      "resolved_canonical": "Partial Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Dimensional Analysis",
      "resolved_canonical": "Dimensional Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# DimINO: Dimension-Informed Neural Operator Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2410.05894.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2410.05894](https://arxiv.org/abs/2410.05894)

## 🔗 유사한 논문
- [[2025-09-23/Physics-Informed Operator Learning for Hemodynamic Modeling_20250923|Physics-Informed Operator Learning for Hemodynamic Modeling]] (83.5% similar)
- [[2025-09-22/Merging Memory and Space_ A State Space Neural Operator_20250922|Merging Memory and Space: A State Space Neural Operator]] (82.7% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (80.8% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (80.7% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Partial Differential Equations|Partial Differential Equations]], [[keywords/Dimensional Analysis|Dimensional Analysis]]
**⚡ Unique Technical**: [[keywords/DimINO|DimINO]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.05894v4 Announce Type: replace 
Abstract: In computational physics, a longstanding challenge lies in finding numerical solutions to partial differential equations (PDEs). Recently, research attention has increasingly focused on Neural Operator methods, which are notable for their ability to approximate operators-mappings between functions. Although neural operators benefit from a universal approximation theorem, achieving reliable error bounds often necessitates large model architectures, such as deep stacks of Fourier layers. This raises a natural question: Can we design lightweight models without sacrificing generalization? To address this, we introduce DimINO (Dimension-Informed Neural Operators), a framework inspired by dimensional analysis. DimINO incorporates two key components, DimNorm and a redimensionalization operation, which can be seamlessly integrated into existing neural operator architectures. These components enhance the model's ability to generalize across datasets with varying physical parameters. Theoretically, we establish a universal approximation theorem for DimINO and prove that it satisfies a critical property we term Similar Transformation Invariance (STI). Empirically, DimINO achieves up to 76.3% performance gain on PDE datasets while exhibiting clear evidence of the STI property.

## 📝 요약

이 논문은 부분 미분 방정식(PDE)의 수치 해법을 찾는 문제를 다루며, Neural Operator 방법론에 주목합니다. 기존의 Neural Operator는 보편 근사 정리를 갖지만, 신뢰할 수 있는 오류 범위를 얻기 위해서는 대규모 모델이 필요합니다. 이를 해결하기 위해, 본 연구는 DimINO(Dimension-Informed Neural Operators)라는 프레임워크를 제안합니다. DimINO는 DimNorm과 재차원화 연산을 통해 다양한 물리적 매개변수를 가진 데이터셋에서 일반화 성능을 향상시킵니다. 이론적으로, DimINO의 보편 근사 정리를 확립하고, 유사 변환 불변성(STI)을 만족함을 증명했습니다. 실험 결과, DimINO는 PDE 데이터셋에서 최대 76.3%의 성능 향상을 보이며 STI 특성을 입증했습니다.

## 🎯 주요 포인트

- 1. Neural Operator 방법은 함수 간의 사상(operators-mappings)을 근사하는 데 주목받고 있으며, 보편적 근사 정리를 활용한다.
- 2. DimINO는 차원 분석에서 영감을 받은 프레임워크로, DimNorm과 재차원화(redimensionalization) 작업을 포함하여 기존 신경 연산자 구조에 통합될 수 있다.
- 3. DimINO는 다양한 물리적 매개변수를 가진 데이터셋에서 모델의 일반화 능력을 향상시킨다.
- 4. DimINO는 유사 변환 불변성(Similar Transformation Invariance, STI)이라는 중요한 속성을 만족하며, 이론적으로 보편적 근사 정리를 확립한다.
- 5. 실험적으로, DimINO는 편미분 방정식(PDE) 데이터셋에서 최대 76.3%의 성능 향상을 달성하며 STI 속성을 명확히 보여준다.


---

*Generated on 2025-09-24 02:35:29*