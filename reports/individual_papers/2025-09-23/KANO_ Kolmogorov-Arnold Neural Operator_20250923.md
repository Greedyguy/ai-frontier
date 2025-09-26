---
keywords:
  - Kolmogorov-Arnold Neural Operator
  - Fourier Neural Operator
  - Quantum Hamiltonian Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16825
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:34:57.976182",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kolmogorov-Arnold Neural Operator",
    "Fourier Neural Operator",
    "Quantum Hamiltonian Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kolmogorov-Arnold Neural Operator": 0.85,
    "Fourier Neural Operator": 0.78,
    "Quantum Hamiltonian Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kolmogorov-Arnold Neural Operator",
        "canonical": "Kolmogorov-Arnold Neural Operator",
        "aliases": [
          "KANO"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel neural operator with unique properties that differentiate it from existing operators, making it a valuable addition to the graph.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Fourier Neural Operator",
        "canonical": "Fourier Neural Operator",
        "aliases": [
          "FNO"
        ],
        "category": "specific_connectable",
        "rationale": "FNO is a known operator in the field, providing a point of comparison and connection to the new KANO model.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "quantum Hamiltonian learning",
        "canonical": "Quantum Hamiltonian Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This specific application of KANO demonstrates its potential in quantum physics, offering a unique technical link.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "position-dependent dynamics",
      "projective measurement data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Kolmogorov-Arnold Neural Operator",
      "resolved_canonical": "Kolmogorov-Arnold Neural Operator",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Fourier Neural Operator",
      "resolved_canonical": "Fourier Neural Operator",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "quantum Hamiltonian learning",
      "resolved_canonical": "Quantum Hamiltonian Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# KANO: Kolmogorov-Arnold Neural Operator

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16825.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16825](https://arxiv.org/abs/2509.16825)

## 🔗 유사한 논문
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (78.8% similar)
- [[2025-09-22/Merging Memory and Space_ A State Space Neural Operator_20250922|Merging Memory and Space: A State Space Neural Operator]] (78.1% similar)
- [[2025-09-18/Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (76.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Fourier Neural Operator|Fourier Neural Operator]]
**⚡ Unique Technical**: [[keywords/Kolmogorov-Arnold Neural Operator|Kolmogorov-Arnold Neural Operator]], [[keywords/Quantum Hamiltonian Learning|Quantum Hamiltonian Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16825v1 Announce Type: cross 
Abstract: We introduce Kolmogorov--Arnold Neural Operator (KANO), a dual-domain neural operator jointly parameterized by both spectral and spatial bases with intrinsic symbolic interpretability. We theoretically demonstrate that KANO overcomes the pure-spectral bottleneck of Fourier Neural Operator (FNO): KANO remains expressive over generic position-dependent dynamics for any physical input, whereas FNO stays practical only for spectrally sparse operators and strictly imposes a fast-decaying input Fourier tail. We verify our claims empirically on position-dependent differential operators, for which KANO robustly generalizes but FNO fails to. In the quantum Hamiltonian learning benchmark, KANO reconstructs ground-truth Hamiltonians in closed-form symbolic representations accurate to the fourth decimal place in coefficients and attains $\approx 6\times10^{-6}$ state infidelity from projective measurement data, substantially outperforming that of the FNO trained with ideal full wave function data, $\approx 1.5\times10^{-2}$, by orders of magnitude.

## 📝 요약

Kolmogorov--Arnold Neural Operator (KANO)는 스펙트럼 및 공간 기반으로 공동 매개변수화된 이중 도메인 신경 연산자로, 본질적인 상징적 해석 가능성을 제공합니다. KANO는 Fourier Neural Operator (FNO)의 스펙트럼 한계를 극복하여, 위치 의존적 동역학에 대해 일반적으로 표현력을 유지합니다. 이는 FNO가 스펙트럼이 희소한 연산자에만 실용적인 것과 대조적입니다. 위치 의존적 미분 연산자에 대한 실험에서 KANO는 강력한 일반화 능력을 보였으나 FNO는 실패했습니다. 또한, 양자 해밀토니안 학습 벤치마크에서 KANO는 기저 해밀토니안을 정확하게 재구성하며, 상태 불일치도에서 FNO보다 훨씬 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Kolmogorov--Arnold Neural Operator (KANO)는 스펙트럼 및 공간 기반으로 공동 매개변수화된 이중 도메인 신경 연산자로, 본질적인 상징적 해석 가능성을 갖추고 있습니다.
- 2. KANO는 Fourier Neural Operator (FNO)의 순수 스펙트럼 병목 현상을 극복하며, 위치 의존적 동역학에 대해 일반적인 물리적 입력에 대해 표현력을 유지합니다.
- 3. KANO는 위치 의존적 미분 연산자에 대해 강력하게 일반화하는 반면, FNO는 실패하는 것으로 실증적으로 확인되었습니다.
- 4. 양자 해밀토니안 학습 벤치마크에서 KANO는 정확한 상징적 표현으로 해밀토니안을 재구성하며, 상태 불일치도 측면에서 FNO보다 훨씬 뛰어난 성능을 보였습니다.


---

*Generated on 2025-09-23 23:34:57*