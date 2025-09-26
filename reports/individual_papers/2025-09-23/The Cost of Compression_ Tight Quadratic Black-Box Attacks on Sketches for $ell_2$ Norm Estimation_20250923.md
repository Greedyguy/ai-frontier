---
keywords:
  - Dimensionality Reduction
  - Linear Sketching
  - Adversarial Attack
  - Johnson-Lindenstrauss Transform
  - AMS Sketch
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2507.16345
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:47:25.462100",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dimensionality Reduction",
    "Linear Sketching",
    "Adversarial Attack",
    "Johnson-Lindenstrauss Transform",
    "AMS Sketch"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dimensionality Reduction": 0.79,
    "Linear Sketching": 0.78,
    "Adversarial Attack": 0.83,
    "Johnson-Lindenstrauss Transform": 0.81,
    "AMS Sketch": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dimensionality reduction",
        "canonical": "Dimensionality Reduction",
        "aliases": [
          "dimension reduction"
        ],
        "category": "broad_technical",
        "rationale": "Dimensionality reduction is a foundational concept in data processing and compression, linking it to various techniques in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.79
      },
      {
        "surface": "linear sketching",
        "canonical": "Linear Sketching",
        "aliases": [
          "sketching"
        ],
        "category": "unique_technical",
        "rationale": "Linear sketching is a specific technique in dimensionality reduction, crucial for understanding the paper's focus on adversarial attacks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.64,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "adversarial attack",
        "canonical": "Adversarial Attack",
        "aliases": [
          "adversarial input"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial attacks are a key area of research in machine learning, linking to security and robustness studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.83
      },
      {
        "surface": "Johnson Lindenstrauss transform",
        "canonical": "Johnson-Lindenstrauss Transform",
        "aliases": [
          "JL transform"
        ],
        "category": "unique_technical",
        "rationale": "The Johnson-Lindenstrauss transform is a specific mathematical technique relevant to the paper's discussion on sketching.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.81
      },
      {
        "surface": "AMS sketch",
        "canonical": "AMS Sketch",
        "aliases": [
          "Alon-Matias-Szegedy sketch"
        ],
        "category": "unique_technical",
        "rationale": "AMS sketches are a specific type of sketching method, directly relevant to the paper's focus on norm estimation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "system",
      "query"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "dimensionality reduction",
      "resolved_canonical": "Dimensionality Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.68,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "linear sketching",
      "resolved_canonical": "Linear Sketching",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.64,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "adversarial attack",
      "resolved_canonical": "Adversarial Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Johnson Lindenstrauss transform",
      "resolved_canonical": "Johnson-Lindenstrauss Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "AMS sketch",
      "resolved_canonical": "AMS Sketch",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# The Cost of Compression: Tight Quadratic Black-Box Attacks on Sketches for $\ell_2$ Norm Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.16345.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2507.16345](https://arxiv.org/abs/2507.16345)

## 🔗 유사한 논문
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.7% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (79.7% similar)
- [[2025-09-23/Bias-variance Tradeoff in Tensor Estimation_20250923|Bias-variance Tradeoff in Tensor Estimation]] (78.5% similar)
- [[2025-09-22/Permutation recovery of spikes in noisy high-dimensional tensor estimation_20250922|Permutation recovery of spikes in noisy high-dimensional tensor estimation]] (78.3% similar)
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dimensionality Reduction|Dimensionality Reduction]]
**🔗 Specific Connectable**: [[keywords/Adversarial Attack|Adversarial Attack]]
**⚡ Unique Technical**: [[keywords/Linear Sketching|Linear Sketching]], [[keywords/Johnson-Lindenstrauss Transform|Johnson-Lindenstrauss Transform]], [[keywords/AMS Sketch|AMS Sketch]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.16345v2 Announce Type: replace 
Abstract: Dimensionality reduction via linear sketching is a powerful and widely used technique, but it is known to be vulnerable to adversarial inputs. We study the black-box adversarial setting, where a fixed, hidden sketching matrix $A \in R^{k \times n}$ maps high-dimensional vectors $v \in R^n$ to lower-dimensional sketches $A v \in R^k$, and an adversary can query the system to obtain approximate $\ell_2$-norm estimates that are computed from the sketch. We present a universal, nonadaptive attack that, using $\tilde{O}(k^2)$ queries, either causes a failure in norm estimation or constructs an adversarial input on which the optimal estimator for the query distribution (used by the attack) fails. The attack is completely agnostic to the sketching matrix and to the estimator: it applies to any linear sketch and any query responder, including those that are randomized, adaptive, or tailored to the query distribution. Our lower bound construction tightly matches the known upper bounds of $\tilde{\Omega}(k^2)$, achieved by specialized estimators for Johnson Lindenstrauss transforms and AMS sketches. Beyond sketching, our results uncover structural parallels to adversarial attacks in image classification, highlighting fundamental vulnerabilities of compressed representations.

## 📝 요약

이 논문은 선형 스케칭을 통한 차원 축소 기법의 취약성을 연구합니다. 특히, 고정된 스케칭 행렬을 사용하는 블랙박스 적대적 환경에서의 공격을 다룹니다. 저자는 $\tilde{O}(k^2)$번의 쿼리를 통해 노름 추정 실패를 유도하거나 적대적 입력을 생성하는 보편적이고 비적응적인 공격 방법을 제안합니다. 이 공격은 스케칭 행렬이나 추정기에 무관하며, 모든 선형 스케치와 쿼리 응답자에 적용됩니다. 또한, 이 연구는 이미지 분류의 적대적 공격과 유사한 구조적 취약성을 드러내며, 압축 표현의 근본적인 취약성을 강조합니다.

## 🎯 주요 포인트

- 1. 선형 스케칭을 통한 차원 축소는 강력하지만 적대적 입력에 취약하다.
- 2. 블랙박스 적대적 환경에서 고차원 벡터를 저차원 스케치로 변환하는 고정된 스케칭 행렬을 연구한다.
- 3. 제안된 비적응적 공격은 $\tilde{O}(k^2)$ 쿼리를 사용하여 노름 추정 실패를 유발하거나 최적 추정기를 실패시킨다.
- 4. 공격은 스케칭 행렬과 추정기에 무관하며, 임의의 선형 스케치와 쿼리 응답자에 적용 가능하다.
- 5. 연구 결과는 이미지 분류의 적대적 공격과의 구조적 유사성을 드러내며, 압축 표현의 근본적인 취약성을 강조한다.


---

*Generated on 2025-09-24 02:47:25*