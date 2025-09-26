---
keywords:
  - FP4 Training
  - Hadamard Transformation
  - Stochastic Rounding
  - Tensor Scaling
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17791
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:56:44.490275",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "FP4 Training",
    "Hadamard Transformation",
    "Stochastic Rounding",
    "Tensor Scaling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "FP4 Training": 0.78,
    "Hadamard Transformation": 0.75,
    "Stochastic Rounding": 0.8,
    "Tensor Scaling": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FP4 training",
        "canonical": "FP4 Training",
        "aliases": [
          "4-bit Floating Point Training"
        ],
        "category": "unique_technical",
        "rationale": "FP4 Training is a distinct topic within low-precision training, offering unique insights into computational efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hadamard transformations",
        "canonical": "Hadamard Transformation",
        "aliases": [
          "Hadamard Transform"
        ],
        "category": "specific_connectable",
        "rationale": "Hadamard transformations are crucial for optimizing computational efficiency in FP4 training.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "stochastic rounding",
        "canonical": "Stochastic Rounding",
        "aliases": [
          "Randomized Rounding"
        ],
        "category": "specific_connectable",
        "rationale": "Stochastic rounding is a key technique for stabilizing low-precision training, enhancing model performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "tensor scaling",
        "canonical": "Tensor Scaling",
        "aliases": [
          "Scaling of Tensors"
        ],
        "category": "specific_connectable",
        "rationale": "Tensor scaling is integral to managing precision and computational overhead in FP4 training.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "foundation models",
      "computational overheads"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "FP4 training",
      "resolved_canonical": "FP4 Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hadamard transformations",
      "resolved_canonical": "Hadamard Transformation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "stochastic rounding",
      "resolved_canonical": "Stochastic Rounding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "tensor scaling",
      "resolved_canonical": "Tensor Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Elucidating the Design Space of FP4 training

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17791.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17791](https://arxiv.org/abs/2509.17791)

## 🔗 유사한 논문
- [[2025-09-23/Search-Optimized Quantization in Biomedical Ontology Alignment_20250923|Search-Optimized Quantization in Biomedical Ontology Alignment]] (82.8% similar)
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (82.5% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.3% similar)
- [[2025-09-23/PTQTP_ Post-Training Quantization to Trit-Planes for Large Language Models_20250923|PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models]] (82.3% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Hadamard Transformation|Hadamard Transformation]], [[keywords/Stochastic Rounding|Stochastic Rounding]], [[keywords/Tensor Scaling|Tensor Scaling]]
**⚡ Unique Technical**: [[keywords/FP4 Training|FP4 Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17791v1 Announce Type: new 
Abstract: The increasing computational demands of foundation models have spurred research into low-precision training, with 4-bit floating-point (\texttt{FP4}) formats emerging as a frontier for maximizing hardware throughput. While numerous techniques have been proposed to stabilize \texttt{FP4} training, they often present isolated solutions with varying, and not always clear, computational overheads. This paper aims to provide a unified view of the design space of \texttt{FP4} training. We introduce a comprehensive, quantisation gradient-based framework for microscaling quantization that allows for a theoretical analysis of the computational costs associated with different stabilization methods on both the forward and backward passes. Using a simulator built on this framework, we conduct an extensive empirical study across a wide range of machine learning tasks, including regression, image classification, diffusion models, and language models. By systematically evaluating thousands of combinations of techniques, such as novel gradient approximations, rounding strategies, and scaling methods, we identify which configurations offer the most favourable performance-to-overhead trade-off. We find that the techniques enabling the best trade-off involve carefully combining Hadamard transformations, tensor scaling and stochastic rounding. We further find that using \texttt{UE5M3} as a scaling factor potentially offers a good compromise between range and precision with manageable computational overhead.

## 📝 요약

이 논문은 기초 모델의 계산 요구가 증가함에 따라 하드웨어 처리량을 극대화하기 위한 4비트 부동소수점(\texttt{FP4}) 형식의 저정밀도 학습 연구를 다룹니다. \texttt{FP4} 학습을 안정화하기 위한 다양한 기술이 제안되었으나, 이들은 종종 개별적인 해결책으로 명확하지 않은 계산 비용을 수반합니다. 본 연구는 \texttt{FP4} 학습의 설계 공간을 통합적으로 분석하고, 미세 스케일 양자화를 위한 포괄적인 프레임워크를 제시합니다. 이를 통해 다양한 안정화 방법의 계산 비용을 이론적으로 분석하고, 시뮬레이터를 활용해 회귀, 이미지 분류, 확산 모델, 언어 모델 등 다양한 머신러닝 작업을 대상으로 광범위한 실증 연구를 수행했습니다. 수천 가지 기술 조합을 체계적으로 평가한 결과, Hadamard 변환, 텐서 스케일링, 확률적 반올림을 결합한 방법이 가장 효율적인 성능-오버헤드 균형을 제공함을 발견했습니다. 또한, \texttt{UE5M3} 스케일링 팩터가 범위와 정밀도 사이에서 적절한 타협을 제공할 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 기초 모델의 계산 수요 증가로 인해 4비트 부동소수점(\texttt{FP4}) 형식을 활용한 저정밀도 훈련 연구가 활발히 진행되고 있습니다.
- 2. \texttt{FP4} 훈련의 설계 공간을 통합적으로 이해하기 위해 미세 스케일 양자화에 기반한 포괄적인 프레임워크를 제안합니다.
- 3. 다양한 기법의 성능과 계산 오버헤드를 체계적으로 평가하여 가장 유리한 성능-오버헤드 균형을 제공하는 구성 요소를 식별했습니다.
- 4. Hadamard 변환, 텐서 스케일링, 확률적 반올림을 조합하는 것이 최적의 성능-오버헤드 균형을 제공함을 발견했습니다.
- 5. \texttt{UE5M3} 스케일링 팩터를 사용하면 범위와 정밀도 사이에서 적절한 타협을 이루면서 계산 오버헤드를 관리할 수 있습니다.


---

*Generated on 2025-09-24 01:56:44*