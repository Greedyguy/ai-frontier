---
keywords:
  - Large Language Model
  - Quantization
  - Walsh-Hadamard Transform
  - Fourier Transform
  - Parameter-Efficient Fine-Tuning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17428
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:26:03.089951",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Quantization",
    "Walsh-Hadamard Transform",
    "Fourier Transform",
    "Parameter-Efficient Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Quantization": 0.8,
    "Walsh-Hadamard Transform": 0.78,
    "Fourier Transform": 0.75,
    "Parameter-Efficient Fine-Tuning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on quantization and fine-tuning, linking to broader discussions in NLP and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Quantization",
        "canonical": "Quantization",
        "aliases": [
          "Quantized Models"
        ],
        "category": "unique_technical",
        "rationale": "Quantization is a key technical focus of the paper, crucial for efficient model deployment and fine-tuning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Walsh-Hadamard Transform",
        "canonical": "Walsh-Hadamard Transform",
        "aliases": [
          "WHT"
        ],
        "category": "unique_technical",
        "rationale": "The Walsh-Hadamard Transform is a novel approach proposed in the paper, enhancing the representational capacity of quantized models.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fourier-related Transform",
        "canonical": "Fourier Transform",
        "aliases": [
          "FT-based Adapters"
        ],
        "category": "specific_connectable",
        "rationale": "Fourier-related Transforms are discussed as a comparative method, linking to broader mathematical techniques in signal processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "unique_technical",
        "rationale": "PEFT is a central theme in the paper, addressing the need for efficient model adaptation with minimal parameter updates.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Quantization",
      "resolved_canonical": "Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Walsh-Hadamard Transform",
      "resolved_canonical": "Walsh-Hadamard Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fourier-related Transform",
      "resolved_canonical": "Fourier Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# QWHA: Quantization-Aware Walsh-Hadamard Adaptation for Parameter-Efficient Fine-Tuning on Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17428.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17428](https://arxiv.org/abs/2509.17428)

## 🔗 유사한 논문
- [[2025-09-23/How Can Quantum Deep Learning Improve Large Language Models?_20250923|How Can Quantum Deep Learning Improve Large Language Models?]] (88.0% similar)
- [[2025-09-23/Does quantization affect models' performance on long-context tasks?_20250923|Does quantization affect models' performance on long-context tasks?]] (87.3% similar)
- [[2025-09-23/GuidedQuant_ Large Language Model Quantization via Exploiting End Loss Guidance_20250923|GuidedQuant: Large Language Model Quantization via Exploiting End Loss Guidance]] (87.1% similar)
- [[2025-09-23/PTQTP_ Post-Training Quantization to Trit-Planes for Large Language Models_20250923|PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models]] (87.0% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (86.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fourier Transform|Fourier Transform]]
**⚡ Unique Technical**: [[keywords/Quantization|Quantization]], [[keywords/Walsh-Hadamard Transform|Walsh-Hadamard Transform]], [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17428v1 Announce Type: new 
Abstract: The demand for efficient deployment of large language models (LLMs) has driven interest in quantization, which reduces inference cost, and parameter-efficient fine-tuning (PEFT), which lowers training overhead. This motivated the development of quantization-aware PEFT to produce accurate yet efficient quantized models. In this setting, reducing quantization error prior to fine-tuning is crucial for achieving high model accuracy. However, existing methods that rely on low-rank adaptation suffer from limited representational capacity. Recent Fourier-related transform (FT)-based adapters offer greater representational power than low-rank adapters, but their direct integration into quantized models often results in ineffective error reduction and increased computational overhead. To overcome these limitations, we propose QWHA, a method that integrates FT-based adapters into quantized models by employing the Walsh-Hadamard Transform (WHT) as the transform kernel, together with a novel adapter initialization scheme incorporating adaptive parameter selection and value refinement. We demonstrate that QWHA effectively mitigates quantization errors while facilitating fine-tuning, and that its design substantially reduces computational cost. Experimental results show that QWHA consistently outperforms baselines in low-bit quantization accuracy and achieves significant training speedups over existing FT-based adapters. The code is available at https://github.com/vantaa89/qwha.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 효율적인 배포를 위한 양자화 및 파라미터 효율적 미세 조정(PEFT)에 중점을 둡니다. 저자들은 양자화 오류를 줄이고 모델의 정확성을 높이기 위해 Walsh-Hadamard Transform(WHT)을 활용한 QWHA 방법을 제안합니다. 기존의 저차원 적응 방식은 표현력이 제한적이며, 최근의 푸리에 변환 기반 어댑터는 양자화 모델에 직접 통합 시 오류 감소에 비효율적입니다. QWHA는 적응적 파라미터 선택 및 값 정제를 포함한 새로운 어댑터 초기화 방식을 통해 이러한 문제를 해결하고, 계산 비용을 크게 줄입니다. 실험 결과, QWHA는 낮은 비트 양자화 정확도에서 기존 방법보다 우수한 성능을 보이며, 훈련 속도도 크게 향상됩니다. 코드 링크는 https://github.com/vantaa89/qwha입니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델의 효율적 배포를 위해 양자화와 파라미터 효율적 미세 조정(PEFT)이 중요하다.
- 2. 기존의 저랭크 적응 방식은 표현력의 한계로 인해 양자화 오류 감소에 비효율적이다.
- 3. QWHA는 Walsh-Hadamard 변환(WHT)을 사용하여 FT 기반 어댑터를 양자화된 모델에 통합하여 양자화 오류를 효과적으로 완화한다.
- 4. QWHA는 적응형 파라미터 선택과 값 정제를 포함한 새로운 어댑터 초기화 방식을 통해 연산 비용을 크게 줄인다.
- 5. 실험 결과, QWHA는 저비트 양자화 정확도에서 일관되게 우수한 성능을 보이며, 기존 FT 기반 어댑터 대비 훈련 속도를 크게 향상시킨다.


---

*Generated on 2025-09-24 03:26:03*