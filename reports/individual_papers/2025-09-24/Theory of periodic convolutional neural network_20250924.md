<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:54:56.447334",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Periodic Convolutional Neural Network",
    "Ridge Functions",
    "Image Analysis on Wrapped Domains",
    "Physics-Informed Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Periodic Convolutional Neural Network": 0.78,
    "Ridge Functions": 0.72,
    "Image Analysis on Wrapped Domains": 0.7,
    "Physics-Informed Learning": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "periodic CNN",
        "canonical": "Periodic Convolutional Neural Network",
        "aliases": [
          "periodic convolutional neural network"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel architecture with specific boundary conditions, expanding CNN theory.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "ridge functions",
        "canonical": "Ridge Functions",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the paper's theoretical contribution, describing the function class approximated by periodic CNNs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "image analysis on wrapped domains",
        "canonical": "Image Analysis on Wrapped Domains",
        "aliases": [
          "wrapped domain image analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a practical application area for periodic CNNs, linking to computer vision contexts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "physics-informed learning",
        "canonical": "Physics-Informed Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Indicates a specific application domain where periodic CNNs can be particularly effective.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "convolutional layers",
      "approximation theorem",
      "high intrinsic dimension"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "periodic CNN",
      "resolved_canonical": "Periodic Convolutional Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ridge functions",
      "resolved_canonical": "Ridge Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "image analysis on wrapped domains",
      "resolved_canonical": "Image Analysis on Wrapped Domains",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "physics-informed learning",
      "resolved_canonical": "Physics-Informed Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Theory of periodic convolutional neural network

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18744.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18744](https://arxiv.org/abs/2509.18744)

## 🔗 유사한 논문
- [[2025-09-22/Incorporating Visual Cortical Lateral Connection Properties into CNN_ Recurrent Activation and Excitatory-Inhibitory Separation_20250922|Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation]] (81.0% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (80.8% similar)
- [[2025-09-22/Region-Aware Deformable Convolutions_20250922|Region-Aware Deformable Convolutions]] (79.7% similar)
- [[2025-09-24/ConceptFlow_ Hierarchical and Fine-grained Concept-Based Explanation for Convolutional Neural Networks_20250924|ConceptFlow: Hierarchical and Fine-grained Concept-Based Explanation for Convolutional Neural Networks]] (79.5% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Image Analysis on Wrapped Domains|Image Analysis on Wrapped Domains]], [[keywords/Physics-Informed Learning|Physics-Informed Learning]]
**⚡ Unique Technical**: [[keywords/Periodic Convolutional Neural Network|Periodic Convolutional Neural Network]], [[keywords/Ridge Functions|Ridge Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18744v1 Announce Type: new 
Abstract: We introduce a novel convolutional neural network architecture, termed the \emph{periodic CNN}, which incorporates periodic boundary conditions into the convolutional layers. Our main theoretical contribution is a rigorous approximation theorem: periodic CNNs can approximate ridge functions depending on $d-1$ linear variables in a $d$-dimensional input space, while such approximation is impossible in lower-dimensional ridge settings ($d-2$ or fewer variables). This result establishes a sharp characterization of the expressive power of periodic CNNs. Beyond the theory, our findings suggest that periodic CNNs are particularly well-suited for problems where data naturally admits a ridge-like structure of high intrinsic dimension, such as image analysis on wrapped domains, physics-informed learning, and materials science. The work thus both expands the mathematical foundation of CNN approximation theory and highlights a class of architectures with surprising and practically relevant approximation capabilities.

## 📝 요약

이 논문에서는 주기적 경계 조건을 합성곱 계층에 통합한 새로운 합성곱 신경망 구조인 '주기적 CNN'을 소개합니다. 주요 이론적 기여는 주기적 CNN이 $d$차원 입력 공간에서 $d-1$개의 선형 변수에 의존하는 리지 함수를 근사할 수 있다는 엄밀한 근사 정리를 제시한 것입니다. 이는 낮은 차원의 리지 설정에서는 불가능한 근사입니다. 이러한 결과는 주기적 CNN의 표현 능력을 명확히 규명합니다. 또한, 주기적 CNN은 이미지 분석, 물리학 기반 학습, 재료 과학 등 고차원 리지 구조가 자연스럽게 나타나는 문제에 적합하다는 것을 시사합니다. 이 연구는 CNN 근사 이론의 수학적 기초를 확장하고, 실질적으로 유용한 근사 능력을 가진 아키텍처를 강조합니다.

## 🎯 주요 포인트

- 1. 주기적 CNN은 컨볼루션 층에 주기적 경계 조건을 통합한 새로운 신경망 구조입니다.
- 2. 주기적 CNN은 $d$차원 입력 공간에서 $d-1$개의 선형 변수에 의존하는 리지 함수를 근사할 수 있습니다.
- 3. 주기적 CNN은 이미지 분석, 물리학 기반 학습, 재료 과학 등 고차원 리지 구조를 갖는 문제에 적합합니다.
- 4. 본 연구는 CNN 근사 이론의 수학적 기초를 확장하고 실용적인 근사 능력을 가진 아키텍처를 강조합니다.


---

*Generated on 2025-09-24 14:54:56*