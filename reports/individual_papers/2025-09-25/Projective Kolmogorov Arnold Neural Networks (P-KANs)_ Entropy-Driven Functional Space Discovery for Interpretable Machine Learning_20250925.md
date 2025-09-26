---
keywords:
  - Kolmogorov-Arnold Networks
  - Projective Kolmogorov-Arnold Networks
  - Entropy Minimization
  - Sparse Dictionary Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20049
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:57:25.431579",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kolmogorov-Arnold Networks",
    "Projective Kolmogorov-Arnold Networks",
    "Entropy Minimization",
    "Sparse Dictionary Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kolmogorov-Arnold Networks": 0.78,
    "Projective Kolmogorov-Arnold Networks": 0.82,
    "Entropy Minimization": 0.77,
    "Sparse Dictionary Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kolmogorov-Arnold Networks",
        "canonical": "Kolmogorov-Arnold Networks",
        "aliases": [
          "KANs"
        ],
        "category": "unique_technical",
        "rationale": "Kolmogorov-Arnold Networks are central to the paper's methodology and offer a unique approach to neural network design.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Projective Kolmogorov-Arnold Networks",
        "canonical": "Projective Kolmogorov-Arnold Networks",
        "aliases": [
          "P-KANs"
        ],
        "category": "unique_technical",
        "rationale": "P-KANs represent a novel extension of KANs with specific improvements in interpretability and efficiency.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Entropy-minimisation",
        "canonical": "Entropy Minimization",
        "aliases": [
          "Entropy Reduction"
        ],
        "category": "specific_connectable",
        "rationale": "Entropy minimization is a key technique used in the paper to guide functional representation discovery.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Sparse Dictionary Learning",
        "canonical": "Sparse Dictionary Learning",
        "aliases": [
          "Sparse Coding"
        ],
        "category": "specific_connectable",
        "rationale": "Sparse dictionary learning is integral to the paper's method for achieving efficient functional representations.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
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
      "candidate_surface": "Kolmogorov-Arnold Networks",
      "resolved_canonical": "Kolmogorov-Arnold Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Projective Kolmogorov-Arnold Networks",
      "resolved_canonical": "Projective Kolmogorov-Arnold Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Entropy-minimisation",
      "resolved_canonical": "Entropy Minimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Sparse Dictionary Learning",
      "resolved_canonical": "Sparse Dictionary Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Projective Kolmogorov Arnold Neural Networks (P-KANs): Entropy-Driven Functional Space Discovery for Interpretable Machine Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20049.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20049](https://arxiv.org/abs/2509.20049)

## 🔗 유사한 논문
- [[2025-09-25/On the Rate of Convergence of Kolmogorov-Arnold Network Regression Estimators_20250925|On the Rate of Convergence of Kolmogorov-Arnold Network Regression Estimators]] (89.1% similar)
- [[2025-09-23/Interpretable Clinical Classification with Kolgomorov-Arnold Networks_20250923|Interpretable Clinical Classification with Kolgomorov-Arnold Networks]] (86.6% similar)
- [[2025-09-24/Physics-informed time series analysis with Kolmogorov-Arnold Networks under Ehrenfest constraints_20250924|Physics-informed time series analysis with Kolmogorov-Arnold Networks under Ehrenfest constraints]] (86.1% similar)
- [[2025-09-18/Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (83.8% similar)
- [[2025-09-23/KANO_ Kolmogorov-Arnold Neural Operator_20250923|KANO: Kolmogorov-Arnold Neural Operator]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Entropy Minimization|Entropy Minimization]], [[keywords/Sparse Dictionary Learning|Sparse Dictionary Learning]]
**⚡ Unique Technical**: [[keywords/Kolmogorov-Arnold Networks|Kolmogorov-Arnold Networks]], [[keywords/Projective Kolmogorov-Arnold Networks|Projective Kolmogorov-Arnold Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20049v1 Announce Type: cross 
Abstract: Kolmogorov-Arnold Networks (KANs) relocate learnable nonlinearities from nodes to edges, demonstrating remarkable capabilities in scientific machine learning and interpretable modeling. However, current KAN implementations suffer from fundamental inefficiencies due to redundancy in high-dimensional spline parameter spaces, where numerous distinct parameterisations yield functionally equivalent behaviors. This redundancy manifests as a "nuisance space" in the model's Jacobian, leading to susceptibility to overfitting and poor generalization. We introduce Projective Kolmogorov-Arnold Networks (P-KANs), a novel training framework that guides edge function discovery towards interpretable functional representations through entropy-minimisation techniques from signal analysis and sparse dictionary learning. Rather than constraining functions to predetermined spaces, our approach maintains spline space flexibility while introducing "gravitational" terms that encourage convergence towards optimal functional representations. Our key insight recognizes that optimal representations can be identified through entropy analysis of projection coefficients, compressing edge functions to lower-parameter projective spaces (Fourier, Chebyshev, Bessel). P-KANs demonstrate superior performance across multiple domains, achieving up to 80% parameter reduction while maintaining representational capacity, significantly improved robustness to noise compared to standard KANs, and successful application to industrial automated fiber placement prediction. Our approach enables automatic discovery of mixed functional representations where different edges converge to different optimal spaces, providing both compression benefits and enhanced interpretability for scientific machine learning applications.

## 📝 요약

Kolmogorov-Arnold Networks(KANs)는 비선형성을 엣지로 이동시켜 과학적 머신러닝과 해석 가능한 모델링에서 뛰어난 성능을 보입니다. 그러나 기존 KAN은 고차원 스플라인 매개변수 공간의 중복성으로 인해 비효율적입니다. 이를 해결하기 위해 우리는 Projective Kolmogorov-Arnold Networks(P-KANs)를 제안합니다. P-KANs는 신호 분석과 희소 사전 학습의 엔트로피 최소화 기법을 통해 해석 가능한 함수 표현을 유도합니다. 이 방법은 스플라인 공간의 유연성을 유지하면서 최적의 함수 표현으로 수렴하도록 유도하는 "중력" 항을 도입합니다. 우리의 주요 발견은 투영 계수의 엔트로피 분석을 통해 최적의 표현을 식별하고, 엣지 함수를 저차원 투영 공간으로 압축할 수 있다는 것입니다. P-KANs는 여러 분야에서 최대 80%의 매개변수 감소와 함께 표준 KANs보다 뛰어난 노이즈에 대한 강건성을 보여주며, 산업 자동화 섬유 배치 예측에 성공적으로 적용되었습니다. 이 접근법은 다양한 엣지가 서로 다른 최적 공간으로 수렴하도록 하여 과학적 머신러닝 응용에 대한 압축 이점과 해석 가능성을 제공합니다.

## 🎯 주요 포인트

- 1. Kolmogorov-Arnold Networks(KANs)는 노드 대신 엣지에 학습 가능한 비선형성을 배치하여 과학적 머신러닝과 해석 가능한 모델링에서 뛰어난 성능을 보여줍니다.
- 2. 기존 KAN 구현은 고차원 스플라인 매개변수 공간의 중복성으로 인해 비효율성을 겪고 있으며, 이는 모델의 Jacobian에서 "장애 공간"으로 나타나 과적합과 일반화 문제를 유발합니다.
- 3. Projective Kolmogorov-Arnold Networks(P-KANs)는 신호 분석과 희소 사전 학습의 엔트로피 최소화 기법을 통해 해석 가능한 함수 표현을 유도하는 새로운 훈련 프레임워크를 제안합니다.
- 4. P-KANs는 다양한 도메인에서 최대 80%의 매개변수 감소를 달성하면서 표현 능력을 유지하고, 표준 KANs에 비해 노이즈에 대한 강력한 내성을 보여줍니다.
- 5. P-KANs는 산업 자동화 섬유 배치 예측에 성공적으로 적용되었으며, 과학적 머신러닝 응용에서 혼합 함수 표현의 자동 발견을 가능하게 합니다.


---

*Generated on 2025-09-25 15:57:25*